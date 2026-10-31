import json

OUT_DIR = "./production_run_2026-07-27/prediction_agreement"

for name, canon_file in [("cora", "cora_canonical_vs_gspell_full.json"), ("products", "products_canonical_vs_gspell_full.json")]:
    canon = json.load(open(f"{OUT_DIR}/{canon_file}"))["per_node"]
    stoch = json.load(open(f"{OUT_DIR}/{name}_graphnarrator_own_predictions_STOCHASTIC.json"))["per_node"]

    n = 0
    agree = 0
    acc = 0
    for nid, row in stoch.items():
        pred = row["graphnarrator_own_pred_stochastic"]
        if pred is None or nid not in canon:
            continue
        n += 1
        if pred == canon[nid]["canonical_pred"]:
            agree += 1
        if pred == row["true_label"]:
            acc += 1

    print(f"{name}: n={n} agreement_vs_canonical={agree/n:.4f} own_accuracy={acc/n:.4f}")
