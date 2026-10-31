"""
train_gnn.py

Train a GraphSAGE GNN on cora_canonical.pt using the canonical train/val/test splits.
Architecture and hyperparameters match LOGIC2/GSPELL cora.yaml:
  - SAGEConv(1433 → 768 → 7), 2 layers, dropout=0.0
  - Adam(lr=1e-5, weight_decay=0.0), 5 epochs, batch_size=16

Usage:
    python src/train_gnn.py \
        --cora_data_path ./cora_canonical.pt \
        --output_ckpt pretrained/sage_canonical.pt \
        --seed 42
"""

import argparse
import os
import random

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from sklearn.metrics import f1_score

from gnn_model import GraphSAGE


def fix_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def evaluate(model: GraphSAGE, data, mask: torch.Tensor, device: torch.device) -> tuple:
    model.eval()
    with torch.no_grad():
        logits = model(data.x.to(device), data.edge_index.to(device))
        preds = logits[mask].argmax(dim=-1).cpu()
        labels = data.y[mask].cpu()
    acc = (preds == labels).float().mean().item()
    f1 = f1_score(labels.numpy(), preds.numpy(), average="macro", zero_division=0)
    return acc, f1


def train(args) -> None:
    fix_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    print(f"Loading {args.cora_data_path} ...")
    data = torch.load(args.cora_data_path, map_location="cpu", weights_only=False)
    num_nodes = data.num_nodes
    in_channels = data.x.size(1)
    num_classes = len(data.label_names)
    print(f"  Nodes: {num_nodes}, Features: {in_channels}, Classes: {num_classes}")
    print(f"  Train: {data.train_mask.sum().item()}, Val: {data.val_mask.sum().item()}, Test: {data.test_mask.sum().item()}")

    # Create a clean Data object with only tensors so NeighborLoader can index all attributes
    data = Data(
        x=data.x,
        edge_index=data.edge_index,
        y=data.y,
        train_mask=data.train_mask,
        val_mask=data.val_mask,
        test_mask=data.test_mask,
    )

    model = GraphSAGE(
        in_channels=in_channels,
        hidden_channels=768,
        out_channels=num_classes,
        num_layers=2,
        dropout=0.0,
    ).to(device)
    print(f"Model: {model}")

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=0.0)

    # Full-graph training (Cora is small enough)
    data = data.to(device)
    for epoch in range(1, args.epochs + 1):
        model.train()
        optimizer.zero_grad()
        out = model(data.x, data.edge_index)
        loss = F.cross_entropy(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        optimizer.step()

        val_acc, val_f1 = evaluate(model, data, data.val_mask, device)
        print(f"Epoch {epoch:02d} | Loss: {loss.item():.4f} | Val Acc: {val_acc:.4f} | Val F1: {val_f1:.4f}")

    test_acc, test_f1 = evaluate(model, data, data.test_mask, device)
    print(f"\nTest Acc: {test_acc:.4f} | Test F1 (macro): {test_f1:.4f}")

    os.makedirs(os.path.dirname(args.output_ckpt) if os.path.dirname(args.output_ckpt) else ".", exist_ok=True)
    torch.save(model.state_dict(), args.output_ckpt)
    print(f"Saved checkpoint to {args.output_ckpt}")


def main():
    parser = argparse.ArgumentParser(description="Train GraphSAGE on cora_canonical.pt")
    parser.add_argument("--cora_data_path", type=str, required=True,
                        help="Path to cora_canonical.pt")
    parser.add_argument("--output_ckpt", type=str, default="pretrained/sage_canonical.pt",
                        help="Path to save the trained model checkpoint")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=5,
                        help="Number of training epochs (matches GSPELL cora.yaml)")
    parser.add_argument("--batch_size", type=int, default=16,
                        help="Mini-batch size for NeighborLoader (matches GSPELL cora.yaml)")
    args = parser.parse_args()
    train(args)


if __name__ == "__main__":
    main()
