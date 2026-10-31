"""
Train the canonical GraphSAGE GNN on products_canonical.pt.

Architecture matches sage_canonical.pt (Cora):
  SAGEConv(2000 → 768 → 47), 2 layers, dropout=0.0
  Adam(lr=1e-3, weight_decay=0.0)

Saves: ./sage_products_canonical.pt

Usage:
    cd ./LOGIC2/GSPELL
    source narratives/bin/activate
    python train_products_canonical_gnn.py
"""

import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "./llm-graph-cf/src")

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from sklearn.metrics import f1_score

from gnn_model import GraphSAGE

DATA_PATH  = "./products_canonical.pt"
SPLIT_PATH = "./products_splits_seed42.npz"
OUT_CKPT   = "./sage_products_canonical.pt"
SEED       = 42
EPOCHS     = 200
LR         = 1e-3


def fix_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def evaluate(model, data, mask, device):
    model.eval()
    with torch.no_grad():
        logits = model(data.x.to(device), data.edge_index.to(device))
        preds  = logits[mask].argmax(dim=-1).cpu()
        labels = data.y[mask].cpu()
    acc = (preds == labels).float().mean().item()
    f1  = f1_score(labels.numpy(), preds.numpy(), average="macro", zero_division=0)
    return acc, f1


def main():
    fix_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    print(f"Loading {DATA_PATH} ...")
    raw = torch.load(DATA_PATH, map_location="cpu", weights_only=False)
    in_channels  = raw.x.size(1)       # 2000
    num_classes  = len(raw.label_names) # 47
    print(f"  Nodes={raw.x.size(0)}, Features={in_channels}, Classes={num_classes}")
    print(f"  Train={raw.train_mask.sum().item()}, Val={raw.val_mask.sum().item()}, Test={raw.test_mask.sum().item()}")

    # Strip non-tensor attributes so PyG doesn't choke on lists
    data = Data(
        x          = raw.x,
        edge_index = raw.edge_index,
        y          = raw.y,
        train_mask = raw.train_mask,
        val_mask   = raw.val_mask,
        test_mask  = raw.test_mask,
    ).to(device)

    model = GraphSAGE(
        in_channels     = in_channels,
        hidden_channels = 768,
        out_channels    = num_classes,
        num_layers      = 2,
        dropout         = 0.0,
    ).to(device)
    print(f"\nModel: SAGEConv({in_channels}→768→{num_classes}), 2 layers")

    optimizer = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=0.0)

    best_val_acc = 0.0
    best_state   = None

    print(f"\nTraining for {EPOCHS} epochs ...")
    for epoch in range(1, EPOCHS + 1):
        model.train()
        optimizer.zero_grad()
        out  = model(data.x, data.edge_index)
        loss = F.cross_entropy(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0 or epoch == 1:
            val_acc, val_f1 = evaluate(model, data, data.val_mask, device)
            print(f"  Epoch {epoch:03d} | Loss {loss.item():.4f} | Val Acc {val_acc:.4f} | Val F1 {val_f1:.4f}")
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                best_state   = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    # Evaluate best checkpoint on test
    model.load_state_dict(best_state)
    model.to(device)
    test_acc, test_f1 = evaluate(model, data, data.test_mask, device)
    print(f"\nBest val acc: {best_val_acc:.4f}")
    print(f"Test Acc: {test_acc:.4f} | Test F1 (macro): {test_f1:.4f}")

    # Also check eval_idx (the 200-node explanation subset)
    splits   = np.load(SPLIT_PATH)
    eval_idx = torch.as_tensor(splits["eval_idx"], dtype=torch.long)
    eval_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
    eval_mask[eval_idx] = True
    eval_acc, eval_f1 = evaluate(model, data, eval_mask.to(device), device)
    print(f"Eval-200 Acc: {eval_acc:.4f} | Eval-200 F1 (macro): {eval_f1:.4f}")

    torch.save(best_state, OUT_CKPT)
    print(f"\nSaved: {OUT_CKPT}")


if __name__ == "__main__":
    main()
