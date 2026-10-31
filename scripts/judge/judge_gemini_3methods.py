#!/usr/bin/env python3
"""Gemini judge for the 21 hand-labeled GraphNarrator / GraphXAIN / CF-GNNExplainer texts. New file.

  source ~/.bashrc
  python judge_gemini_3methods.py --run-dir runs/gemini_full/3methods

Prompt, rules, model, temperature, JSON mode and retry policy are judge_gemini.py's, imported unchanged
(judge_gemini.SYSTEM via judge_gemini.Gemini; judge.user_msg; judge.parse; judge.BATCH). Only the claim source and the
REFERENCE differ, because judge_gemini.py reads the GSPELL sheets:
  claims    : grounding_answer_key_3methods_2026-10-13/answer_key_3methods_labeled.csv, rows with verdict != not_a_claim,
              in sheet order (excluded rows are also left out of the "previous claims" used for duplicate checks).
  REFERENCE : grounding_judge_pilot/reference_packets/<method>_<ds>_<node>.md (whole packet), followed by a
              FULL NODE TEXT section: target, every canonical 1-hop neighbour and every other cited node, with the
              complete raw_text (no 600-char cut), true label and hop distance, from {cora,products}_canonical.pt.
Outputs in --run-dir: raw.jsonl (timestamp, model_version, prompt, output, usage), judgments.csv, failures.csv, run_info.json.
"""
import argparse, csv, json, os, re, sys, time
from collections import OrderedDict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import judge  # noqa: E402
import judge_gemini as jg  # noqa: E402  (SYSTEM, Gemini, MODEL_ID: unchanged)
import torch  # noqa: E402

csv.field_size_limit(sys.maxsize)
AK = "./grounding_answer_key_3methods_2026-10-13/"
PKT = "./grounding_judge_pilot/reference_packets/"
CANON = {"cora": "./cora_canonical.pt", "products": "./products_canonical.pt"}


def load_graph(ds):
    g = torch.load(CANON[ds], weights_only=False)
    ei = g.edge_index
    adj = {}
    for a, b in zip(ei[0].tolist(), ei[1].tolist()):
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    return g, adj


def hops(adj, t):
    h1 = adj.get(t, set()); h2 = set().union(*(adj.get(x, set()) for x in h1)) - h1 - {t}
    return lambda n: 0 if n == t else 1 if n in h1 else 2 if n in h2 else "not within 2 hops"


def full_text_section(ds, node, g, adj, cited):
    hop = hops(adj, node)
    names = g.label_names
    order = [node] + sorted(adj.get(node, set())) + sorted(c for c in cited if c != node and c not in adj.get(node, set()))
    L = ["", "FULL NODE TEXT (complete canonical raw_text, no truncation; true label and hop distance from the target):"]
    for n in OrderedDict.fromkeys(order):
        if not (0 <= n < g.num_nodes):
            L.append(f"- node {n}: DOES NOT EXIST"); continue
        h = hop(n)
        role = "TARGET" if n == node else ("1-hop (direct neighbor)" if h == 1 else f"{h}-hop" if h == 2 else str(h))
        L.append(f"- node {n} [{role}] true label: {names[int(g.y[n])]}")
        L.append("    " + re.sub(r"\s+", " ", g.raw_text[n]).strip())
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--max-output-tokens", type=int, default=8192)
    a = ap.parse_args()
    rd = a.run_dir if os.path.isabs(a.run_dir) else os.path.join(HERE, a.run_dir)
    os.makedirs(rd, exist_ok=True)
    raw_path = os.path.join(rd, "raw.jsonl")

    key = [r for r in csv.DictReader(open(AK + "answer_key_3methods_labeled.csv", encoding="utf-8")) if r["verdict"] != "not_a_claim"]
    texts = OrderedDict()
    for r in key:
        texts.setdefault((r["method"], r["dataset"], int(r["node"])), []).append(r)
    graphs = {ds: load_graph(ds) for ds in {k[1] for k in texts}}

    done = {}
    if os.path.exists(raw_path):
        for line in open(raw_path):
            e = json.loads(line)
            if e["status"] in ("ok", "failed"):
                done[(e["text"], e["batch"])] = e
    llm = jg.Gemini(a.max_output_tokens)
    t0 = time.time()
    plans = {}
    for (method, ds, node), rows in texts.items():
        tid = f"{method}_{ds}_{node}"
        sheet = {r["claim_id"]: r for r in csv.DictReader(open(AK + f"claims_{tid}_labeled.csv", encoding="utf-8"))}
        cited = {int(x) for r in rows for x in re.findall(r"\d+", sheet[r["claim_id"]].get("cited_ids", ""))}
        g, adj = graphs[ds]
        packet = open(PKT + tid + ".md", encoding="utf-8").read().rstrip() + "\n" + full_text_section(ds, node, g, adj, cited)
        batches = [(b // judge.BATCH, rows[b:b + judge.BATCH], rows[:b]) for b in range(0, len(rows), judge.BATCH)]
        plans[tid] = batches
        for bi, batch, prev in batches:
            if (tid, bi) in done:
                continue
            ids = [r["claim_id"] for r in batch]
            msgs = [{"role": "system", "content": jg.SYSTEM}, {"role": "user", "content": judge.user_msg(packet, prev, batch)}]
            for attempt in (1, 2):
                ts = time.time()
                try:
                    raw, usage, mv, fr = llm(msgs)
                    res, why = judge.parse(raw, ids)
                except RuntimeError as err:
                    raw, usage, mv, fr, res, why = "", {}, None, None, None, f"API error: {str(err)[:300]}"
                status = "ok" if res else ("retry" if attempt == 1 else "failed")
                e = {"timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"), "model": jg.MODEL_ID,
                     "model_version": mv, "text": tid, "method": method, "dataset": ds, "node": node, "batch": bi,
                     "attempt": attempt, "status": status, "why": why, "finish_reason": fr, "usage": usage,
                     "seconds": round(time.time() - ts, 2), "ids": ids, "messages": msgs, "raw_output": raw, "verdicts": res}
                with open(raw_path, "a") as f:
                    f.write(json.dumps(e) + "\n")
                print(f"{tid} batch {bi} attempt {attempt}: {status} ({why}) tokens={usage} version={mv}", flush=True)
                if res:
                    break
                msgs = msgs + [{"role": "assistant", "content": raw},
                               {"role": "user", "content": f"Your output was not valid ({why}). Return JSON only, in the exact "
                                                           f"format given, with one verdict for each of these ids: {', '.join(ids)}"}]

    final = {}
    for line in open(raw_path):
        e = json.loads(line)
        if e["status"] in ("ok", "failed"):
            final[(e["text"], e["batch"])] = e
    out, fails = [], []
    for (method, ds, node), rows in texts.items():
        tid = f"{method}_{ds}_{node}"
        for bi, batch, _ in plans[tid]:
            e = final.get((tid, bi))
            if e and e["status"] == "failed":
                fails.append({"text": tid, "batch": bi, "why": e["why"], "ids": " ".join(e["ids"])})
            for r in batch:
                v, why = (e["verdicts"][r["claim_id"]] if e and e["status"] == "ok" else ("PARSE_FAIL", e["why"] if e else "not run"))
                out.append({"method": method, "dataset": ds, "node": node, "batch": bi, "claim_id": r["claim_id"],
                            "judge_verdict": v, "judge_reason": why, "claim_text": r["claim_text"]})
    with open(os.path.join(rd, "judgments.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    with open(os.path.join(rd, "failures.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "batch", "why", "ids"]); w.writeheader(); w.writerows(fails)
    calls = [json.loads(l) for l in open(raw_path)]
    tok = {k: sum(c["usage"].get(k, 0) for c in calls) for k in ("prompt", "output", "thoughts", "total")}
    info = {"backend": "gemini (google-genai, Developer API)", "model": llm.name,
            "model_versions_seen": sorted({c["model_version"] for c in calls if c["model_version"]}), "hybrid": False,
            "texts": len(texts), "claims": len(out), "batch_size": judge.BATCH, "batches": len(final), "calls": len(calls),
            "retries": sum(c["attempt"] == 2 for c in calls), "failed_batches": len(fails),
            "parse_fail_rows": sum(r["judge_verdict"] == "PARSE_FAIL" for r in out), "tokens": tok,
            "seconds_this_invocation": round(time.time() - t0, 1)}
    json.dump(info, open(os.path.join(rd, "run_info.json"), "w"), indent=1)
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
