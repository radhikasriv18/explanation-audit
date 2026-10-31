"""
FK-grade components (words/sentence, syllables/word, sentences/explanation,
words/explanation) per method x dataset on the full evaluation sets used by
the current entity-graph v5 / entity-complexity analysis (Sept 2026):

  GraphNarrator   Cora      outputs/generated_expls-3  (+ pkls)            519
  GraphNarrator   Products  outputs/generated_expls-20 (+ pkls_products)   199
  GraphXAIN       Cora      GraphXAIN_Cora/production_corrected_2026-09-07  542
  GraphXAIN       Products  GraphXAIN_Products/production_corrected_...    200
  CF-GNNExplainer Cora      cf-gnnexplainer-canonical ..._cora_standard_Response.json      184
  CF-GNNExplainer Products  cf-gnnexplainer-canonical ..._products_standard_Response.json   60

Loaders reused unmodified from compute_entity_graph_v2.py (by absolute path).
Counts come from textstat itself (sentence_count / lexicon_count /
syllable_count) so that 0.39*WPS + 11.8*SPW - 15.59 reproduces
textstat.flesch_kincaid_grade(). Read-only; writes new files only. No model calls.
"""
import csv, importlib.util, json, os, statistics as st, sys
import textstat

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from tag import TAG  # noqa: E402,F401  (needed to unpickle GN pkls)

V2 = "./grounding_recall_f1_2026-09-07/compute_entity_graph_v2.py"
_s = importlib.util.spec_from_file_location("v2", V2); v2 = importlib.util.module_from_spec(_s); _s.loader.exec_module(v2)

GN = "./graphnarrCora/GraphNarrator/outputs"
CF = "./llm-graph-cf/data"
SOURCES = [
    ("GraphNarrator", "cora", lambda: v2.load_graphnarrator(f"{GN}/generated_expls-3", f"{GN}/pkls")),
    ("GraphNarrator", "products", lambda: v2.load_graphnarrator(f"{GN}/generated_expls-20", f"{GN}/pkls_products")),
    ("GraphXAIN", "cora", lambda: v2.load_graphxain_json("./GraphXAIN_Cora/production_corrected_2026-09-07/graphxain_cora_corrected.json")),
    ("GraphXAIN", "products", lambda: v2.load_graphxain_json("./GraphXAIN_Products/production_corrected_2026-09-07/graphxain_products_corrected.json")),
    ("CF-GNNExplainer", "cora", lambda: v2.load_cf_response_json(
        f"{CF}/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json,"
        f"{CF}/cora/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json")),
    ("CF-GNNExplainer", "products", lambda: v2.load_cf_response_json(
        f"{CF}/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json,"
        f"{CF}/products/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json")),
]
OUT = os.path.dirname(os.path.abspath(__file__))

per_text, summary = [], []
for method, ds, load in SOURCES:
    rows = []
    for node, text, _ in load():
        s, w, y = textstat.sentence_count(text), textstat.lexicon_count(text), textstat.syllable_count(text)
        fk = textstat.flesch_kincaid_grade(text)
        rows.append({"method": method, "dataset": ds, "node": node, "sentences": s, "words": w,
                     "syllables": y, "words_per_sentence": w / s, "syllables_per_word": y / w,
                     "fk_grade": fk, "fk_recon": 0.39 * w / s + 11.8 * y / w - 15.59})
    per_text += rows
    m = lambda k: st.mean(r[k] for r in rows)
    S, W, Y = (sum(r[k] for r in rows) for k in ("sentences", "words", "syllables"))
    summary.append({"method": method, "dataset": ds, "n": len(rows),
                    "mean_words_per_sentence": m("words_per_sentence"),
                    "mean_syllables_per_word": m("syllables_per_word"),
                    "mean_sentences_per_expl": m("sentences"), "mean_words_per_expl": m("words"),
                    "pooled_words_per_sentence": W / S, "pooled_syllables_per_word": Y / W,
                    "mean_fk_grade": m("fk_grade"),
                    "max_abs_fk_recon_err": max(abs(r["fk_grade"] - r["fk_recon"]) for r in rows)})

for name, data in [("fk_components_per_text.csv", per_text), ("fk_components_summary.csv", summary)]:
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)

print(f"textstat {textstat.__version__ if hasattr(textstat,'__version__') else '?'}")
hdr = f"{'method':16s} {'ds':9s} {'n':>4s} {'W/S':>6s} {'Syl/W':>6s} {'S/expl':>7s} {'W/expl':>7s} | {'pW/S':>6s} {'pSyl/W':>6s} {'FK':>6s} {'reconErr':>8s}"
print(hdr)
for r in summary:
    print(f"{r['method']:16s} {r['dataset']:9s} {r['n']:4d} {r['mean_words_per_sentence']:6.2f} {r['mean_syllables_per_word']:6.3f} "
          f"{r['mean_sentences_per_expl']:7.2f} {r['mean_words_per_expl']:7.1f} | {r['pooled_words_per_sentence']:6.2f} "
          f"{r['pooled_syllables_per_word']:6.3f} {r['mean_fk_grade']:6.2f} {r['max_abs_fk_recon_err']:8.4f}")
