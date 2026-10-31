"""
Consolidate llm-graph-cf (Cora, Products). Native output is
responses[sequential_key] = (prompt, generated_text) -- sequential_key is
NOT the global node ID. Mapped via factual_target_dict_repr.json[key]
["Target_Node_ID"], built from the same entry_idx/target_global pair in the
same cf_gnnfeatures.py loop iteration that wrote both files (single source
of truth -- verified response keys are a strict subset of target_dict keys,
and all mapped global IDs are unique, for both datasets, before running this).
"""
import json

GEN_CONFIG = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct (llama_8B)",
    "temperature": 0.1,
    "top_p": 0.8,
    "repetition_penalty": 1.05,
    "max_tokens": 2048,
    "seed": 42,
    "sampler": "vLLM SamplingParams(seed=42) -- seed now genuinely threaded through (see standardization_notes.md deviation note)",
}


def consolidate(response_path, target_dict_path, out_path):
    with open(response_path) as f:
        responses = json.load(f)
    with open(target_dict_path) as f:
        target_dict = json.load(f)

    out = {}
    unmapped = []
    for key, (prompt, text) in responses.items():
        if key not in target_dict:
            unmapped.append(key)
            continue
        global_id = target_dict[key]["Target_Node_ID"]
        out[str(global_id)] = {
            "explanation_text": text,
            "prompt": prompt,
            "generation_config": GEN_CONFIG,
        }

    if unmapped:
        print(f"WARNING: {len(unmapped)} response keys had no target_dict entry: {unmapped}")
    if len(out) != len(responses) - len(unmapped):
        print("WARNING: output count mismatch after mapping")

    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"{out_path}: {len(out)} nodes (from {len(responses)} response entries)")


if __name__ == "__main__":
    consolidate(
        "./llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json",
        "./llm-graph-cf/data/cora/cf-gnnfeatures-canonical-production-2026-07-27/random_seed_42_factual_target_dict_repr.json",
        "./production_run_2026-07-27/consolidated/llmgraphcf_cora.json",
    )
    consolidate(
        "./llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json",
        "./llm-graph-cf/data/products/cf-gnnfeatures-canonical-production-2026-07-27/random_seed_42_factual_target_dict_repr.json",
        "./production_run_2026-07-27/consolidated/llmgraphcf_products.json",
    )
