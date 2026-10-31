"""
Full-batch prediction-agreement check for the paper-aligned retrained
checkpoints (same methodology as prediction_agreement/predict_graphnarrator.py,
just pointed at the new checkpoint files) -- one prediction per exact global
eval node (542 Cora / 200 Products), full-graph forward pass.
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

DEVICE = "cuda"
OUT_DIR = "./production_run_2026-07-27/prediction_agreement"
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
    return torch.cat(embs, dim=0)


def run_dataset(name, canonical_pt_path, ckpt_path, eval_ids):
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

    text_embs = encode_all_text(model, texts).to(DEVICE)
    edge_index = data.edge_index.to(DEVICE)

    with torch.no_grad():
        logits = model.forward_gnn(text_embs, edge_index)
        pred = logits.argmax(dim=-1).cpu()

    results = {}
    for nid in eval_ids:
        results[str(nid)] = {
            "true_label": label_names[y[nid].item()],
            "graphnarrator_paperaligned_pred": label_names[pred[nid].item()],
        }

    n = len(results)
    acc = sum(1 for v in results.values() if v["graphnarrator_paperaligned_pred"] == v["true_label"]) / n

    canon = json.load(open(f"{OUT_DIR}/{name}_canonical_vs_gspell_full.json"))["per_node"]
    agree = sum(1 for nid, v in results.items() if v["graphnarrator_paperaligned_pred"] == canon[nid]["canonical_pred"]) / n

    summary = {"dataset": name, "n_eval_nodes": n, "own_accuracy": acc, "agreement_vs_canonical": agree, "checkpoint": ckpt_path}
    with open(f"{OUT_DIR}/{name}_graphnarrator_paperaligned_predictions.json", "w") as f:
        json.dump({"summary": summary, "per_node": results}, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    cora_splits = np.load(f"{REPO}/cora_splits_seed42.npz")
    products_splits = np.load("./LOGIC2/GSPELL/products_splits_seed42.npz")

    run_dataset(
        "cora", "./cora_canonical.pt",
        f"{REPO}/checkpoints_paperaligned_2026-08-04/GNN_cora_seed_42_paperaligned.pt",
        cora_splits["test_idx"].tolist(),
    )
    run_dataset(
        "products", "./products_canonical.pt",
        f"{REPO}/checkpoints_paperaligned_2026-08-04/GNN_products_seed_42_paperaligned.pt",
        products_splits["eval_idx"].tolist(),
    )
