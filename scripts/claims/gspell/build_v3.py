#!/usr/bin/env python3
"""
v3 sheets from v2 (v2 never modified). Rule R3:
  a row with claim_kind = other, whose v2 suggested_verdict is contradicted ONLY because its cited id
  is not within 2 hops / does not exist, AND which restates the topic of the same block's Summary row
  -> suggested_verdict = duplicate, suggest_reason = "restates summary row <claim_id> (R3)".
Same block = same node, batch_idx and cited_node_id; the Summary row is the closest preceding
neighbor_content row starting "Summary:" in the ORIGINAL v1 sheet (if v2 merged it into an earlier
row, the kept claim_id from collapse_log.csv is used).
Restates the topic = topic phrase (text after "focus on" / "connection to" / "related to" / "focuses on" /
"discusses" ..., else the whole sentence) has >= 50% of its content words (5-letter stems) present in the
Summary text, with at least one match. Rows meeting every other condition but failing the overlap test
are written to v3_near_misses.csv. Every change is logged in v3_changes.csv. No model calls.
"""
import csv, re, sys
csv.field_size_limit(sys.maxsize)
D = "./gspell_grounding_manual_2026-10-10/"
NODES = [("cora", "510"), ("cora", "2334"), ("cora", "1062"), ("cora", "884"),
         ("products", "6813"), ("products", "1852"), ("products", "8766"), ("products", "8438")]
TOPIC = re.compile(r"\b(?:focus(?:es|ed)? on|connection to|related to|relates to|relevance to|relevant to|"
                   r"associated with|discuss(?:es)?|about)\b\s*(.*)", re.I)
STOP = set("""a an and are as at be but by category categories classification classify classified connection
different does doesn't focus for from has have in indicate indicates into is it its keywords keyword more not of
on or product products article articles paper target that the their these this those to which with suggest
suggests strong which supports support supporting supported class align aligns aligned is also than other""".split())
stems = lambda s: {w[:5] for w in re.findall(r"[a-z][a-z\-']+", s.lower()) if w not in STOP and len(w) > 2}
contr_reason = re.compile(r"^cited id \d+ (is not within 2 hops|does not exist)")

merged_into = {}
for r in csv.DictReader(open(D + "collapse_log.csv")):
    merged_into[(r["node"], r["merged_claim_id"])] = r["kept_claim_id"]

changes, near, summary = [], [], []
for ds, node in NODES:
    v1 = list(csv.DictReader(open(D + f"claims_{ds}_{node}.csv")))
    v2 = list(csv.DictReader(open(D + f"claims_{ds}_{node}_v2.csv")))
    pos = {r["claim_id"]: i for i, r in enumerate(v1)}
    n_changed = 0
    for r in v2:
        if not (r["claim_kind"] == "other" and r["suggested_verdict"] == "contradicted" and contr_reason.match(r["suggest_reason"])):
            continue
        i = pos[r["claim_id"]]
        summ = next((v1[j] for j in range(i - 1, -1, -1)
                     if v1[j]["batch_idx"] == r["batch_idx"] and v1[j]["cited_node_id"] == r["cited_node_id"]
                     and v1[j]["claim_kind"] == "neighbor_content" and re.match(r"[\W_]*Summary\s*:", v1[j]["claim_text"], re.I)), None)
        if summ is None:
            near.append({"node": node, "claim_id": r["claim_id"], "claim_text": r["claim_text"][:300], "summary_claim_id": "",
                         "topic_words": "", "matched": "", "overlap": "", "why_not": "no Summary row in the same block"})
            continue
        sid = merged_into.get((node, summ["claim_id"]), summ["claim_id"])
        m = TOPIC.search(r["claim_text"])
        topic = m.group(1) if m else r["claim_text"]
        topic = re.split(r",\s*which\b|\bwhich\b", topic)[0]
        tw, sw = stems(topic), stems(summ["claim_text"])
        hit = tw & sw
        ov = len(hit) / len(tw) if tw else 0.0
        if hit and ov >= 0.5:
            old_v, old_r = r["suggested_verdict"], r["suggest_reason"]
            r["suggested_verdict"], r["suggest_reason"] = "duplicate", f"restates summary row {sid} (R3)"
            n_changed += 1
            changes.append({"node": node, "dataset": ds, "claim_id": r["claim_id"], "batch_idx": r["batch_idx"],
                            "cited_node_id": r["cited_node_id"], "old_suggested_verdict": old_v, "old_suggest_reason": old_r,
                            "new_suggested_verdict": "duplicate", "new_suggest_reason": r["suggest_reason"],
                            "summary_claim_id": sid, "topic_stems": " ".join(sorted(tw)), "matched_stems": " ".join(sorted(hit)),
                            "overlap": round(ov, 2), "claim_text": r["claim_text"][:300], "summary_text": summ["claim_text"][:300]})
        else:
            near.append({"node": node, "claim_id": r["claim_id"], "claim_text": r["claim_text"][:300], "summary_claim_id": sid,
                         "topic_words": " ".join(sorted(tw)), "matched": " ".join(sorted(hit)), "overlap": round(ov, 2),
                         "why_not": "topic overlap < 50%" if hit else "no topic word in Summary"})
    with open(D + f"claims_{ds}_{node}_v3.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(v2[0])); w.writeheader(); w.writerows(v2)
    cnt = lambda v: sum(x["suggested_verdict"] == v for x in v2)
    eligible = sum(x["claim_kind"] == "other" and contr_reason.match(x["suggest_reason"] or "") is not None for x in v2) + 0
    summary.append({"dataset": ds, "node": node, "rows": len(v2), "changed_to_duplicate": n_changed,
                    "eligible_other_contradicted_rows": n_changed + sum(n["node"] == node for n in near),
                    "near_misses": sum(n["node"] == node for n in near),
                    "supported": cnt("supported"), "contradicted": cnt("contradicted"), "unverifiable": cnt("unverifiable"),
                    "duplicate": cnt("duplicate"), "manual_blank": cnt("")})

allv3 = []
for ds, node in NODES:
    allv3 += list(csv.DictReader(open(D + f"claims_{ds}_{node}_v3.csv")))
with open(D + "claims_all_nodes_v3.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(allv3[0])); w.writeheader(); w.writerows(allv3)
for name, rows, fields in (("v3_changes.csv", changes, None), ("v3_near_misses.csv", near, None), ("v3_summary.csv", summary, None)):
    with open(D + name, "w", newline="") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        else:
            f.write("(none)\n")
out = [f"{'node':>6s} {'eligible':>8s} {'->dup':>6s} {'near-miss':>9s} | {'supp':>5s} {'contr':>5s} {'unver':>5s} {'dup':>4s} {'manual':>6s}"]
for s in summary:
    out.append(f"{s['node']:>6s} {s['eligible_other_contradicted_rows']:8d} {s['changed_to_duplicate']:6d} {s['near_misses']:9d} | "
               f"{s['supported']:5d} {s['contradicted']:5d} {s['unverifiable']:5d} {s['duplicate']:4d} {s['manual_blank']:6d}")
out.append(f"{'total':>6s} {sum(s['eligible_other_contradicted_rows'] for s in summary):8d} {sum(s['changed_to_duplicate'] for s in summary):6d} "
           f"{sum(s['near_misses'] for s in summary):9d} | {sum(s['supported'] for s in summary):5d} {sum(s['contradicted'] for s in summary):5d} "
           f"{sum(s['unverifiable'] for s in summary):5d} {sum(s['duplicate'] for s in summary):4d} {sum(s['manual_blank'] for s in summary):6d}")
print("\n".join(out)); open(D + "v3_results.txt", "w").write("\n".join(out) + "\n")
