"""Convert GSPELL_explanations.pt to a readable .txt file."""
import torch
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--pt", type=str, required=True, help="Path to GSPELL_explanations.pt")
parser.add_argument("--out", type=str, default=None, help="Output .txt path (default: same dir as .pt)")
args = parser.parse_args()

data = torch.load(args.pt, map_location="cpu")

out_path = args.out or args.pt.replace(".pt", ".txt")

with open(out_path, "w") as f:
    for node_data in data:
        for item in node_data:
            f.write(f"Target node: {item['target_node']}\n")
            f.write(f"Neighbors: {item['neighbors']}\n")
            f.write(f"Explanation:\n{item['explanation']}\n")
            f.write("=" * 80 + "\n\n")

print(f"Saved to: {out_path}")
