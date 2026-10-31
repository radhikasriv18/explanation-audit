#!/usr/bin/env python3
"""
Stage B (/usr/bin/python3: textstat 0.7.13, scipy 1.13.1 -- the interpreter of the
existing readability_checks_2026-10-05 tables).

GSPELL rows for the readability / lexical / entity-graph tables, from Stage A's per-node
texts (final embedding-path sources: Cora job 51247846, Products job 50765167, both Summary prompt).
  - empty texts are dropped (as for the counterfactual framework); malformed texts are
    counted and KEPT.
  - repetition loop = v3 token-repeat regex (a word repeated 5+ times in a row) OR a
    content line (>= 6 words, not a "Support:" verdict line) repeated >= 5 times.
    The raw v3 detect_repetition flag (line threshold 5 on any line > 3 chars) is also
    reported; on joined multi-batch GSPELL output it mostly fires on template lines
    such as "Support: NO" / "<<BEGIN KEYWORDS>>".
  - malformed = non-empty and (no "Support:" line or repetition loop).
FK components: textstat sentence_count / lexicon_count / syllable_count, per-text means
(same as cf_nonempty_followup.py). Halstead = compute_text_metrics.halstead (unmodified).
Kruskal-Wallis across 4 methods; GraphXAIN / GraphNarrator / Counterfactual exactly as in
the existing tables:
  FK : GraphXAIN, GraphNarrator from readability_checks_2026-10-05/fk_components_pooled_sources_per_text.csv;
       Counterfactual non-empty rows of cf_nonempty_per_text.csv
  VPW: GraphXAIN, GraphNarrator from lexical_complexity_results.csv;
       Counterfactual non-empty rows of cf_nonempty_per_text.csv
Pairwise two-sided Mann-Whitney, Bonferroni x6. Read-only; new files only. No model calls.
"""
import collections, csv, importlib.util, itertools, json, os, re, statistics as st
import textstat, scipy
from scipy.stats import kruskal, mannwhitneyu

R = "./"
OUT = R + "gspell_metrics_2026-10-09/final/"
RC = R + "readability_checks_2026-10-05/"
_s = importlib.util.spec_from_file_location("ctm", R + "compute_text_metrics.py")
ctm = importlib.util.module_from_spec(_s); _s.loader.exec_module(ctm)
assert textstat.__version__ == (0, 7, 13)
TOK = re.compile(r'\b(\w+)\b(?:\W+\1\b){4,}', re.IGNORECASE)  # = compute_entity_graph_v3.TOKEN_REPEAT_RE
SUPPORT = re.compile(r"Support\s*:", re.I)
lines = []
P = lambda s="": (print(s), lines.append(s))


def loop(t):
    content = [l.strip() for l in t.split("\n")
               if len(l.strip().split()) >= 6 and not re.match(r"\W*Support\s*:", l.strip(), re.I)]
    worst = max(collections.Counter(content).values(), default=0)
    return bool(TOK.search(t)) or worst >= 5


recs = json.load(open(OUT + "gspell_per_node_records.json"))
rows = []
for r in recs:
    t = r["text"]
    out = {k: r[k] for k in ("dataset", "job", "node", "pred", "true", "correct", "n_batches", "empty", "has_support",
                             "repetition_flagged", "n_batches_without_support", "n_cited_ids", "n_cited_outside_batches",
                             "fk_with_role_header")}
    out["repetition_loop"] = (not r["empty"]) and loop(t)
    out["malformed"] = (not r["empty"]) and (not r["has_support"] or out["repetition_loop"])
    if not r["empty"]:
        s, w, y = textstat.sentence_count(t), textstat.lexicon_count(t), textstat.syllable_count(t)
        h = ctm.halstead(t)
        out.update({"sentences": s, "words": w, "syllables": y, "words_per_sentence": w / s, "syllables_per_word": y / w,
                    "fk_grade": textstat.flesch_kincaid_grade(t), "volume_per_word": h["volume_per_word"],
                    "halstead_length_N": h["length_N"], "C_state": r["C_state"], "C_cycle": r["C_cycle"]})
    rows.append(out)

P(f"textstat {'.'.join(map(str, textstat.__version__))}, scipy {scipy.__version__}")
P("\n== 0. Output quality (all nodes)")
for ds in ("cora", "products"):
    s = [r for r in rows if r["dataset"] == ds]
    P(f"{ds} (job {s[0]['job']}): n={len(s)} | empty {sum(r['empty'] for r in s)} | no Support line "
      f"{sum(not r['has_support'] and not r['empty'] for r in s)} | repetition loop {sum(r['repetition_loop'] for r in s)} | "
      f"malformed (either) {sum(r['malformed'] for r in s)} | raw v3 repetition flag {sum(r['repetition_flagged'] for r in s)} | "
      f"batches without Support line {sum(r['n_batches_without_support'] for r in s)}/{sum(r['n_batches'] for r in s)}")

NE = [r for r in rows if not r["empty"]]
P("\n== 1. Readability (FK components), non-empty texts")
for ds in ("cora", "products"):
    s = [r for r in NE if r["dataset"] == ds]
    P(f"{ds}: n={len(s)} FK={st.mean(r['fk_grade'] for r in s):.2f} W/S={st.mean(r['words_per_sentence'] for r in s):.2f} "
      f"Syl/W={st.mean(r['syllables_per_word'] for r in s):.3f} S/expl={st.mean(r['sentences'] for r in s):.2f} "
      f"W/expl={st.mean(r['words'] for r in s):.1f} | sensitivity: FK with 'assistant' role header kept "
      f"{st.mean(r['fk_with_role_header'] for r in s):.2f} | FK excluding malformed "
      f"{st.mean(r['fk_grade'] for r in s if not r['malformed']):.2f} (n={sum(not r['malformed'] for r in s)})")

P("\n== 2. FK by correctness (canonical GraphSAGE pred vs true label), two-sided Mann-Whitney U")
for ds in ("cora", "products"):
    c = [r["fk_grade"] for r in NE if r["dataset"] == ds and r["correct"]]
    i = [r["fk_grade"] for r in NE if r["dataset"] == ds and not r["correct"]]
    u = mannwhitneyu(c, i, alternative="two-sided")
    P(f"{ds}: correct {st.mean(c):.2f} (n={len(c)}) / incorrect {st.mean(i):.2f} (n={len(i)})  U={u.statistic:.1f} p={u.pvalue:.3f}")

P("\n== 3. Halstead volume per word, non-empty")
for ds in ("cora", "products"):
    v = [r["volume_per_word"] for r in NE if r["dataset"] == ds]
    P(f"{ds}: {st.mean(v):.2f} (n={len(v)})")

P("\n== 4. Entity graph (v5), non-empty")
for ds in ("cora", "products"):
    s = [r for r in NE if r["dataset"] == ds]
    P(f"{ds}: n={len(s)} C_state={st.mean(r['C_state'] for r in s):.2f} C_cycle={st.mean(r['C_cycle'] for r in s):.2f} "
      f"(median C_state {st.median(r['C_state'] for r in s)}, C_cycle {st.median(r['C_cycle'] for r in s)})")

fkp = list(csv.DictReader(open(RC + "fk_components_pooled_sources_per_text.csv")))
cf = [r for r in csv.DictReader(open(RC + "cf_nonempty_per_text.csv")) if r["empty"] == "False"]
lex = list(csv.DictReader(open(R + "lexical_complexity_results.csv")))
groups = {}
for ds in ("cora", "products"):
    groups[("fk", ds)] = {
        "GraphXAIN": [float(r["fk_grade"]) for r in fkp if r["method"] == "GraphXAIN" and r["dataset"] == ds],
        "GraphNarrator": [float(r["fk_grade"]) for r in fkp if r["method"] == "GraphNarrator" and r["dataset"] == ds],
        "Counterfactual": [float(r["fk_grade"]) for r in cf if r["dataset"] == ds],
        "GSPELL": [r["fk_grade"] for r in NE if r["dataset"] == ds]}
    groups[("vpw", ds)] = {
        "GraphXAIN": [float(r["volume_per_word"]) for r in lex if r["method"] == "graphxain" and r["dataset"] == ds],
        "GraphNarrator": [float(r["volume_per_word"]) for r in lex if r["method"] == "graphnarrator" and r["dataset"] == ds],
        "Counterfactual": [float(r["volume_per_word"]) for r in cf if r["dataset"] == ds],
        "GSPELL": [r["volume_per_word"] for r in NE if r["dataset"] == ds]}

kw_rows = []
for metric, label in (("fk", "FK grade"), ("vpw", "Halstead volume per word")):
    P(f"\n== {5 if metric == 'fk' else 6}. Kruskal-Wallis on {label}, 4 methods (pairwise MWU, Bonferroni x6)")
    for ds in ("cora", "products"):
        g = groups[(metric, ds)]
        three = kruskal(*(g[m] for m in ("GraphXAIN", "GraphNarrator", "Counterfactual")))
        P(f"{ds}: " + ", ".join(f"{m} {st.mean(v):.2f} (n={len(v)})" for m, v in g.items()))
        P(f"   check: 3-method H={three.statistic:.2f} (existing table reproduced if equal)")
        kw = kruskal(*g.values())
        P(f"   Kruskal-Wallis H={kw.statistic:.2f} p={kw.pvalue:.3g}")
        kw_rows.append({"metric": metric, "dataset": ds, "comparison": "Kruskal-Wallis (4 methods)", "statistic": kw.statistic,
                        "p": kw.pvalue, "p_bonferroni": "", **{f"n_{m}": len(v) for m, v in g.items()},
                        **{f"mean_{m}": st.mean(v) for m, v in g.items()}})
        for a, b in itertools.combinations(g, 2):
            u = mannwhitneyu(g[a], g[b], alternative="two-sided")
            P(f"   {a} vs {b}: U={u.statistic:.1f} p={u.pvalue:.3g} Bonferroni(x6) p={min(1, 6 * u.pvalue):.3g}")
            kw_rows.append({"metric": metric, "dataset": ds, "comparison": f"{a} vs {b}", "statistic": u.statistic,
                            "p": u.pvalue, "p_bonferroni": min(1, 6 * u.pvalue)})

P("\n== 7. Sensitivity: FK distribution (runaway keyword lists with no sentence punctuation give 1-3 'sentences' of 300-1000 words)")
for ds in ("cora", "products"):
    s = [r for r in NE if r["dataset"] == ds]
    fk = sorted(r["fk_grade"] for r in s)
    hi = [r for r in s if r["fk_grade"] > 30]
    keep = [r for r in s if r["fk_grade"] <= 30]
    c = [r["fk_grade"] for r in keep if r["correct"]]
    i = [r["fk_grade"] for r in keep if not r["correct"]]
    u = mannwhitneyu(c, i, alternative="two-sided")
    P(f"{ds}: median FK {st.median(fk):.2f} (IQR {fk[len(fk) // 4]:.2f}-{fk[3 * len(fk) // 4]:.2f}), max {fk[-1]:.1f}; "
      f"FK>30: {len(hi)} texts (nodes {[r['node'] for r in hi]})")
    P(f"   without FK>30 texts: mean FK {st.mean(r['fk_grade'] for r in keep):.2f} (n={len(keep)}), W/S "
      f"{st.mean(r['words_per_sentence'] for r in keep):.2f}; correct {st.mean(c):.2f} (n={len(c)}) / incorrect "
      f"{st.mean(i):.2f} (n={len(i)}) p={u.pvalue:.3f}")

with open(OUT + "gspell_per_node_metrics.csv", "w", newline="") as f:
    keys = list(dict.fromkeys(k for r in rows for k in r))
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
with open(OUT + "kruskal_wallis_4methods.csv", "w", newline="") as f:
    keys = list(dict.fromkeys(k for r in kw_rows for k in r))
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(kw_rows)
open(OUT + "stage_b_results.txt", "w").write("\n".join(lines) + "\n")
