"""
claim_answer_key_v4.csv = v3 sheet rows (same clean-up output in cleaned_v3/, no model call) with
  - span_check recomputed by span_check_v4.span_check (markdown markers, case, quote characters
    and spacing around punctuation ignored; paraphrased/stitched spans still fail)
  - reference_file: the packet in reference_packets/ for that text.
Also writes span_check_failures_v4.csv. Verdict values: supported, contradicted, unverifiable, not_a_claim.
"""
import csv
import json
from pathlib import Path

from span_check_v4 import span_check

HERE = Path(__file__).resolve().parent
AK = json.load(open(HERE / "answer_key_texts.json"))
COLUMNS = ["method", "dataset", "node", "claim_id", "claim_text", "claim_type", "entities", "source_text_file", "source_span", "span_check", "corrected_type", "verdict", "note", "reference_file"]

rows, fails, per_text = [], [], []
for e in AK:
    ref = f"reference_packets/{e['id']}.md"
    assert (HERE / ref).exists(), ref
    cl = json.load(open(HERE / "cleaned_v3" / f"{e['id']}.json"))
    n_fail = 0
    for c in cl["claims_final"]:
        sc = span_check(c.get("source_span"), e["text_scored"])
        cid = f"{e['id']}_c{c['extraction_index']:02d}"
        rows.append(
            {
                "method": e["method"], "dataset": e["dataset"], "node": e["node"], "claim_id": cid,
                "claim_text": c["claim"], "claim_type": c["claim_type"],
                "entities": json.dumps(c["entities"], ensure_ascii=False, separators=(",", ":")),
                "source_text_file": e["source_file"], "source_span": c.get("source_span", ""),
                "span_check": sc, "corrected_type": "", "verdict": "", "note": "", "reference_file": ref,
            }
        )
        if sc == "fail":
            n_fail += 1
            fails.append({"claim_id": cid, "claim": c["claim"], "source_span": c.get("source_span", ""), "v3_span_check": c["span_check"]})
    per_text.append((e["id"], cl["n_final"], sum(c["span_check"] == "fail" for c in cl["claims_final"]), n_fail))

with open(HERE / "claim_answer_key_v4.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writeheader()
    w.writerows(rows)
with open(HERE / "span_check_failures_v4.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["claim_id", "claim", "source_span", "v3_span_check"])
    w.writeheader()
    w.writerows(fails)
print(f"claim_answer_key_v4.csv: {len(rows)} rows; span fail {len(fails)}")
for t in per_text:
    print(f"{t[0]:32s} claims={t[1]:3d} v3_fail={t[2]:2d} v4_fail={t[3]:2d}")
