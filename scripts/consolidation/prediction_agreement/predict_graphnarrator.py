"""
Prediction agreement check, part 2: GraphNarrator's own checkpoint.

Run under GraphNarrator's own venv, with CWD = the GraphNarrator repo root
(models/joint_model.py loads a config json via a path relative to CWD).
Imports GraphNarrator's own LM_GNN_Joint_Model + BERT config directly so the
forward pass matches its own pipeline exactly (custom MyBertModel, not stock
HF BertModel -- weights are copied from HF but the module implementation
differs, so reuse is required for a faithful check, not just numerically
close).

Full-batch approach: compute BERT-pooled embeddings for EVERY node's raw text
once (not GraphNarrator's stochastic 2-hop NeighborLoader sampling used during
its own training/pkl generation), then run the checkpoint's SAGE sublayer over
the FULL graph edge_index. This is deliberately more complete than the
10-neighbor x 2-hop sample GraphNarrator trains/evals with (full neighborhood
is a superset) and removes sampling randomness from the agreement number, so
results are exactly reproducible given the fixed checkpoint. This is a
methodological deviation from GraphNarrator's own validation loop, called out
in standardization_notes.md.

Writes JSON with per-node predictions + ground truth.
"""
import json
import os
import sys

import numpy as np
import torch

REPO = "./graphnarrCora/GraphNarrator"
os.chdir(REPO)
sys.path.insert(0, REPO)

from models.joint_model import LM_GNN_Joint_Model  # noqa: E402

torch.manual_seed(42)
np.random.seed(42)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
assert DEVICE == "cuda", "GraphNarrator's BERT encoder hardcodes .to('cuda')"
OUT_DIR = "./production_run_2026-07-27/prediction_agreement"

SURVEY_NODES_CORA = [510, 2334, 1062, 884]
SURVEY_NODES_PRODUCTS = [6813, 1852, 8766, 8438]

BERT_BATCH = 32


@torch.no_grad()
def encode_all_text(model, texts):
    embs = []
    for i in range(0, len(texts), BERT_BATCH):
        batch_texts = texts[i : i + BERT_BATCH]
        inputs = model.tokenizer(
            batch_texts, return_tensors="pt", truncation=True, padding="max_length", max_length=512
        ).to(DEVICE)
        pooled = model.bert(**inputs)[1]
        embs.append(pooled.cpu())
        if i % (BERT_BATCH * 20) == 0:
            print(f"  encoded {i}/{len(texts)}", flush=True)
    return torch.cat(embs, dim=0)


def run_dataset(name, canonical_pt_path, ckpt_path, eval_ids, survey_ids):
    print(f"=== {name} ===", flush=True)
    data = torch.load(canonical_pt_path, map_location="cpu", weights_only=False)
    texts = list(data.raw_text)
    label_names = data.label_names
    y = data.y
    out_dim = len(label_names)

    model = LM_GNN_Joint_Model(out_dim=out_dim).to(DEVICE)
    ckpt = torch.load(ckpt_path, map_location=DEVICE, weights_only=True)
    model.gnn.load_state_dict(ckpt)
    model.eval()

    print(f"encoding {len(texts)} node texts with BERT...", flush=True)
    text_embs = encode_all_text(model, texts).to(DEVICE)
    edge_index = data.edge_index.to(DEVICE)

    with torch.no_grad():
        logits = model.forward_gnn(text_embs, edge_index)
        pred = logits.argmax(dim=-1).cpu()

    results = {}
    for nid in eval_ids:
        results[str(nid)] = {
            "true_label": label_names[y[nid].item()],
            "graphnarrator_own_pred": label_names[pred[nid].item()],
        }

    n = len(results)
    acc = sum(1 for v in results.values() if v["graphnarrator_own_pred"] == v["true_label"]) / n

    summary = {
        "dataset": name,
        "n_eval_nodes": n,
        "graphnarrator_own_accuracy": acc,
        "checkpoint": ckpt_path,
        "survey_nodes": {str(nid): results[str(nid)] for nid in survey_ids if str(nid) in results},
    }

    out_path = f"{OUT_DIR}/{name}_graphnarrator_own_predictions.json"
    with open(out_path, "w") as f:
        json.dump({"summary": summary, "per_node": results}, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    cora_splits = np.load(f"{REPO}/cora_splits_seed42.npz")
    cora_eval_ids = cora_splits["test_idx"].tolist()
    assert len(cora_eval_ids) == 542

    products_splits = np.load("./LOGIC2/GSPELL/products_splits_seed42.npz")
    products_eval_ids = products_splits["eval_idx"].tolist()
    assert len(products_eval_ids) == 200

    run_dataset(
        "cora",
        "./cora_canonical.pt",
        f"{REPO}/GNN_cora_seed_42.pt",
        cora_eval_ids,
        SURVEY_NODES_CORA,
    )
    run_dataset(
        "products",
        "./products_canonical.pt",
        f"{REPO}/GNN_products_seed_42.pt",
        products_eval_ids,
        SURVEY_NODES_PRODUCTS,
    )
