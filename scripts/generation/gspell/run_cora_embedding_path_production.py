"""
Additive persistence wrapper around GSPELL's Cora pipeline, forced down the
projected-embedding generation path (build_inputs_embeds_vanilla_eos) via the
new -fep/--force_embedding_path flag added to eval_utils.generate_exp_by_llm
and main.py.

Does NOT change eval_utils.py's build_inputs_cora_bow (text path stays
untouched and remains the default when -fep is absent) and does NOT retrain
the projector -- it loads the existing seed-42 Cora projector checkpoint from
2026-03-09-23-12-28 (the same one used for the original text-path survey
stimuli), verified by md5 below.

Modeled on run_cora_production_with_persistence.py (the text-path wrapper),
adapted because build_inputs_embeds_vanilla_eos returns a tensor of
interleaved text+soft-prompt embeddings, not decodable token ids. This
wrapper:
  1. Calls the real, unmodified build_inputs_embeds_vanilla_eos to get the
     exact embeddings tensor handed to model.generate (untouched).
  2. Independently reconstructs a human-readable prompt transcript using the
     same literal string templates as the real function, with a
     <<PROJECTED EMBEDDING (k=5 tokens)>> placeholder wherever soft-prompt
     tokens are spliced in (matching the paper's own Figure 2/3 convention).
  3. Records a sha256 checksum of each spliced-in embedding segment (target
     node's and each neighbor's) so the numeric provenance back to the
     projector's actual output is independently verifiable, not just the
     human-readable skeleton.
  4. Records the raw generated text exactly as GSPELL's own
     generate_exp_by_llm already does inside GSPELL_explanations.pt -- this
     wrapper only adds the missing prompt-side piece.

Writes to a brand-new directory; does not touch
production_run_2026-07-27/gspell_cora (text-path survey stimuli + full run)
or GSPELL's own output/cora-meta-llama/*-2026-05-22-20-50-49 directory.
"""
import hashlib
import json
import os
import sys
import time

import torch

REPO = "./LOGIC2/GSPELL"
PROD_DIR = "./production_run_2026-07-27/gspell_cora_embedding_path_2026-08-10"
os.makedirs(PROD_DIR, exist_ok=True)
PROMPT_LOG_PATH = f"{PROD_DIR}/prompts_raw.jsonl"
CHECKPOINT_MD5_PATH = f"{PROD_DIR}/checkpoint_md5.json"

os.chdir(REPO)
sys.path.insert(0, REPO)

GNN_PATH = "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/sage.pth"
DATA_PATH = "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth"
PROJECTOR_PATH = "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-23-12-28/projector.pth"

sys.argv = [
    "main.py",
    "-cff", "./config/cora.yaml",
    "-m", "gspell",
    "-wno",
    "-fep",
    "--cora_data_path", "./cora_canonical.pt",
    "--split_path", "./cora_splits_seed42.npz",
    "-pgp", GNN_PATH,
    "-pdp", DATA_PATH,
    "-ppp", PROJECTOR_PATH,
    "--seed", "42",
]


def _md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


checkpoint_md5 = {
    "projector_checkpoint": PROJECTOR_PATH,
    "projector_md5": _md5(PROJECTOR_PATH),
    "gnn_checkpoint": GNN_PATH,
    "gnn_md5": _md5(GNN_PATH),
    "data_canonical": DATA_PATH,
    "data_canonical_md5": _md5(DATA_PATH),
    "note": "projector is the pre-existing seed-42 Cora projector trained 2026-03-09-23-12-28; "
            "loaded via -ppp, NOT retrained. Same checkpoint used for the original text-path "
            "survey run (2026-05-22-20-50-49), confirmed identical path in that run's logged "
            "argparse Namespace.",
    "timestamp": time.time(),
}
with open(CHECKPOINT_MD5_PATH, "w") as f:
    json.dump(checkpoint_md5, f, indent=2)
print(f"Checkpoint md5s written to {CHECKPOINT_MD5_PATH}")
print(json.dumps(checkpoint_md5, indent=2))

import eval_utils  # noqa: E402

_orig_build_inputs_embeds_vanilla_eos = eval_utils.build_inputs_embeds_vanilla_eos


def _sha256_tensor(t):
    # bfloat16 has no numpy equivalent -- numpy() fails directly on it (TypeError:
    # Got unsupported ScalarType BFloat16). Upcast to float32 for hashing only;
    # the real tensor handed to model.generate below is untouched.
    return hashlib.sha256(t.detach().to("cpu", dtype=torch.float32).contiguous().numpy().tobytes()).hexdigest()


def _instrumented(embed_func, tokenizer, gnn_embeds, gnn_preds, target_node,
                   selected_neighbors, dataset, with_chat_template, descriptive_prompt):
    full_embeds = _orig_build_inputs_embeds_vanilla_eos(
        embed_func, tokenizer, gnn_embeds, gnn_preds, target_node,
        selected_neighbors, dataset, with_chat_template, descriptive_prompt
    )

    system_message, user_intro, node_type = eval_utils.get_characterization(
        dataset, target_node, dataset._data.label_info[str(gnn_preds[target_node].item())]
    )
    predicted_label = dataset._data.label_info[str(gnn_preds[target_node].item())]
    placeholder = f"<<PROJECTED EMBEDDING (k={gnn_embeds.shape[1]} tokens)>>"

    skeleton_parts = [
        f"[SYSTEM] {system_message}",
        f"[USER] {user_intro}",
        f"\n\nTarget {node_type} Embedding Representation:\n<<BEGIN TARGET KEYWORDS>> {placeholder} <<END TARGET KEYWORDS>>",
        f"\nNeighboring {node_type}s in the Network:\nEach {node_type} below is described by keywords.\n",
    ]
    embed_checksums = {"target_node": {"id": target_node, "sha256": _sha256_tensor(gnn_embeds[target_node])}}
    neighbor_checksums = []
    for nid in selected_neighbors:
        skeleton_parts.append(f"\n- {node_type} {nid}:\n<<BEGIN KEYWORDS>> {placeholder} <<END KEYWORDS>>")
        neighbor_checksums.append({"id": nid, "sha256": _sha256_tensor(gnn_embeds[nid])})
    embed_checksums["neighbors"] = neighbor_checksums

    desciprtion_req = f"""\n\t3. For better understanding, justify your reasoning by **one sentence** to **generally** clarify what are the common patterns among the supporting {node_type}s \
to explain the classification into '{predicted_label}. Give this reasoning after marking all neighbors at the end by Reasoning:<YOURE_REASONING_GOES_HERE>'. \n""" if descriptive_prompt else "\n"
    instructions_text = f"""
        Instructions:
        You are given a target {node_type} and a list of neighboring {node_type}s, each described by keywords.

        For each neighboring {node_type}:
        1. Clearly state whether this {node_type} supports the classification of the Target {node_type} into category '{predicted_label}'.{desciprtion_req}
        Use the following format for each neighbor:

        {node_type} <ID>:
        Support: YES or NO — Does this {node_type} support the classification into '{predicted_label}'?

        Base your reasoning only on the keywords and proximity to the target {node_type}.

        Start your analysis below:
    """
    skeleton_parts.append(instructions_text)
    reconstructed_prompt_skeleton = "".join(skeleton_parts)

    record = {
        "target_node": target_node,
        "neighbors": list(selected_neighbors),
        "predicted_category_in_prompt": predicted_label,
        "prompt_skeleton_with_embedding_placeholders": reconstructed_prompt_skeleton,
        "full_embeds_shape": list(full_embeds.shape),
        "embedding_segment_checksums": embed_checksums,
        "note": "prompt is a tensor of interleaved text+soft-prompt embeddings, not text; "
                "the skeleton above reconstructs the literal text segments verbatim from "
                "build_inputs_embeds_vanilla_eos's own templates, with a placeholder marking "
                "where each 5-token projected embedding is spliced in. The full_embeds tensor "
                "actually passed to model.generate is untouched by this wrapper.",
        "timestamp": time.time(),
    }
    with open(PROMPT_LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")
    return full_embeds


eval_utils.build_inputs_embeds_vanilla_eos = _instrumented

import runpy  # noqa: E402

runpy.run_path("main.py", run_name="__main__")
