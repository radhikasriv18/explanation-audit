"""
Generation run using the newly-retrained (canonical-embedding-sourced) Cora
projector, forced down the embedding path. Parameterized by env vars so the
same script serves both Step 3 (sanity check, small custom split) and
Step 4 (full 542-node test set) without duplicating the wrapper logic.

Env vars:
  SPLIT_PATH   -- path to .npz split file (default: full test set)
  OUT_SUBDIR   -- subdirectory name under production_run_2026-07-27/ for
                  this run's persisted prompts/checksums (required)
  PROJECTOR_PATH -- path to projector.pth (default: new canonical-trained one)

Same persistence pattern as run_cora_embedding_path_production.py (which
produced job 51180082's output): monkeypatches build_inputs_embeds_vanilla_eos
to log a reconstructed prompt skeleton + per-node embedding checksums,
without touching eval_utils.py. -m gspell -fep, seed 42 throughout.
"""
import hashlib
import json
import os
import sys
import time

import torch

_orig_load = torch.load
def _default_cpu_map(*a, **k):
    k.setdefault("map_location", "cpu")
    return _orig_load(*a, **k)
torch.load = _default_cpu_map

REPO = "./LOGIC2/GSPELL"
OUT_SUBDIR = os.environ["OUT_SUBDIR"]
SPLIT_PATH = os.environ.get("SPLIT_PATH", "./cora_splits_seed42.npz")
PROJECTOR_PATH = os.environ.get(
    "PROJECTOR_PATH",
    "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-canonical-projector-retrain-2026-08-16/projector.pth",
)

PROD_DIR = f"./production_run_2026-07-27/{OUT_SUBDIR}"
os.makedirs(PROD_DIR, exist_ok=True)
PROMPT_LOG_PATH = f"{PROD_DIR}/prompts_raw.jsonl"
CHECKPOINT_MD5_PATH = f"{PROD_DIR}/checkpoint_md5.json"

os.chdir(REPO)
sys.path.insert(0, REPO)

GNN_PATH = "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/sage.pth"
DATA_PATH = "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth"

sys.argv = [
    "main.py",
    "-cff", "./config/cora.yaml",
    "-m", "gspell",
    "-wno",
    "-fep",
    "--cora_data_path", "./cora_canonical.pt",
    "--split_path", SPLIT_PATH,
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
    "split_path": SPLIT_PATH,
    "note": "projector is the NEW canonical-embedding-trained checkpoint (retrained from "
            "data_canonical.pth, not the original data.pth-trained 2026-03-09-23-12-28 one). "
            "Not retrained further here, loaded via -ppp.",
    "timestamp": time.time(),
}
with open(CHECKPOINT_MD5_PATH, "w") as f:
    json.dump(checkpoint_md5, f, indent=2)
print(f"Checkpoint md5s written to {CHECKPOINT_MD5_PATH}")
print(json.dumps(checkpoint_md5, indent=2))

import eval_utils  # noqa: E402

_orig_build_inputs_embeds_vanilla_eos = eval_utils.build_inputs_embeds_vanilla_eos


def _sha256_tensor(t):
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

    record = {
        "target_node": target_node,
        "neighbors": list(selected_neighbors),
        "predicted_category_in_prompt": predicted_label,
        "full_embeds_shape": list(full_embeds.shape),
        "embedding_segment_checksums": embed_checksums,
        "timestamp": time.time(),
    }
    with open(PROMPT_LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")
    return full_embeds


eval_utils.build_inputs_embeds_vanilla_eos = _instrumented

import runpy  # noqa: E402

runpy.run_path("main.py", run_name="__main__")
