"""
Build the claim-level answer-key sheet from the v2 extractions (no model call).

claim_answer_key_v2.csv — one row per extracted claim, in answer-key order:
  method, dataset, node, claim_id, claim_text, claim_type, entities, source_text_file, verdict, note
verdict (supported / contradicted / unverifiable) and note are left empty for manual annotation.
entities is the claim's entity dict as compact JSON.

count_comparison_v1_v2.csv — per text: v1 count, v2 count, manual count (primary scope only).
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
AK = json.load(open(HERE / "answer_key_texts.json"))
COLUMNS = ["method", "dataset", "node", "claim_id", "claim_text", "claim_type", "entities", "source_text_file", "verdict", "note"]

rows, comp = [], []
for e in AK:
    v2 = json.load(open(HERE / "extractions_v2" / f"{e['id']}.json"))
    v1 = json.load(open(HERE / "extractions" / f"{e['id']}.json"))
    assert v2["input_text"] == e["text_scored"] == v1["input_text"], e["id"]
    for i, c in enumerate(v2["claims"], 1):
        rows.append(
            {
                "method": e["method"],
                "dataset": e["dataset"],
                "node": e["node"],
                "claim_id": f"{e['id']}_c{i:02d}",
                "claim_text": c["claim"],
                "claim_type": c["claim_type"],
                "entities": json.dumps(c["entities"], ensure_ascii=False, separators=(",", ":")),
                "source_text_file": e["source_file"],
                "verdict": "",
                "note": "",
            }
        )
    m = e["manual"]
    comp.append(
        {
            "id": e["id"],
            "method": e["method"],
            "dataset": e["dataset"],
            "node": e["node"],
            "n_claims_v1": v1["n_claims"],
            "n_claims_v2": v2["n_claims"],
            "delta": v2["n_claims"] - v1["n_claims"],
            "n_manual_adjudicated": m["n_claims_adjudicated"],
            "manual_supported": m["n_supported"],
            "manual_unsupported": m["n_unsupported"],
            "chat_csv_precision": e["chat_csv_precision"],
            "v2_parse_mode": v2["parse_diagnostics"]["parse_mode"],
            "v2_n_repairs": len(v2["parse_diagnostics"]["repairs"]),
            "v2_n_merged_duplicates": v2["parse_diagnostics"]["n_merged_duplicates"],
            "v2_n_bad_type": v2["parse_diagnostics"]["n_bad_type"],
            **{f"v2_n_{k}": v for k, v in v2["claim_type_counts"].items()},
        }
    )

with open(HERE / "claim_answer_key_v2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writeheader()
    w.writerows(rows)
with open(HERE / "count_comparison_v1_v2.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(comp[0].keys()))
    w.writeheader()
    w.writerows(comp)
print(f"claim_answer_key_v2.csv: {len(rows)} claim rows from {len(AK)} texts")
for c in comp:
    print(f"{c['id']:32s} v1={c['n_claims_v1']:3d} v2={c['n_claims_v2']:3d} manual={c['n_manual_adjudicated']}")
