"""
Read-only diagnostic: reconstructs the per-epoch loss/prediction trace for
specific nodes, since the original production run's find_counterfactual_edges()
(cf_gnnexplainer.py:160-248) has no per-epoch logging at all (confirmed:
no print/logger call anywhere in its epoch loop, and the production job logs
contain nothing but a tqdm bar + final summary line) -- there is nothing to
recover from existing logs, so this re-runs the IDENTICAL search algorithm
(same Adam optimizer, same lr=0.3, same max_epochs=500, same P_hat init,
imported unmodified from cf_gnnexplainer.py) with print statements added
around it, for exactly the 3 example nodes -- not a change to the original
method, not an LLM call, just instrumentation. Writes a new CSV only.
"""
import csv
import sys

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.utils import k_hop_subgraph

sys.path.insert(0, "./llm-graph-cf/src")
from gnn_model import GraphSAGE  # noqa: E402
from cf_gnnexplainer import build_dense_adj, sage_forward, undirected_edge_list, greedy_prune  # noqa: E402

CORA_DATA = "./cora_canonical.pt"
CORA_CKPT = "./llm-graph-cf/pretrained/sage_canonical.pt"
NODES = [2534, 709, 130]
MAX_EPOCHS = 500
LR = 0.3


def load_model(data, gnn_ckpt, device):
    model = GraphSAGE(in_channels=data.x.size(1), hidden_channels=768,
                       out_channels=len(data.label_names), num_layers=2, dropout=0.0).to(device)
    state = torch.load(gnn_ckpt, map_location=device, weights_only=True)
    if "model_state_dict" in state:
        state = state["model_state_dict"]
    remapped = {k.replace("gnn_layers.", "convs.", 1) if k.startswith("gnn_layers.") else k: v
                for k, v in state.items()}
    model.load_state_dict(remapped)
    model.eval()
    for p in model.parameters():
        p.requires_grad_(False)
    return model


def traced_search(model, x_sub, adj_bin, target_local, orig_pred, device, max_epochs, lr):
    n = x_sub.size(0)
    edges = undirected_edge_list(adj_bin)
    trace = []
    if not edges:
        return trace, None, None

    edge_idx = torch.tensor(edges, dtype=torch.long, device=device)
    P_hat = torch.zeros(len(edges), device=device, requires_grad=True)
    with torch.no_grad():
        P_hat.fill_(4.0)
    P_hat.requires_grad_(True)
    optimizer = torch.optim.Adam([P_hat], lr=lr)
    convs, decoder = model.convs, model.decoder

    found_removed_pairs = None
    found_cf_pred = None

    for epoch in range(max_epochs):
        optimizer.zero_grad()
        p = torch.sigmoid(P_hat)
        P_soft = torch.zeros((n, n), device=device)
        P_soft[edge_idx[:, 0], edge_idx[:, 1]] = p
        P_soft[edge_idx[:, 1], edge_idx[:, 0]] = p
        logits_soft = sage_forward(x_sub, P_soft, convs, decoder)
        log_probs_soft = F.log_softmax(logits_soft, dim=-1)
        pred_loss = log_probs_soft[target_local, orig_pred]
        pred_loss.backward()
        optimizer.step()

        with torch.no_grad():
            p_hard = (torch.sigmoid(P_hat) >= 0.5).float()
            P_hard = torch.zeros((n, n), device=device)
            P_hard[edge_idx[:, 0], edge_idx[:, 1]] = p_hard
            P_hard[edge_idx[:, 1], edge_idx[:, 0]] = p_hard
            logits_hard = sage_forward(x_sub, P_hard, convs, decoder)
            cf_pred_hard = logits_hard[target_local].argmax().item()
            n_removed_hard = int((p_hard == 0).sum().item())
            soft_probs = F.softmax(logits_soft, dim=-1)[target_local].detach().cpu().tolist()

        if epoch < 10 or epoch % 25 == 0 or cf_pred_hard != orig_pred:
            trace.append({
                "epoch": epoch, "pred_loss": pred_loss.item(),
                "p_mean": p.mean().item(), "n_edges_removed_hard": n_removed_hard,
                "hard_pred": cf_pred_hard, "soft_prob_orig_class": soft_probs[orig_pred],
            })

        if cf_pred_hard != orig_pred and n_removed_hard > 0:
            found_removed_pairs = [(edges[i][0], edges[i][1]) for i in range(len(edges)) if p_hard[i].item() == 0.0]
            found_cf_pred = cf_pred_hard
            break

    return trace, found_removed_pairs, found_cf_pred


def main():
    device = torch.device("cpu")
    data = torch.load(CORA_DATA, map_location="cpu", weights_only=False)
    model = load_model(data, CORA_CKPT, device)

    all_rows = []
    for target_global in NODES:
        subset, edge_index_sub, mapping, _ = k_hop_subgraph(
            node_idx=target_global, num_hops=2, edge_index=data.edge_index,
            relabel_nodes=True, num_nodes=data.num_nodes, flow="target_to_source",
        )
        n = len(subset)
        target_local = mapping.item() if mapping.numel() == 1 else mapping[0].item()
        x_sub = data.x[subset].to(device)
        adj_bin = build_dense_adj(edge_index_sub.to(device), n, device)

        with torch.no_grad():
            logits = sage_forward(x_sub, adj_bin, model.convs, model.decoder)
            orig_pred = logits[target_local].argmax().item()

        print(f"\n=== node {target_global}: subgraph_n={n}, n_undirected_edges={len(undirected_edge_list(adj_bin))}, orig_pred={orig_pred} ===")
        trace, removed, cf_pred = traced_search(model, x_sub, adj_bin, target_local, orig_pred, device, MAX_EPOCHS, LR)
        for row in trace:
            row["node"] = target_global
            all_rows.append(row)
            print(f"  epoch={row['epoch']:3d}  pred_loss={row['pred_loss']:+.4f}  "
                  f"p_mean={row['p_mean']:.4f}  n_removed(hard)={row['n_edges_removed_hard']:2d}  "
                  f"hard_pred={row['hard_pred']}  soft_prob(orig_class)={row['soft_prob_orig_class']:.4f}")
        print(f"  FINAL: {'FOUND cf_pred=' + str(cf_pred) if removed else 'NOT FOUND within ' + str(MAX_EPOCHS) + ' epochs'}")

    out_csv = "./cf_gnnexplainer_run_2026-08-10/isolation_upper_bound_2026-09-28/instrumented_search_trace.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["node", "epoch", "pred_loss", "p_mean",
                                           "n_edges_removed_hard", "hard_pred", "soft_prob_orig_class"])
        w.writeheader()
        w.writerows(all_rows)
    print(f"\n-> {out_csv}")


if __name__ == "__main__":
    main()
