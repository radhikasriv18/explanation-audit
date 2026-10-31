"""
Read-only upper-bound test for CF-GNNExplainer coverage: does isolating a
target node (removing ALL edges within its k-hop computation subgraph) ever
flip the prediction, on nodes where the actual CF-GNNExplainer search found
nothing? If isolation (the most extreme possible edge-removal edit) still
doesn't flip a node, no search could ever find an edge-removal counterfactual
for it -- low coverage there is a property of the node/model, not a search
failure. If isolation DOES flip it but the search found nothing, that's
evidence of an actual search shortfall.

Reuses the EXACT model-loading, checkpoint-remap, and subgraph-construction
code from llm-graph-cf/src/cf_gnnexplainer.py (imported by absolute path,
unmodified) -- same checkpoint, same k_hop_subgraph call (num_hops=2,
flow="target_to_source", relabel_nodes=True), same eval-node source
(cora_splits_seed42.npz test_idx / products_splits_seed42.npz eval_idx).

No LLM calls. This only runs the frozen canonical GraphSAGE classifier
forward pass (deterministic, no training, no text generation) -- explicitly
in scope per the request ("no LLM calls").

Writes only new files under this directory; nothing in llm-graph-cf/ or
cf_gnnexplainer_run_2026-08-10/ is modified.
"""
import csv
import json
import sys

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.utils import k_hop_subgraph

sys.path.insert(0, "./llm-graph-cf/src")
from gnn_model import GraphSAGE  # noqa: E402
from cf_gnnexplainer import build_dense_adj, sage_forward  # noqa: E402  (unmodified reuse)

DATASETS = {
    "cora": dict(
        data_path="./cora_canonical.pt",
        gnn_ckpt="./llm-graph-cf/pretrained/sage_canonical.pt",
        split_path="./LOGIC2/GSPELL/cora_splits_seed42.npz",
        target_dict_path="./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json",
    ),
    "products": dict(
        data_path="./products_canonical.pt",
        gnn_ckpt="./sage_products_canonical.pt",
        split_path="./LOGIC2/GSPELL/products_splits_seed42.npz",
        target_dict_path="./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json",
    ),
}

NUM_HOPS = 2  # matches cf_gnnexplainer.py's --num_hops default, and the production run (not overridden)
MAX_SUBGRAPH_NODES = 1000  # matches cf_gnnexplainer.py's --max_subgraph_nodes default


def load_model(data, gnn_ckpt, device):
    model = GraphSAGE(
        in_channels=data.x.size(1), hidden_channels=768,
        out_channels=len(data.label_names), num_layers=2, dropout=0.0,
    ).to(device)
    state = torch.load(gnn_ckpt, map_location=device, weights_only=True)
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
    return model


def run_dataset(name, cfg, device):
    data = torch.load(cfg["data_path"], map_location="cpu", weights_only=False)
    model = load_model(data, cfg["gnn_ckpt"], device)

    splits = np.load(cfg["split_path"])
    if "eval_idx" in splits:
        test_indices = splits["eval_idx"].tolist()
    else:
        test_indices = splits["test_idx"].tolist()

    found_ids = set()
    with open(cfg["target_dict_path"]) as f:
        target_dict = json.load(f)
    for entry in target_dict.values():
        found_ids.add(int(entry["Target_Node_ID"]))

    rows = []
    skipped_large = 0
    for target_global in test_indices:
        subset, edge_index_sub, mapping, _ = k_hop_subgraph(
            node_idx=target_global, num_hops=NUM_HOPS, edge_index=data.edge_index,
            relabel_nodes=True, num_nodes=data.num_nodes, flow="target_to_source",
        )
        n = len(subset)
        if n > MAX_SUBGRAPH_NODES:
            skipped_large += 1
            continue
        target_local = mapping.item() if mapping.numel() == 1 else mapping[0].item()
        x_sub = data.x[subset].to(device)
        adj_bin = build_dense_adj(edge_index_sub.to(device), n, device)
        n_edges_in_subgraph = int((adj_bin.sum().item()))

        with torch.no_grad():
            logits_orig = sage_forward(x_sub, adj_bin, model.convs, model.decoder)
            orig_pred = logits_orig[target_local].argmax().item()

            adj_isolated = torch.zeros_like(adj_bin)  # remove ALL edges in the subgraph
            logits_iso = sage_forward(x_sub, adj_isolated, model.convs, model.decoder)
            iso_pred = logits_iso[target_local].argmax().item()

        flips = iso_pred != orig_pred
        search_found = target_global in found_ids
        rows.append({
            "dataset": name, "node": target_global, "subgraph_n": n,
            "subgraph_n_edges": n_edges_in_subgraph,
            "orig_pred": orig_pred, "isolated_pred": iso_pred,
            "isolation_flips": flips, "search_found_cf": search_found,
        })

    print(f"{name}: {len(rows)} nodes evaluated ({skipped_large} skipped, subgraph > {MAX_SUBGRAPH_NODES} nodes)")
    return rows


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    all_rows = []
    for name, cfg in DATASETS.items():
        all_rows.extend(run_dataset(name, cfg, device))

    out_csv = "./cf_gnnexplainer_run_2026-08-10/isolation_upper_bound_2026-09-28/isolation_upper_bound.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["dataset", "node", "subgraph_n", "subgraph_n_edges",
                                           "orig_pred", "isolated_pred", "isolation_flips", "search_found_cf"])
        w.writeheader()
        w.writerows(all_rows)
    print(f"-> {out_csv}")

    # summary
    from collections import Counter
    for name in DATASETS:
        rows = [r for r in all_rows if r["dataset"] == name]
        n = len(rows)
        n_flip = sum(1 for r in rows if r["isolation_flips"])
        print(f"\n=== {name} ===")
        print(f"  n={n}  isolation_flips={n_flip} ({100*n_flip/n:.1f}%)")
        cross = Counter((r["isolation_flips"], r["search_found_cf"]) for r in rows)
        print(f"  cross-tab (isolation_flips, search_found_cf) -> count:")
        for k in [(True, True), (True, False), (False, True), (False, False)]:
            print(f"    {k}: {cross.get(k, 0)}")


if __name__ == "__main__":
    main()
