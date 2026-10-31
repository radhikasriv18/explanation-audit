"""
Consolidate GraphXAIN's per-node persistence log (explainer_and_prompts.jsonl,
already keyed by real global node ID -- target_node in that file IS the
global node ID used throughout the run, e.g. matching test_idx/eval_idx)
into {global_node_id: {explanation_text, prompt, generation_config}}.
"""
import json

GEN_CONFIG = {
    "temperature": 1.0,
    "top_p": 0.95,
    "do_sample": True,
    "repetition_penalty": 1.1,
    "max_new_tokens": 600,
    "seed": 42,
}


def consolidate(jsonl_path, out_path):
    out = {}
    with open(jsonl_path) as f:
        for line in f:
            rec = json.loads(line)
            nid = str(rec["target_node"])
            out[nid] = {
                "explanation_text": rec["raw_llm_output"],
                "prompt": rec["prompt"],
                "generation_config": GEN_CONFIG,
            }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"{out_path}: {len(out)} nodes")
    return out


if __name__ == "__main__":
    consolidate(
        "./production_run_2026-07-27/graphxain_cora/explainer_and_prompts.jsonl",
        "./production_run_2026-07-27/consolidated/graphxain_cora.json",
    )
    consolidate(
        "./production_run_2026-07-27/graphxain_products/explainer_and_prompts.jsonl",
        "./production_run_2026-07-27/consolidated/graphxain_products.json",
    )
