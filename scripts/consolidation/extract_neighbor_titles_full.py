#!/usr/bin/env python3
"""
Full-eval-set generalization of readability_analysis/extract_neighbor_titles.py
to all 200 Products eval nodes (the original only covered the 4 survey nodes
6813/1852/8766/8438). Same logic, unchanged: 1-hop/2-hop membership from the
node's own GraphNarrator pkl subgraph (outputs/pkls_products/{local_idx}.pkl),
title extraction via the same get_title() regex against products_canonical.pt.

Node_id -> local_idx (pkl filename) comes from
graphnarrator_products/index_to_global_node_id_mapping.json (already built
and verified for the production run: 200/200 eval_idx nodes, root_global_id
read directly from each pkl) rather than a hardcoded dict.

Run with GraphNarrator's venv (torch/torch_geometric/networkx stack).
"""
import json
import re
import sys
from collections import defaultdict

import torch

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from tag import TAG  # noqa: E402

PKL_DIR = "./graphnarrCora/GraphNarrator/outputs/pkls_products"
PRODUCTS_PT = "./products_canonical.pt"
MAPPING_PATH = "./production_run_2026-07-27/graphnarrator_products/index_to_global_node_id_mapping.json"
OUT_PATH = "./production_run_2026-07-27/consolidated/neighbor_titles_full.json"


def get_title(data, nid):
    """Same title-extraction logic as extract_neighbor_titles.py::get_title."""
    txt = data.raw_text[nid]
    txt = re.sub(r"^Product from Amazon platform with title and content:\s*", "", txt)
    m = re.search(r"[Tt]itle\s*:\s*(.+?)(?:\.\s*[Cc]ontent|$)", txt, re.DOTALL)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return txt[:70].strip()


def main():
    with open(MAPPING_PATH) as f:
        mapping = json.load(f)["mapping"]
    node_to_local_idx = {v["root_global_id"]: int(k) for k, v in mapping.items()}
    print(f"{len(node_to_local_idx)} nodes to process")

    print("Loading products_canonical.pt ...")
    data = torch.load(PRODUCTS_PT, map_location="cpu", weights_only=False)

    result = {}
    for node_id, local_idx in sorted(node_to_local_idx.items()):
        pkl_path = f"{PKL_DIR}/{local_idx}.pkl"
        g = TAG.load(pkl_path)

        gids = g.global_nids
        root_li = g.root_local_id
        assert gids[root_li] == node_id, (
            f"root global id mismatch for local_idx={local_idx}: expected {node_id}, got {gids[root_li]}"
        )

        adj = defaultdict(set)
        for s, d in zip(g.edges[0], g.edges[1]):
            if s != d:
                adj[s].add(d)
                adj[d].add(s)

        hop1_li = sorted(adj[root_li])
        hop1_set = set(hop1_li)
        hop1_gids = [gids[li] for li in hop1_li]
        hop2_gids = [
            gids[li] for li in range(len(g.nodes))
            if li != root_li and li not in hop1_set
        ]

        neighbors = []
        for nid in hop1_gids:
            neighbors.append({"node_id": nid, "title": get_title(data, nid), "hop": 1})
        for nid in hop2_gids:
            neighbors.append({"node_id": nid, "title": get_title(data, nid), "hop": 2})

        result[str(node_id)] = {"neighbors": neighbors}

    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote {OUT_PATH}: {len(result)} nodes")

    # sanity: cross-check against the original 4-node file for exact match
    with open("./readability_analysis/neighbor_titles.json") as f:
        orig = json.load(f)
    mismatches = []
    for node_id in orig:
        if result.get(node_id) != orig[node_id]:
            mismatches.append(node_id)
    print(f"Cross-check vs original 4-node neighbor_titles.json: {'MATCH' if not mismatches else 'MISMATCH: ' + str(mismatches)}")


if __name__ == "__main__":
    main()
