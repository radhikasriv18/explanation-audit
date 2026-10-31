#!/usr/bin/env python3
"""LLM-only grounding judge with Gemini (google-genai, Gemini Developer API). New file; judge.py is unchanged.

  source ~/.bashrc   # sets GEMINI_API_KEY (never printed)
  python judge_gemini.py --nodes cora:884 --run-dir runs/gemini_884

Differences from judge.py:
  - backend: google-genai Client(api_key=$GEMINI_API_KEY), model MODEL_ID (newest stable Flash, checked 2026-10-30:
    the test call returned model_version 'gemini-3.8-flash'), temperature 0, JSON output (response_mime_type).
  - NO hybrid mode: the model labels every claim (supported / contradicted / unverifiable / duplicate).
  - rubric R1-R6 plus the importance / hop / meaning rules, stated in the system prompt (RULES below).
Reused unchanged from judge.py (imported): user_msg (packet + previous claims + batch), parse (JSON validation),
plan(..., hybrid=False) (v4 sheet rows in batches of judge.BATCH = 10), same reference packets packets/packet_<ds>_<node>.txt.
A batch that fails to parse is retried once with a correction turn; a second failure gives PARSE_FAIL rows.

Outputs in --run-dir: raw.jsonl (every call: timestamp, model_version, prompt, raw output, token usage, status),
judgments.csv (same columns as judge.py, readable by compare.py), failures.csv, run_info.json (tokens + cost estimate).
"""
import argparse, csv, json, os, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import judge  # noqa: E402  (user_msg, parse, plan, BATCH; importing it does not load any model)

from google import genai  # noqa: E402
from google.genai import types  # noqa: E402

MODEL_ID = "gemini-3.8-flash"
# USD per 1M tokens, for the cost ESTIMATE only. Set from the published price list before trusting the estimate;
# thinking tokens are billed as output tokens.
PRICE_IN, PRICE_OUT = None, None

RULES = """- supported: the REFERENCE confirms the claim. contradicted: the REFERENCE shows it is false.
  unverifiable: it cannot be checked against the REFERENCE. duplicate: it repeats an earlier claim.
- R1 A keyword or topic list is ONE claim. Judge each item against the node; the majority decides.
  A tie (equal numbers fitting and not fitting) counts as contradicted.
- R2 A statement about a neighbor's class ("X is a <class> paper/product", "X is more related to <class>")
  is checked against that node's TRUE label in the REFERENCE.
- R3 A claim that repeats an earlier claim of this explanation (same content about the same thing) is duplicate.
- R4 Headings, procedure descriptions, YES/NO support verdicts, support or importance judgments
  ("supports the classification", "strengthens", "is relevant") and opinions are unverifiable.
- R5 If a node's title and abstract/description are about different things, a description that matches
  EITHER the title or the abstract counts as matching that node.
- R6 Repetition loops, spam and boilerplate text are unverifiable.
- Importance claims ("pivotal", "most important", "high importance") are checked against the saliency rank
  in the REFERENCE when one is given; if the REFERENCE gives no ranking, they are unverifiable.
- A node within 2 hops of the target counts as "connected". "Direct" (or 1-hop, immediate) means hop 1;
  calling a 2-hop node a direct neighbor is contradicted. Citing a node that is not within 2 hops or does not
  exist is contradicted.
- Judge the meaning of the claim, not its exact wording."""

SYSTEM = f"""You are a strict fact-checker. You check claims taken from an explanation that a language model wrote about
why a graph neural network (GNN) classified a target node. Each node is a paper (Cora citation graph) or a product
(Amazon co-purchase graph). You are given a REFERENCE with the ground truth: the target node and every node ID the
explanation mentions, with its title, text, true label, GNN prediction and hop distance from the target.
Judge each claim ONLY against the REFERENCE.

Verdicts: supported / contradicted / unverifiable / duplicate.
Rules:
{RULES}

Output JSON only, no other text, in exactly this form, one entry per claim, in the given order:
{{"verdicts": [{{"id": "<claim id>", "verdict": "supported|contradicted|unverifiable|duplicate", "reason": "<one line>"}}]}}"""


class Gemini:
    def __init__(self, max_out):
        key = os.environ.get("GEMINI_API_KEY", "")
        if not key:
            sys.exit("GEMINI_API_KEY is empty (run: source ~/.bashrc)")
        self._key = key
        self.client = genai.Client(api_key=key)
        self.cfg = types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0,
                                               response_mime_type="application/json", max_output_tokens=max_out)
        self.name = MODEL_ID + " temperature 0, JSON"

    def __call__(self, messages):
        """messages = [system, user, (assistant, user)...]; system is passed via system_instruction."""
        contents = [types.Content(role="model" if m["role"] == "assistant" else "user", parts=[types.Part(text=m["content"])])
                    for m in messages[1:]]
        try:
            r = self.client.models.generate_content(model=MODEL_ID, contents=contents, config=self.cfg)
        except Exception as e:  # keep the key out of any error text
            raise RuntimeError(f"{type(e).__name__}: {str(e).replace(self._key, '<REDACTED>')}") from None
        u = r.usage_metadata
        usage = {"prompt": u.prompt_token_count or 0, "output": u.candidates_token_count or 0,
                 "thoughts": getattr(u, "thoughts_token_count", None) or 0, "total": u.total_token_count or 0}
        fr = r.candidates[0].finish_reason if r.candidates else None
        return (r.text or ""), usage, r.model_version, str(fr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes", required=True, help="comma list like cora:884")
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--max-output-tokens", type=int, default=8192)
    a = ap.parse_args()
    nodes = [(x.split(":")[0], int(x.split(":")[1])) for x in a.nodes.split(",")]
    rd = a.run_dir if os.path.isabs(a.run_dir) else os.path.join(HERE, a.run_dir)
    os.makedirs(rd, exist_ok=True)
    raw_path = os.path.join(rd, "raw.jsonl")
    done = {}
    if os.path.exists(raw_path):
        for line in open(raw_path):
            e = json.loads(line)
            if e["status"] in ("ok", "failed"):
                done[(e["node"], e["batch"])] = e
    plans = {(ds, node): judge.plan(ds, node, False) for ds, node in nodes}
    llm = Gemini(a.max_output_tokens)
    t0 = time.time()
    for ds, node in nodes:
        packet = open(os.path.join(HERE, f"packets/packet_{ds}_{node}.txt")).read()
        for bi, batch, prev in plans[(ds, node)][2]:
            if (node, bi) in done:
                continue
            ids = [r["claim_id"] for r in batch]
            msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": judge.user_msg(packet, prev, batch)}]
            for attempt in (1, 2):
                ts = time.time()
                try:
                    raw, usage, mv, fr = llm(msgs)
                    res, why = judge.parse(raw, ids)
                except RuntimeError as err:
                    raw, usage, mv, fr, res, why = "", {}, None, None, None, f"API error: {str(err)[:300]}"
                status = "ok" if res else ("retry" if attempt == 1 else "failed")
                e = {"timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"), "model": MODEL_ID,
                     "model_version": mv, "dataset": ds, "node": node, "batch": bi, "attempt": attempt, "status": status,
                     "why": why, "finish_reason": fr, "usage": usage, "seconds": round(time.time() - ts, 2), "ids": ids,
                     "messages": msgs, "raw_output": raw, "verdicts": res}
                with open(raw_path, "a") as f:
                    f.write(json.dumps(e) + "\n")
                print(f"{ds} {node} batch {bi} attempt {attempt}: {status} ({why}) tokens={usage} version={mv}", flush=True)
                if res:
                    break
                msgs = msgs + [{"role": "assistant", "content": raw},
                               {"role": "user", "content": f"Your output was not valid ({why}). Return JSON only, in the exact "
                                                           f"format given, with one verdict for each of these ids: {', '.join(ids)}"}]
    run_seconds = time.time() - t0

    final = {}
    for line in open(raw_path):
        e = json.loads(line)
        if e["status"] in ("ok", "failed"):
            final[(e["node"], e["batch"])] = e
    out, fails = [], []
    for ds, node in nodes:
        rows, _, batches = plans[(ds, node)]
        got = {}
        for bi, batch, _ in batches:
            e = final.get((node, bi))
            if e and e["status"] == "failed":
                fails.append({"dataset": ds, "node": node, "batch": bi, "why": e["why"], "ids": " ".join(e["ids"])})
            for r in batch:
                got[r["claim_id"]] = (bi, *(e["verdicts"][r["claim_id"]] if e and e["status"] == "ok"
                                            else ("PARSE_FAIL", e["why"] if e else "not run")))
        for r in rows:
            bi, v, why = got[r["claim_id"]]
            out.append({"dataset": ds, "node": node, "batch": bi, "claim_id": r["claim_id"], "claim_kind": r["claim_kind"],
                        "cited_node_id": r["cited_node_id"], "judge_verdict": v, "judge_reason": why, "claim_text": r["claim_text"]})
    with open(os.path.join(rd, "judgments.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    with open(os.path.join(rd, "failures.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["dataset", "node", "batch", "why", "ids"]); w.writeheader(); w.writerows(fails)
    calls = [json.loads(l) for l in open(raw_path)]
    tok = {k: sum(c["usage"].get(k, 0) for c in calls) for k in ("prompt", "output", "thoughts", "total")}
    cost = None if PRICE_IN is None else round((tok["prompt"] * PRICE_IN + (tok["output"] + tok["thoughts"]) * PRICE_OUT) / 1e6, 4)
    info = {"backend": "gemini (google-genai, Developer API)", "model": llm.name,
            "model_versions_seen": sorted({c["model_version"] for c in calls if c["model_version"]}), "hybrid": False,
            "nodes": [f"{d}:{n}" for d, n in nodes], "batch_size": judge.BATCH, "max_output_tokens": a.max_output_tokens,
            "claims": len(out), "batches": len(final), "calls": len(calls), "retries": sum(c["attempt"] == 2 for c in calls),
            "failed_batches": len(fails), "parse_fail_rows": sum(r["judge_verdict"] == "PARSE_FAIL" for r in out),
            "tokens": tok, "price_usd_per_1M": {"input": PRICE_IN, "output_incl_thinking": PRICE_OUT}, "cost_usd_estimate": cost,
            "seconds_this_invocation": round(run_seconds, 1)}
    json.dump(info, open(os.path.join(rd, "run_info.json"), "w"), indent=1)
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
