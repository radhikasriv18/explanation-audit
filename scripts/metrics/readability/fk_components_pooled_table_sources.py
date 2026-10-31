"""
FK components on the sources that reproduce the pooled FK table (identified
2026-10-05 by matching mean FK; see fk_components_full_eval.py for the run on
the Sept-2026 v5 sources, which did NOT reproduce the table).

  GraphXAIN       Cora 542      graphxain_paperaligned_rerun_2026-08-03/cora/graphxain_cora_llama_2hop_narratives_full.json      -> 18.00
  GraphXAIN       Products 200  graphxain_paperaligned_rerun_2026-08-03/products/graphxain_products_llama_narratives_fulleval.json -> 16.64
  GraphNarrator   Cora 541/542  outputs/generated_expls-100, Free-Text section only (fence stripped); 483.json has none -> 15.05 (table 15.04)
  GraphNarrator   Products 200  outputs/generated_expls-101, Free-Text section only (fence stripped)                         -> 9.52
  Counterfactual  no source reproducing 13.77 / 13.53 found; CF-GNNExplainer canonical Response JSONs scored for reference.

Read-only; writes new CSVs only. No model calls.
"""
import csv, glob, json, os, re, statistics as st
import textstat

R = "./"
GN = R + "graphnarrCora/GraphNarrator/outputs/"
OUT = os.path.dirname(os.path.abspath(__file__))


def free_text(a):
    i = a.find("Free-Text Explanation")
    if i < 0:
        return None
    rest = a[i:].split("\n", 1)[1] if "\n" in a[i:] else ""
    return re.sub(r"\s*```\s*$", "", re.sub(r"^```(markdown)?\s*", "", rest.strip())).strip()


def gxain(path):
    for node, rec in json.load(open(path)).items():
        t = rec.get("explanation_text") if isinstance(rec, dict) else rec
        if t:
            yield node, t


def gn_free(d):
    for f in sorted(glob.glob(GN + d + "/*.json")):
        t = free_text(json.load(open(f))["messages"][2]["content"])
        if t:
            yield "pos" + os.path.basename(f)[:-5], t


def cf(path):
    for k, v in json.load(open(path)).items():
        if isinstance(v, list) and len(v) > 1 and v[1]:
            yield k, v[1]


SOURCES = [
    ("GraphXAIN", "cora", "matched", lambda: gxain(R + "graphxain_paperaligned_rerun_2026-08-03/cora/graphxain_cora_llama_2hop_narratives_full.json")),
    ("GraphXAIN", "products", "matched", lambda: gxain(R + "graphxain_paperaligned_rerun_2026-08-03/products/graphxain_products_llama_narratives_fulleval.json")),
    ("GraphNarrator", "cora", "matched(15.05 vs 15.04)", lambda: gn_free("generated_expls-100")),
    ("GraphNarrator", "products", "matched", lambda: gn_free("generated_expls-101")),
    ("CF-GNNExplainer", "cora", "NOT the table source", lambda: cf(R + "llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json")),
    ("CF-GNNExplainer", "products", "NOT the table source", lambda: cf(R + "llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json")),
]

per_text, summary = [], []
for method, ds, status, load in SOURCES:
    rows = []
    for node, text in load():
        s, w, y = textstat.sentence_count(text), textstat.lexicon_count(text), textstat.syllable_count(text)
        rows.append({"method": method, "dataset": ds, "node": node, "sentences": s, "words": w, "syllables": y,
                     "words_per_sentence": w / s, "syllables_per_word": y / w,
                     "fk_grade": textstat.flesch_kincaid_grade(text)})
    per_text += rows
    m = lambda k: st.mean(r[k] for r in rows)
    summary.append({"method": method, "dataset": ds, "status": status, "n": len(rows), "mean_fk_grade": m("fk_grade"),
                    "mean_words_per_sentence": m("words_per_sentence"), "mean_syllables_per_word": m("syllables_per_word"),
                    "mean_sentences_per_expl": m("sentences"), "mean_words_per_expl": m("words")})

for name, data in [("fk_components_pooled_sources_per_text.csv", per_text), ("fk_components_pooled_sources_summary.csv", summary)]:
    with open(os.path.join(OUT, name), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(data[0])); wr.writeheader(); wr.writerows(data)

for r in summary:
    print(f"{r['method']:16s} {r['dataset']:9s} n={r['n']:3d} FK={r['mean_fk_grade']:.4f} W/S={r['mean_words_per_sentence']:.2f} "
          f"Syl/W={r['mean_syllables_per_word']:.3f} S/expl={r['mean_sentences_per_expl']:.2f} W/expl={r['mean_words_per_expl']:.1f}  [{r['status']}]")
