"""
Entity graph complexity for CF-GNNExplainer (edge-removal counterfactual --
distinct from CF-GNNFeatures/llm-graph-cf, already computed elsewhere).

SCOPE CORRECTION (2026-09-07): a full-scale run exists, not just the
8-survey-node one. Confirmed via ./cf_gnnexplainer_run_2026-08-10/README.md:
  - Counterfactual-search coverage: Cora 198/542 (36.5%), Products 60/200 (30.0%)
    -- expected per methodology (edge removal only indirectly influences a
    GraphSAGE prediction), not a bug.
  - LLM-narration coverage (of the above): Cora 184/198 (14 skipped -- prompt
    too long, up to ~51k tokens), Products 60/60 (none skipped).
  - `cf_gnnexplainer_run_2026-08-10/cora/` and `.../products/` are EMPTY --
    the real generation output lives in llm-graph-cf/data/{cora,products}/
    cf-gnnexplainer-canonical/ and llm-graph-cf/data/results/
    cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{cora,products}_standard_Response.json
    (184 and 60 entries respectively, matching the README exactly).
This script computes entity graph complexity on the FULL 184+60, and
separately reports the 8-survey-node subset (5 with real text: Cora 510,
2334, 1062; Products 1852, 8438 -- 884/6813/8766 have no counterfactual at
all, consistent with the grounding precision/recall work already done).

Consolidation mirrors consolidate_llmgraphcf.py's approach exactly (same
response-list-format, same target_dict Target_Node_ID mapping) -- read-only,
does not modify any source file.

Entity-extraction: numeric-only for Cora (no neighbours arg), title/brand
fallback for Products (neighbor_titles_full.json), consistent with how
GraphXAIN/GraphNarrator/llm-graph-cf(CF-GNNFeatures) were already computed
in this project.

Dict-literal vs. prose question (point 4): verified directly on a real
sample (Cora key 0, target node 1) -- ENTITY_REF_RE requires the literal
word "Node"/"Article"/"Product" immediately before the number (or bare
"ROOT"). Bare numbers inside dict-literal lists like
`Factual_Target_Node_Neighbors = [344]` or a raw comma list `316, 335, 348,
...` are NOT preceded by that word and are correctly excluded automatically
-- no special-casing needed. Natural-language citations like "the node 1"
or "the node 344" (including ones appearing inside the dict's own
Natural_Language_Explanation string value, which is genuine prose, not
structural list data) ARE matched, which is the intended, consistent
behavior -- confirmed on the sample: 8 matches (node 1 x5, node 344 x3),
zero contamination from the bare neighbor-id list in the same text.
"""
import importlib.util
import json
import sys

sys.path.insert(0, "./graphnarrCora/GraphNarrator")

CTM_PATH = "./compute_text_metrics.py"
spec = importlib.util.spec_from_file_location("compute_text_metrics", CTM_PATH)
ctm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctm)

OUT_DIR = "./grounding_recall_f1_2026-09-07"
NEIGHBOR_TITLES_FULL = "./production_run_2026-07-27/consolidated/neighbor_titles_full.json"

SURVEY_NODES = {
    "cora": {510, 2334, 1062, 884},
    "products": {6813, 1852, 8766, 8438},
}

SOURCES = {
    "cora": {
        "response": "./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json",
        "target_dict": "./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json",
        "neighbours": False,
    },
    "products": {
        "response": "./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json",
        "target_dict": "./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json",
        "neighbours": True,
    },
}


def consolidate(response_path, target_dict_path):
    responses = json.load(open(response_path))
    target_dict = json.load(open(target_dict_path))
    out = {}
    for key, (prompt, text) in responses.items():
        if key not in target_dict:
            continue
        global_id = target_dict[key]["Target_Node_ID"]
        out[global_id] = text
    return out


def main():
    neighbour_data = json.load(open(NEIGHBOR_TITLES_FULL))
    all_rows = {}

    for ds, cfg in SOURCES.items():
        texts = consolidate(cfg["response"], cfg["target_dict"])
        rows = []
        for global_id, text in texts.items():
            h = ctm.halstead(text)
            neighbours = neighbour_data.get(str(global_id), {}).get("neighbors") if cfg["neighbours"] else None
            e = ctm.entity_measures(text, neighbours, h["length_N"])
            rows.append({
                "node": global_id, "length_N_words": h["length_N"],
                "S_entities": e["S_entities"], "T_relations": e["T_relations"],
                "C_state": e["C_state"], "C_fan": round(e["C_fan"], 4),
                "C_cycle": e["C_cycle"], "C_density": round(e["C_density"], 4),
                "C_state_per100w": round(e["C_state_per100w"], 4),
                "C_cycle_per100w": round(e["C_cycle_per100w"], 4),
            })
        rows.sort(key=lambda r: r["node"])
        all_rows[ds] = rows

        out_path = f"{OUT_DIR}/metrics_entity_complexity_cf_gnnexplainer_{ds}.csv"
        import csv
        with open(out_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote {out_path} ({len(rows)} rows)")

        import statistics as stats
        cstates = [r["C_state"] for r in rows]
        ccycles = [r["C_cycle"] for r in rows]
        print(f"  {ds}: n={len(rows)}  mean C_state={stats.mean(cstates):.3f}  median={stats.median(cstates):.3f}  "
              f"mean C_cycle={stats.mean(ccycles):.3f}  C_state>0 count={sum(1 for c in cstates if c>0)}/{len(cstates)}")

        print(f"  {ds} survey-node subset:")
        by_node = {r["node"]: r for r in rows}
        for nid in sorted(SURVEY_NODES[ds]):
            r = by_node.get(nid)
            if r:
                print(f"    node {nid}: {r}")
            else:
                print(f"    node {nid}: NO COUNTERFACTUAL / NO NARRATION (excluded, consistent with grounding precision/recall scope)")


if __name__ == "__main__":
    main()
