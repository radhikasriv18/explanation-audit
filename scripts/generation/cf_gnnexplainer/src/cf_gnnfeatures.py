"""
cf_gnnfeatures.py

Generate CF-GNNFeatures counterfactual explanations for Cora node classification.

For each test node:
  1. Extract its 2-hop subgraph.
  2. Compute gradient of P(predicted_class) w.r.t. input features.
  3. Greedily zero out features (from highest gradient magnitude to lowest) across
     all nodes in the subgraph until the GNN changes its prediction for the target.
  4. Record factual and counterfactual descriptions in the format expected by the
     existing LLM pipeline (4 JSON files).

Output files in data/cora/cf-gnnfeatures-canonical/:
  random_seed_42_factual_graph_descriptions.json
  random_seed_42_counterfactual_graph_descriptions.json
  random_seed_42_factual_target_dict_repr.json
  random_seed_42_counterfactual_target_dict_repr.json

Usage:
    python src/cf_gnnfeatures.py \\
        --cora_data_path ./cora_canonical.pt \\
        --gnn_ckpt pretrained/sage_canonical.pt \\
        --seed 42
"""

import argparse
import json
import os
import random

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.utils import k_hop_subgraph
from tqdm import tqdm

from gnn_model import GraphSAGE


LABEL_NAMES = [
    "Case_Based",
    "Genetic_Algorithms",
    "Neural_Networks",
    "Probabilistic_Methods",
    "Reinforcement_Learning",
    "Rule_Learning",
    "Theory",
]


def fix_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_vocab(vocab_path: str) -> list:
    with open(vocab_path, "r", encoding="utf-8") as f:
        return json.load(f)


def describe_subgraph(
    subgraph_nodes: list,  # global node IDs in subgraph, ordered
    target_global_id: int,
    x_sub: torch.Tensor,  # (sub_n, F) features for subgraph nodes
    preds: list,          # predicted class index for each subgraph node
    node_words: dict,     # global_id → word list (from canonical raw_text)
    label_names: list,
    local_to_global: list,
) -> str:
    """Build a natural-language description of the subgraph, matching the existing JSON format."""
    parts = []
    for local_idx, global_id in enumerate(local_to_global):
        words = node_words.get(str(global_id), [])
        if not words:
            words_str = "(no features)"
        else:
            words_str = ", ".join(words)
        # find neighbors of this node within the subgraph
        neighbors = []
        for j, gj in enumerate(local_to_global):
            if j != local_idx and gj in subgraph_nodes:
                pass  # we'll use edge_index below
        pred_class = label_names[preds[local_idx]]
        is_target = "it is the target node" if global_id == target_global_id else "it is not the target node"
        parts.append(
            f"The node {global_id} has as attributes the words {words_str} "
            f"and it is classified as {pred_class}, {is_target}."
        )
    return " ".join(parts)


def _extract_product_title(raw_text: str) -> str:
    """Extract product title from 'Product from Amazon platform ... Title: X. Content: Y' format."""
    import re
    m = re.search(r'[Tt]itle:\s*(.+?)(?:\.\s*[Cc]ontent:|$)', raw_text)
    if m:
        return m.group(1).strip()[:120]
    # Fallback: first 100 chars
    return raw_text[:100].strip()


def describe_subgraph_with_edges(
    local_to_global: list,
    edge_index_sub: torch.Tensor,
    target_global_id: int,
    preds: list,
    node_words_per_node: dict,  # local_idx → list of words to show
    label_names: list,
    raw_texts: list = None,  # optional: if provided, use product title for richer descriptions
) -> str:
    """Build description matching existing format including neighbor lists."""
    # Build adjacency from subgraph edge_index
    n = len(local_to_global)
    adj: dict = {i: [] for i in range(n)}
    for u, v in edge_index_sub.t().tolist():
        if v not in adj[u]:
            adj[u].append(v)

    parts = []
    for local_idx, global_id in enumerate(local_to_global):
        words = node_words_per_node.get(local_idx, [])
        # Deduplicate words while preserving order so repeated generic stems
        # (e.g. "use" × 10) don't dominate the description.
        seen: set = set()
        unique_words = [w for w in words if not (w in seen or seen.add(w))]
        words_str = ", ".join(unique_words) if unique_words else "(no features)"

        neighbor_globals = [local_to_global[j] for j in adj[local_idx] if j != local_idx]
        if neighbor_globals:
            if len(neighbor_globals) == 1:
                neigh_str = f"the node {neighbor_globals[0]}"
            else:
                neigh_str = "the nodes " + ", ".join(str(g) for g in neighbor_globals)
        else:
            neigh_str = "no other nodes"

        pred_class = label_names[preds[local_idx]]
        is_target = "it is the target node" if global_id == target_global_id else "it is not the target node"

        if raw_texts is not None:
            title = _extract_product_title(raw_texts[global_id])
            parts.append(
                f"The node {global_id} is a product titled '{title}' "
                f"with key attributes: {words_str} "
                f"and is connected with {neigh_str} "
                f"and it is classified as {pred_class}, {is_target}."
            )
        else:
            parts.append(
                f"The node {global_id} has as attributes the words {words_str} "
                f"and is connected with {neigh_str} "
                f"and it is classified as {pred_class}, {is_target}."
            )
    return " ".join(parts)


def find_counterfactual(
    model: GraphSAGE,
    x_full: torch.Tensor,
    edge_index: torch.Tensor,
    target_global: int,
    orig_pred: int,
    subset: torch.Tensor,
    edge_index_sub: torch.Tensor,
    mapping: torch.Tensor,
    device: torch.device,
    max_steps: int = 200,
) -> tuple:
    """
    Greedily remove features (from highest gradient magnitude to lowest)
    until the GNN changes its prediction for the target node.

    Returns:
        (mask, cf_pred) where mask is a boolean tensor of shape (F,)
        with True meaning the feature is KEPT (False = removed/zeroed).
        Returns (None, None) if no counterfactual found within max_steps.
    """
    F_dim = x_full.size(1)
    target_local = mapping.item() if mapping.numel() == 1 else mapping[0].item()

    # Work on the subgraph features
    x_sub = x_full[subset].clone().to(device).requires_grad_(True)
    edge_sub = edge_index_sub.to(device)

    # Initial prediction check
    with torch.no_grad():
        logits = model(x_sub.detach(), edge_sub)
        curr_pred = logits[target_local].argmax().item()
    if curr_pred != orig_pred:
        # Already flipped — no perturbation needed (shouldn't happen normally)
        mask = torch.ones(F_dim, dtype=torch.bool)
        return mask, curr_pred

    # Compute gradient of P(orig_pred) w.r.t. x_sub
    x_var = x_sub.detach().clone().requires_grad_(True)
    logits = model(x_var, edge_sub)
    prob = F.softmax(logits, dim=-1)[target_local, orig_pred]
    prob.backward()
    grad = x_var.grad.abs()  # (sub_n, F)

    # Aggregate gradient across all subgraph nodes (sum over nodes)
    feat_importance = grad.sum(dim=0).cpu()  # (F,)

    # Sort feature dims by importance descending; only consider dims where
    # at least one subgraph node has value 1
    x_sub_cpu = x_full[subset].cpu()
    active_dims = (x_sub_cpu.sum(dim=0) > 0).nonzero(as_tuple=True)[0]
    importance_active = feat_importance[active_dims]
    sorted_order = active_dims[importance_active.argsort(descending=True)]

    mask = torch.ones(F_dim, dtype=torch.bool)  # True = keep feature
    x_working = x_sub_cpu.clone()  # (sub_n, F)

    removed = []
    for step, feat_dim in enumerate(sorted_order):
        if step >= max_steps:
            break
        feat_dim = feat_dim.item()
        mask[feat_dim] = False
        removed.append(feat_dim)
        x_working[:, feat_dim] = 0.0

        with torch.no_grad():
            logits = model(x_working.to(device), edge_sub)
            new_pred = logits[target_local].argmax().item()

        if new_pred != orig_pred:
            return mask, new_pred, removed

    return None, None, None  # no counterfactual found


def generate_cf_jsons(args) -> None:
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
    if "model_state_dict" in state:
        state = state["model_state_dict"]
    # Remap GSPELL checkpoint keys (gnn_layers -> convs, keep decoder)
    remapped = {}
    for k, v in state.items():
        if k.startswith("gnn_layers."):
            remapped[k.replace("gnn_layers.", "convs.", 1)] = v
        else:
            remapped[k] = v
    if remapped:
        state = remapped
    model.load_state_dict(state)
    model.eval()
    print(f"Loaded GNN from {args.gnn_ckpt}")

    # Load vocabulary (index → Porter-stemmed word matching data.x dims)
    print(f"Loading vocabulary from {args.node_words_path} ...")
    vocab: list = load_vocab(args.node_words_path)

    # Use raw_text for richer node descriptions when available (e.g. Products titles)
    raw_texts = getattr(data, "raw_text", None)

    # Eval nodes to explain
    if args.split_path:
        import numpy as np
        splits = np.load(args.split_path)
        if "eval_idx" in splits:
            test_indices = splits["eval_idx"].tolist()
            print(f"Using eval_idx from {args.split_path}: {len(test_indices)} nodes")
        else:
            test_indices = splits["test_idx"].tolist()
            print(f"Using test_idx from {args.split_path}: {len(test_indices)} nodes")
    else:
        test_indices = data.test_mask.nonzero(as_tuple=True)[0].tolist()
    if args.max_nodes > 0:
        test_indices = test_indices[: args.max_nodes]
    if args.target_node_ids:
        wanted = set(int(x) for x in args.target_node_ids.split(","))
        missing_from_split = wanted - set(test_indices)
        if missing_from_split:
            raise ValueError(f"--target_node_ids contains IDs not in the eval split: {sorted(missing_from_split)}")
        test_indices = [n for n in test_indices if n in wanted]
    print(f"Explaining {len(test_indices)} test nodes ...")

    # Output containers
    factual_graph_desc: dict = {}
    cf_graph_desc: dict = {}
    factual_target_dict: dict = {}
    cf_target_dict: dict = {}
    cf_removed_dims: dict = {}  # key -> list of removed canonical feature indices

    found = 0
    for entry_idx, target_global in enumerate(tqdm(test_indices, desc="CF-GNNFeatures")):
        # Extract k-hop subgraph
        subset, edge_index_sub, mapping, _ = k_hop_subgraph(
            node_idx=target_global,
            num_hops=args.num_hops,
            edge_index=data.edge_index,
            relabel_nodes=True,
            num_nodes=data.num_nodes,
            flow="target_to_source",
        )
        local_to_global: list = subset.tolist()

        # Original GNN prediction for target
        with torch.no_grad():
            x_sub = data.x[subset].to(device)
            logits = model(x_sub, edge_index_sub.to(device))
            target_local = mapping.item() if mapping.numel() == 1 else mapping[0].item()
            orig_pred = logits[target_local].argmax().item()
            orig_probs_sub = F.softmax(logits, dim=-1).cpu()

        orig_preds_sub = orig_probs_sub.argmax(dim=-1).tolist()

        # Get word lists for each subgraph node (factual) directly from data.x + vocab
        factual_words_per_local: dict = {}
        for local_idx, g_id in enumerate(local_to_global):
            active_dims = data.x[g_id].nonzero(as_tuple=True)[0].tolist()
            factual_words_per_local[local_idx] = [vocab[j] for j in active_dims]

        # Find counterfactual
        cf_mask, cf_pred, removed_dims = find_counterfactual(
            model=model,
            x_full=data.x,
            edge_index=data.edge_index,
            target_global=target_global,
            orig_pred=orig_pred,
            subset=subset,
            edge_index_sub=edge_index_sub,
            mapping=mapping,
            device=device,
        )

        if cf_mask is None:
            # Could not find CF — skip this node
            continue

        found += 1
        key = str(entry_idx)
        cf_removed_dims[key] = removed_dims

        # Compute CF subgraph predictions
        x_sub_cf = data.x[subset].clone()
        x_sub_cf[:, ~cf_mask] = 0.0  # zero out removed features
        with torch.no_grad():
            logits_cf = model(x_sub_cf.to(device), edge_index_sub.to(device))
            cf_probs_sub = F.softmax(logits_cf, dim=-1).cpu()
        cf_preds_sub = cf_probs_sub.argmax(dim=-1).tolist()

        # CF word lists: same active dims as factual, but only those kept by cf_mask.
        # This accurately reflects which GNN features were retained vs. removed.
        cf_words_per_local: dict = {}
        for local_idx, g_id in enumerate(local_to_global):
            active_dims = data.x[g_id].nonzero(as_tuple=True)[0].tolist()
            cf_words_per_local[local_idx] = [vocab[j] for j in active_dims if cf_mask[j]]

        # Build text descriptions
        factual_desc = describe_subgraph_with_edges(
            local_to_global=local_to_global,
            edge_index_sub=edge_index_sub,
            target_global_id=target_global,
            preds=orig_preds_sub,
            node_words_per_node=factual_words_per_local,
            label_names=label_names,
            raw_texts=raw_texts,
        )
        cf_desc = describe_subgraph_with_edges(
            local_to_global=local_to_global,
            edge_index_sub=edge_index_sub,
            target_global_id=target_global,
            preds=cf_preds_sub,
            node_words_per_node=cf_words_per_local,
            label_names=label_names,
            raw_texts=raw_texts,
        )

        factual_graph_desc[key] = (
            f"given the factual graph: {factual_desc} "
            f"and given the counterfactual example: {cf_desc}"
        )
        cf_graph_desc[key] = cf_desc

        # Target-node structured dicts
        target_local_idx = mapping.item() if mapping.numel() == 1 else mapping[0].item()
        f_words_target = factual_words_per_local.get(target_local_idx, [])
        cf_words_target = cf_words_per_local.get(target_local_idx, [])

        # Neighbors of target in subgraph
        target_neighbors_local = []
        for u, v in edge_index_sub.t().tolist():
            if u == target_local_idx and v != target_local_idx:
                target_neighbors_local.append(local_to_global[v])

        target_neighbors_str = (
            ", ".join(str(n) for n in sorted(set(target_neighbors_local)))
            if target_neighbors_local else ""
        )

        # Words removed from target node to flip the prediction
        target_active_dims = data.x[target_global].nonzero(as_tuple=True)[0].tolist()
        removed_words_target = [vocab[j] for j in target_active_dims if not cf_mask[j]]

        factual_target_dict[key] = {
            "Target_Node_ID": target_global,
            "Factual_Target_Node_Neighbors": target_neighbors_str,
            "Factual_Target_Node_Features": ", ".join(f_words_target),
            "Counterfactual_Target_Node_Neighbors": target_neighbors_str,
            "Counterfactual_Target_Node_Features": ", ".join(cf_words_target),
            "Factual_Target_Node_Class": label_names[orig_pred],
            "Counterfactual_Target_Node_class": label_names[cf_pred],
            "Target_Node_Features_Changed_From_Factual_To_Counterfactual": ", ".join(removed_words_target),
            "Natural_Language_Explanation": None,
        }

        cf_target_dict[key] = {
            "Target_Node_ID": target_global,
            "Factual_Target_Node_Neighbors": target_neighbors_str,
            "Factual_Target_Node_Features": ", ".join(f_words_target),
            "Counterfactual_Target_Node_Neighbors": target_neighbors_str,
            "Counterfactual_Target_Node_Features": ", ".join(cf_words_target),
            "Factual_Target_Node_Class": label_names[orig_pred],
            "Counterfactual_Target_Node_class": label_names[cf_pred],
            "Target_Node_Features_Changed_From_Factual_To_Counterfactual": ", ".join(removed_words_target),
            "Natural_Language_Explanation": None,
        }

    print(f"\nCounterfactuals found: {found} / {len(test_indices)}")

    # Save outputs
    os.makedirs(args.output_dir, exist_ok=True)
    prefix = f"random_seed_{args.seed}"
    paths = {
        "factual_graph": os.path.join(args.output_dir, f"{prefix}_factual_graph_descriptions.json"),
        "cf_graph": os.path.join(args.output_dir, f"{prefix}_counterfactual_graph_descriptions.json"),
        "factual_target": os.path.join(args.output_dir, f"{prefix}_factual_target_dict_repr.json"),
        "cf_target": os.path.join(args.output_dir, f"{prefix}_counterfactual_target_dict_repr.json"),
        "cf_removed_dims": os.path.join(args.output_dir, f"{prefix}_cf_removed_dims.json"),
    }
    contents = {
        "factual_graph": factual_graph_desc,
        "cf_graph": cf_graph_desc,
        "factual_target": factual_target_dict,
        "cf_target": cf_target_dict,
        "cf_removed_dims": cf_removed_dims,
    }
    for name, path in paths.items():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(contents[name], f, indent=2, ensure_ascii=False)
        print(f"Saved {name} → {path}")


def main():
    parser = argparse.ArgumentParser(description="Generate CF-GNNFeatures explanations from cora_canonical.pt")
    parser.add_argument("--cora_data_path", type=str, required=True,
                        help="Path to cora_canonical.pt")
    parser.add_argument("--gnn_ckpt", type=str, default="pretrained/sage_canonical.pt",
                        help="Path to trained GNN checkpoint")
    parser.add_argument("--node_words_path", type=str, default="data/cora_vocab.json",
                        help="Path to 1433-word vocabulary list (from build_vocab.py)")
    parser.add_argument("--output_dir", type=str, default="data/cora/cf-gnnfeatures-canonical",
                        help="Output directory for the 4 CF JSON files")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--num_hops", type=int, default=2,
                        help="Number of hops for subgraph extraction")
    parser.add_argument("--max_nodes", type=int, default=-1,
                        help="Max number of test nodes to explain (-1 = all)")
    parser.add_argument("--max_steps", type=int, default=200,
                        help="Max greedy steps to find counterfactual per node")
    parser.add_argument("--split_path", type=str, default=None,
                        help="Path to .npz split file; uses eval_idx (or test_idx) instead of data.test_mask")
    parser.add_argument("--target_node_ids", type=str, default=None,
                        help="Comma-separated global node IDs to restrict the run to (must be a subset of the "
                             "resolved eval split). Does not change node selection logic otherwise -- used to "
                             "re-run only previously CF-not-found nodes with a different --max_steps.")
    args = parser.parse_args()
    generate_cf_jsons(args)


if __name__ == "__main__":
    main()
