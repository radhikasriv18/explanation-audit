"""
Consolidate GraphNarrator (Cora exp_id=100, Products exp_id=101). Native
output is per-local-index JSON files (outputs/generated_expls-{id}/{local_index}.json,
{"messages": [system, user=prompt, assistant=response]}) -- local_index is
the pkl filename stem, NOT the global node ID. Mapped via each dataset's
index_to_global_node_id_mapping.json (root_global_id field read directly
from each pkl by TAG.load(), verified against the eval split -- not assumed
from file order).
"""
import json
from pathlib import Path

GEN_CONFIG = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct (local HF)",
    "max_new_tokens": 2048,
    "do_sample": True,
    "temperature": 0.3,
    "top_p": 0.95,
    "seed": 42,
}


def consolidate(exp_dir, mapping_path, out_path):
    with open(mapping_path) as f:
        mapping = json.load(f)["mapping"]
    # mapping keys are local_index (int, loaded as str from JSON)
    local_to_global = {int(k): v["root_global_id"] for k, v in mapping.items()}

    out = {}
    missing_mapping = []
    exp_dir = Path(exp_dir)
    for jf in sorted(exp_dir.glob("*.json"), key=lambda p: int(p.stem)):
        local_idx = int(jf.stem)
        global_id = local_to_global.get(local_idx)
        if global_id is None:
            missing_mapping.append(local_idx)
            continue
        with open(jf) as f:
            data = json.load(f)
        msgs = {m["role"]: m["content"] for m in data["messages"]}
        out[str(global_id)] = {
            "explanation_text": msgs.get("assistant", ""),
            "prompt": msgs.get("user", ""),
            "generation_config": GEN_CONFIG,
        }

    if missing_mapping:
        print(f"WARNING: {len(missing_mapping)} local indices had no mapping entry: {missing_mapping}")

    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"{out_path}: {len(out)} nodes")


if __name__ == "__main__":
    consolidate(
        "./graphnarrCora/GraphNarrator/outputs/generated_expls-100",
        "./production_run_2026-07-27/graphnarrator_cora/index_to_global_node_id_mapping.json",
        "./production_run_2026-07-27/consolidated/graphnarrator_cora.json",
    )
    consolidate(
        "./graphnarrCora/GraphNarrator/outputs/generated_expls-101",
        "./production_run_2026-07-27/graphnarrator_products/index_to_global_node_id_mapping.json",
        "./production_run_2026-07-27/consolidated/graphnarrator_products.json",
    )
