"""
Consolidate GSPELL/Products, real embedding-projection pipeline
(GSPELL_explanations.pt from job 50765167, seed=42). Unlike Cora, no
persistence wrapper was built for this job -- the prompt is not captured,
and is only PARTIALLY representable as text in the first place: this path
(generate_by="embedding", dataset.name_ != "cora") uses
build_inputs_embeds_vanilla_eos, which feeds the LLM a mix of literal text
(instructions, category label, node IDs) AND continuous GNN-embedding soft-
prompt tokens with no discrete text form (see
gspell_products/FAILURE_CHARACTERIZATION.md for the full trace). "prompt" is
therefore explicitly set to null with a reason, not fabricated or
approximated -- explanation_text is real and complete (GSPELL's own raw,
undecoded model output, native to GSPELL_explanations.pt).
"""
import json

import torch

GEN_CONFIG = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "seed": 42,
    "pipeline": "embedding-projection (generate_by='embedding', build_inputs_embeds_vanilla_eos)",
    "projector_checkpoint": "LOGIC2/GSPELL/pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/projector.pth",
    "known_issue": "reproduces known fabrication/hallucination failure -- see gspell_products/FAILURE_CHARACTERIZATION.md",
}

PROMPT_UNAVAILABLE_REASON = (
    "Not captured (no persistence wrapper built for this job) and only "
    "partially representable as text: this pipeline feeds the LLM continuous "
    "GNN-embedding soft-prompt tokens (via build_inputs_embeds_vanilla_eos), "
    "which have no discrete text form to record -- only the surrounding "
    "literal-text scaffold (instructions/category label) is text at all."
)


def consolidate():
    pt = torch.load(
        "./LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt",
        weights_only=False,
    )
    out = {}
    for node_batches in pt:
        nid = node_batches[0]["target_node"]
        parts = []
        for i, b in enumerate(node_batches):
            header = f"--- neighbor batch {i + 1} (neighbors: {b['neighbors']}) ---"
            parts.append(f"{header}\n{b['explanation']}")
        out[str(nid)] = {
            "explanation_text": "\n\n".join(parts),
            "prompt": None,
            "prompt_unavailable_reason": PROMPT_UNAVAILABLE_REASON,
            "generation_config": GEN_CONFIG,
        }

    out_path = "./production_run_2026-07-27/consolidated/gspell_products_embedding.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"{out_path}: {len(out)} nodes")


if __name__ == "__main__":
    consolidate()
