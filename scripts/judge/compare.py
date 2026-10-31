#!/usr/bin/env python3
"""Step 4: compare judge verdicts with hand verdicts (no model calls).

  python3 compare.py --run-dir runs/llama_all [--hand <csv>]

Hand verdicts: --hand (default gspell_grounding_manual_2026-10-10/gspell_grounding_verdicts.csv). Matched on claim_id;
the verdict column is the first of hand_verdict / verdict / manual_verdict / final_verdict that exists. Rows whose hand
verdict is blank are left out; rows where the judge failed to parse (PARSE_FAIL) are counted and left out.

Outputs in --run-dir/compare/: summary.txt, confusion_all.csv, confusion_supp_contr.csv, by_claim_kind.csv, per_node_prf.csv,
disagreements.csv; for a hybrid run (judgments.csv has decided_by) also confusion_model_rows.csv and the decided_by column.

Per-node grounding:
  precision = supported / (supported + contradicted), over all of the node's rows (unverifiable, duplicate excluded)
  recall    = |{g in G : some content row citing g is supported}| / |G|; G = G_<ds>_<node>.csv (1-hop neighbours given
              to GSPELL); content row = claim_kind neighbor_content, feature, other or class (not neighbor_exists,
              not support_verdict)
  F1 per node; dataset means = mean of per-node values (Table 13 convention).
"""
import argparse, csv, os, sys
from collections import Counter

csv.field_size_limit(sys.maxsize)
HERE = os.path.dirname(os.path.abspath(__file__))
SHEETS = "./gspell_grounding_manual_2026-10-10/"
V = ["supported", "contradicted", "unverifiable", "duplicate"]
CONTENT = {"neighbor_content", "feature", "other", "class"}


def kappa(pairs, labels):
    n = len(pairs)
    if n == 0:
        return float("nan")
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[l] * cb[l] for l in labels) / n ** 2
    return float("nan") if pe == 1 else (po - pe) / (1 - pe)


def confusion(pairs, labels, path):
    c = Counter(pairs)
    with open(path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["hand \\ judge"] + labels + ["total"])
        for h in labels:
            w.writerow([h] + [c[(h, j)] for j in labels] + [sum(c[(h, j)] for j in labels)])
        w.writerow(["total"] + [sum(c[(h, j)] for h in labels) for j in labels] + [len(pairs)])
    L = ["hand \\ judge".rjust(14) + " " + " ".join(f"{l[:12]:>12s}" for l in labels)]
    for h in labels:
        L.append(f"{h:>14s} " + " ".join(f"{c[(h, j)]:12d}" for j in labels))
    return L


def prf(rows, vkey, G):
    s = sum(r[vkey] == "supported" for r in rows); c = sum(r[vkey] == "contradicted" for r in rows)
    p = s / (s + c) if s + c else float("nan")
    hit = {r["cited_node_id"] for r in rows if r[vkey] == "supported" and r["claim_kind"] in CONTENT and r["cited_node_id"]}
    rc = len(G & hit) / len(G) if G else float("nan")
    f1 = 0.0 if (p != p or p + rc == 0) else 2 * p * rc / (p + rc)
    return p, rc, f1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--hand", default=SHEETS + "gspell_grounding_verdicts.csv")
    a = ap.parse_args()
    rd = a.run_dir if os.path.isabs(a.run_dir) else os.path.join(HERE, a.run_dir)
    out = os.path.join(rd, "compare"); os.makedirs(out, exist_ok=True)
    if not os.path.exists(a.hand):
        sys.exit(f"hand verdicts not found: {a.hand}")
    hand_rows = list(csv.DictReader(open(a.hand)))
    col = next((c for c in ("hand_verdict", "verdict", "manual_verdict", "final_verdict") if c in hand_rows[0]), None)
    if col is None or "claim_id" not in hand_rows[0]:
        sys.exit(f"need claim_id and a verdict column; columns are {list(hand_rows[0])}")
    hand = {r["claim_id"]: (r[col].strip().lower(), r.get("reason", "") or r.get("notes", "") or r.get("hand_reason", ""),
                            r.get("source", ""), r.get("borderline", "")) for r in hand_rows}
    judge = list(csv.DictReader(open(os.path.join(rd, "judgments.csv"))))

    L = [f"judge run: {rd}", f"hand verdicts: {a.hand} (column '{col}')", ""]
    rows, pf, nohand, bad = [], 0, 0, Counter()
    for r in judge:
        h = hand.get(r["claim_id"], ("", ""))[0]
        if not h:
            nohand += 1; continue
        if h not in V:
            bad[h] += 1; continue
        if r["judge_verdict"] == "PARSE_FAIL":
            pf += 1; continue
        rows.append({**r, "hand_verdict": h, "hand_reason": hand[r["claim_id"]][1], "hand_source": hand[r["claim_id"]][2],
                     "hand_borderline": hand[r["claim_id"]][3]})
    L.append(f"rows judged: {len(judge)}; compared: {len(rows)}; no hand verdict: {nohand}; judge PARSE_FAIL (excluded): {pf}"
             + (f"; hand verdict not one of the 4 labels (excluded): {dict(bad)}" if bad else ""))

    for name, sub, labels, fn in (("ALL rows", rows, V, "confusion_all.csv"),
                                  ("rows hand-labelled supported/contradicted", [r for r in rows if r["hand_verdict"] in V[:2]], V,
                                   "confusion_supp_contr.csv")):
        pairs = [(r["hand_verdict"], r["judge_verdict"]) for r in sub]
        ag = sum(x == y for x, y in pairs) / len(pairs) if pairs else float("nan")
        L += ["", f"== {name}: n = {len(pairs)}, agreement = {ag:.1%}, Cohen's kappa = {kappa(pairs, labels):.3f}"]
        L += confusion(pairs, labels, os.path.join(out, fn))
        if name.startswith("rows hand"):
            both = [(h, j) for h, j in pairs if j in V[:2]]
            L.append(f"   of these, judge also said supported/contradicted: {len(both)}; agreement on those = "
                     f"{sum(h == j for h, j in both) / len(both):.1%}, kappa (2 labels) = {kappa(both, V[:2]):.3f}" if both else "")

    if "decided_by" in judge[0]:
        sub = [r for r in rows if r["decided_by"] == "model"]
        pairs = [(r["hand_verdict"], r["judge_verdict"]) for r in sub]
        L += ["", f"== rows the MODEL judged (hybrid): n = {len(pairs)}, agreement = {sum(x == y for x, y in pairs) / len(pairs):.1%}, "
                  f"Cohen's kappa = {kappa(pairs, V):.3f}"]
        L += confusion(pairs, V, os.path.join(out, "confusion_model_rows.csv"))
        sc = [p for p in pairs if p[0] in V[:2]]
        L.append(f"   of these, rows hand-labelled supported/contradicted: n = {len(sc)}, agreement = "
                 f"{sum(x == y for x, y in sc) / len(sc):.1%}, kappa = {kappa(sc, V):.3f}" if sc else "")
        cd = [(r["hand_verdict"], r["judge_verdict"]) for r in rows if r["decided_by"] == "code"]
        L.append(f"   rows CODE decided: n = {len(cd)}, agreement = {sum(x == y for x, y in cd) / len(cd):.1%}, kappa = {kappa(cd, V):.3f}")

    kinds = sorted({r["claim_kind"] for r in rows}, key=lambda k: -sum(r["claim_kind"] == k for r in rows))
    hyb = "decided_by" in judge[0]
    L += ["", "== by claim_kind" + (" (decided by: code rows / model rows)" if hyb else ""),
          f"{'claim_kind':17s} {'n':>5s} {'agree':>6s} {'kappa':>6s}" + (f" {'n_code':>6s} {'n_model':>7s} {'agree_model':>11s}" if hyb else "")
          + "  top disagreements (hand -> judge)"]
    kstats = []
    for k in kinds:
        sub = [r for r in rows if r["claim_kind"] == k]
        pairs = [(r["hand_verdict"], r["judge_verdict"]) for r in sub]
        ag = sum(x == y for x, y in pairs) / len(pairs)
        line = f"{k:17s} {len(pairs):5d} {ag:6.1%} {kappa(pairs, V):6.3f}"
        st = {"claim_kind": k, "n": len(pairs), "agreement": ag, "kappa": kappa(pairs, V)}
        if hyb:
            m = [(r["hand_verdict"], r["judge_verdict"]) for r in sub if r["decided_by"] == "model"]
            am = sum(x == y for x, y in m) / len(m) if m else float("nan")
            line += f" {len(pairs) - len(m):6d} {len(m):7d} {am:11.1%}"
            st.update({"n_code": len(pairs) - len(m), "n_model": len(m), "agreement_model_rows": am})
        top = Counter((x, y) for x, y in pairs if x != y).most_common(3)
        L.append(line + "  " + ", ".join(f"{x}->{y} {n}" for (x, y), n in top))
        kstats.append(st)
    with open(os.path.join(out, "by_claim_kind.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(kstats[0])); w.writeheader(); w.writerows(kstats)

    L += ["", "== per-node grounding (precision = S/(S+C); recall = G nodes with a supported content row / |G|)",
          f"{'dataset':9s}{'node':>6s} {'|G|':>4s} | {'P hand':>7s} {'R hand':>7s} {'F1 hand':>7s} | {'P judge':>7s} {'R judge':>7s} {'F1 judge':>8s}"]
    prow = []
    for (ds, node) in sorted({(r["dataset"], r["node"]) for r in judge}, key=lambda k: (k[0], [r["node"] for r in judge].index(k[1]))):
        G = {g["neighbor_id"] for g in csv.DictReader(open(SHEETS + f"G_{ds}_{node}.csv"))}
        sub = [r for r in rows if r["node"] == node]
        ph, rh, fh = prf(sub, "hand_verdict", G); pj, rj, fj = prf(sub, "judge_verdict", G)
        prow.append({"dataset": ds, "node": node, "G": len(G), "rows_compared": len(sub), "precision_hand": ph, "recall_hand": rh,
                     "f1_hand": fh, "precision_judge": pj, "recall_judge": rj, "f1_judge": fj})
        L.append(f"{ds:9s}{node:>6s} {len(G):4d} | {ph:7.3f} {rh:7.3f} {fh:7.3f} | {pj:7.3f} {rj:7.3f} {fj:8.3f}")
    for ds in ("cora", "products"):
        d = [p for p in prow if p["dataset"] == ds]
        if d:
            m = lambda k: sum(p[k] for p in d if p[k] == p[k]) / max(1, sum(p[k] == p[k] for p in d))
            L.append(f"{ds:9s}{'mean':>6s} {'':4s} | {m('precision_hand'):7.3f} {m('recall_hand'):7.3f} {m('f1_hand'):7.3f} | "
                     f"{m('precision_judge'):7.3f} {m('recall_judge'):7.3f} {m('f1_judge'):8.3f}")
    with open(os.path.join(out, "per_node_prf.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(prow[0])); w.writeheader(); w.writerows(prow)
    dk = ("decided_by",) if "decided_by" in judge[0] else ()
    dis = [{k: r[k] for k in dk + ("dataset", "node", "claim_id", "claim_kind", "cited_node_id", "hand_verdict", "hand_reason",
                               "hand_source", "hand_borderline", "judge_verdict", "judge_reason", "claim_text")} for r in rows if r["hand_verdict"] != r["judge_verdict"]]
    with open(os.path.join(out, "disagreements.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(dk) + ["dataset", "node", "claim_id", "claim_kind", "cited_node_id", "hand_verdict", "hand_reason",
                                          "hand_source", "hand_borderline", "judge_verdict", "judge_reason", "claim_text"]); w.writeheader(); w.writerows(dis)
    L += ["", f"disagreements: {len(dis)} -> compare/disagreements.csv"]
    print("\n".join(L)); open(os.path.join(out, "summary.txt"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
