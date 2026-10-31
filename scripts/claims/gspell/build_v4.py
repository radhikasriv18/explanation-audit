#!/usr/bin/env python3
"""
v4 sheets from v3 (v3 never modified). Rule R6: the 19 rows listed in v3_near_misses.csv
(Products 8766, loop/boilerplate lines under a fake product id in a block with no Summary row)
-> suggested_verdict = unverifiable, suggest_reason = "loop/boilerplate text, not a claim about the
node (R6); fake id already counted in its neighbor_exists row". Changes logged in v4_changes.csv.
Also checks that each row's block has a contradicted neighbor_exists row for the same fake id.
No model calls.
"""
import csv, sys
csv.field_size_limit(sys.maxsize)
D = "./gspell_grounding_manual_2026-10-10/"
NODES = [("cora", "510"), ("cora", "2334"), ("cora", "1062"), ("cora", "884"),
         ("products", "6813"), ("products", "1852"), ("products", "8766"), ("products", "8438")]
REASON = "loop/boilerplate text, not a claim about the node (R6); fake id already counted in its neighbor_exists row"
targets = {(r["node"], r["claim_id"]) for r in csv.DictReader(open(D + "v3_near_misses.csv"))}
assert len(targets) == 19, len(targets)
changes, summary, allv4, seen = [], [], [], set()
for ds, node in NODES:
    rows = list(csv.DictReader(open(D + f"claims_{ds}_{node}_v3.csv")))
    exists = {(r["batch_idx"], r["cited_node_id"]) for r in rows
              if r["claim_kind"] == "neighbor_exists" and r["suggested_verdict"] == "contradicted"}
    for r in rows:
        if (node, r["claim_id"]) in targets:
            seen.add((node, r["claim_id"]))
            changes.append({"node": node, "dataset": ds, "claim_id": r["claim_id"], "batch_idx": r["batch_idx"],
                            "cited_node_id": r["cited_node_id"], "claim_kind": r["claim_kind"],
                            "old_suggested_verdict": r["suggested_verdict"], "old_suggest_reason": r["suggest_reason"],
                            "new_suggested_verdict": "unverifiable", "new_suggest_reason": REASON,
                            "fake_id_has_contradicted_neighbor_exists_row_in_batch": (r["batch_idx"], r["cited_node_id"]) in exists,
                            "claim_text": r["claim_text"][:300]})
            r["suggested_verdict"], r["suggest_reason"] = "unverifiable", REASON
    with open(D + f"claims_{ds}_{node}_v4.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    allv4 += rows
    c = lambda v: sum(x["suggested_verdict"] == v for x in rows)
    summary.append({"dataset": ds, "node": node, "rows": len(rows), "changed_R6": sum(ch["node"] == node for ch in changes),
                    "supported": c("supported"), "contradicted": c("contradicted"), "unverifiable": c("unverifiable"),
                    "duplicate": c("duplicate"), "manual_blank": c("")})
assert seen == targets, targets - seen
with open(D + "claims_all_nodes_v4.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(allv4[0])); w.writeheader(); w.writerows(allv4)
for name, rows in (("v4_changes.csv", changes), ("v4_summary.csv", summary)):
    with open(D + name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
out = [f"{'node':>6s} {'rows':>5s} {'R6':>3s} | {'supp':>5s} {'contr':>5s} {'unver':>5s} {'dup':>4s} {'manual':>6s}"]
for s in summary:
    out.append(f"{s['node']:>6s} {s['rows']:5d} {s['changed_R6']:3d} | {s['supported']:5d} {s['contradicted']:5d} "
               f"{s['unverifiable']:5d} {s['duplicate']:4d} {s['manual_blank']:6d}")
tot = lambda k: sum(s[k] for s in summary)
out.append(f"{'total':>6s} {tot('rows'):5d} {tot('changed_R6'):3d} | {tot('supported'):5d} {tot('contradicted'):5d} "
           f"{tot('unverifiable'):5d} {tot('duplicate'):4d} {tot('manual_blank'):6d}")
out.append("R6 rows whose fake id has a contradicted neighbor_exists row in the same batch: "
           f"{sum(ch['fake_id_has_contradicted_neighbor_exists_row_in_batch'] for ch in changes)}/{len(changes)}; "
           f"fake ids: {sorted({ch['cited_node_id'] for ch in changes})}")
print("\n".join(out)); open(D + "v4_results.txt", "w").write("\n".join(out) + "\n")
