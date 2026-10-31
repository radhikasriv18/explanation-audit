"""
Follow-up on the non-empty counterfactual texts (151 Cora / 55 Products) from
cf_nonempty_recompute.py (same cleaning rules, re-applied here).

1. FK components (textstat 0.7.13 counters) for the counterfactual method.
2. Kruskal-Wallis + pairwise Mann-Whitney (Bonferroni x3) on Halstead volume
   per word; GraphXAIN / GraphNarrator rows read unchanged from
   lexical_complexity_results.csv.
3. Entity graph: entity_graph_v5_output/entity_graph_v5_CF-GNNExplainer_*.csv
   scored the RAW response text (infos dict included, no cleaning, all 184/60
   keys). First reproduce those rows with compute_entity_graph_v5's own
   entity_graph_measures_v5() (imported unmodified), then rerun it on the
   cleaned non-empty texts.
Read-only; writes new files only. No model calls.
"""
import csv, importlib.util, itertools, json, os, statistics as st, sys
import textstat
from scipy.stats import kruskal, mannwhitneyu

R = "./"
OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, R + "graphnarrCora/GraphNarrator")
_s = importlib.util.spec_from_file_location("v5", R + "grounding_recall_f1_2026-09-07/compute_entity_graph_v5.py")
v5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(v5)
_s = importlib.util.spec_from_file_location("ne", os.path.join(OUT, "cf_nonempty_recompute.py"))
EXCL = {"cora": {"3", "67", "71", "192", "260", "262", "532"}, "products": set()}


def clean(r):  # identical to cf_nonempty_recompute.clean
    i = r.find("{")
    if i < 0:
        return r.strip()
    d = 0
    for j in range(i, len(r)):
        if r[j] == "{":
            d += 1
        elif r[j] == "}":
            d -= 1
            if d == 0:
                return r[j + 1:].strip()
    return r


titles = json.load(open(R + "production_run_2026-07-27/consolidated/neighbor_titles_full.json"))
lines = []
P = lambda s="": (print(s), lines.append(s))
per_text = []

recs = {}
for ds in ["cora", "products"]:
    resp = json.load(open(R + f"llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{ds}_standard_Response.json"))
    td = json.load(open(R + f"llm-graph-cf/data/{ds}/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json"))
    recs[ds] = [(k, str(td[k]["Target_Node_ID"]), v[1]) for k, v in resp.items()]

P("== 1. FK components, counterfactual, non-empty cleaned texts")
for ds in ["cora", "products"]:
    rows = []
    for k, node, raw in recs[ds]:
        if k in EXCL[ds]:
            continue
        t = clean(raw)
        if not t:
            continue
        s, w, y = textstat.sentence_count(t), textstat.lexicon_count(t), textstat.syllable_count(t)
        rows.append((s, w, y))
    P(f"{ds}: n={len(rows)} W/S={st.mean(w / s for s, w, y in rows):.2f} Syl/W={st.mean(y / w for s, w, y in rows):.3f} "
      f"S/expl={st.mean(s for s, w, y in rows):.2f} W/expl={st.mean(w for s, w, y in rows):.1f}")

P("\n== 2. Kruskal-Wallis on Halstead volume per word")
lex = list(csv.DictReader(open(R + "lexical_complexity_results.csv")))
ne = [r for r in csv.DictReader(open(os.path.join(OUT, "cf_nonempty_per_text.csv"))) if r["empty"] == "False"]
for ds in ["cora", "products"]:
    g = {"GraphXAIN": [float(r["volume_per_word"]) for r in lex if r["method"] == "graphxain" and r["dataset"] == ds],
         "GraphNarrator": [float(r["volume_per_word"]) for r in lex if r["method"] == "graphnarrator" and r["dataset"] == ds],
         "Counterfactual": [float(r["volume_per_word"]) for r in ne if r["dataset"] == ds]}
    P(f"{ds}: " + ", ".join(f"{m} {st.mean(v):.2f} (n={len(v)})" for m, v in g.items()))
    kw = kruskal(*g.values())
    P(f"   Kruskal-Wallis H={kw.statistic:.2f} p={kw.pvalue:.3g}")
    for a, b in itertools.combinations(g, 2):
        u = mannwhitneyu(g[a], g[b], alternative="two-sided")
        P(f"   {a} vs {b}: U={u.statistic:.1f} p={u.pvalue:.3g} Bonferroni(x3) p={min(1, 3 * u.pvalue):.3g}")

P("\n== 3. Entity graph (v5 measures), counterfactual")
for ds in ["cora", "products"]:
    old = {r["node"]: r for r in csv.DictReader(open(R + f"grounding_recall_f1_2026-09-07/entity_graph_v5_output/entity_graph_v5_CF-GNNExplainer_{ds}.csv"))}
    nb = lambda node: titles.get(node, {}).get("neighbors") if ds == "products" else None
    match = 0
    variants = {"raw_all": [], "raw_7excluded": [], "raw_nonempty_keys": [], "cleaned_nonempty": []}
    for k, node, raw in recs[ds]:
        m, _ = v5.entity_graph_measures_v5(raw, node, nb(node))
        o = old[node]
        match += int(int(o["C_state"]) == m["C_state"] and int(o["C_cycle"]) == m["C_cycle"])
        variants["raw_all"].append(m)
        if k in EXCL[ds]:
            continue
        variants["raw_7excluded"].append(m)
        t = clean(raw)
        if not t:
            continue
        variants["raw_nonempty_keys"].append(m)
        mc, _ = v5.entity_graph_measures_v5(t, node, nb(node))
        variants["cleaned_nonempty"].append(mc)
        per_text.append({"dataset": ds, "key": k, "node": node, "C_state_raw": m["C_state"], "C_cycle_raw": m["C_cycle"],
                         "C_state_cleaned": mc["C_state"], "C_cycle_cleaned": mc["C_cycle"]})
    P(f"{ds}: reproduces existing v5 CSV row-for-row (C_state & C_cycle) {match}/{len(old)}")
    for name, ms in variants.items():
        P(f"   {name:18s} n={len(ms):3d} C_state={st.mean(x['C_state'] for x in ms):.2f} C_cycle={st.mean(x['C_cycle'] for x in ms):.2f}")

with open(os.path.join(OUT, "cf_nonempty_entity_graph_per_text.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(per_text[0])); w.writeheader(); w.writerows(per_text)
open(os.path.join(OUT, "cf_nonempty_followup_results.txt"), "w").write("\n".join(lines) + "\n")
