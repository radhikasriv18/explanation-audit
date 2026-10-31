"""
Entity graph complexity for GraphNarrator, using the confirmed untruncated,
checkpoint-correct sources (NOT the truncated production run already in
metrics_per_text_{cora,products}.csv):

  Cora:     outputs/generated_expls-3      (519/519 nodes, outputs/pkls checkpoint --
            confirmed node 510 = Neural_Networks, matching every other analysis
            this project has used)
  Products: outputs/generated_expls-20     (199/200 nodes, pkls_products checkpoint --
            confirmed Beauty/HPC/Beauty/HPC for the 4 survey nodes)

Reuses ENTITY_REF_RE and entity_measures()/entity_counts() from
compute_text_metrics.py UNCHANGED (imported by absolute path, module code
never edited). Only the extraction step (reading generated_expls-3/-20's
{"messages":[...]} format instead of the survey .txt files) is new.

Entity-extraction approach matches what compute_text_metrics_production.py
already does per dataset (checked directly before writing this):
  - Cora:     neighbours=None -- numeric "Node/Article N"/"ROOT" citations only,
              no title fallback (matches run_dataset("cora", CORA_METHOD_FILES,
              None, out_dir) in the production script).
  - Products: neighbours=<real product graph 1-hop/2-hop neighbor titles for
              that node, from neighbor_titles_full.json> -- title/brand-word
              longest-match fallback IS active (matches
              run_dataset("products", PRODUCTS_METHOD_FILES,
              neighbor_titles_full.json, out_dir) in the production script).
              neighbor_titles_full.json is keyed by real graph node id and
              reflects actual product-graph structure, not method output, so
              it applies to GraphNarrator's Products nodes exactly as it does
              to GraphXAIN's.

Does NOT modify metrics_per_text_cora.csv / metrics_per_text_products.csv,
generated_expls-3, generated_expls-20, or compute_text_metrics.py -- writes
only two new CSVs.
"""
import csv
import glob
import importlib.util
import json
import os
import sys

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from tag import TAG  # noqa: E402

CTM_PATH = "./compute_text_metrics.py"
spec = importlib.util.spec_from_file_location("compute_text_metrics", CTM_PATH)
ctm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctm)  # unmodified: halstead(), entity_measures(), ENTITY_REF_RE all reused as-is

OUT_DIR = "./grounding_recall_f1_2026-09-07"

CORA_EXPL_DIR = "./graphnarrCora/GraphNarrator/outputs/generated_expls-3"
CORA_PKL_DIR = "./graphnarrCora/GraphNarrator/outputs/pkls"

PRODUCTS_EXPL_DIR = "./graphnarrCora/GraphNarrator/outputs/generated_expls-20"
PRODUCTS_PKL_DIR = "./graphnarrCora/GraphNarrator/outputs/pkls_products"
NEIGHBOR_TITLES_FULL = "./production_run_2026-07-27/consolidated/neighbor_titles_full.json"

FIELDNAMES = [
    "node", "length_N_words", "S_entities", "T_relations",
    "C_state", "C_fan", "C_cycle", "C_density",
    "C_state_per100w", "C_cycle_per100w",
]


def position_to_global(pkl_dir):
    mapping = {}
    for f in glob.glob(os.path.join(pkl_dir, "*.pkl")):
        pos = int(os.path.basename(f).split(".")[0])
        g = TAG.load(f)
        mapping[pos] = g.root_global_id
    return mapping


def compute_rows(expl_dir, pkl_dir, neighbour_data=None):
    pos_to_global = position_to_global(pkl_dir)
    rows = []
    for f in sorted(glob.glob(os.path.join(expl_dir, "*.json")), key=lambda p: int(os.path.basename(p).split(".")[0])):
        pos = int(os.path.basename(f).split(".")[0])
        global_id = pos_to_global.get(pos)
        if global_id is None:
            continue  # position not present in this checkpoint's pkl set -- skip, not a gap in exp_id-3/-20 itself
        data = json.load(open(f))
        text = data["messages"][2]["content"]  # assistant response = explanation_text
        h = ctm.halstead(text)
        neighbours = None
        if neighbour_data is not None:
            neighbours = neighbour_data.get(str(global_id), {}).get("neighbors")
        e = ctm.entity_measures(text, neighbours, h["length_N"])
        rows.append({
            "node": global_id,
            "length_N_words": h["length_N"],
            "S_entities": e["S_entities"],
            "T_relations": e["T_relations"],
            "C_state": e["C_state"],
            "C_fan": round(e["C_fan"], 4),
            "C_cycle": e["C_cycle"],
            "C_density": round(e["C_density"], 4),
            "C_state_per100w": round(e["C_state_per100w"], 4),
            "C_cycle_per100w": round(e["C_cycle_per100w"], 4),
        })
    return rows


def write_csv(rows, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path} ({len(rows)} rows)")


def summarize(rows, label):
    import statistics as stats
    print(f"\n=== {label}: n={len(rows)} ===")
    for field in ("S_entities", "C_state", "C_fan", "C_cycle", "C_density", "C_state_per100w", "C_cycle_per100w"):
        vals = [r[field] for r in rows]
        print(f"  {field:18s} mean={stats.mean(vals):8.3f}  median={stats.median(vals):8.3f}  "
              f"min={min(vals):8.3f}  max={max(vals):8.3f}")


def main():
    cora_rows = compute_rows(CORA_EXPL_DIR, CORA_PKL_DIR, neighbour_data=None)
    write_csv(cora_rows, os.path.join(OUT_DIR, "metrics_entity_complexity_graphnarrator_cora.csv"))
    summarize(cora_rows, "GraphNarrator Cora (exp_id=3, untruncated)")

    neighbour_data = json.load(open(NEIGHBOR_TITLES_FULL))
    products_rows = compute_rows(PRODUCTS_EXPL_DIR, PRODUCTS_PKL_DIR, neighbour_data=neighbour_data)
    write_csv(products_rows, os.path.join(OUT_DIR, "metrics_entity_complexity_graphnarrator_products.csv"))
    summarize(products_rows, "GraphNarrator Products (exp_id=20, untruncated)")

    print("\n=== Survey node spot-check ===")
    cora_by_node = {r["node"]: r for r in cora_rows}
    for nid in (510, 2334, 1062, 884):
        r = cora_by_node.get(nid)
        print(f"  Cora node {nid}: {r}")
    products_by_node = {r["node"]: r for r in products_rows}
    for nid in (6813, 1852, 8766, 8438):
        r = products_by_node.get(nid)
        print(f"  Products node {nid}: {r}")


if __name__ == "__main__":
    main()
