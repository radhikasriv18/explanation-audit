"""
Consolidate GSPELL/Products text-based fallback (LLM_explanations.pkl from
job 50783204, -m llm, literal BOW-keyword-text prompts via
build_inputs_vanilla). Native output already stores the full chat message
list (system/user/assistant) per neighbor-batch -- prompt = user message
content, explanation_text = assistant message content. No wrapper was
needed; this is byte-exact from GSPELL's own persistence.
"""
import json

import torch

GEN_CONFIG = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "seed": 42,
    "pipeline": "text-based fallback (-m llm, generate_by='tokens', build_inputs_vanilla, literal BOW keyword text)",
    "note": "does not use embedding projection; run to characterize whether the embedding-projection pipeline's fabrication failure is architecture-specific (see gspell_products/FAILURE_CHARACTERIZATION.md)",
}


def consolidate():
    pt = torch.load(
        "./LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-28-11-08-30/LLM_explanations.pkl",
        weights_only=False,
    )
    out = {}
    for node_batches in pt:
        nid = node_batches[0]["target_node"]
        expl_parts = []
        prompt_parts = []
        for i, b in enumerate(node_batches):
            header = f"--- neighbor batch {i + 1} (neighbors: {b['neighbors']}) ---"
            msgs = {m["role"]: m["content"] for m in b["explanation"]}
            expl_parts.append(f"{header}\n{msgs.get('assistant', '')}")
            prompt_parts.append(f"{header}\n{msgs.get('system', '')}\n\n{msgs.get('user', '')}")
        out[str(nid)] = {
            "explanation_text": "\n\n".join(expl_parts),
            "prompt": "\n\n".join(prompt_parts),
            "generation_config": GEN_CONFIG,
        }

    out_path = "./production_run_2026-07-27/consolidated/gspell_products_textfallback.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"{out_path}: {len(out)} nodes")


if __name__ == "__main__":
    consolidate()
