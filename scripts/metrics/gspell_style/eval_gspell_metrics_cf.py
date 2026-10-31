"""
eval_gspell_metrics.py

Standalone GSPELL-style evaluation metrics for llm-graph-cf's CF-GNNFeatures explanations.

Metrics (feature-space adaptation of GSPELL node-space metrics):
  - fidelity            : fraction of nodes where GNN prediction flipped (CF was successful)
  - comprehensiveness_drop : mean drop in P(orig_class) from factual → counterfactual features
  - random_baseline_drop   : same drop but removing an equal number of RANDOM features
  - explanation_size    : mean fraction of features removed to achieve the flip

The CF explanations are derived from the 4 JSON files produced by src/cf_gnnfeatures.py.
The GNN and canonical.pt are needed to compute probability-based metrics.

Outputs:
  data/results/gspell_metrics_{explainer}_seed{seed}.json
  data/results/gspell_metrics_{explainer}_seed{seed}.csv (appended)

Usage:
    python eval_gspell_metrics.py \\
        --cora_data_path ./cora_canonical.pt \\
        --gnn_ckpt pretrained/sage_canonical.pt \\
        --explainer cf-gnnfeatures-canonical \\
        --seed 42
"""

import argparse
import csv
import json
import os
import random
from datetime import datetime

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.utils import k_hop_subgraph
from tqdm import tqdm

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from gnn_model import GraphSAGE


def fix_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_prob(model: GraphSAGE, x_sub: torch.Tensor, edge_index_sub: torch.Tensor,
             target_local: int, class_idx: int, device: torch.device) -> float:
    """Return P(class_idx) for the target node given a feature matrix."""
    model.eval()
    with torch.no_grad():
        logits = model(x_sub.to(device), edge_index_sub.to(device))
        probs = F.softmax(logits, dim=-1)
        return probs[target_local, class_idx].item()


def words_to_feature_mask(words: list, vocab: list) -> torch.Tensor:
    """
    Convert a word list back to a binary feature mask over the CountVectorizer vocab.
    Returns a bool tensor of shape (len(vocab),): True = feature is present.
    """
    word_set = set(words)
    mask = torch.tensor([w in word_set for w in vocab], dtype=torch.bool)
    return mask


def evaluate(args) -> dict:
    fix_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # Load data
    print(f"Loading {args.cora_data_path} ...")
    data = torch.load(args.cora_data_path, map_location="cpu", weights_only=False)
    num_classes = len(data.label_names)
    label_names = data.label_names

    # Load model
    model = GraphSAGE(
        in_channels=data.x.size(1),
        hidden_channels=768,
        out_channels=num_classes,
        num_layers=2,
        dropout=0.0,
    ).to(device)
    state = torch.load(args.gnn_ckpt, map_location=device, weights_only=True)
    model.load_state_dict(state)
    model.eval()
    print(f"Loaded GNN from {args.gnn_ckpt}")

    # Load CF JSON files
    data_dir = os.path.join("data", args.dataset, args.explainer)
    prefix = f"random_seed_{args.seed}"
    factual_target = load_json(os.path.join(data_dir, f"{prefix}_factual_target_dict_repr.json"))
    cf_target = load_json(os.path.join(data_dir, f"{prefix}_counterfactual_target_dict_repr.json"))

    # Load actual removed dims if available (avoids word-list approximation)
    removed_dims_path = os.path.join(data_dir, f"{prefix}_cf_removed_dims.json")
    removed_dims_map = load_json(removed_dims_path) if os.path.exists(removed_dims_path) else None
    if removed_dims_map:
        print(f"Loaded exact CF removed dims from {removed_dims_path}")

    # Load vocabulary for feature mask reconstruction
    vocab_path = "data/cora_vocab.json"
    if os.path.exists(vocab_path):
        with open(vocab_path, "r") as f:
            vocab: list = json.load(f)
    else:
        vocab = None
        print(f"WARNING: {vocab_path} not found. Feature mask reconstruction will use word-count heuristic.")

    # Metrics accumulators
    fidelity_scores = []
    prob_orig_list = []
    prob_cf_list = []
    prob_rand_list = []
    explanation_sizes = []

    keys = list(factual_target.keys())
    for key in tqdm(keys, desc="Evaluating GSPELL metrics"):
        f_entry = factual_target[key]
        c_entry = cf_target[key]

        target_global = f_entry["Target_Node_ID"]
        orig_class_name = f_entry.get("Factual_Target_Node_Class", "")
        cf_class_name = c_entry.get("Counterfactual_Target_Node_class", "")

        # Skip entries where CF was not successfully found
        if not cf_class_name or cf_class_name == orig_class_name:
            continue

        try:
            orig_class_idx = label_names.index(orig_class_name)
        except ValueError:
            continue

        # Extract subgraph
        subset, edge_index_sub, mapping, _ = k_hop_subgraph(
            node_idx=target_global,
            num_hops=2,
            edge_index=data.edge_index,
            relabel_nodes=True,
            num_nodes=data.num_nodes,
            flow="target_to_source",
        )
        target_local = mapping.item() if mapping.numel() == 1 else mapping[0].item()
        x_sub_full = data.x[subset].clone()  # (sub_n, F), canonical BOW

        # --- P(orig_class | factual features) ---
        p_orig = get_prob(model, x_sub_full, edge_index_sub, target_local, orig_class_idx, device)

        # Get dims to remove: use exact saved dims if available, else word-list approximation
        active_dims = (x_sub_full.sum(dim=0) > 0).nonzero(as_tuple=True)[0]

        if removed_dims_map and key in removed_dims_map:
            dims_to_remove = torch.tensor(removed_dims_map[key], dtype=torch.long)
            n_to_remove = len(dims_to_remove)
        else:
            # Fallback: word-list approximation
            f_words_raw = f_entry.get("Factual_Target_Node_Features", "")
            cf_words_raw = c_entry.get("Counterfactual_Target_Node_Features", "")
            f_words = [w.strip() for w in f_words_raw.split(",") if w.strip()] if isinstance(f_words_raw, str) and f_words_raw else []
            cf_words = [w.strip() for w in cf_words_raw.split(",") if w.strip()] if isinstance(cf_words_raw, str) and cf_words_raw else []
            n_factual = len(f_words)
            if n_factual == 0:
                continue
            keep_ratio = len(cf_words) / n_factual
            x_var = x_sub_full.clone().to(device).requires_grad_(True)
            logits = model(x_var, edge_index_sub.to(device))
            prob_t = F.softmax(logits, dim=-1)[target_local, orig_class_idx]
            prob_t.backward()
            with torch.no_grad():
                feat_importance = x_var.grad.abs().sum(dim=0).cpu()
            importance_active = feat_importance[active_dims]
            sorted_order = active_dims[importance_active.argsort(descending=True)]
            n_to_remove = int(round((1.0 - keep_ratio) * len(active_dims)))
            dims_to_remove = sorted_order[:n_to_remove]

        # CF feature matrix
        x_sub_cf = x_sub_full.clone()
        if len(dims_to_remove) > 0:
            x_sub_cf[:, dims_to_remove] = 0.0

        # --- P(orig_class | CF features) ---
        p_cf = get_prob(model, x_sub_cf, edge_index_sub, target_local, orig_class_idx, device)

        # Fidelity: did prediction actually flip?
        with torch.no_grad():
            logits_cf = model(x_sub_cf.to(device), edge_index_sub.to(device))
            cf_actual_pred = logits_cf[target_local].argmax().item()
        fidelity_flipped = (cf_actual_pred != orig_class_idx)

        # --- Random baseline: remove same number of random active features ---
        active_list = active_dims.tolist()
        if len(active_list) >= n_to_remove > 0:
            rand_dims = random.sample(active_list, n_to_remove)
            x_sub_rand = x_sub_full.clone()
            x_sub_rand[:, rand_dims] = 0.0
            p_rand = get_prob(model, x_sub_rand, edge_index_sub, target_local, orig_class_idx, device)
        else:
            p_rand = p_orig

        # Record
        fidelity_scores.append(fidelity_flipped)
        prob_orig_list.append(p_orig)
        prob_cf_list.append(p_cf)
        prob_rand_list.append(p_rand)
        explanation_sizes.append(n_to_remove / max(len(active_list), 1))

    n_eval = len(fidelity_scores)
    if n_eval == 0:
        print("No valid CF entries found. Check that CF JSON files exist and are non-empty.")
        return {}

    avg_fidelity = float(np.mean(fidelity_scores))
    avg_comp_drop = float(np.mean(np.array(prob_orig_list) - np.array(prob_cf_list)))
    avg_rand_drop = float(np.mean(np.array(prob_orig_list) - np.array(prob_rand_list)))
    avg_size = float(np.mean(explanation_sizes))

    summary = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "explainer": args.explainer,
        "dataset": args.dataset,
        "seed": args.seed,
        "gnn_ckpt": args.gnn_ckpt,
        "num_evaluated": n_eval,
        "fidelity": avg_fidelity,
        "comprehensiveness_drop": avg_comp_drop,
        "random_baseline_drop": avg_rand_drop,
        "explanation_size_ratio": avg_size,
    }

    print("\n--- GSPELL-style Metrics ---")
    print(f"  Evaluated:             {n_eval}")
    print(f"  Fidelity (flip rate):  {avg_fidelity:.4f}")
    print(f"  Comprehensiveness drop:{avg_comp_drop:.4f}")
    print(f"  Random baseline drop:  {avg_rand_drop:.4f}")
    print(f"  Explanation size:      {avg_size:.4f}")

    # Save JSON
    os.makedirs("data/results", exist_ok=True)
    json_path = f"data/results/gspell_metrics_{args.explainer}_seed{args.seed}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved JSON metrics: {json_path}")

    # Append to CSV
    csv_path = "data/results/gspell_metrics_all.csv"
    csv_exists = os.path.exists(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary.keys()))
        if not csv_exists:
            writer.writeheader()
        writer.writerow(summary)
    print(f"Appended CSV metrics: {csv_path}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Compute GSPELL-style metrics for CF-GNNFeatures explanations")
    parser.add_argument("--cora_data_path", type=str, required=True,
                        help="Path to cora_canonical.pt")
    parser.add_argument("--gnn_ckpt", type=str, default="pretrained/sage_canonical.pt",
                        help="Path to trained GNN checkpoint")
    parser.add_argument("--explainer", type=str, default="cf-gnnfeatures-canonical",
                        help="Explainer folder name under data/{dataset}/")
    parser.add_argument("--dataset", type=str, default="cora")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    evaluate(args)


if __name__ == "__main__":
    main()
