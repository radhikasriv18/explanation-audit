"""
Build claim_answer_key_v3.csv from cleaned_v3/ (no model call), plus count_comparison_v2_v3.csv.

Columns: method, dataset, node, claim_id, claim_text, claim_type, entities, source_text_file,
         source_span, span_check, corrected_type, verdict, note
- claim_id = <answer-key id>_c<extraction index>, so ids match cleanup_log_v3.csv / span_check_failures_v3.csv.
- claim_type is the type after the rule-based clean-up; corrected_type, verdict and note are empty.
- verdict must be one of: supported, contradicted, unverifiable, not_a_claim (see claim_answer_key_v3_codebook.md).
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
AK = json.load(open(HERE / "answer_key_texts.json"))
COLUMNS = ["method", "dataset", "node", "claim_id", "claim_text", "claim_type", "entities", "source_text_file", "source_span", "span_check", "corrected_type", "verdict", "note"]

rows, comp = [], []
for e in AK:
    cl = json.load(open(HERE / "cleaned_v3" / f"{e['id']}.json"))
    v3 = json.load(open(HERE / "extractions_v3" / f"{e['id']}.json"))
    v2 = json.load(open(HERE / "extractions_v2" / f"{e['id']}.json"))
    assert v3["input_text"] == v2["input_text"] == e["text_scored"], e["id"]
    for c in cl["claims_final"]:
        rows.append(
            {
                "method": e["method"],
                "dataset": e["dataset"],
                "node": e["node"],
                "claim_id": f"{e['id']}_c{c['extraction_index']:02d}",
                "claim_text": c["claim"],
                "claim_type": c["claim_type"],
                "entities": json.dumps(c["entities"], ensure_ascii=False, separators=(",", ":")),
                "source_text_file": e["source_file"],
                "source_span": c.get("source_span", ""),
                "span_check": c["span_check"],
                "corrected_type": "",
                "verdict": "",
                "note": "",
            }
        )
    acts = {}
    for l in cl["cleanup_log"]:
        acts[l["action"]] = acts.get(l["action"], 0) + 1
    m = e["manual"]
    comp.append(
        {
            "id": e["id"],
            "n_v2": v2["n_claims"],
            "n_v3_extracted": cl["n_extracted"],
            "n_v3_after_cleanup": cl["n_final"],
            "n_relabel": acts.get("relabel", 0),
            "n_drop_evaluation_only": acts.get("drop_evaluation_only", 0),
            "n_merge_into_field": acts.get("merge_into_field", 0),
            "n_merge_ambiguous_kept": acts.get("merge_ambiguous_kept", 0),
            "n_span_fail_extracted": cl["n_span_fail_extracted"],
            "n_span_fail_final": cl["n_span_fail_final"],
            "n_manual_adjudicated": m["n_claims_adjudicated"],
            "chat_csv_precision": e["chat_csv_precision"],
            "v3_parse_mode": v3["parse_diagnostics"]["parse_mode"],
            "v3_n_repairs": len(v3["parse_diagnostics"]["repairs"]),
        }
    )

with open(HERE / "claim_answer_key_v3.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writeheader()
    w.writerows(rows)
with open(HERE / "count_comparison_v2_v3.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(comp[0].keys()))
    w.writeheader()
    w.writerows(comp)
print(f"claim_answer_key_v3.csv: {len(rows)} rows")
for c in comp:
    print(" ".join(f"{k}={v}" for k, v in c.items() if k not in ("chat_csv_precision",)))
