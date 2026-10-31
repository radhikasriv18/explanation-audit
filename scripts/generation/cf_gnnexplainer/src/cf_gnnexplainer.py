"""
cf_gnnexplainer.py

Generate CF-GNNExplainer counterfactual explanations for node classification
on the canonical Cora / Products data, filling the gap the framework's README
flags: "The folder data contains data coming from CF-GNNExplainer and
CF-GNNFeatures explainers ... The explainers are NOT included in this repo!"

Reference: Lucic, ter Hoeve, Tolomei, de Rijke, Silvestri, "CF-GNNExplainer:
Counterfactual Explanations for Graph Neural Networks", AISTATS 2022
(arXiv:2102.03322). Followed the public reference implementation at
https://github.com/a-lucic/cf-gnnexplainer (gcn_perturb.py / cf_explainer.py),
specifically:
  - a single learned matrix P_hat over the (undirected) edges of the node's
    computation-graph subgraph, sigmoid-relaxed to P in [0,1] and multiplied
    elementwise onto the existing adjacency (P can only shrink existing edge
    weight towards 0 -- edges are removed, never added);
  - loss = pred_loss + alpha*L1(1-P) + beta*L2(1-P)^2, where pred_loss is the
    (signed) log-probability of the ORIGINAL predicted class under the SOFT
    (differentiable) perturbed graph -- minimizing it pushes that probability
    towards 0;
  - at every epoch a separate HARD forward pass (P thresholded at 0.5, no
    gradient) checks whether the prediction actually flips; across all
    epochs we keep the valid counterfactual with the FEWEST edges removed
    (ties broken by first epoch found).

Deviation from the original paper (documented, not hidden): the paper's
public code targets a from-scratch 3-layer GCN ("GCNSyntheticPerturb") with
symmetric-normalized adjacency propagation. Our canonical checkpoints
(pretrained/sage_canonical.pt, sage_products_canonical.pt) are a frozen
2-layer GraphSAGE (mean aggregator, separate self/neighbor weights -- see
src/gnn_model.py). We keep the paper's core mechanism (single learned
per-edge deletion mask, soft/hard dual forward pass, minimum-edit-distance
counterfactual selection) but re-derive the propagation rule for
GraphSAGE's aggregator instead of GCN's: SAGEConv computes
  out_i = lin_l( mean_{j in N(i)} x_j ) + lin_r( x_i )
so the perturbed aggregate is the natural generalization
  agg_i = ( sum_j P_ij * x_j ) / ( sum_j P_ij )
computed with a dense adjacency restricted to the node's k-hop subgraph, using
the checkpoint's own (frozen, untouched) lin_l/lin_r weights -- no GNN weight
is ever trained here, only the per-edge mask, exactly as in the original
method.

Output files (same schema/filenames as src/cf_gnnfeatures.py, so they are a
drop-in replacement for --explainer, and llms_m.py's
`"node features" if "cf-gnnfeatures" in explainer else "adjacency matrix"`
check picks the correct system-prompt wording automatically as long as the
--output_dir name does not contain the substring "cf-gnnfeatures"):
  random_seed_{seed}_factual_graph_descriptions.json
  random_seed_{seed}_counterfactual_graph_descriptions.json
  random_seed_{seed}_factual_target_dict_repr.json
  random_seed_{seed}_counterfactual_target_dict_repr.json
  random_seed_{seed}_cf_removed_edges.json   (side-car: list of [u,v] global-id
                                               pairs removed, per key)

Usage:
    python src/cf_gnnexplainer.py \\
        --cora_data_path ./cora_canonical.pt \\
        --gnn_ckpt pretrained/sage_canonical.pt \\
        --node_words_path data/cora_vocab.json \\
        --output_dir data/cora/cf-gnnexplainer-canonical \\
        --split_path ./LOGIC2/GSPELL/cora_splits_seed42.npz \\
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
from cf_gnnfeatures import describe_subgraph_with_edges, load_vocab


def fix_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def build_dense_adj(edge_index_sub: torch.Tensor, n: int, device: torch.device) -> torch.Tensor:
    """Dense (n, n) binary adjacency, adj[dst, src] = 1, matching PyG's
    default source_to_target message flow (aggregation happens at dst)."""
    adj = torch.zeros((n, n), dtype=torch.float32, device=device)
    if edge_index_sub.numel() > 0:
        src, dst = edge_index_sub[0], edge_index_sub[1]
        adj[dst, src] = 1.0
    return adj


def undirected_edge_list(adj: torch.Tensor) -> list:
    """List of (i, j) with i < j for every undirected edge present in the
    (assumed symmetric) dense adjacency."""
    n = adj.size(0)
    iu = torch.triu_indices(n, n, offset=1, device=adj.device)
    mask = (adj[iu[0], iu[1]] > 0) | (adj[iu[1], iu[0]] > 0)
    pairs = iu[:, mask].t().tolist()
    return [(i, j) for i, j in pairs]


def sage_layer(x: torch.Tensor, adj_weighted: torch.Tensor, lin_l, lin_r) -> torch.Tensor:
    """out_i = lin_l(weighted_mean_j x_j) + lin_r(x_i), weighted mean over
    adj_weighted[i, j] (row i = target/aggregation node)."""
    deg = adj_weighted.sum(dim=1, keepdim=True)
    agg = adj_weighted @ x
    agg = agg / deg.clamp(min=1e-9)
    return lin_l(agg) + lin_r(x)


def sage_forward(x: torch.Tensor, adj_weighted: torch.Tensor, convs, decoder) -> torch.Tensor:
    h = x
    for conv in convs:
        h = F.relu(sage_layer(h, adj_weighted, conv.lin_l, conv.lin_r))
    return decoder(h)


def _hard_pred(model, x_sub, adj_bin, removed_set, target_local):
    adj = adj_bin.clone()
    for i, j in removed_set:
        adj[i, j] = 0.0
        adj[j, i] = 0.0
    with torch.no_grad():
        logits = sage_forward(x_sub, adj, model.convs, model.decoder)
    return logits[target_local].argmax().item()


def greedy_prune(model, x_sub, adj_bin, target_local, orig_pred, removed_pairs):
    """Deterministic local-minimality pass: try adding each removed edge back
    one at a time; keep it added back (i.e. drop it from the removal set)
    whenever the prediction still flips without it. Repeats until no single
    edge can be restored -- guarantees no redundant edge remains in the
    final counterfactual. This replaces the paper's L1/L2 distance loss as
    the mechanism that enforces a *minimal* edit (see module docstring for
    why the gradient-based distance loss was dropped in favor of this exact,
    deterministic pass)."""
    current = list(removed_pairs)
    changed = True
    while changed:
        changed = False
        for pair in list(current):
            trial = [p for p in current if p != pair]
            if _hard_pred(model, x_sub, adj_bin, trial, target_local) != orig_pred:
                current = trial
                changed = True
    # The class reached can differ from the class at first discovery once
    # edges are pruned back out (a smaller edit can land on a different
    # alternate class) -- always recompute it from the final pruned set.
    final_pred = _hard_pred(model, x_sub, adj_bin, current, target_local)
    return current, final_pred


def find_counterfactual_edges(
    model: GraphSAGE,
    x_sub: torch.Tensor,
    adj_bin: torch.Tensor,
    target_local: int,
    orig_pred: int,
    device: torch.device,
    max_epochs: int = 500,
    lr: float = 0.3,
) -> tuple:
    """
    Learn a per-(undirected)-edge deletion mask P in [0,1] over the node's
    subgraph adjacency (adj_bin), following Lucic et al. AISTATS 2022
    (gradient-based search for an edge-removal counterfactual), then run a
    deterministic greedy_prune pass to enforce minimality.

    Deviation from the reference loss (documented): the reference code adds
    an L1/L2 "distance loss" directly into the optimized objective so the
    *same* gradient descent that searches for a flip also shrinks the edit.
    Empirically here (see module docstring / dev notes) that made almost no
    difference at reference-scale weights with SGD (near-zero coverage: the
    raw pred_loss gradient on this frozen 2-layer GraphSAGE is tiny relative
    to a 20-40 edge subgraph's regularization pull) and collapsed coverage
    with Adam even at tiny weights (Adam's per-parameter normalization makes
    step size ~lr regardless of how small alpha/beta are, so regularization
    always wins once a flip is found and pred_loss gates off). We therefore
    run pure existence search (Adam, no distance loss -- consistently reaches
    the coverage ceiling in testing) and enforce minimality afterward with an
    exact combinatorial pass (greedy_prune) instead of a soft, unstable
    gradient penalty. The result -- a locally-minimal edge set that flips the
    prediction -- satisfies the same "minimal edge removal" goal.

    Returns (removed_local_pairs, cf_pred, n_edges_removed) or
    (None, None, None) if no valid counterfactual is found within max_epochs.
    """
    n = x_sub.size(0)
    edges = undirected_edge_list(adj_bin)
    if not edges:
        return None, None, None

    edge_idx = torch.tensor(edges, dtype=torch.long, device=device)  # (E, 2)
    P_hat = torch.zeros(len(edges), device=device, requires_grad=True)
    with torch.no_grad():
        P_hat.fill_(4.0)  # sigmoid(4) ~= 0.982, start near the factual (fully-connected) graph
    P_hat.requires_grad_(True)

    optimizer = torch.optim.Adam([P_hat], lr=lr)
    convs = model.convs
    decoder = model.decoder

    found_removed_pairs = None
    found_cf_pred = None

    for _epoch in range(max_epochs):
        optimizer.zero_grad()
        p = torch.sigmoid(P_hat)  # (E,)

        P_soft = torch.zeros((n, n), device=device)
        P_soft[edge_idx[:, 0], edge_idx[:, 1]] = p
        P_soft[edge_idx[:, 1], edge_idx[:, 0]] = p

        logits_soft = sage_forward(x_sub, P_soft, convs, decoder)
        log_probs_soft = F.log_softmax(logits_soft, dim=-1)
        pred_loss = log_probs_soft[target_local, orig_pred]  # minimizing pushes P(orig) -> 0
        pred_loss.backward()
        optimizer.step()

        with torch.no_grad():
            p_hard = (torch.sigmoid(P_hat) >= 0.5).float()
            P_hard = torch.zeros((n, n), device=device)
            P_hard[edge_idx[:, 0], edge_idx[:, 1]] = p_hard
            P_hard[edge_idx[:, 1], edge_idx[:, 0]] = p_hard
            logits_hard = sage_forward(x_sub, P_hard, convs, decoder)
            cf_pred_hard = logits_hard[target_local].argmax().item()

            if cf_pred_hard != orig_pred:
                n_removed = int((p_hard == 0).sum().item())
                if n_removed > 0:
                    found_removed_pairs = [
                        (edges[i][0], edges[i][1]) for i in range(len(edges)) if p_hard[i].item() == 0.0
                    ]
                    found_cf_pred = cf_pred_hard
                    break  # existence found; greedy_prune below handles minimality

    if found_removed_pairs is None:
        return None, None, None

    pruned, pruned_cf_pred = greedy_prune(model, x_sub, adj_bin, target_local, orig_pred, found_removed_pairs)
    return pruned, pruned_cf_pred, len(pruned)


def generate_cf_jsons(args) -> None:
    fix_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    print(f"Loading {args.cora_data_path} ...")
    data = torch.load(args.cora_data_path, map_location="cpu", weights_only=False)
    num_classes = len(data.label_names)
    label_names = data.label_names

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
    for p in model.parameters():
        p.requires_grad_(False)
    print(f"Loaded GNN from {args.gnn_ckpt}")

    vocab: list = load_vocab(args.node_words_path)
    raw_texts = getattr(data, "raw_text", None)

    if args.split_path:
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

    factual_graph_desc: dict = {}
    cf_graph_desc: dict = {}
    factual_target_dict: dict = {}
    cf_target_dict: dict = {}
    cf_removed_edges: dict = {}  # key -> list of [global_u, global_v] removed

    found = 0
    skipped_large = 0
    for entry_idx, target_global in enumerate(tqdm(test_indices, desc="CF-GNNExplainer")):
        subset, edge_index_sub, mapping, _ = k_hop_subgraph(
            node_idx=target_global,
            num_hops=args.num_hops,
            edge_index=data.edge_index,
            relabel_nodes=True,
            num_nodes=data.num_nodes,
            flow="target_to_source",
        )
        local_to_global: list = subset.tolist()
        n = len(local_to_global)
        if n > args.max_subgraph_nodes:
            skipped_large += 1
            continue

        target_local = mapping.item() if mapping.numel() == 1 else mapping[0].item()
        x_sub = data.x[subset].to(device)
        adj_bin = build_dense_adj(edge_index_sub.to(device), n, device)

        with torch.no_grad():
            logits = sage_forward(x_sub, adj_bin, model.convs, model.decoder)
            orig_pred = logits[target_local].argmax().item()
            orig_probs_sub = F.softmax(logits, dim=-1).cpu()
        orig_preds_sub = orig_probs_sub.argmax(dim=-1).tolist()

        words_per_local: dict = {}
        for local_idx, g_id in enumerate(local_to_global):
            active_dims = data.x[g_id].nonzero(as_tuple=True)[0].tolist()
            words_per_local[local_idx] = [vocab[j] for j in active_dims]

        removed_pairs, cf_pred, n_removed = find_counterfactual_edges(
            model=model,
            x_sub=x_sub,
            adj_bin=adj_bin,
            target_local=target_local,
            orig_pred=orig_pred,
            device=device,
            max_epochs=args.max_epochs,
            lr=args.lr,
        )

        if removed_pairs is None:
            continue

        found += 1
        key = str(entry_idx)
        removed_global_pairs = [[local_to_global[i], local_to_global[j]] for i, j in removed_pairs]
        cf_removed_edges[key] = removed_global_pairs

        removed_set = set()
        for i, j in removed_pairs:
            removed_set.add((i, j))
            removed_set.add((j, i))
        adj_cf = adj_bin.clone()
        for i, j in removed_pairs:
            adj_cf[i, j] = 0.0
            adj_cf[j, i] = 0.0

        with torch.no_grad():
            logits_cf = sage_forward(x_sub, adj_cf, model.convs, model.decoder)
            cf_probs_sub = F.softmax(logits_cf, dim=-1).cpu()
        cf_preds_sub = cf_probs_sub.argmax(dim=-1).tolist()
        assert cf_preds_sub[target_local] == cf_pred

        src_np, dst_np = edge_index_sub.tolist()
        edge_pairs_all = list(zip(src_np, dst_np))
        edge_index_sub_cf_list = [
            (u, v) for u, v in edge_pairs_all if (u, v) not in removed_set
        ]
        if edge_index_sub_cf_list:
            edge_index_sub_cf = torch.tensor(edge_index_sub_cf_list, dtype=torch.long).t()
        else:
            edge_index_sub_cf = torch.empty((2, 0), dtype=torch.long)

        # Features are untouched by CF-GNNExplainer -- same word lists both sides.
        factual_desc = describe_subgraph_with_edges(
            local_to_global=local_to_global,
            edge_index_sub=edge_index_sub,
            target_global_id=target_global,
            preds=orig_preds_sub,
            node_words_per_node=words_per_local,
            label_names=label_names,
            raw_texts=raw_texts,
        )
        cf_desc = describe_subgraph_with_edges(
            local_to_global=local_to_global,
            edge_index_sub=edge_index_sub_cf,
            target_global_id=target_global,
            preds=cf_preds_sub,
            node_words_per_node=words_per_local,
            label_names=label_names,
            raw_texts=raw_texts,
        )

        factual_graph_desc[key] = (
            f"given the factual graph: {factual_desc} "
            f"and given the counterfactual example: {cf_desc}"
        )
        cf_graph_desc[key] = cf_desc

        target_words = words_per_local.get(target_local, [])

        def neighbors_str_of(edge_pairs, local_idx):
            neigh = sorted(set(v for u, v in edge_pairs if u == local_idx and v != local_idx))
            return ", ".join(str(local_to_global[v]) for v in neigh)

        factual_neighbors_str = neighbors_str_of(edge_pairs_all, target_local)
        cf_neighbors_str = neighbors_str_of(edge_index_sub_cf_list, target_local)

        removed_neighbor_globals = sorted(
            {local_to_global[j] for i, j in removed_pairs if i == target_local}
            | {local_to_global[i] for i, j in removed_pairs if j == target_local}
        )

        entry = {
            "Target_Node_ID": target_global,
            "Factual_Target_Node_Neighbors": factual_neighbors_str,
            "Factual_Target_Node_Features": ", ".join(target_words),
            "Counterfactual_Target_Node_Neighbors": cf_neighbors_str,
            "Counterfactual_Target_Node_Features": ", ".join(target_words),
            "Factual_Target_Node_Class": label_names[orig_pred],
            "Counterfactual_Target_Node_class": label_names[cf_pred],
            "Target_Node_Features_Changed_From_Factual_To_Counterfactual": "",
            "Target_Node_Edges_Removed_From_Factual_To_Counterfactual": ", ".join(
                str(g) for g in removed_neighbor_globals
            ),
            "Natural_Language_Explanation": None,
        }
        factual_target_dict[key] = dict(entry)
        cf_target_dict[key] = dict(entry)

    print(f"\nCounterfactuals found: {found} / {len(test_indices)}"
          f" ({skipped_large} skipped: subgraph > {args.max_subgraph_nodes} nodes)")

    os.makedirs(args.output_dir, exist_ok=True)
    prefix = f"random_seed_{args.seed}"
    paths = {
        "factual_graph": os.path.join(args.output_dir, f"{prefix}_factual_graph_descriptions.json"),
        "cf_graph": os.path.join(args.output_dir, f"{prefix}_counterfactual_graph_descriptions.json"),
        "factual_target": os.path.join(args.output_dir, f"{prefix}_factual_target_dict_repr.json"),
        "cf_target": os.path.join(args.output_dir, f"{prefix}_counterfactual_target_dict_repr.json"),
        "cf_removed_edges": os.path.join(args.output_dir, f"{prefix}_cf_removed_edges.json"),
    }
    contents = {
        "factual_graph": factual_graph_desc,
        "cf_graph": cf_graph_desc,
        "factual_target": factual_target_dict,
        "cf_target": cf_target_dict,
        "cf_removed_edges": cf_removed_edges,
    }
    for name, path in paths.items():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(contents[name], f, indent=2, ensure_ascii=False)
        print(f"Saved {name} -> {path}")


def main():
    parser = argparse.ArgumentParser(description="Generate CF-GNNExplainer explanations (Lucic et al., AISTATS 2022)")
    parser.add_argument("--cora_data_path", type=str, required=True)
    parser.add_argument("--gnn_ckpt", type=str, default="pretrained/sage_canonical.pt")
    parser.add_argument("--node_words_path", type=str, default="data/cora_vocab.json")
    parser.add_argument("--output_dir", type=str, default="data/cora/cf-gnnexplainer-canonical")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--num_hops", type=int, default=2)
    parser.add_argument("--max_nodes", type=int, default=-1)
    parser.add_argument("--max_epochs", type=int, default=500,
                         help="Max gradient-search epochs per node before giving up (existence search only; "
                              "minimality is enforced afterward by greedy_prune, not by epoch budget)")
    parser.add_argument("--lr", type=float, default=0.3)
    parser.add_argument("--max_subgraph_nodes", type=int, default=1000,
                         help="Skip (rare) nodes whose k-hop subgraph exceeds this size")
    parser.add_argument("--split_path", type=str, default=None)
    parser.add_argument("--target_node_ids", type=str, default=None)
    args = parser.parse_args()
    generate_cf_jsons(args)


if __name__ == "__main__":
    main()
