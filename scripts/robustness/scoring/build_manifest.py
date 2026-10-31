"""Collect the texts to score for the robustness experiment into texts.json.

9 configurations x 60 nodes (30 Cora + 30 Products from ../robustness_subset.json).
Scored text, as in the main results / answer key:
  GraphNarrator   "### Free-Text Explanation" section of the assistant message
                  (freetext_section, verbatim copy of grounding_judge_pilot/build_answer_key.py)
  GraphXAIN       whole narrative
  CF-GNNExplainer whole raw output
Configurations whose output file is missing (70B jobs still running) are skipped and listed;
rerun this script to add them. Existing entries never change (asserted by sha).
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

R = Path(".")
RB = R / "robustness_2026-10-30"
GN = R / "graphnarrCora/GraphNarrator/outputs"
HERE = Path(__file__).resolve().parent
OUT = HERE / "texts.json"


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def freetext_section(text):  # verbatim from grounding_judge_pilot/build_answer_key.py
    m = re.search(r"^#+\s*Free-Text Explanation\s*$", text, re.M)
    if not m:
        return None
    return text[m.end():].strip()


_cache = {}


def jload(p):
    p = str(p)
    if p not in _cache:
        _cache[p] = json.load(open(p))
    return _cache[p]


def src_cf_8b(ds, n):
    f = R / f"llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{ds}_standard_Response.json"
    return f, f"[{n['cf_key']}][1]", jload(f)[n["cf_key"]][1]


def src_cf_qwen(ds, n):
    f = RB / f"production_a100/qwen14b_gptq_int4_{ds}_Response.json"
    return f, f"[{n['cf_key']}][1]", jload(f)[n["cf_key"]][1]


def src_70b(method):
    def get(ds, n):
        f = RB / f"llama70b/{method}/{ds}/{n['global_node_id']}.json"
        d = json.load(open(f))
        assert d["status"] == "ok", (f, d["status"])
        return f, "response", d["response"]
    return get


def src_gx_8b(ds, n):
    name = "graphxain_cora_llama_2hop_narratives_full.json" if ds == "cora" else "graphxain_products_llama_narratives_fulleval.json"
    f = R / f"graphxain_schemaaligned_production_2026-08-16/{ds}/{name}"
    return f, f"[{n['global_node_id']}]", jload(f)[str(n["global_node_id"])]


def src_gx_gpt4o(ds, n):
    f = RB / f"graphxain_gpt4o/{ds}/{n['global_node_id']}.json"
    return f, "narrative", json.load(open(f))["narrative"]


def src_gn(exp_dir):
    def get(ds, n):
        e = exp_dir[ds]
        f = e / f"{n['cf_key']}.json"
        return f, "messages[assistant]", json.load(open(f))["messages"][2]["content"]
    return get


GN_70B = src_70b("graphnarrator")


def src_gn_70b(ds, n):
    f, _, full = GN_70B(ds, n)
    return f, "response", full


CONFIGS = [
    ("CF-GNNExplainer", "Llama-8B", src_cf_8b),
    ("CF-GNNExplainer", "Qwen-14B", src_cf_qwen),
    ("CF-GNNExplainer", "Llama-70B", src_70b("cf")),
    ("GraphXAIN", "Llama-8B", src_gx_8b),
    ("GraphXAIN", "GPT-4o", src_gx_gpt4o),
    ("GraphXAIN", "Llama-70B", src_70b("graphxain")),
    ("GraphNarrator", "Llama-8B", src_gn({"cora": GN / "generated_expls-100", "products": GN / "generated_expls-101"})),
    ("GraphNarrator", "gpt-4o-mini", src_gn({"cora": RB / "graphnarrator_gpt4omini/generated_expls-600",
                                              "products": RB / "graphnarrator_gpt4omini/generated_expls-601"})),
    ("GraphNarrator", "Llama-70B", src_gn_70b),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exclude", nargs="*", default=[], help="method__config ids still being generated")
    args = ap.parse_args()
    subset = json.load(open(RB / "robustness_subset.json"))
    old = {e["id"]: e for e in json.load(open(OUT))} if OUT.exists() else {}
    entries, missing = [], []
    for method, config, get in CONFIGS:
        if f"{method}__{config}" in args.exclude:
            continue
        for ds in ("cora", "products"):
            for n in subset["datasets"][ds]["nodes"]:
                tid = f"{method}__{config}__{ds}__{n['global_node_id']}"
                try:
                    f, loc, full = get(ds, n)
                except (FileNotFoundError, KeyError, AssertionError) as exc:
                    missing.append((tid, type(exc).__name__))
                    continue
                if method == "GraphNarrator":
                    scored, scope = freetext_section(full), "### Free-Text Explanation section"
                else:
                    scored, scope = full, "whole output"
                e = {"id": tid, "method": method, "config": config, "dataset": ds,
                     "node": str(n["global_node_id"]), "cf_key": n["cf_key"], "is_survey": n["is_survey"],
                     "source_file": str(f), "source_locator": loc, "scored_scope": scope,
                     "text_full": full, "text_scored": scored,
                     "text_scored_sha256_16": sha(scored) if scored else None}
                if tid in old:
                    assert old[tid]["text_scored_sha256_16"] == e["text_scored_sha256_16"], f"{tid} changed"
                entries.append(e)
    json.dump(entries, open(OUT, "w"), indent=1)
    no_scope = [e["id"] for e in entries if not e["text_scored"]]
    print(f"texts.json: {len(entries)} texts; missing sources: {len(missing)}; empty scored text: {len(no_scope)} {no_scope}")
    by = {}
    for e in entries:
        by[(e["method"], e["config"])] = by.get((e["method"], e["config"]), 0) + 1
    for k, v in by.items():
        print(f"  {k[0]:16s} {k[1]:12s} {v}")
    if missing:
        print("  missing:", sorted({m[0].rsplit('__', 2)[0] for m in missing}))


if __name__ == "__main__":
    main()
