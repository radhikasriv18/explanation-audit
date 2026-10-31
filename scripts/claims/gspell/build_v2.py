#!/usr/bin/env python3
"""
v2 labeling sheets (reads claims_*.csv, G_*.csv, joined_text_*.txt; never modifies them).

1. Collapse repeats ("repeated statements of the same claim are counted once"): within a node,
   rows with identical claim_text after whitespace/case normalization AND identical cited_node_id
   are merged into the first row; n_repeats = number of rows merged into it (incl. itself).
   Every merge is logged in collapse_log.csv.
2. suggested_verdict / suggest_reason (verdict stays blank). Precedence:
   a. support_verdict                -> unverifiable (YES/NO judgment, not a checkable fact)
   b. any row citing an ID not within 2 hops of the target (incl. non-existent IDs)
                                     -> contradicted
   c. neighbor_exists: cited ID is the target itself -> contradicted;
      2-hop ID that the text calls a direct / 1-hop neighbour -> contradicted;
      in this batch's prompt list and within 2 hops -> supported;
      within 2 hops but not in this batch -> blank (manual)
   d. class: class labels named in the sentence; exactly one label named:
        == canonical_pred -> supported; == true_label with true-class wording -> supported;
        otherwise -> contradicted.  None or several labels named -> blank (manual)
   e. neighbor_content, feature, other -> blank (manual)
3. Recall: G ids cited by id anywhere in the joined text; recall = cited / |G|.
No model calls; plain Python.
"""
import csv, glob, re, sys
csv.field_size_limit(sys.maxsize)
D = "./gspell_grounding_manual_2026-10-10/"
CITE = re.compile(r"(?:Article|Paper|Product|Node)\s*#?\s*(\d+)|\bID\s*[:#]?\s*(\d+)|<<\s*(\d+)\s*>>", re.I)  # = build_labeling_sheets.CITE
DIRECT = re.compile(r"\bdirect(ly)?\b|\b1-hop\b|\bone-hop\b|\bfirst[- ]order\b|\bimmediate\b", re.I)
TRUE_WORDS = re.compile(r"\b(true|actual|correct(ly)?|really|in fact|ground[- ]truth)\b", re.I)
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(*\[])|\n+")
norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
lnorm = lambda s: re.sub(r"[\s_]+", " ", s).strip().lower()
ids_in = lambda s: [int(next(g for g in m.groups() if g)) for m in CITE.finditer(s)]
lines_out = []
P = lambda s="": (print(s), lines_out.append(s))

LABELS = {}
for ds in ("cora", "products"):
    import json
    # label vocabulary = every true/pred label seen in the G files and sheets of that dataset + agreement json
    agree = json.load(open(f"./production_run_2026-07-27/prediction_agreement/{ds}_canonical_vs_gspell_full.json"))["per_node"]
    LABELS[ds] = sorted({v["true_label"] for v in agree.values()} | {v["canonical_pred"] for v in agree.values()}, key=len, reverse=True)

log, summary, recall_rows = [], [], []
for path in sorted(glob.glob(D + "claims_*_*.csv")):
    if path.endswith("_v2.csv") or "claims_all_nodes" in path:
        continue
    ds, node = re.match(r".*claims_(\w+?)_(\d+)\.csv$", path).groups()
    rows = list(csv.DictReader(open(path)))
    joined = open(D + f"joined_text_{ds}_{node}.txt").read()
    G = list(csv.DictReader(open(D + f"G_{ds}_{node}.csv")))
    labels = LABELS[ds]
    target = int(node)

    # ---- 1. collapse
    kept, first = [], {}
    for r in rows:
        key = (norm(r["claim_text"]), r["cited_node_id"])
        if key in first:
            k = first[key]; k["n_repeats"] += 1
            log.append({"node": node, "dataset": ds, "kept_claim_id": k["claim_id"], "merged_claim_id": r["claim_id"],
                        "claim_kind": r["claim_kind"], "cited_node_id": r["cited_node_id"],
                        "normalized_claim_text": key[0][:300]})
        else:
            r = dict(r); r["n_repeats"] = 1; first[key] = r; kept.append(r)

    # sentences of the joined text that call a cited id a direct / 1-hop neighbour
    direct_claimed = set()
    for s in SENT.split(joined):
        if DIRECT.search(s):
            direct_claimed |= set(ids_in(s))

    # ---- 2. suggested verdicts
    for r in kept:
        kind, cid = r["claim_kind"], r["cited_node_id"]
        c = int(cid) if cid != "" else None
        within2 = c is not None and (r["is_1hop"] == "True" or r["is_2hop"] == "True")
        v, why = "", ""
        if kind == "support_verdict":
            v, why = "unverifiable", "YES/NO judgment, not a checkable fact"
        elif c is not None and c != target and not within2:
            v, why = "contradicted", (f"cited id {c} does not exist" if r["true_title"] == "(no such node)"
                                      else f"cited id {c} is not within 2 hops of target {target}")
        elif kind == "neighbor_exists":
            if c == target:
                v, why = "contradicted", "target cited as its own neighbour"
            elif r["is_2hop"] == "True" and c in direct_claimed:
                v, why = "contradicted", f"{c} is a 2-hop neighbour but the text calls it direct/1-hop"
            elif r["in_batch"] == "True":
                v, why = "supported", f"{c} is in this batch's prompt list and is a {'1' if r['is_1hop'] == 'True' else '2'}-hop neighbour"
            else:
                why = f"{c} is within 2 hops but not in this batch's prompt list (manual)"
        elif kind == "class":
            t, found = lnorm(r["claim_text"]), []
            for lab in labels:
                if lnorm(lab) in t and not any(lnorm(lab) in lnorm(f) for f in found):
                    found.append(lab)
            if len(found) == 1:
                lab = found[0]
                if lab == r["canonical_pred"]:
                    v, why = "supported", f"states '{lab}' = canonical prediction"
                elif lab == r["true_label"] and TRUE_WORDS.search(r["claim_text"]):
                    v, why = "supported", f"states '{lab}' as the true class = true label"
                else:
                    v, why = "contradicted", (f"states '{lab}'; canonical prediction is '{r['canonical_pred']}'"
                                              f" (true label '{r['true_label']}')")
            else:
                why = "no class label named (manual)" if not found else f"several labels named: {found} (manual)"
        r["suggested_verdict"], r["suggest_reason"] = v, why

    fields = list(rows[0].keys()) + ["n_repeats", "suggested_verdict", "suggest_reason"]
    with open(D + f"claims_{ds}_{node}_v2.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(kept)

    # ---- 3. recall
    cited_all = ids_in(joined)
    rec = []
    for g in G:
        gid = int(g["neighbor_id"])
        n = cited_all.count(gid)
        rec.append({**g, "cited_in_text": n > 0, "n_mentions": n})
    with open(D + f"recall_{ds}_{node}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rec[0])); w.writeheader(); w.writerows(rec)
    nc = sum(r["cited_in_text"] for r in rec)
    recall_rows.append({"dataset": ds, "node": node, "G_size": len(G), "G_cited": nc, "recall": nc / len(G),
                        "G_not_cited": " ".join(r["neighbor_id"] for r in rec if not r["cited_in_text"])})

    cnt = lambda val: sum(r["suggested_verdict"] == val for r in kept)
    summary.append({"dataset": ds, "node": node, "rows_before": len(rows), "rows_after": len(kept),
                    "merged": len(rows) - len(kept), "supported": cnt("supported"), "contradicted": cnt("contradicted"),
                    "unverifiable": cnt("unverifiable"), "manual_blank": cnt(""),
                    "manual_neighbor_content_feature_other": sum(r["suggested_verdict"] == "" and r["claim_kind"] in
                                                                 ("neighbor_content", "feature", "other") for r in kept),
                    "manual_exists_or_class": sum(r["suggested_verdict"] == "" and r["claim_kind"] in
                                                  ("neighbor_exists", "class") for r in kept),
                    "support_verdict_rows_citing_non_neighbor": sum(r["claim_kind"] == "support_verdict" and r["cited_node_id"] != ""
                                                                    and r["is_1hop"] != "True" and r["is_2hop"] != "True"
                                                                    and int(r["cited_node_id"]) != target for r in kept)})

order = ["510", "2334", "1062", "884", "6813", "1852", "8766", "8438"]
summary.sort(key=lambda s: order.index(s["node"])); recall_rows.sort(key=lambda s: order.index(s["node"]))
allv2 = []
for s in summary:
    allv2 += list(csv.DictReader(open(D + f"claims_{s['dataset']}_{s['node']}_v2.csv")))
with open(D + "claims_all_nodes_v2.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(allv2[0])); w.writeheader(); w.writerows(allv2)
for name, rows in (("collapse_log.csv", log), ("v2_summary.csv", summary), ("recall_summary.csv", recall_rows)):
    with open(D + name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

P(f"{'node':>6s} {'before':>6s} {'after':>6s} {'merged':>6s} {'supp':>5s} {'contr':>5s} {'unver':>5s} {'manual':>6s} "
  f"{'(content/feat/other':>19s} {'exists/class)':>13s}")
for s in summary:
    P(f"{s['node']:>6s} {s['rows_before']:6d} {s['rows_after']:6d} {s['merged']:6d} {s['supported']:5d} {s['contradicted']:5d} "
      f"{s['unverifiable']:5d} {s['manual_blank']:6d} {s['manual_neighbor_content_feature_other']:19d} {s['manual_exists_or_class']:13d}")
P(f"{'total':>6s} {sum(s['rows_before'] for s in summary):6d} {sum(s['rows_after'] for s in summary):6d} "
  f"{sum(s['merged'] for s in summary):6d} {sum(s['supported'] for s in summary):5d} {sum(s['contradicted'] for s in summary):5d} "
  f"{sum(s['unverifiable'] for s in summary):5d} {sum(s['manual_blank'] for s in summary):6d}")
P("support_verdict rows citing a non-neighbour (kept unverifiable): " +
  ", ".join(f"{s['node']}:{s['support_verdict_rows_citing_non_neighbor']}" for s in summary))
P("\nRecall (G ids cited by id anywhere in the joined text / |G|):")
for r in recall_rows:
    P(f"   {r['dataset']:9s}{r['node']:>6s}  {r['G_cited']}/{r['G_size']} = {r['recall']:.3f}   not cited: {r['G_not_cited'] or '-'}")
open(D + "v2_results.txt", "w").write("\n".join(lines_out) + "\n")
