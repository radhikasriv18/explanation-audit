"""Build the 30-node-per-dataset robustness-experiment subset (2026-10-30).

Pool = locked LLM-judge CF scope: CF-GNNExplainer nodes that have a
Llama-3.1-8B narration, minus Cora local keys 3, 67, 71, 192, 260, 262, 532
(-> 177 Cora / 60 Products). Survey nodes are always included; the rest are
drawn with numpy.random.default_rng(42) without replacement from the pool
sorted by global node ID. Read-only on all inputs; writes only
robustness_subset.json next to this script.
"""
import json
import os

import numpy as np

ROOT = "."
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SEED = 42
N_PER_DATASET = 30

CFG = {
    "cora": {
        "split": f"{ROOT}/LOGIC2/GSPELL/cora_splits_seed42.npz",
        "excluded_keys": {"3", "67", "71", "192", "260", "262", "532"},
        "survey": [510, 2334, 1062],
        "expected_pool": 177,
        "graphxain": f"{ROOT}/graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json",
    },
    "products": {
        "split": f"{ROOT}/LOGIC2/GSPELL/products_splits_seed42.npz",
        "excluded_keys": set(),
        "survey": [1852, 8438],
        "expected_pool": 60,
        "graphxain": f"{ROOT}/graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json",
    },
}


def load_eval(split_path):
    s = np.load(split_path)
    return (s["eval_idx"] if "eval_idx" in s.files else s["test_idx"]).tolist()


def build(ds, cfg):
    cf_dir = f"{ROOT}/llm-graph-cf/data/{ds}/cf-gnnexplainer-canonical"
    targets = json.load(open(f"{cf_dir}/random_seed_42_counterfactual_target_dict_repr.json"))
    resp = json.load(open(f"{ROOT}/llm-graph-cf/data/results/"
                          f"cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{ds}_standard_Response.json"))

    pool = {targets[k]["Target_Node_ID"]: k for k in resp if k not in cfg["excluded_keys"]}
    assert len(pool) == cfg["expected_pool"], f"{ds}: pool {len(pool)} != {cfg['expected_pool']}"
    for s in cfg["survey"]:
        assert s in pool, f"{ds}: survey node {s} not in pool"

    rest = sorted(g for g in pool if g not in cfg["survey"])
    n_draw = N_PER_DATASET - len(cfg["survey"])
    rng = np.random.default_rng(SEED)
    drawn = [int(x) for x in rng.choice(rest, size=n_draw, replace=False)]

    nodes = [{"global_node_id": g, "cf_key": pool[g], "dataset": ds, "is_survey": g in cfg["survey"]}
             for g in sorted(cfg["survey"] + drawn)]
    return nodes, len(pool), len(rest)


def verify(ds, cfg, nodes):
    ev = load_eval(cfg["split"])
    targets = json.load(open(f"{ROOT}/llm-graph-cf/data/{ds}/cf-gnnexplainer-canonical/"
                             f"random_seed_42_counterfactual_target_dict_repr.json"))
    resp = json.load(open(f"{ROOT}/llm-graph-cf/data/results/"
                          f"cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{ds}_standard_Response.json"))
    gx = json.load(open(cfg["graphxain"]))
    failures = []
    for n in nodes:
        g, k = n["global_node_id"], n["cf_key"]
        if not (ev[int(k)] == g == targets[k]["Target_Node_ID"]):
            failures.append((g, "key->global mismatch"))
        r = resp.get(k)
        if not (isinstance(r, list) and len(r) == 2 and isinstance(r[1], str) and r[1].strip()):
            failures.append((g, "missing/empty CF narration"))
        t = gx.get(str(g))
        if not (isinstance(t, str) and t.strip()):
            failures.append((g, "missing/empty GraphXAIN narrative"))
    return failures


def main():
    out = {"seed": SEED, "n_per_dataset": N_PER_DATASET, "datasets": {}}
    for ds, cfg in CFG.items():
        nodes, pool_n, rest_n = build(ds, cfg)
        failures = verify(ds, cfg, nodes)
        print(f"{ds}: pool={pool_n} non-survey candidates={rest_n} subset={len(nodes)} failures={failures}")
        print("  ids:", [n["global_node_id"] for n in nodes])
        out["datasets"][ds] = {"pool_size": pool_n, "excluded_cf_keys": sorted(cfg["excluded_keys"], key=int),
                               "nodes": nodes}
    path = os.path.join(OUT_DIR, "robustness_subset.json")
    assert not os.path.exists(path), f"{path} exists; refusing to overwrite"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", path)


if __name__ == "__main__":
    main()
