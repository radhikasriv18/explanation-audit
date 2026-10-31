"""GraphXAIN narrations with gpt-4o-2024-08-06 for the 30+30 robustness subset.

Only the model changes vs the locked schema-aligned Llama run: prompts are read
verbatim from graphxain_schemaaligned_production_2026-08-16/{cora,products}/prompts_dump.jsonl,
sent as a single user message (as in GraphXAIN's apply_chat_template call), with
temperature 1.0, top_p 0.95, 600 output tokens. repetition_penalty=1.1 has no
OpenAI equivalent and is not applied. seed=42 is best-effort on OpenAI's side.

Usage:
  python run_gpt4o_graphxain.py --check      # free models.retrieve check only
  python run_gpt4o_graphxain.py              # all 60 nodes (resumable, skips existing)
"""
import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

from openai import OpenAI

MODEL = "gpt-4o-2024-08-06"
GEN = dict(temperature=1.0, top_p=0.95, max_completion_tokens=600, seed=42)
# USD per 1M tokens for gpt-4o-2024-08-06 (standard tier); used for the estimate only.
PRICE_IN, PRICE_OUT = 2.50, 10.00

ROOT = Path(".")
SUBSET = ROOT / "robustness_2026-10-30/robustness_subset.json"
PROMPTS = ROOT / "graphxain_schemaaligned_production_2026-08-16/{ds}/prompts_dump.jsonl"
OUT_DIR = ROOT / "robustness_2026-10-30/graphxain_gpt4o"


def load_jobs():
    subset = json.load(open(SUBSET))
    jobs = []
    for ds in ("cora", "products"):
        by_node = {}
        for line in open(str(PROMPTS).format(ds=ds)):
            rec = json.loads(line)
            assert rec["target_node"] not in by_node, f"duplicate {ds} {rec['target_node']}"
            by_node[rec["target_node"]] = rec
        for n in subset["datasets"][ds]["nodes"]:
            jobs.append((ds, n["global_node_id"], by_node[n["global_node_id"]]))
    return jobs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="only run models.retrieve (no charge)")
    args = ap.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY is not set")
    client = OpenAI()

    m = client.models.retrieve(MODEL)
    print(f"models.retrieve OK: id={m.id} owned_by={m.owned_by}")
    if args.check:
        return

    jobs = load_jobs()
    assert len(jobs) == 60, len(jobs)
    for ds in ("cora", "products"):
        (OUT_DIR / ds).mkdir(parents=True, exist_ok=True)

    for ds, nid, rec in jobs:
        out = OUT_DIR / ds / f"{nid}.json"
        if out.exists():
            continue
        for attempt in range(1, 6):
            try:
                t0 = time.time()
                r = client.chat.completions.create(
                    model=MODEL, messages=[{"role": "user", "content": rec["prompt"]}], **GEN
                )
                break
            except Exception as exc:
                print(f"[{ds} {nid}] attempt {attempt} failed: {type(exc).__name__}: {exc}")
                if attempt == 5:
                    r = None
                else:
                    time.sleep(5 * attempt)
        if r is None:
            continue
        c = r.choices[0]
        json.dump(
            {
                "dataset": ds,
                "global_node_id": nid,
                "model_requested": MODEL,
                "model_returned": r.model,
                "response_id": r.id,
                "system_fingerprint": r.system_fingerprint,
                "generation_config": GEN,
                "finish_reason": c.finish_reason,
                "usage": {"prompt_tokens": r.usage.prompt_tokens, "completion_tokens": r.usage.completion_tokens},
                "latency_s": round(time.time() - t0, 2),
                "prediction": rec["prediction"],
                "prompt": rec["prompt"],
                "narrative": c.message.content,
            },
            open(out, "w"),
            indent=1,
        )
        print(f"[{ds} {nid}] {c.finish_reason} in={r.usage.prompt_tokens} out={r.usage.completion_tokens}")

    # summary over everything on disk
    done = [json.load(open(OUT_DIR / ds / f"{nid}.json")) for ds, nid, _ in jobs if (OUT_DIR / ds / f"{nid}.json").exists()]
    tin = sum(d["usage"]["prompt_tokens"] for d in done)
    tout = sum(d["usage"]["completion_tokens"] for d in done)
    summary = {
        "success": len(done),
        "failed": [f"{ds}:{nid}" for ds, nid, _ in jobs if not (OUT_DIR / ds / f"{nid}.json").exists()],
        "finish_reasons": dict(Counter(d["finish_reason"] for d in done)),
        "prompt_tokens": tin,
        "completion_tokens": tout,
        "est_cost_usd": round(tin / 1e6 * PRICE_IN + tout / 1e6 * PRICE_OUT, 4),
        "models_returned": dict(Counter(d["model_returned"] for d in done)),
    }
    json.dump(summary, open(OUT_DIR / "run_summary.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
