"""Gemini grounding judge for the robustness texts, with a hard budget stop. Resumable.

Frozen, imported unchanged from grounding_judge_2026-10-13: judge_gemini.SYSTEM (rules R1-R6 etc.),
judge_gemini.Gemini (gemini-3.8-flash, temperature 0, JSON mode, max_output_tokens 8192),
judge.user_msg (REFERENCE + previous claims + batch), judge.parse, judge.BATCH (10 claims per call),
and judge_gemini_3methods' policy: one correction retry when the output fails to parse, then PARSE_FAIL.
REFERENCE = packets_full/<text>.md (survey-style packet + FULL NODE TEXT section, see prepare_judge_inputs.py).
Claims = every row of claims.csv for the text, in sheet order (automated extraction, no hand pass).
Only texts of the nodes in judge_subset.json (12 per dataset, fixed before any judging) are judged.

Additions, none of which change a prompt:
  - 4 calls in flight (--workers).
  - API errors that are rate limits / server errors (429, 500, 503, RESOURCE_EXHAUSTED, UNAVAILABLE)
    resend the identical request with backoff (up to 8 times) instead of using the correction retry.
  - Budget: cost = prompt * $0.75/1M + (output + thinking) * $3.75/1M (Google price list, valid to
    2026-12-31), summed over every logged call, including earlier invocations.
    Configurations run one at a time in --configs order. A configuration starts only if
    spent + its estimated cost <= --budget, so a configuration is never left half-judged.
    The estimate scales the configuration's prompt characters by the cost per prompt character
    observed so far (a fixed conservative default before any call), times 1.15 for retries.
    A safety stop also refuses any new call once spent + in-flight reservations would pass --budget.
Outputs (run dir): raw.jsonl (every call), judgments.csv, run_status.json (spend, per-config status).
GEMINI_API_KEY must be set in the environment (never printed).
"""
import argparse
import csv
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "./grounding_judge_2026-10-13")
import judge  # noqa: E402
import judge_gemini as jg  # noqa: E402

csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
PRICE_IN, PRICE_OUT = 0.75, 3.75  # USD per 1M tokens, output includes thinking
DEFAULT_USD_PER_PROMPT_CHAR = 0.75e-6 / 2.5  # validated 3-method run: 2.67 chars/token; 2.5 is conservative
OUT_USD_PER_CALL_DEFAULT = 2000 * PRICE_OUT / 1e6  # validated run: 1630 output+thinking tokens/call
RETRYABLE = ("429", "500", "503", "RESOURCE_EXHAUSTED", "UNAVAILABLE", "INTERNAL", "DEADLINE")


def cost(u):
    return (u.get("prompt", 0) * PRICE_IN + (u.get("output", 0) + u.get("thoughts", 0)) * PRICE_OUT) / 1e6


class Ledger:
    def __init__(self, raw_path, budget):
        self.raw_path, self.budget, self.lock = raw_path, budget, threading.Lock()
        self.calls = [json.loads(l) for l in open(raw_path)] if raw_path.exists() else []
        self.spent = sum(cost(c["usage"]) for c in self.calls)
        self.reserved = 0.0

    def final(self):
        out = {}
        for c in self.calls:
            if c["status"] in ("ok", "failed"):
                out[(c["text"], c["batch"])] = c
        return out

    def reserve(self, est):
        with self.lock:
            if self.spent + self.reserved + est > self.budget:
                return False
            self.reserved += est
            return True

    def record(self, entry, est):
        with self.lock:
            self.reserved -= est
            self.spent += cost(entry["usage"])
            self.calls.append(entry)
            with open(self.raw_path, "a") as f:
                f.write(json.dumps(entry) + "\n")

    def rate(self):
        """Observed USD per prompt character and output USD per call (None before any call)."""
        ok = [c for c in self.calls if c["usage"]]
        if len(ok) < 5:
            return None
        chars = sum(c["prompt_chars"] for c in ok)
        return (sum(c["usage"]["prompt"] for c in ok) * PRICE_IN / 1e6 / chars,
                sum((c["usage"]["output"] + c["usage"]["thoughts"]) for c in ok) * PRICE_OUT / 1e6 / len(ok))


def call_with_backoff(llm, msgs):
    for k in range(9):
        try:
            return llm(msgs)
        except RuntimeError as err:
            s = str(err)
            if k < 8 and any(x in s for x in RETRYABLE):
                time.sleep(min(60, 4 * 2 ** k))
                continue
            raise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--configs", nargs="+", required=True, help="method__config ids, in priority order")
    ap.add_argument("--run-dir", default="judge_run")
    ap.add_argument("--budget", type=float, default=9.50)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--subset", default="judge_subset.json", help="nodes to judge (fixed before any judging)")
    ap.add_argument("--dry-run", action="store_true", help="print the per-configuration estimates and stop")
    a = ap.parse_args()
    rd = HERE / a.run_dir
    rd.mkdir(exist_ok=True)
    led = Ledger(rd / "raw.jsonl", a.budget)

    # Judge subset (fixed before any judging): 12 nodes per dataset, judge_subset.json
    js = json.load(open(HERE / a.subset))["datasets"]
    in_subset = {(ds, str(n["global_node_id"])) for ds, ns in js.items() for n in ns}
    claims = [r for r in csv.DictReader(open(HERE / "claims.csv", encoding="utf-8")) if (r["dataset"], r["node"]) in in_subset]
    texts = {}
    for r in claims:
        texts.setdefault(r["text_id"], []).append(r)
    units_by_cfg = {}
    for tid, rows in texts.items():
        cfg = f"{rows[0]['method']}__{rows[0]['config']}"
        packet = (HERE / "packets_full" / f"{tid}.md").read_text(encoding="utf-8")
        for b in range(0, len(rows), judge.BATCH):
            batch, prev = rows[b:b + judge.BATCH], rows[:b]
            msgs = [{"role": "system", "content": jg.SYSTEM}, {"role": "user", "content": judge.user_msg(packet, prev, batch)}]
            units_by_cfg.setdefault(cfg, []).append((tid, b // judge.BATCH, batch, msgs, rows[0]))
    expected_texts = {}
    for e in json.load(open(HERE / "texts.json")):
        if e["text_scored"] and (e["dataset"], e["node"]) in in_subset:  # failed generations have no claims to judge
            expected_texts.setdefault(f"{e['method']}__{e['config']}", set()).add(e["id"])

    def est_unit(msgs):
        r = led.rate()
        chars = sum(len(m["content"]) for m in msgs)
        per_char, out_call = r if r else (DEFAULT_USD_PER_PROMPT_CHAR, OUT_USD_PER_CALL_DEFAULT)
        return chars * per_char + out_call

    llm = None if a.dry_run else jg.Gemini(8192)
    status = {"budget_usd": a.budget, "configs": {}}

    def run_unit(cfg, tid, bi, batch, msgs, meta, est):
        ids = [r["claim_id"] for r in batch]
        m = msgs
        for attempt in (1, 2):
            ts = time.time()
            try:
                raw, usage, mv, fr = call_with_backoff(llm, m)
                res, why = judge.parse(raw, ids)
            except RuntimeError as err:
                raw, usage, mv, fr, res, why = "", {}, None, None, None, f"API error: {str(err)[:300]}"
            st = "ok" if res else ("retry" if attempt == 1 else "failed")
            entry = {"timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"), "model": jg.MODEL_ID,
                     "model_version": mv, "config": cfg, "text": tid, "method": meta["method"], "dataset": meta["dataset"],
                     "node": meta["node"], "batch": bi, "attempt": attempt, "status": st, "why": why, "finish_reason": fr,
                     "usage": usage, "prompt_chars": sum(len(x["content"]) for x in m), "seconds": round(time.time() - ts, 2),
                     "ids": ids, "messages": m, "raw_output": raw, "verdicts": res}
            led.record(entry, est if attempt == 1 else 0.0)
            if res:
                return
            if attempt == 1:
                if not led.reserve(est):
                    led.record({**entry, "attempt": 2, "status": "failed", "why": "budget stop before correction retry",
                                "usage": {}, "raw_output": "", "verdicts": None}, est)
                    return
                m = m + [{"role": "assistant", "content": raw},
                         {"role": "user", "content": f"Your output was not valid ({why}). Return JSON only, in the exact "
                                                     f"format given, with one verdict for each of these ids: {', '.join(ids)}"}]

    stopped = None
    for cfg in a.configs:
        done = led.final()
        units = units_by_cfg.get(cfg, [])
        texts_ready = {u[0] for u in units}
        missing_texts = sorted(expected_texts.get(cfg, set()) - texts_ready)
        todo = [u for u in units if (u[0], u[1]) not in done]
        est = sum(est_unit(u[3]) for u in todo) * 1.15
        info = {"texts_with_claims": len(texts_ready), "texts_expected": len(expected_texts.get(cfg, ())),
                "units_total": len(units), "units_todo_before": len(todo), "estimated_usd": round(est, 3)}
        print(f"{cfg}: {len(todo)}/{len(units)} batches to judge, estimate ${est:.2f}; spent so far ${led.spent:.3f}", flush=True)
        if a.dry_run:
            status["configs"][cfg] = info
            continue
        if missing_texts:
            info["state"] = f"not started: {len(missing_texts)} texts have no claims yet"
            status["configs"][cfg] = info
            print("  " + info["state"], flush=True)
            continue
        if stopped or led.spent + est > a.budget:
            stopped = stopped or cfg
            info["state"] = "not started: estimated cost would pass the budget"
            status["configs"][cfg] = info
            print(f"  {info['state']} (${led.spent:.2f} + ${est:.2f} > ${a.budget:.2f})", flush=True)
            continue
        with ThreadPoolExecutor(a.workers) as ex:
            futs = []
            for u in todo:
                e = est_unit(u[3])
                while not led.reserve(e):
                    if not any(not f.done() for f in futs):
                        break
                    time.sleep(1)
                else:
                    futs.append(ex.submit(run_unit, cfg, *u, e))
                    continue
                stopped = cfg
                break
            for f in futs:
                f.result()
        final = led.final()
        n_ok = sum(final.get((u[0], u[1]), {}).get("status") == "ok" for u in units)
        n_failed = sum(final.get((u[0], u[1]), {}).get("status") == "failed" for u in units)
        info.update(units_ok=n_ok, units_failed=n_failed, units_not_run=len(units) - n_ok - n_failed,
                    state="fully judged" if n_ok + n_failed == len(units) else "partial (budget stop)",
                    spent_after_usd=round(led.spent, 4))
        status["configs"][cfg] = info
        print(f"  {cfg}: {info['state']}; ok {n_ok}, failed {n_failed}; total spent ${led.spent:.3f}", flush=True)

    final = led.final()
    out = []
    for cfg in a.configs:
        for tid, bi, batch, _, meta in units_by_cfg.get(cfg, []):
            e = final.get((tid, bi))
            for r in batch:
                if e and e["status"] == "ok":
                    v, why = e["verdicts"][r["claim_id"]]
                else:
                    v, why = ("PARSE_FAIL", e["why"]) if e else ("NOT_JUDGED", "")
                out.append({"config": cfg, "text_id": tid, "method": r["method"], "dataset": r["dataset"], "node": r["node"],
                            "batch": bi, "claim_id": r["claim_id"], "span_check": r["span_check"], "judge_verdict": v,
                            "judge_reason": why, "claim_text": r["claim_text"]})
    if not a.dry_run and out:
        with open(rd / "judgments.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    status.update(spent_usd=round(led.spent, 4), calls=len(led.calls),
                  tokens={k: sum(c["usage"].get(k, 0) for c in led.calls) for k in ("prompt", "output", "thoughts")},
                  model_versions_seen=sorted({c["model_version"] for c in led.calls if c.get("model_version")}),
                  google_genai_version=__import__("google.genai").genai.__version__,
                  price_usd_per_1M={"input": PRICE_IN, "output_incl_thinking": PRICE_OUT},
                  updated=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    if not a.dry_run:
        json.dump(status, open(rd / "run_status.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in status.items() if k != "configs"}, indent=1))


if __name__ == "__main__":
    main()
