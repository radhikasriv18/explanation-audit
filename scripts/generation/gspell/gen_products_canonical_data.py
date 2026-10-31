"""
Generate products_data_canonical.pth for GSPELL by running sage_products_canonical.pt
forward pass on the Products dataset object.

Output: ./output/products-meta-llama/data_canonical.pth
  {dataset, gnn_embeds, gnn_logits, gnn_preds}

Usage:
    cd ./LOGIC2/GSPELL
    source narratives/bin/activate
    python gen_products_canonical_data.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "./llm-graph-cf/src")

import torch
from data_utils import get_node_dataset
from model import PretrainedModel

CANONICAL_GNN = "./sage_products_canonical.pt"
SPLIT_PATH    = "./products_splits_seed42.npz"
OUT_DIR       = "./output/products-meta-llama/Meta-Llama-3.1-8B-Instruct"
OUT_PATH      = os.path.join(OUT_DIR, "data_canonical.pth")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")

# ── 1. Load Products dataset ──────────────────────────────────────────────────
print("Loading Products dataset ...")
dataset = get_node_dataset(
    dataset_name        = "products",
    train_test_split    = [0.60, 0.30],
    batch_size          = 64,
    normal_mode         = "na",
    seed                = 42,
    split_path          = SPLIT_PATH,
    sample_size         = -1,
    random_sampling     = False,
    num_workers         = 0,
    use_bow             = True,
    num_hops            = 2,
    max_num_frequent_words = 2000,
)
data = dataset._data
print(f"  nodes={data.num_nodes}, features={data.x.shape[1]}, classes={dataset.num_classes}")

# ── 2. Load canonical SAGE (remap llm-graph-cf key names → GSPELL key names) ─
print(f"Loading {CANONICAL_GNN} ...")
state = torch.load(CANONICAL_GNN, map_location=device)

model = PretrainedModel(
    gnn_type        = "sage",
    in_channels     = dataset.n_feats,      # 2000
    hidden_channels = 768,
    out_channels    = dataset.num_classes,  # 47
    gnn_num_hid_layers = 2,
    decoder_type    = "linear",
    mode            = "node",
    device          = device,
    with_last_dropout = False,
)

# llm-graph-cf saves keys as convs.X.* — GSPELL PretrainedModel uses gnn_layers.X.*
remapped = {k.replace("convs.", "gnn_layers."): v for k, v in state.items()}
model.load_state_dict(remapped)
model = model.to(device)
model.eval()

# ── 3. Forward pass ───────────────────────────────────────────────────────────
print("Running forward pass ...")
x          = data.x.to(device)
edge_index = data.edge_index.to(device)
with torch.no_grad():
    gnn_logits, gnn_embeds = model(x=x, edge_index=edge_index)
    gnn_preds = gnn_logits.argmax(dim=1)

# ── 4. Sanity check on eval-200 nodes ─────────────────────────────────────────
import numpy as np
splits   = np.load(SPLIT_PATH)
eval_idx = torch.as_tensor(splits["eval_idx"], dtype=torch.long)
eval_acc = (gnn_preds.cpu()[eval_idx] == data.y[eval_idx]).float().mean()
test_idx = torch.as_tensor(splits["test_idx"], dtype=torch.long)
test_acc = (gnn_preds.cpu()[test_idx] == data.y[test_idx]).float().mean()
print(f"  Test acc  (full):   {test_acc.item():.4f}")
print(f"  Eval acc  (200):    {eval_acc.item():.4f}")
print(f"  Pred distribution (top 5): { sorted([(i, (gnn_preds==i).sum().item()) for i in range(dataset.num_classes)], key=lambda x: -x[1])[:5] }")

# ── 5. Save ───────────────────────────────────────────────────────────────────
os.makedirs(OUT_DIR, exist_ok=True)

# Save data canonical (for -pdp)
outdict = dict(
    dataset    = dataset,
    gnn_embeds = gnn_embeds.detach().cpu(),
    gnn_logits = gnn_logits.detach().cpu(),
    gnn_preds  = gnn_preds.detach().cpu(),
)
torch.save(outdict, OUT_PATH)
print(f"\nSaved data: {OUT_PATH}")

# Save GSPELL-compatible GNN checkpoint (for -pgp)
# GSPELL load_model expects {"model_state_dict": state} with gnn_layers.* keys
gspell_ckpt_path = "./pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct/sage_canonical.pth"
os.makedirs(os.path.dirname(gspell_ckpt_path), exist_ok=True)
torch.save({"model_state_dict": remapped}, gspell_ckpt_path)
print(f"Saved GNN:  {gspell_ckpt_path}")
