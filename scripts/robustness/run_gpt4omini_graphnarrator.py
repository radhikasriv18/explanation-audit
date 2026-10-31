"""Robustness analysis 1: GraphNarrator narrations with gpt-4o-mini-2024-07-18 for the
30+30 robustness subset.

Only the model changes relative to exp100 (Cora) / exp101 (Products), base
Llama-3.1-8B-Instruct via FreeTextExpGenerator.gen(use_local_hf=True):
- same locked pkls (pkls_cora_eval, pkls_products), templates (v6 + example v1 for
  Cora, v_products for Products) and 6000-char document truncation. The user prompt
  is read verbatim from generated_expls-{100,101}/{pkl_index}.json. Rebuilding all 60
  prompts from the pkls with the same truncation matched them byte for byte (2026-10-30).
- same system message the Llama path sent ("...reliable and responsible...").
  generated_expls-*/ files record save()'s default string instead, which was never sent.
- same sampling as the Llama path: temperature 0.3, top_p 0.95, 2048 new tokens.
  seed=42 is added (best-effort on OpenAI's side); the Llama run was unseeded.
pkl index == cf_key for every subset node in both locked pkl dirs.

Usage (run with ~/openai_env):
  OPENAI_API_KEY="$(head -c 164 ~/.openai_key)" ~/openai_env/bin/python run_gpt4omini_graphnarrator.py --check
  OPENAI_API_KEY="$(head -c 164 ~/.openai_key)" ~/openai_env/bin/python run_gpt4omini_graphnarrator.py
"""
import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

from openai import OpenAI

MODEL = "gpt-4o-mini-2024-07-18"
SYSTEM = "You are a helpful, reliable and responsible AI assistant."
GEN = dict(temperature=0.3, top_p=0.95, max_completion_tokens=2048, seed=42)
# USD per 1M tokens for gpt-4o-mini-2024-07-18 (standard tier); used for the estimate only.
PRICE_IN, PRICE_OUT = 0.15, 0.60

ROOT = Path(".")
SUBSET = ROOT / "robustness_2026-10-30/robustness_subset.json"
GN_OUT = ROOT / "graphnarrCora/GraphNarrator/outputs"
SOURCE_EXP = {"cora": 100, "products": 101}
NEW_EXP = {"cora": 600, "products": 601}
OUT_DIR = ROOT / "robustness_2026-10-30/graphnarrator_gpt4omini"


def load_jobs():
    subset = json.load(open(SUBSET))
    jobs = []
    for ds in ("cora", "products"):
        for n in subset["datasets"][ds]["nodes"]:
            src = GN_OUT / f"generated_expls-{SOURCE_EXP[ds]}/{n['cf_key']}.json"
            prompt = json.load(open(src))["messages"][1]["content"]
            jobs.append((ds, n, prompt))
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
    for ds in NEW_EXP:
        (OUT_DIR / f"generated_expls-{NEW_EXP[ds]}").mkdir(parents=True, exist_ok=True)

    def out_path(ds, n):
        return OUT_DIR / f"generated_expls-{NEW_EXP[ds]}" / f"{n['cf_key']}.json"

    for ds, n, prompt in jobs:
        out = out_path(ds, n)
        if out.exists():
            continue
        messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}]
        r = None
        for attempt in range(1, 6):
            try:
                t0 = time.time()
                r = client.chat.completions.create(model=MODEL, messages=messages, **GEN)
                break
            except Exception as exc:
                print(f"[{ds} {n['global_node_id']}] attempt {attempt} failed: {type(exc).__name__}: {exc}")
                if attempt < 5:
                    time.sleep(5 * attempt)
        if r is None:
            continue
        c = r.choices[0]
        json.dump(
            {
                # same shape as FreeTextExpGenerator.save(), but with the system message actually sent
                "messages": messages + [{"role": "assistant", "content": c.message.content}],
                "dataset": ds,
                "global_node_id": n["global_node_id"],
                "pkl_index": int(n["cf_key"]),
                "source_prompt": f"generated_expls-{SOURCE_EXP[ds]}/{n['cf_key']}.json",
                "model_requested": MODEL,
                "model_returned": r.model,
                "response_id": r.id,
                "system_fingerprint": r.system_fingerprint,
                "generation_config": GEN,
                "finish_reason": c.finish_reason,
                "usage": {"prompt_tokens": r.usage.prompt_tokens, "completion_tokens": r.usage.completion_tokens},
                "latency_s": round(time.time() - t0, 2),
            },
            open(out, "w"),
            indent=1,
        )
        print(f"[{ds} {n['global_node_id']}] {c.finish_reason} in={r.usage.prompt_tokens} out={r.usage.completion_tokens}")

    done = [json.load(open(out_path(ds, n))) for ds, n, _ in jobs if out_path(ds, n).exists()]
    tin = sum(d["usage"]["prompt_tokens"] for d in done)
    tout = sum(d["usage"]["completion_tokens"] for d in done)
    summary = {
        "success": len(done),
        "failed": [f"{ds}:{n['global_node_id']}" for ds, n, _ in jobs if not out_path(ds, n).exists()],
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
