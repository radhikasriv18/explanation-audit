"""
Re-measures GraphNarrator-vs-canonical prediction agreement using
GraphNarrator's OWN inference procedure (preprocess.py train()'s
validation/test loop: NeighborLoader(num_neighbors=[10]*2, batch_size=16),
stochastic 2-hop neighbor sampling, embeddings computed on the sampled
subgraph only) instead of the full-batch forward pass used in the original
prediction-agreement check.

Uses batch.input_id / batch.batch_size to extract exactly the seed (target)
node's own prediction per batch -- not the sampled context neighbors' -- so
each of the 542 Cora / 200 Products eval nodes gets exactly one prediction,
directly comparable to the earlier full-batch measurement.

A fixed torch seed (42) is set before building the NeighborLoader for
reproducibility of this specific re-measurement -- note this is an addition
for reproducibility, not a property of the original (unseeded) train()/eval
loops.
"""
import json
import sys

import numpy as np
import torch
from torch_geometric.loader import NeighborLoader

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from dataset import Encoder  # noqa: E402
from models.GNNs.sage import SAGE  # noqa: E402

torch.manual_seed(42)
np.random.seed(42)

DEVICE = "cuda"
OUT_DIR = "./production_run_2026-07-27/prediction_agreement"

SURVEY_NODES_CORA = [510, 2334, 1062, 884]
SURVEY_NODES_PRODUCTS = [6813, 1852, 8766, 8438]


@torch.no_grad()
def run_dataset(name, canonical_pt_path, ckpt_path, target_ids, survey_ids, batch_size=16):
    print(f"=== {name} ===", flush=True)
    data = torch.load(canonical_pt_path, map_location="cpu", weights_only=False)
    texts = list(data.raw_text)
    label_names = data.label_names
    y = data.y
    out_dim = len(label_names)

    target_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
    target_mask[torch.as_tensor(target_ids, dtype=torch.long)] = True

    data_gpu = data.clone()
    if hasattr(data_gpu, "raw_text"):
        delattr(data_gpu, "raw_text")
    if hasattr(data_gpu, "text"):
        delattr(data_gpu, "text")
    data_gpu = data_gpu.to(DEVICE)

    encoder = Encoder()  # bert-base-uncased, frozen, .to("cuda") internally

    gnn = SAGE(in_channels=768, hidden_channels=768, out_channels=out_dim, num_layers=2, dropout=0.0).to(DEVICE)
    gnn.load_state_dict(torch.load(ckpt_path, map_location=DEVICE))
    gnn.eval()

    loader = NeighborLoader(data_gpu, num_neighbors=[10, 10], batch_size=batch_size, input_nodes=target_mask.to(DEVICE))

    pred_by_node = {}
    n_batches = 0
    for batch in loader:
        n_batches += 1
        seed_n = batch.batch_size
        seed_global_ids = batch.input_id[:seed_n].tolist()
        sampled_local_ids = batch.n_id.tolist()

        embs = torch.cat([encoder.encode(texts[i]).detach() for i in sampled_local_ids], dim=0).to(DEVICE)
        edge_index = batch.edge_index.to(DEVICE)

        logits = gnn(embs, edge_index)
        pred = logits.argmax(dim=-1)

        for i, gid in enumerate(seed_global_ids):
            pred_by_node[gid] = pred[i].item()

        if n_batches % 10 == 0:
            print(f"  batch {n_batches}, {len(pred_by_node)}/{len(target_ids)} nodes done", flush=True)

    print(f"  total batches: {n_batches}, nodes predicted: {len(pred_by_node)} / {len(target_ids)}")

    results = {}
    for nid in target_ids:
        pred_cls = pred_by_node.get(nid)
        results[str(nid)] = {
            "true_label": label_names[y[nid].item()],
            "graphnarrator_own_pred_stochastic": label_names[pred_cls] if pred_cls is not None else None,
        }

    n = sum(1 for v in results.values() if v["graphnarrator_own_pred_stochastic"] is not None)
    acc = sum(1 for v in results.values() if v["graphnarrator_own_pred_stochastic"] == v["true_label"]) / n

    summary = {
        "dataset": name,
        "n_eval_nodes": len(target_ids),
        "n_predicted": n,
        "graphnarrator_own_accuracy_stochastic": acc,
        "batch_size": batch_size,
        "num_neighbors": [10, 10],
        "seed": 42,
        "survey_nodes": {str(nid): results[str(nid)] for nid in survey_ids if str(nid) in results},
    }

    out_path = f"{OUT_DIR}/{name}_graphnarrator_own_predictions_STOCHASTIC.json"
    with open(out_path, "w") as f:
        json.dump({"summary": summary, "per_node": results}, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    cora_splits = np.load("./graphnarrCora/GraphNarrator/cora_splits_seed42.npz")
    cora_eval_ids = cora_splits["test_idx"].tolist()
    assert len(cora_eval_ids) == 542

    products_splits = np.load("./LOGIC2/GSPELL/products_splits_seed42.npz")
    products_eval_ids = products_splits["eval_idx"].tolist()
    assert len(products_eval_ids) == 200

    run_dataset(
        "cora",
        "./cora_canonical.pt",
        "./graphnarrCora/GraphNarrator/GNN_cora_seed_42.pt",
        cora_eval_ids,
        SURVEY_NODES_CORA,
    )
    run_dataset(
        "products",
        "./products_canonical.pt",
        "./graphnarrCora/GraphNarrator/GNN_products_seed_42.pt",
        products_eval_ids,
        SURVEY_NODES_PRODUCTS,
        batch_size=8,
    )
