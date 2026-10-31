"""
Consolidate GSPELL/Cora. Native output is batched by neighbor-group (up to
llm_node_batch_size=5 neighbors per LLM call, several batches per node for
nodes with >5 2-hop neighbors) across two sources that must be joined:
  - GSPELL_explanations.pt: [[{target_node, neighbors, explanation}, ...], ...]
    (raw LLM output per batch, GSPELL's own native persistence)
  - prompts_raw.jsonl: {target_node, neighbors, predicted_category_in_prompt,
    prompt, timestamp} per batch (this run's persistence-wrapper capture)

Both target_node values are already the real global node ID (confirmed:
eval_utils.py passes GLOBAL node IDs throughout, batch loop iterates
`nx.ego_graph(G, node_idx, ...)` where node_idx comes directly from
`eval_config["node_ids"]` = the real test_idx list).

Joined by (target_node, tuple(neighbors)) -- verified 1:1, both files have
exactly 4103 batch entries in the same order. Batches for the same node are
concatenated into one explanation_text / prompt string with clear separators
(GSPELL splits generation across multiple LLM calls per node when a node has
more than 5 2-hop neighbors -- concatenation, not truncation).
"""
import json

import torch

GEN_CONFIG = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "sampling": "HF default (no explicit temperature override in generate_exp_by_llm)",
    "seed": 42,
    "llm_node_batch_size": 5,
    "note": "multiple neighbor-batch LLM calls per node are concatenated below with '--- neighbor batch N (neighbors: ...) ---' separators",
}


def consolidate():
    pt = torch.load(
        "./LOGIC2/GSPELL/output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-14-17-08/GSPELL_explanations.pt",
        weights_only=False,
    )
    prompts = {}
    with open("./production_run_2026-07-27/gspell_cora/prompts_raw.jsonl") as f:
        for line in f:
            rec = json.loads(line)
            key = (rec["target_node"], tuple(rec["neighbors"]))
            prompts[key] = rec["prompt"]

    by_node = {}
    unmatched = 0
    for node_batches in pt:
        for batch in node_batches:
            nid = batch["target_node"]
            key = (nid, tuple(batch["neighbors"]))
            prompt = prompts.get(key)
            if prompt is None:
                unmatched += 1
            by_node.setdefault(nid, []).append(
                {"neighbors": batch["neighbors"], "explanation": batch["explanation"], "prompt": prompt}
            )

    print(f"unmatched batches (no captured prompt found): {unmatched} / {sum(len(v) for v in by_node.values())}")

    out = {}
    for nid, batches in by_node.items():
        expl_parts = []
        prompt_parts = []
        for i, b in enumerate(batches):
            header = f"--- neighbor batch {i + 1} (neighbors: {b['neighbors']}) ---"
            expl_parts.append(f"{header}\n{b['explanation']}")
            prompt_parts.append(f"{header}\n{b['prompt']}")
        out[str(nid)] = {
            "explanation_text": "\n\n".join(expl_parts),
            "prompt": "\n\n".join(prompt_parts),
            "generation_config": GEN_CONFIG,
        }

    out_path = "./production_run_2026-07-27/consolidated/gspell_cora.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"{out_path}: {len(out)} nodes")


if __name__ == "__main__":
    consolidate()
