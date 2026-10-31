"""
Canonical GraphSAGE prediction for EVERY node (the persisted
production_run_2026-07-27/prediction_agreement/*_canonical_vs_gspell_full.json covers only the
542 Cora / 200 Products eval nodes, so most cited neighbours had no canonical prediction).
Same model class, weights and full-graph forward pass as predict_canonical_and_gspell.py
(canonical part only). Asserts agreement with every persisted eval-node prediction.
Run: PYTHONDONTWRITEBYTECODE=1 ~/.conda/envs/graphnarr/bin/python predict_canonical_allnodes.py
"""
import json
import sys
from pathlib import Path

import torch

sys.path.insert(0, "./llm-graph-cf/src")
from gnn_model import GraphSAGE  # noqa: E402

R = Path(".")
OUT = Path(__file__).resolve().parent / "canonical_pred_allnodes"
CFG = {"cora": (R / "cora_canonical.pt", R / "llm-graph-cf/pretrained/sage_canonical.pt"),
       "products": (R / "products_canonical.pt", R / "sage_products_canonical.pt")}

for ds, (dp, wp) in CFG.items():
    data = torch.load(dp, map_location="cpu", weights_only=False)
    m = GraphSAGE(in_channels=data.x.shape[1], hidden_channels=768, out_channels=len(data.label_names), num_layers=2, dropout=0.0)
    m.load_state_dict(torch.load(wp, map_location="cpu", weights_only=True))
    m.eval()
    with torch.no_grad():
        pred = m(data.x, data.edge_index).argmax(-1).tolist()
    names = [data.label_names[p] for p in pred]
    ref = json.load(open(R / f"production_run_2026-07-27/prediction_agreement/{ds}_canonical_vs_gspell_full.json"))["per_node"]
    mism = [k for k, v in ref.items() if v["canonical_pred"] != names[int(k)]]
    print(ds, "nodes", len(names), "persisted eval nodes", len(ref), "mismatches", len(mism), mism[:10])
    assert not mism
    json.dump({"source": str(wp), "graph": str(dp), "n_nodes": len(names), "checked_against_persisted": len(ref),
               "canonical_pred": names}, open(OUT / f"{ds}_canonical_pred_allnodes.json", "w"))
