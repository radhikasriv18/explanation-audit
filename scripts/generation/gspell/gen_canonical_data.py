"""
Generate data_canonical.pth by replacing gnn_embeds/gnn_logits/gnn_preds
in the existing data.pth with outputs from sage_canonical.pt.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import torch
import torch.nn.functional as F

ORIG_DATA = "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data.pth"
CANONICAL_GNN = "./llm-graph-cf/pretrained/sage_canonical.pt"
OUT_DATA = "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth"

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading original data.pth ...")
orig = torch.load(ORIG_DATA, map_location=device)
dataset = orig["dataset"]
data = dataset._data

print("Loading sage_canonical.pt state dict ...")
state = torch.load(CANONICAL_GNN, map_location=device)

# Remap keys: convs.X -> gnn_layers.X to match GSPELL's PretrainedModel
from model import PretrainedModel
model = PretrainedModel(
    gnn_type="sage",
    in_channels=1433,
    hidden_channels=768,
    out_channels=7,
    gnn_num_hid_layers=2,
    decoder_type="linear",
    mode="node",
    device=device,
    with_last_dropout=False,
)
remapped = {}
for k, v in state.items():
    new_k = k.replace("convs.", "gnn_layers.")
    remapped[new_k] = v
model.load_state_dict(remapped)
model = model.to(device)
model.eval()

print("Running forward pass ...")
x = data.x.to(device)
edge_index = data.edge_index.to(device)
with torch.no_grad():
    gnn_logits, gnn_embeds = model(x=x, edge_index=edge_index)
    gnn_preds = gnn_logits.argmax(dim=1)

test_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
import numpy as np
split = np.load("./cora_splits_seed42.npz")
test_idx = split["test_idx"]
test_mask[test_idx] = True
test_acc = (gnn_preds[test_mask] == data.y.to(device)[test_mask]).float().mean()
print(f"Canonical SAGE test acc on split: {test_acc.item():.4f}")
print(f"Pred distribution: { {i: (gnn_preds==i).sum().item() for i in range(7)} }")

outdict = {
    "dataset": dataset,
    "gnn_embeds": gnn_embeds.detach().cpu(),
    "gnn_logits": gnn_logits.detach().cpu(),
    "gnn_preds": gnn_preds.detach().cpu(),
}
torch.save(outdict, OUT_DATA)
print(f"Saved to {OUT_DATA}")
