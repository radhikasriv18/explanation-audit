#!/usr/bin/env python3
"""Re-apply the current hybrid code rules (judge.code_decide, v2: duplicate before range check, negated class
statement -> unverifiable, code duplicate detection) to an existing hybrid run WITHOUT any model call.

  python rescore_hybrid.py --from runs/llama_hybrid --dup-preset spec   -> runs/llama_hybrid_rescored_spec/
  python rescore_hybrid.py --from runs/llama_hybrid --dup-preset strict -> runs/llama_hybrid_rescored_strict/

Rows the new rules decide in code take the code verdict; every other row keeps the model verdict from --from. The new
rules only move rows from model to code, never back (asserted), so no row needs a fresh model call. Note the model saw
those rows with the batch composition of the original run.
"""
import argparse, csv, json, os, sys
from collections import Counter
sys.argv_saved = list(sys.argv)
import judge

csv.field_size_limit(sys.maxsize)
ap = argparse.ArgumentParser()
ap.add_argument("--from", dest="src", default="runs/llama_hybrid")
ap.add_argument("--dup-preset", choices=sorted(judge.DUP_PRESETS), default="spec")
a = ap.parse_args()
judge.DUP.update(judge.DUP_PRESETS[a.dup_preset])
src = os.path.join(judge.HERE, a.src)
rd = os.path.join(judge.HERE, f"runs/{os.path.basename(a.src.rstrip('/'))}_rescored_{a.dup_preset}")
os.makedirs(rd, exist_ok=True)
old = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(src, "judgments.csv")))}

out, codec, moved = [], [], Counter()
for ds, node in judge.ALL_NODES:
    rows, dec, _ = judge.plan(ds, node, True)
    for r in rows:
        o = old[r["claim_id"]]
        if r["claim_id"] in dec:
            v, why = dec[r["claim_id"]]
            if o["decided_by"] == "model":
                moved[("model->code", r["claim_kind"], v)] += 1
            elif (v, why) != (o["judge_verdict"], o["judge_reason"]):
                moved[("code changed", r["claim_kind"], f"{o['judge_verdict']}->{v}")] += 1
            by = "code"
            codec.append({"dataset": ds, "node": node, "claim_id": r["claim_id"], "claim_kind": r["claim_kind"],
                          "cited_node_id": r["cited_node_id"], "verdict": v, "reason": why, "claim_text": r["claim_text"]})
        else:
            assert o["decided_by"] == "model", f"{r['claim_id']} would need a new model call"
            v, why, by = o["judge_verdict"], o["judge_reason"], "model"
        out.append({**{k: o[k] for k in ("dataset", "node", "batch", "claim_id", "claim_kind", "cited_node_id")},
                    "judge_verdict": v, "judge_reason": why, "claim_text": r["claim_text"], "decided_by": by})
for name, rows_ in (("judgments.csv", out), ("code_decisions.csv", codec)):
    with open(os.path.join(rd, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows_[0])); w.writeheader(); w.writerows(rows_)
info = {"source_run": src, "dup_preset": a.dup_preset, "dup_settings": judge.DUP, "claims": len(out),
        "code_decided": len(codec), "model_rows": len(out) - len(codec),
        "changes_vs_source": {" | ".join(k): n for k, n in sorted(moved.items())}}
json.dump(info, open(os.path.join(rd, "rescore_info.json"), "w"), indent=1)
print(json.dumps(info, indent=1))
