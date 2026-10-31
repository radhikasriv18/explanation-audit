"""
Counterfactual (CF-GNNExplainer edge-removal) rows of three tables, recomputed
with EMPTY cleaned texts DROPPED. Cleaning rules = those that reproduce the
pooled-FK table's 13.77 / 13.53 (first "{" -> matched "}" -> text after,
stripped; no "{" -> full text stripped; unclosed -> full text; Cora keys
3, 67, 71, 192, 260, 262, 532 excluded).

Correctness: Factual_Target_Node_Class (the frozen canonical GraphSAGE's own
prediction recorded by the CF run) == label_names[y[node]] from
{cora,products}_canonical.pt; cross-checked against lexical_complexity_results.csv.
GraphXAIN / GraphNarrator per-text FK for Kruskal-Wallis are read unchanged from
fk_components_pooled_sources_per_text.csv (the sources that reproduce the table).
Halstead = compute_text_metrics.halstead(), unmodified (same function the old
lexical numbers used; verified below by reproducing 5.51 / 6.05 incl. empties).
Read-only; writes new files only. No model calls.
"""
import csv, importlib.util, itertools, json, os, statistics as st
import textstat, torch
from scipy.stats import kruskal, mannwhitneyu

R = "./"
OUT = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("ctm", R + "compute_text_metrics.py")
ctm = importlib.util.module_from_spec(_s); _s.loader.exec_module(ctm)

EXCL = {"cora": {"3", "67", "71", "192", "260", "262", "532"}, "products": set()}


def clean(r):
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


old_lex = {(r["dataset"], r["global_node_id"]): r for r in csv.DictReader(open(R + "lexical_complexity_results.csv"))
           if r["method"] == "cf_gnnexplainer"}

rows = []
for ds in ["cora", "products"]:
    resp = json.load(open(R + f"llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{ds}_standard_Response.json"))
    tdict = json.load(open(R + f"llm-graph-cf/data/{ds}/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json"))
    data = torch.load(R + f"{ds}_canonical.pt", map_location="cpu", weights_only=False)
    for k, v in resp.items():
        if k in EXCL[ds]:
            continue
        t = clean(v[1])
        node = str(tdict[k]["Target_Node_ID"])
        pred = tdict[k]["Factual_Target_Node_Class"]
        true = data.label_names[int(data.y[int(node)])]
        h = ctm.halstead(t)
        rows.append({"dataset": ds, "key": k, "node": node, "pred": pred, "true": true, "correct": pred == true,
                     "empty": t == "", "fk_grade": textstat.flesch_kincaid_grade(t),
                     "volume_per_word": h["volume_per_word"], "length_N": h["length_N"]})

lines = []
P = lambda s="": (print(s), lines.append(s))

P("== Checks against old numbers (ALL rows, empties kept)")
for ds in ["cora", "products"]:
    s = [r for r in rows if r["dataset"] == ds]
    agree = sum(str(r["correct"]) == old_lex[(ds, r["node"])]["correct"] for r in s)
    vpw_match = sum(abs(r["volume_per_word"] - float(old_lex[(ds, r["node"])]["volume_per_word"])) < 1e-9 for r in s)
    P(f"{ds}: n={len(s)} empty={sum(r['empty'] for r in s)} meanFK={st.mean(r['fk_grade'] for r in s):.4f} "
      f"meanVPW={st.mean(r['volume_per_word'] for r in s):.4f} | correctness agrees with old CSV {agree}/{len(s)}, "
      f"per-row VPW identical {vpw_match}/{len(s)}")

NE = [r for r in rows if not r["empty"]]
P("\n== 1. FK by correctness (non-empty), two-sided Mann-Whitney U")
for ds in ["cora", "products"]:
    c = [r["fk_grade"] for r in NE if r["dataset"] == ds and r["correct"]]
    i = [r["fk_grade"] for r in NE if r["dataset"] == ds and not r["correct"]]
    u = mannwhitneyu(c, i, alternative="two-sided")
    P(f"{ds}: correct {st.mean(c):.2f} (n={len(c)}) / incorrect {st.mean(i):.2f} (n={len(i)})  U={u.statistic:.1f} p={u.pvalue:.3f}")

P("\n== 2. Pooled FK + Kruskal-Wallis across methods (GraphXAIN/GraphNarrator unchanged)")
other = list(csv.DictReader(open(os.path.join(OUT, "fk_components_pooled_sources_per_text.csv"))))
for ds in ["cora", "products"]:
    g = {m: [float(r["fk_grade"]) for r in other if r["method"] == m and r["dataset"] == ds] for m in ["GraphXAIN", "GraphNarrator"]}
    g["Counterfactual"] = [r["fk_grade"] for r in NE if r["dataset"] == ds]
    P(f"{ds}: " + ", ".join(f"{m} {st.mean(v):.2f} (n={len(v)})" for m, v in g.items()))
    kw = kruskal(*g.values())
    P(f"   Kruskal-Wallis H={kw.statistic:.2f} p={kw.pvalue:.3g}")
    for a, b in itertools.combinations(g, 2):
        u = mannwhitneyu(g[a], g[b], alternative="two-sided")
        P(f"   {a} vs {b}: U={u.statistic:.1f} p={u.pvalue:.3g} Bonferroni(x3) p={min(1, 3 * u.pvalue):.3g}")

P("\n== 3. Halstead volume per word (non-empty)")
for ds in ["cora", "products"]:
    v = [r["volume_per_word"] for r in NE if r["dataset"] == ds]
    P(f"{ds}: {st.mean(v):.2f} (n={len(v)})")

with open(os.path.join(OUT, "cf_nonempty_per_text.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
open(os.path.join(OUT, "cf_nonempty_results.txt"), "w").write("\n".join(lines) + "\n")
