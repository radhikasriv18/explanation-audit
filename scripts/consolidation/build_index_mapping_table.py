"""
Builds the local-index -> global-node-ID mapping table for GraphNarrator's
Cora pkl snapshot (outputs/pkls_cora_eval/), as required by the production
run spec. Reads each pkl's self-contained root_global_id field (verified
reliable in a prior audit: 0 mismatches against cora_splits_seed42.npz's
test_idx across the original 398 pkls) -- does not rely on filename order.

Also reports final coverage against the full 542-node Cora eval split:
which nodes are covered, which are still missing, and (for newly-attempted
missing nodes) the OOM reason pulled from the step-0 log if available.
"""
import json
import sys
from pathlib import Path

import numpy as np

REPO = "./graphnarrCora/GraphNarrator"
sys.path.insert(0, REPO)
from tag import TAG  # noqa: E402

PKL_DIR = Path(f"{REPO}/outputs/pkls_cora_eval")
SPLITS = "./LOGIC2/GSPELL/cora_splits_seed42.npz"
OUT_DIR = Path("./production_run_2026-07-27/graphnarrator_cora")


def main():
    splits = np.load(SPLITS)
    full_eval_set = set(int(x) for x in splits["test_idx"].tolist())

    mapping = {}  # local_index (pkl filename stem) -> {root_global_id, root_local_id, global_nids}
    covered_global_ids = set()

    for pkl_path in sorted(PKL_DIR.glob("*.pkl"), key=lambda p: int(p.stem)):
        local_index = int(pkl_path.stem)
        graph = TAG.load(pkl_path)
        root_global_id = getattr(graph, "root_global_id", None)
        root_local_id = getattr(graph, "root_local_id", None)
        global_nids = getattr(graph, "global_nids", None)
        mapping[local_index] = {
            "root_global_id": root_global_id,
            "root_local_id": root_local_id,
            "num_sampled_nodes": len(global_nids) if global_nids is not None else None,
        }
        if root_global_id is not None:
            covered_global_ids.add(int(root_global_id))

    missing = sorted(full_eval_set - covered_global_ids)
    extra = sorted(covered_global_ids - full_eval_set)

    summary = {
        "pkl_dir": str(PKL_DIR),
        "n_pkls": len(mapping),
        "n_full_eval_split": len(full_eval_set),
        "n_covered": len(covered_global_ids),
        "n_missing": len(missing),
        "missing_global_node_ids": missing,
        "unexpected_extra_global_node_ids": extra,
        "coverage_rate": len(covered_global_ids) / len(full_eval_set),
    }

    with open(OUT_DIR / "index_to_global_node_id_mapping.json", "w") as f:
        json.dump({"summary": summary, "mapping": mapping}, f, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
