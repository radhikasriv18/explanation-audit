import json

OUT_DIR = "./production_run_2026-07-27/prediction_agreement"

cora_canon = json.load(open(f"{OUT_DIR}/cora_canonical_vs_gspell_full.json"))
prod_canon = json.load(open(f"{OUT_DIR}/products_canonical_vs_gspell_full.json"))
cora_gn = json.load(open(f"{OUT_DIR}/cora_graphnarrator_own_predictions.json"))
prod_gn = json.load(open(f"{OUT_DIR}/products_graphnarrator_own_predictions.json"))

report = {"cora": {}, "products": {}}

for dataset, canon, gn in [("cora", cora_canon, cora_gn), ("products", prod_canon, prod_gn)]:
    canon_per_node = canon["per_node"]
    gn_per_node = gn["per_node"]
    n = 0
    agree = 0
    gn_acc = 0
    for nid, gn_row in gn_per_node.items():
        if nid not in canon_per_node:
            continue
        n += 1
        c = canon_per_node[nid]["canonical_pred"]
        g = gn_row["graphnarrator_own_pred"]
        if c == g:
            agree += 1
        if g == gn_row["true_label"]:
            gn_acc += 1
    report[dataset]["graphnarrator_vs_canonical_agreement"] = agree / n
    report[dataset]["graphnarrator_own_accuracy"] = gn_acc / n
    report[dataset]["n_nodes_compared"] = n
    report[dataset]["canonical_accuracy"] = canon["summary"]["canonical_accuracy"]
    report[dataset]["gspell_vs_canonical_agreement"] = canon["summary"]["gspell_vs_canonical_agreement"]
    report[dataset]["gspell_own_accuracy"] = canon["summary"]["gspell_own_accuracy"]

# 8 survey nodes
survey_cora = [510, 2334, 1062, 884]
survey_products = [6813, 1852, 8766, 8438]
survey_table = []
for nid in survey_cora:
    key = str(nid)
    canon_row = cora_canon["per_node"][key]
    gn_row = cora_gn["per_node"][key]
    survey_table.append({
        "dataset": "cora", "node": nid,
        "true_label": canon_row["true_label"],
        "canonical_pred": canon_row["canonical_pred"],
        "graphnarrator_pred": gn_row["graphnarrator_own_pred"],
        "agrees_with_canonical": canon_row["canonical_pred"] == gn_row["graphnarrator_own_pred"],
    })
for nid in survey_products:
    key = str(nid)
    canon_row = prod_canon["per_node"][key]
    gn_row = prod_gn["per_node"][key]
    survey_table.append({
        "dataset": "products", "node": nid,
        "true_label": canon_row["true_label"],
        "canonical_pred": canon_row["canonical_pred"],
        "graphnarrator_pred": gn_row["graphnarrator_own_pred"],
        "agrees_with_canonical": canon_row["canonical_pred"] == gn_row["graphnarrator_own_pred"],
    })

report["survey_8node_graphnarrator_check"] = survey_table

with open(f"{OUT_DIR}/FINAL_agreement_report.json", "w") as f:
    json.dump(report, f, indent=2)

print(json.dumps(report, indent=2))
