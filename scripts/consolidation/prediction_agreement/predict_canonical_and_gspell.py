"""
Prediction agreement check, part 1: canonical SAGE + GSPELL's own checkpoint.

Run under GSPELL's venv (narratives/bin/activate) since it has torch_geometric
and this script imports GSPELL's own PretrainedModel class directly (so the
GSPELL forward pass is byte-for-byte what GSPELL's own pipeline would compute,
not a reimplementation).

Computes, for every node in the FULL eval split of each dataset:
  - canonical SAGE prediction (sage_canonical.pt / sage_products_canonical.pt,
    same architecture llm-graph-cf/GraphXAIN load directly)
  - GSPELL's own checkpoint prediction (Cora: pretrained sage.pth, a genuinely
    separate ~30%-acc weight set; Products: sage_canonical.pth, which is the
    canonical weights re-keyed -- included for transparency, expected ~100%
    trivial agreement, NOT an independent model)

Writes JSON with per-node predictions + ground truth to this directory.
"""
import json
import sys

import numpy as np
import torch
import torch.nn.functional as F

sys.path.insert(0, "./llm-graph-cf/src")
from gnn_model import GraphSAGE  # noqa: E402

sys.path.insert(0, "./LOGIC2/GSPELL")
from model import PretrainedModel  # noqa: E402

torch.manual_seed(42)
np.random.seed(42)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
OUT_DIR = "./production_run_2026-07-27/prediction_agreement"

SURVEY_NODES_CORA = [510, 2334, 1062, 884]
SURVEY_NODES_PRODUCTS = [6813, 1852, 8766, 8438]


def run_cora():
    data = torch.load("./cora_canonical.pt", map_location="cpu", weights_only=False)
    x = data.x.to(DEVICE)
    edge_index = data.edge_index.to(DEVICE)
    y = data.y
    label_names = data.label_names
    test_id = data.test_id.tolist()
    assert len(test_id) == 542, f"expected 542 Cora test nodes, got {len(test_id)}"

    # --- canonical SAGE ---
    canon = GraphSAGE(in_channels=x.shape[1], hidden_channels=768, out_channels=len(label_names), num_layers=2, dropout=0.0).to(DEVICE)
    canon.load_state_dict(torch.load("./llm-graph-cf/pretrained/sage_canonical.pt", map_location=DEVICE, weights_only=True))
    canon.eval()
    with torch.no_grad():
        canon_logits = canon(x, edge_index)
        canon_pred = canon_logits.argmax(dim=-1).cpu()

    # --- GSPELL's own Cora checkpoint (genuinely separate weights) ---
    gspell = PretrainedModel(
        gnn_type="sage", in_channels=x.shape[1], hidden_channels=768, out_channels=len(label_names),
        gnn_num_hid_layers=2, dropout=0.0, with_bn=False, decoder_type="linear",
        with_last_dropout=False, mode="node", device=DEVICE,
    ).to(DEVICE)
    sd = torch.load(
        "./LOGIC2/GSPELL/pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/sage.pth",
        map_location=DEVICE, weights_only=True,
    )["model_state_dict"]
    gspell.load_state_dict({k: v for k, v in sd.items() if k in gspell.state_dict()})
    gspell.eval()
    with torch.no_grad():
        gspell_logits, _ = gspell(x=x, edge_index=edge_index)
        gspell_pred = gspell_logits.argmax(dim=-1).cpu()

    results = {}
    for nid in test_id:
        results[str(nid)] = {
            "true_label": label_names[y[nid].item()],
            "canonical_pred": label_names[canon_pred[nid].item()],
            "gspell_own_pred": label_names[gspell_pred[nid].item()],
        }

    agree = sum(1 for v in results.values() if v["canonical_pred"] == v["gspell_own_pred"])
    canon_acc = sum(1 for v in results.values() if v["canonical_pred"] == v["true_label"])
    gspell_acc = sum(1 for v in results.values() if v["gspell_own_pred"] == v["true_label"])
    n = len(results)

    summary = {
        "dataset": "cora",
        "n_eval_nodes": n,
        "gspell_vs_canonical_agreement": agree / n,
        "canonical_accuracy": canon_acc / n,
        "gspell_own_accuracy": gspell_acc / n,
        "survey_nodes": {
            str(nid): results[str(nid)] for nid in SURVEY_NODES_CORA if str(nid) in results
        },
    }

    with open(f"{OUT_DIR}/cora_canonical_vs_gspell_full.json", "w") as f:
        json.dump({"summary": summary, "per_node": results}, f, indent=2)
    print("CORA:", json.dumps(summary, indent=2))


def run_products():
    data = torch.load("./products_canonical.pt", map_location="cpu", weights_only=False)
    x = data.x.to(DEVICE)
    edge_index = data.edge_index.to(DEVICE)
    y = data.y
    label_names = data.label_names

    splits = np.load("./LOGIC2/GSPELL/products_splits_seed42.npz")
    eval_id = splits["eval_idx"].tolist()
    assert len(eval_id) == 200, f"expected 200 Products eval nodes, got {len(eval_id)}"

    # --- canonical SAGE ---
    canon = GraphSAGE(in_channels=x.shape[1], hidden_channels=768, out_channels=len(label_names), num_layers=2, dropout=0.0).to(DEVICE)
    canon.load_state_dict(torch.load("./sage_products_canonical.pt", map_location=DEVICE, weights_only=True))
    canon.eval()
    with torch.no_grad():
        canon_logits = canon(x, edge_index)
        canon_pred = canon_logits.argmax(dim=-1).cpu()

    # --- GSPELL's own Products "checkpoint" (re-keyed canonical weights -- tautological, see docstring) ---
    gspell = PretrainedModel(
        gnn_type="sage", in_channels=x.shape[1], hidden_channels=768, out_channels=len(label_names),
        gnn_num_hid_layers=2, dropout=0.0, with_bn=False, decoder_type="linear",
        with_last_dropout=False, mode="node", device=DEVICE,
    ).to(DEVICE)
    sd = torch.load(
        "./LOGIC2/GSPELL/pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct/sage_canonical.pth",
        map_location=DEVICE, weights_only=True,
    )["model_state_dict"]
    gspell.load_state_dict({k: v for k, v in sd.items() if k in gspell.state_dict()})
    gspell.eval()
    with torch.no_grad():
        gspell_logits, _ = gspell(x=x, edge_index=edge_index)
        gspell_pred = gspell_logits.argmax(dim=-1).cpu()

    results = {}
    for nid in eval_id:
        results[str(nid)] = {
            "true_label": label_names[y[nid].item()],
            "canonical_pred": label_names[canon_pred[nid].item()],
            "gspell_own_pred": label_names[gspell_pred[nid].item()],
        }

    agree = sum(1 for v in results.values() if v["canonical_pred"] == v["gspell_own_pred"])
    canon_acc = sum(1 for v in results.values() if v["canonical_pred"] == v["true_label"])
    gspell_acc = sum(1 for v in results.values() if v["gspell_own_pred"] == v["true_label"])
    n = len(results)

    summary = {
        "dataset": "products",
        "n_eval_nodes": n,
        "gspell_vs_canonical_agreement": agree / n,
        "canonical_accuracy": canon_acc / n,
        "gspell_own_accuracy": gspell_acc / n,
        "note": "GSPELL's Products checkpoint is the canonical weights re-keyed (gen_products_canonical_data.py), not an independently trained model -- this agreement number is expected to be ~1.0 by construction, not a meaningful independence check.",
        "survey_nodes": {
            str(nid): results[str(nid)] for nid in SURVEY_NODES_PRODUCTS if str(nid) in results
        },
    }

    with open(f"{OUT_DIR}/products_canonical_vs_gspell_full.json", "w") as f:
        json.dump({"summary": summary, "per_node": results}, f, indent=2)
    print("PRODUCTS:", json.dumps(summary, indent=2))


if __name__ == "__main__":
    print("device:", DEVICE)
    run_cora()
    run_products()
