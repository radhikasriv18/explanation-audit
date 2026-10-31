#!/usr/bin/env python3
"""
Stage C (/usr/bin/python3: textstat 0.7.13, scipy 1.13.1). All four methods, both datasets,
same sources as the existing tables plus the final GSPELL sources:
  GraphXAIN, GraphNarrator: FK from readability_checks_2026-10-05/fk_components_pooled_sources_per_text.csv,
                            volume/word from lexical_complexity_results.csv (joined by node id)
  Counterfactual:           non-empty rows of readability_checks_2026-10-05/cf_nonempty_per_text.csv (FK + VPW)
  GSPELL:                   final/gspell_per_node_metrics.csv (Cora job 51247846, Products job 50765167)
Reports texts with FK > 30, mean FK and mean volume per word with and without them, and the
four-method Kruskal-Wallis (pairwise two-sided Mann-Whitney, Bonferroni x6) on all texts and,
as a sensitivity, without FK > 30 texts. Read-only; new files only. No model calls.
"""
import csv, itertools, json, statistics as st
from scipy.stats import kruskal, mannwhitneyu

R = "./"
RC = R + "readability_checks_2026-10-05/"
OUT = R + "gspell_metrics_2026-10-09/final/"
lines, table, kw_rows = [], [], []
P = lambda s="": (print(s), lines.append(s))

fkp = list(csv.DictReader(open(RC + "fk_components_pooled_sources_per_text.csv")))
lex = list(csv.DictReader(open(R + "lexical_complexity_results.csv")))
cf = [r for r in csv.DictReader(open(RC + "cf_nonempty_per_text.csv")) if r["empty"] == "False"]
gs = list(csv.DictReader(open(OUT + "gspell_per_node_metrics.csv")))

data = {}  # (method, ds) -> list of (node, fk, vpw or None)
for ds in ("cora", "products"):
    for m, lm in (("GraphXAIN", "graphxain"), ("GraphNarrator", "graphnarrator")):
        fk = {r["node"]: float(r["fk_grade"]) for r in fkp if r["method"] == m and r["dataset"] == ds}
        if m == "GraphNarrator":  # FK rows keyed "pos<file index>" -> global id via the consolidation mapping
            mp = json.load(open(R + f"production_run_2026-07-27/graphnarrator_{ds}/index_to_global_node_id_mapping.json"))["mapping"]
            fk = {str(mp[k[3:]]["root_global_id"]): v for k, v in fk.items()}
        vpw = {r["global_node_id"]: float(r["volume_per_word"]) for r in lex if r["method"] == lm and r["dataset"] == ds}
        P(f"join check {m}/{ds}: FK texts {len(fk)}, VPW texts {len(vpw)}, matched node ids {len(set(fk) & set(vpw))}, "
          f"FK-only {sorted(set(fk) - set(vpw))[:5]}, VPW-only {sorted(set(vpw) - set(fk))[:5]}")
        data[(m, ds)] = [(n, fk.get(n), vpw.get(n)) for n in sorted(set(fk) | set(vpw), key=int)]
    data[("Counterfactual", ds)] = [(r["node"], float(r["fk_grade"]), float(r["volume_per_word"])) for r in cf if r["dataset"] == ds]
    data[("GSPELL", ds)] = [(r["node"], float(r["fk_grade"]), float(r["volume_per_word"])) for r in gs
                            if r["dataset"] == ds and r["empty"] == "False"]

METHODS = ["GraphXAIN", "GraphNarrator", "Counterfactual", "GSPELL"]
P("\n== FK > 30 texts and means with / without them")
P(f"{'dataset':9s}{'method':15s}{'n_FK':>6s}{'FK>30':>7s}{'FK all':>9s}{'FK ≤30':>9s}{'n_VPW':>7s}{'VPW all':>9s}{'VPW ≤30':>9s}  nodes with FK>30")
for ds in ("cora", "products"):
    for m in METHODS:
        rows = data[(m, ds)]
        fk_all = [f for _, f, _ in rows if f is not None]
        hi = {n for n, f, _ in rows if f is not None and f > 30}
        fk_keep = [f for n, f, _ in rows if f is not None and n not in hi]
        v_all = [v for _, _, v in rows if v is not None]
        v_keep = [v for n, _, v in rows if v is not None and n not in hi]
        rec = {"dataset": ds, "method": m, "n_fk": len(fk_all), "n_fk_gt30": len(hi),
               "mean_fk_all": st.mean(fk_all), "mean_fk_without_gt30": st.mean(fk_keep),
               "median_fk_all": st.median(fk_all), "n_vpw": len(v_all),
               "mean_vpw_all": st.mean(v_all), "mean_vpw_without_gt30": st.mean(v_keep),
               "nodes_fk_gt30": " ".join(sorted(hi, key=int))}
        table.append(rec)
        P(f"{ds:9s}{m:15s}{len(fk_all):6d}{len(hi):7d}{rec['mean_fk_all']:9.2f}{rec['mean_fk_without_gt30']:9.2f}"
          f"{len(v_all):7d}{rec['mean_vpw_all']:9.2f}{rec['mean_vpw_without_gt30']:9.2f}  {rec['nodes_fk_gt30'][:80]}")

for label, drop in (("all texts", False), ("sensitivity: FK > 30 texts removed", True)):
    for metric, idx in (("FK grade", 1), ("Halstead volume per word", 2)):
        P(f"\n== Kruskal-Wallis on {metric}, 4 methods, {label} (pairwise MWU, Bonferroni x6)")
        for ds in ("cora", "products"):
            g = {}
            for m in METHODS:
                rows = data[(m, ds)]
                hi = {n for n, f, _ in rows if f is not None and f > 30} if drop else set()
                g[m] = [r[idx] for r in rows if r[idx] is not None and r[0] not in hi]
            kw = kruskal(*g.values())
            P(f"{ds}: " + ", ".join(f"{m} {st.mean(v):.2f} (n={len(v)})" for m, v in g.items()))
            P(f"   Kruskal-Wallis H={kw.statistic:.2f} p={kw.pvalue:.3g}")
            kw_rows.append({"set": label, "metric": metric, "dataset": ds, "comparison": "Kruskal-Wallis", "statistic": kw.statistic,
                            "p": kw.pvalue, "p_bonferroni": "", **{f"n_{m}": len(v) for m, v in g.items()}})
            for a, b in itertools.combinations(METHODS, 2):
                u = mannwhitneyu(g[a], g[b], alternative="two-sided")
                P(f"   {a} vs {b}: U={u.statistic:.1f} p={u.pvalue:.3g} Bonferroni(x6) p={min(1, 6 * u.pvalue):.3g}")
                kw_rows.append({"set": label, "metric": metric, "dataset": ds, "comparison": f"{a} vs {b}",
                                "statistic": u.statistic, "p": u.pvalue, "p_bonferroni": min(1, 6 * u.pvalue)})

for name, rows in (("fk_gt30_all_methods.csv", table), ("kruskal_wallis_4methods_final.csv", kw_rows)):
    with open(OUT + name, "w", newline="") as f:
        keys = list(dict.fromkeys(k for r in rows for k in r))
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
open(OUT + "stage_c_results.txt", "w").write("\n".join(lines) + "\n")
