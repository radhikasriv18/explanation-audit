"""
Re-parse the saved raw outputs in extractions/*.json with the current parse_output()
(no model call). raw_output, prompts and generation settings are left untouched; only
claims / n_claims / claim_type_counts / parse_diagnostics are refreshed, and
claim_counts.csv is rewritten. Earlier parse results are kept under "parse_history".
"""
import csv
import json
from pathlib import Path

from extract_claims import CLAIM_TYPES, parse_output

HERE = Path(__file__).resolve().parent
AK = {e["id"]: e for e in json.load(open(HERE / "answer_key_texts.json"))}
ORDER = list(AK)

rows = []
recs = [json.load(open(p)) for p in sorted((HERE / "extractions").glob("*.json"))]
recs.sort(key=lambda r: (ORDER.index(r["answer_key_id"]), r["run_id"].endswith("__full")))
for r in recs:
    claims, diag = parse_output(r["raw_output"])
    for k in ("n_prompt_tokens", "n_output_tokens", "hit_max_new_tokens", "seconds"):
        diag[k] = r["parse_diagnostics"].get(k)
    if claims != r["claims"]:
        r.setdefault("parse_history", []).append({"n_claims": r["n_claims"], "parse_diagnostics": r["parse_diagnostics"]})
    r["claims"], r["n_claims"], r["parse_diagnostics"] = claims, len(claims), diag
    r["claim_type_counts"] = {t: sum(c["claim_type"] == t for c in claims) for t in CLAIM_TYPES}
    json.dump(r, open(HERE / "extractions" / f"{r['run_id']}.json", "w"), indent=1)
    m = r["manual"]
    rows.append(
        {
            "run_id": r["run_id"],
            "method": r["method"],
            "dataset": r["dataset"],
            "node": r["node"],
            "text_scope": r["text_scope"],
            "n_extracted_claims": len(claims),
            "n_manual_adjudicated": m["n_claims_adjudicated"],
            "manual_supported": m["n_supported"],
            "manual_unsupported": m["n_unsupported"],
            "manual_count_source": m["count_source"],
            "chat_csv_precision": AK[r["answer_key_id"]]["chat_csv_precision"],
            "parse_mode": diag["parse_mode"],
            "n_repairs": len(diag["repairs"]),
            "n_unrecoverable": len(diag["unrecoverable_segments"]),
            "n_merged_duplicates": diag["n_merged_duplicates"],
            "n_bad_type": diag["n_bad_type"],
            "hit_max_new_tokens": diag["hit_max_new_tokens"],
            **{f"n_{t}": r["claim_type_counts"][t] for t in CLAIM_TYPES},
        }
    )
    print(f"{r['run_id']:40s} {diag['parse_mode']:22s} claims={len(claims):3d} raw={diag['n_raw_claims']:3d} repairs={len(diag['repairs'])} unrec={len(diag['unrecoverable_segments'])} dup={diag['n_merged_duplicates']} manual={m['n_claims_adjudicated']}")

with open(HERE / "claim_counts.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
