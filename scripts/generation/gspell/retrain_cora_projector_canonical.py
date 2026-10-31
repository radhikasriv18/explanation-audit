"""
Retrain the Cora GSPELL projector, sourcing gnn_embeds from data_canonical.pth
(canonical 89.7%-acc SAGE embeddings) instead of data.pth (GSPELL's own
~30%-acc from-scratch GNN, used by the original 2026-03-09-23-12-28 training
run this replaces). Fixes the train/inference embedding-source mismatch
identified in the audit: the original projector was fit on GSPELL-own-GNN
embeddings but has been fed canonical-GNN embeddings at every generation
time since (both the original text-path survey run and job 51180082).

Standalone script, not a main.py CLI invocation -- main.py couples
--split_path (needed for proj_node_indices, matching the original run's
train-set-only projector training) to eval_node_ids for generation, which
would immediately kick off a full 542-node generation pass right after
training. This script calls train_utils.pretrain_projector directly with the
exact same projector/optimizer/training config as the original run's logged
argparse Namespace (config/cora.yaml's projector_* fields already match it
byte-for-byte -- verified before writing this script), changing only the
gnn_embeds source. No generation happens here (that's Step 3/4, separate).

Original run's logged Namespace (log/general/global_gspell_cora_2026-03-09-23-12-28.log):
  processed_data_path=['.../2026-03-09-20-33-28/data.pth']   <- being replaced
  split_path='./cora_splits_seed42.npz'
  projector_lr=0.0005, projector_step_size=50, projector_weight_decay=0.0,
  projector_gamma=1.0, projector_num_epochs=200, contrastive_temperature=0.2,
  projector_contrastive_w=1.0, projector_context_w=1.0, projector_mutualinfo_w=1.0,
  projector_with_backward=False, num_tokens=5, gnn_h_dim=768, use_bow=True,
  max_num_frequent_words=2000, seed=[42]
"""
import json
import os
import sys
import time

import numpy as np
import torch

REPO = "./LOGIC2/GSPELL"
os.chdir(REPO)
sys.path.insert(0, REPO)

_orig_load = torch.load
def _cpu_load(*a, **k):
    k.setdefault("map_location", "cpu")
    return _orig_load(*a, **k)
torch.load = _cpu_load

from train_utils import pretrain_projector, fix_seed
from transformers import AutoModelForCausalLM, AutoTokenizer

SEED = 42
DATA_CANONICAL = "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth"
SPLIT_PATH = "./cora_splits_seed42.npz"
LLM_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"

OUT_DIR = "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-canonical-projector-retrain-2026-08-16"
os.makedirs(OUT_DIR, exist_ok=True)

fix_seed(SEED)

print(f"Loading canonical data from: {DATA_CANONICAL}")
outdict = torch.load(DATA_CANONICAL)
dataset = outdict["dataset"]
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
gnn_preds = outdict["gnn_preds"].to(device)
gnn_embeds = outdict["gnn_embeds"].to(device)
gnn_logits = outdict["gnn_logits"].to(device)

if not hasattr(dataset._data, "words") or dataset._data.words is None:
    _, dataset._data.words = dataset.get_bow_embedding(dataset._data, 2000)

# Matches main.py:312-330 exactly (proj_node_indices computation)
split = np.load(SPLIT_PATH)
MAX_PROJ_NODES = 3000
train_idx_all = split["train_idx"]
if len(train_idx_all) > MAX_PROJ_NODES:
    rng = np.random.default_rng(42)
    proj_node_indices = rng.choice(train_idx_all, size=MAX_PROJ_NODES, replace=False)
else:
    proj_node_indices = train_idx_all
print(f"Projector will train on {len(proj_node_indices)} nodes (train_idx from {SPLIT_PATH})")

print(f"Loading LLM: {LLM_MODEL}")
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
llm = AutoModelForCausalLM.from_pretrained(LLM_MODEL, torch_dtype=torch.bfloat16, device_map="auto")
embed_func = llm.model.embed_tokens

projector_config = dict(
    gnn_h_dim=768,
    num_tokens=5,
    llm_h_dim=llm.config.hidden_size,
    gnn_out_dim=None,  # projector_with_backward=False in original run
)
optimizer_config = dict(
    lr=0.0005,
    scheduler_step_size=50,
    scheduler_gamma=1.0,
    weight_decay=0.0,
)
training_config = dict(
    num_epochs=200,
    temperature=0.2,
    proj_contrastive_w=1.0,
    proj_context_w=1.0,
    proj_mutualinfo_w=1.0,
)

start = time.time()
projector, p_path = pretrain_projector(
    dataset,
    embed_func,
    tokenizer,
    gnn_embeds,
    gnn_logits,
    projector_config,
    optimizer_config,
    training_config,
    gnn_preds=gnn_preds,
    use_bow=True,
    eval_step=50,
    model_dir=OUT_DIR,
    node_indices=proj_node_indices,
)
elapsed = time.time() - start
print(f"Training complete in {elapsed:.1f}s. Saved to: {p_path}")

manifest = {
    "new_projector_path": p_path,
    "original_projector_path": "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-23-12-28/projector.pth",
    "gnn_embeds_source": DATA_CANONICAL,
    "original_run_gnn_embeds_source": "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data.pth",
    "split_path": SPLIT_PATH,
    "num_train_nodes": int(len(proj_node_indices)),
    "seed": SEED,
    "projector_config": projector_config,
    "optimizer_config": optimizer_config,
    "training_config": training_config,
    "elapsed_seconds": elapsed,
    "timestamp": time.time(),
}
with open(os.path.join(OUT_DIR, "retrain_manifest.json"), "w") as f:
    json.dump(manifest, f, indent=2)
print(json.dumps(manifest, indent=2))
