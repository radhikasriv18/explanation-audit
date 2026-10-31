"""
Phase 1 (pilot) — collect the exact survey-node explanation texts that were
manually / rule-based adjudicated for grounding, plus the persisted claim
counts for each, into answer_key_texts.json. Read-only on every source file.

Text sources (traced 2026-10-06; see README.md for the evidence):
  GraphNarrator Cora      generated_expls-3/{85,463,203,168}.json  (exp_id=3, the survey text;
                          recall values in grounding_per_node_from_chat.csv equal
                          grounding_recall_f1_results.json["graphnarrator_corrected"], which scored exp_id=3)
  GraphNarrator Products  generated_expls-products_untruncated_2026-09-07/{23,3,33,29}.json
                          (source_dir of graphnarrator_products_recall_f1_untruncated.json, whose
                          precision_manual values equal the chat CSV)
  GraphXAIN               graphxain_survey_corrected_2026-08-07/*/explainer_and_prompts.jsonl
                          field raw_llm_output (what grounding_precision_rulebased_v2.py scored)
  CF-GNNExplainer         cf_gnnexplainer_run_2026-08-10/survey_nodes/{cora,products}_survey_nodes.json
                          field llm_raw_output (what grounding_precision_rulebased.py scored)

Adjudicated text scope: GraphNarrator claims were only ever extracted / judged from
the "### Free-Text Explanation" section (extract_node_claims() convention, also used
for the manual Products recall). That section is sliced out verbatim as text_scored;
the full assistant message is kept as text_full. GraphXAIN and CF were scored on the
whole output, so text_scored == text_full.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(".")
GN_OUT = ROOT / "graphnarrCora/GraphNarrator/outputs"
OUT = Path(__file__).resolve().parent / "answer_key_texts.json"

GN_CORA_POS = {510: 85, 2334: 463, 1062: 203, 884: 168}
GN_PROD_POS = {6813: 23, 1852: 3, 8766: 33, 8438: 29}
GX_FILES = {
    "cora": ROOT / "graphxain_survey_corrected_2026-08-07/cora/explainer_and_prompts.jsonl",
    "products_6813_1852": ROOT / "graphxain_survey_corrected_2026-08-07/products_6813_1852/explainer_and_prompts.jsonl",
    "products_8766_8438": ROOT / "graphxain_survey_corrected_2026-08-07/products_8766_8438/explainer_and_prompts.jsonl",
}
CF_FILES = {ds: ROOT / f"cf_gnnexplainer_run_2026-08-10/survey_nodes/{ds}_survey_nodes.json" for ds in ["cora", "products"]}
SURVEY = {"cora": [510, 2334, 1062, 884], "products": [6813, 1852, 8766, 8438]}

GN_RB_CORRECTED = ROOT / "grounding_recall_f1_2026-09-07/grounding_recall_f1_results.json"
GN_PROD_MANUAL = ROOT / "grounding_recall_f1_2026-09-07/graphnarrator_products_recall_f1_untruncated.json"
GX_RB = ROOT / "graphxain_survey_corrected_2026-08-07/grounding_precision_rulebased_v2/graphxain_grounding_precision_RULEBASED_v2.json"
CF_RB = ROOT / "cf_gnnexplainer_run_2026-08-10/grounding_precision_rulebased/cf_gnnexplainer_grounding_precision_RULEBASED.json"
CHAT_CSV = ROOT / "grounding_per_node_from_chat.csv"


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def freetext_section(text):
    m = re.search(r"^#+\s*Free-Text Explanation\s*$", text, re.M)
    if not m:
        return None
    return text[m.end():].strip()


chat = {(r["method"], r["dataset"], int(r["node"])): r for r in csv.DictReader(open(CHAT_CSV))}
rf1 = json.load(open(GN_RB_CORRECTED))
gn_prod_manual = json.load(open(GN_PROD_MANUAL))["results"]
gx_rb = json.load(open(GX_RB))
cf_rb = json.load(open(CF_RB))

entries = []


def add(method, ds, node, source_file, source_locator, text_full, text_scored, scope, manual):
    c = chat.get((method, ds, node), {})
    entries.append(
        {
            "id": f"{method}_{ds}_{node}",
            "method": method,
            "dataset": ds,
            "node": node,
            "source_file": str(source_file),
            "source_locator": source_locator,
            "scored_scope": scope,
            "text_full": text_full,
            "text_full_sha256_16": sha(text_full),
            "text_scored": text_scored,
            "text_scored_sha256_16": sha(text_scored),
            "chat_csv_precision": float(c["precision"]) if c.get("precision") else None,
            "manual": manual,
        }
    )


# ---------------- GraphNarrator
for ds, posmap, d in [("cora", GN_CORA_POS, GN_OUT / "generated_expls-3"), ("products", GN_PROD_POS, GN_OUT / "generated_expls-products_untruncated_2026-09-07")]:
    for node in SURVEY[ds]:
        f = d / f"{posmap[node]}.json"
        msgs = {m["role"]: m["content"] for m in json.load(open(f))["messages"]}
        full = msgs["assistant"]
        scored = freetext_section(full)
        assert scored, f"no Free-Text Explanation section in {f}"
        if ds == "cora":
            r = rf1["graphnarrator_corrected"]["cora"][str(node)]
            manual = {
                "count_source": f"{GN_RB_CORRECTED} [graphnarrator_corrected][cora] (rule-based checker on exp_id=3)",
                "n_claims_adjudicated": r["n_facts"],
                "n_supported": r["n_supported"],
                "n_unsupported": r["n_facts"] - r["n_supported"],
                "precision_in_count_source": r["precision"],
                "all_facts_fallback": r["all_facts_fallback"],
                "note": (
                    "Chat-adjudicated precision (grounding_per_node_from_chat.csv) is NOT backed by any per-claim "
                    "file on disk; its denominator is unknown. The only persisted count is the rule-based n_facts here "
                    "(all via the weak word-overlap fallback, precision 1.0)."
                ),
            }
        else:
            r = gn_prod_manual[str(node)]
            manual = {
                "count_source": None,
                "n_claims_adjudicated": None,
                "n_supported": None,
                "n_unsupported": None,
                "precision_in_count_source": r["precision_manual"],
                "note": (
                    f"Manual precision {r['precision_manual']} from {GN_PROD_MANUAL} (precision_manual, 'given, not "
                    "recomputed'). No per-claim counts persisted anywhere for this text."
                ),
            }
        add("GraphNarrator", ds, node, f, f"messages[assistant]; position {posmap[node]}", full, scored, "### Free-Text Explanation section", manual)

# ---------------- GraphXAIN
gx_records = {}
for f in GX_FILES.values():
    for line in open(f):
        if line.strip():
            r = json.loads(line)
            gx_records[r["target_node"]] = (f, r)
for ds in ["cora", "products"]:
    for node in SURVEY[ds]:
        f, r = gx_records[node]
        text = r["raw_llm_output"]
        rb = gx_rb[str(node)]
        assert rb["narrative"] == text, f"GraphXAIN {node}: rulebased_v2 narrative != jsonl raw_llm_output"
        manual = {
            "count_source": str(GX_RB),
            "n_claims_adjudicated": rb["n_facts"],
            "n_supported": rb["n_supported"],
            "n_unsupported": rb["n_facts"] - rb["n_supported"],
            "precision_in_count_source": rb["grounding_precision"],
            "n_feature_facts": rb["n_feature_facts"],
            "n_neighbor_facts": rb["n_neighbor_facts"],
            "note": "Rule-based v2 counts; chat CSV precision equals this file. Unsupported is not split into contradicted vs unverifiable on disk.",
        }
        add("GraphXAIN", ds, node, f, "raw_llm_output", text, text, "whole output", manual)

# ---------------- CF-GNNExplainer (5 scored nodes)
for ds, f in CF_FILES.items():
    for e in json.load(open(f)):
        if e.get("status") and "llm_raw_output" not in e:
            continue
        node = e["node_id"]
        rb = cf_rb[str(node)]
        assert rb["status"] == "checked"
        text = e["llm_raw_output"]
        manual = {
            "count_source": str(CF_RB),
            "n_claims_adjudicated": rb["n_facts"],
            "n_supported": rb["n_supported"],
            "n_unsupported": rb["n_facts"] - rb["n_supported"],
            "precision_in_count_source": rb["grounding_precision"],
            "n_dict_field_facts": rb["n_dict_field_facts"],
            "n_prose_claim_facts": rb["n_prose_claim_facts"],
            "explainer_key": e["explainer_key"],
            "note": "Rule-based counts; chat CSV precision equals this file. Unsupported is not split into contradicted vs unverifiable on disk.",
        }
        add("CF-GNNExplainer", ds, node, f, f"[node_id={node}].llm_raw_output", text, text, "whole output", manual)

json.dump(entries, open(OUT, "w"), indent=1)
print(f"wrote {OUT}: {len(entries)} texts")
for e in entries:
    m = e["manual"]
    print(f"{e['id']:32s} scored_chars={len(e['text_scored']):5d} n_adj={m['n_claims_adjudicated']} prec_src={m['precision_in_count_source']} chat={e['chat_csv_precision']}  {e['source_file'].replace(str(ROOT)+'/', '')}")
