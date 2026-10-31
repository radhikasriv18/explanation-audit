"""
Grounding RECALL and F1 for GraphNarrator, GraphXAIN, and CF-GNNExplainer on
the 8 survey nodes (Cora: 510, 2334, 1062, 884 | Products: 6813, 1852, 8766,
8438 -- the scope already locked in for grounding PRECISION, see
graphxain_survey_corrected_2026-08-07/grounding_precision_rulebased_v2.py's
SURVEY_NODE_FILTER and cf_gnnexplainer_run_2026-08-10/survey_nodes/*.json;
Cora node 4 is deliberately excluded, matching that prior decision).

This script does NOT modify any existing ground-truth, results, or
precision-adjudication file. It only *imports* the three existing
grounding_precision_rulebased.py modules (one per method, loaded by absolute
path via importlib since all three happen to share the same filename) to
reuse their parsing/extraction helpers exactly as specified in the task, and
reads their already-computed precision JSON outputs. All new numbers
(recall, F1) and the combined report are written to NEW files in this
directory only:

    grounding_recall_f1_results.json   -- full per-node detail, all 3 methods
    grounding_recall_f1_summary.txt    -- printed summary table + node-510
                                           sanity-check listing (also printed
                                           to stdout)

Definitions implemented (locked, see task spec):

GraphNarrator
  Important items = the node's DIRECT (1-hop) neighbors in the verbalized
  graph input (keys matching '^Node-\\d+$', i.e. no dot -- ROOT excluded,
  and 2-hop children like Node-1.1 excluded since they are not "direct").
  Rank by each neighbor's MAX single-word saliency score on its own line
  (reuses real_keyword_scores_per_node, which keeps ALL token scores,
  boilerplate included, exactly as the real verbalized-graph text has them).
  Top 50% by that ranking (round up), with boundary ties included (computed
  by taking every neighbor whose max score is >= the score AT the cutoff
  rank, which automatically pulls in any ties at that boundary rather than
  arbitrarily cutting one of them).
  Mentioned = the neighbor's node key appears in extract_node_claims()'s
  parsed Free-Text Explanation (reused unmodified from GraphNarrator's own
  precision script).

GraphXAIN
  Important items = the real top-7 GNNExplainer features
  (gnnexplainer_top_features in the JSONL record).
  Mentioned = reuses extract_feature_facts() unmodified; a real feature is
  "mentioned" if its Porter stem appears among the stems of any quoted
  citation in the narrative that extract_feature_facts found to exist in
  the real top-7 set (exists_in_real_top7 == True) -- regardless of whether
  that citation's sentence made a presence/absence assertion, and
  regardless of whether the assertion was correct (existence only, per
  task spec point 2).

CF-GNNExplainer
  Important items = the exact real removed-edge set for that node
  (removed_edges_global in survey_nodes/{cora,products}_survey_nodes.json).
  Mentioned = re-derives the SAME per-sentence removal/addition detection
  used by the precision script's check_prose_claims() (REMOVAL_WORDS /
  ADDITION_WORDS regexes and build_node_class_map(), imported unmodified),
  but tracks it PER EDGE instead of a single aggregated per-sentence
  boolean: a real removed edge counts as "mentioned" if some sentence pairs
  its two endpoints together under removal language that is not also
  flagged as addition language (an addition-flagged sentence is never
  counted as correctly citing a removal, mirroring the precision script's
  own "addition claims are always Contradicted" rule).
  Only nodes with status == "llm_generated" are scored (884, 6813, 8766 have
  no counterfactual and are skipped, matching the precision exclusion).

F1 = 2 * precision * recall / (precision + recall), using the grounding
precision already computed by each method's existing script (cited by file
path in the results, not recomputed here).
"""
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

OUT_DIR = Path("./grounding_recall_f1_2026-09-07")

CORA_SURVEY = [510, 2334, 1062, 884]
PRODUCTS_SURVEY = [6813, 1852, 8766, 8438]


def load_module(name, path):
    """Load a module from an absolute path under a private name -- needed
    because all three existing precision scripts happen to be named
    grounding_precision_rulebased.py in different directories, and a plain
    `import` would silently reuse whichever one Python loaded first."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# =============================================================================
# GraphNarrator
# =============================================================================

GN_REPO = Path("./graphnarrCora/GraphNarrator")
GN_PRECISION_FILES = {
    "cora": GN_REPO / "outputs/standardized_run_2026-08-17/grounding_precision_rulebased/cora_RULEBASED.json",
    "products": GN_REPO / "outputs/standardized_run_2026-08-17/grounding_precision_rulebased/products_RULEBASED.json",
}
GN_PKL_DIRS = {
    "cora": GN_REPO / "outputs/pkls_standardized_run_2026-08-17_cora",
    "products": GN_REPO / "outputs/pkls_standardized_run_2026-08-17_products",
}
GN_EXPL_DIRS = {
    "cora": GN_REPO / "outputs/generated_expls-504",
    "products": GN_REPO / "outputs/generated_expls-503",
}

DIRECT_NEIGHBOR_RE = re.compile(r"^Node-\d+$")


def graphnarrator_node_recall(gn, pos_map, expl_dir, node_id):
    pos = pos_map.get(node_id)
    if pos is None:
        return {"error": "node not found in pkl_dir position map"}
    expl_path = Path(expl_dir) / f"{pos}.json"
    if not expl_path.exists():
        return {"error": f"explanation file not found: {expl_path}"}

    data = json.load(open(expl_path))
    user_content = data["messages"][1]["content"]
    assistant_content = data["messages"][2]["content"]

    graph_block = gn.extract_task_graph_block(user_content)
    kw_scores = gn.real_keyword_scores_per_node(graph_block)  # {node_key: {word: [scores]}}
    claims = gn.extract_node_claims(assistant_content)  # {node_key: claim_text}

    direct_neighbors = [k for k in kw_scores if DIRECT_NEIGHBOR_RE.match(k)]
    direct_neighbors.sort(key=lambda k: int(k.split("-")[1]))

    max_score = {}
    for k in direct_neighbors:
        all_scores = [s for scores in kw_scores[k].values() for s in scores]
        max_score[k] = max(all_scores) if all_scores else float("-inf")

    n = len(direct_neighbors)
    if n == 0:
        return {
            "position_index": pos,
            "direct_neighbors": [],
            "important_set": [],
            "mentioned": {},
            "n_important": 0,
            "n_mentioned": 0,
            "recall": None,
        }

    cutoff_count = math.ceil(n / 2)
    scores_sorted_desc = sorted(max_score.values(), reverse=True)
    boundary_score = scores_sorted_desc[cutoff_count - 1]
    important_set = [k for k in direct_neighbors if max_score[k] >= boundary_score]
    important_set.sort(key=lambda k: (-max_score[k], int(k.split("-")[1])))

    mentioned = {k: (k in claims) for k in important_set}
    n_mentioned = sum(mentioned.values())

    # A totally empty `claims` dict means extract_node_claims() found no
    # parseable "Node-X: ..." lines at all -- the SAME generation-failure
    # signal the existing precision script surfaces as n_facts == 0 / a
    # None precision (see e.g. cora nodes 884/1062/2334: the model emitted
    # a mis-formatted "Graph Structure Reconstruction" listing instead of a
    # Free-Text Explanation). Recall is undefined here, not mechanically 0
    # -- there is no explanation text to check "mentioned" against -- so
    # this is reported as generation_failed with recall=None, consistent
    # with precision's own None treatment, rather than silently scoring a
    # broken generation as "0% recall".
    generation_failed = len(claims) == 0
    recall = None if generation_failed else (n_mentioned / len(important_set) if important_set else None)

    return {
        "position_index": pos,
        "generation_failed": generation_failed,
        "direct_neighbors": direct_neighbors,
        "max_score_per_neighbor": max_score,
        "n_total_direct_neighbors": n,
        "cutoff_count_target_50pct": cutoff_count,
        "boundary_score": boundary_score,
        "important_set": important_set,
        "mentioned": mentioned,
        "n_important": len(important_set),
        "n_mentioned": n_mentioned,
        "recall": recall,
    }


GN_CORA_EXP3_DIR = GN_REPO / "outputs/generated_expls-3"

BOLD_NODE_KEY_RE = re.compile(r"\*\*(ROOT|Node-[\d.]+)(:?)\*\*")
TO_RANGE_RE = re.compile(r"(ROOT|Node-[\d.]+)\s+to\s+(Node-[\d.]+)\s*:")


def normalize_markdown_for_claims(assistant_content):
    """exp_id=3's Free-Text Explanation style differs cosmetically from
    exp_id=504's (bold node keys -- '- **Node-1:** ...' -- and an 'X to Y:'
    range phrasing instead of 'X ~ Y:'), which makes gn.extract_node_claims()
    silently find zero claims even though the explanation is fully valid and
    on-topic (verified by hand on node 1062: real prose discussing
    backpropagation, perceptrons, etc., just formatted this way). This is a
    pure text-normalization pass run BEFORE handing the string to
    gn.extract_node_claims() (imported unmodified) -- it does not change
    that function's matching logic, only puts the input into the format it
    already expects, so the SAME node-identification logic still does the
    actual identification."""
    text = BOLD_NODE_KEY_RE.sub(r"\1\2", assistant_content)
    text = TO_RANGE_RE.sub(r"\1 ~ \2:", text)
    return text


def check_explanation_normalized(gn, pkl_path, expl_json_path):
    """Mirrors gn.check_explanation() (imported unmodified) but feeds
    normalize_markdown_for_claims()'s output to gn.extract_node_claims()
    instead of the raw assistant content -- see that function's docstring.
    Every other helper (extract_task_graph_block, real_keywords_per_node,
    real_keyword_scores_per_node, extract_cited_keywords,
    claim_content_words) is used exactly as-is from gn."""
    graph = gn.TAG.load(pkl_path)
    data = json.load(open(expl_json_path))
    user_content = data["messages"][1]["content"]
    assistant_content = normalize_markdown_for_claims(data["messages"][2]["content"])

    real_kw = gn.real_keywords_per_node(gn.extract_task_graph_block(user_content))
    real_kw_scores = gn.real_keyword_scores_per_node(gn.extract_task_graph_block(user_content))
    claims = gn.extract_node_claims(assistant_content)

    facts = []
    for node_key, claim_text in claims.items():
        if node_key not in real_kw:
            continue
        cited = gn.extract_cited_keywords(claim_text)
        if cited:
            for kw, cited_score in cited:
                word_exists = kw in real_kw_scores[node_key]
                facts.append({"node_key": node_key, "supported": word_exists, "fallback": False})
        else:
            real_words = real_kw[node_key]
            claim_words = gn.claim_content_words(claim_text)
            matched = claim_words & real_words
            facts.append({"node_key": node_key, "supported": len(matched) > 0, "fallback": True})

    n_supported = sum(1 for f in facts if f["supported"])
    n_fallback = sum(1 for f in facts if f["fallback"])
    precision = n_supported / len(facts) if facts else None
    return {
        "root_global_id": graph.root_global_id,
        "n_facts": len(facts),
        "n_supported": n_supported,
        "n_fallback_facts": n_fallback,
        # IMPORTANT CAVEAT (found 2026-09-07, see module docstring / memory):
        # exp_id=3's writing style never quotes a "word" (score) citation the
        # way exp_id=504 does, so extract_cited_keywords() finds nothing and
        # EVERY fact for every exp_id=3 node falls back to the loose
        # whole-claim topic-word-overlap check (any shared real word passes).
        # When n_fallback_facts == n_facts, this precision number is NOT
        # comparable to exp_id=504's (which is checked almost entirely via
        # the strict per-citation path) -- it reflects a much weaker test,
        # not better grounding.
        "all_facts_fallback": n_fallback == len(facts) if facts else None,
        "grounding_precision": precision,
    }


def graphnarrator_node_recall_normalized(gn, pos_map, expl_dir, node_id):
    """Same as graphnarrator_node_recall() but runs claims through
    normalize_markdown_for_claims() first -- see that function's docstring."""
    pos = pos_map.get(node_id)
    if pos is None:
        return {"error": "node not found in pkl_dir position map"}
    expl_path = Path(expl_dir) / f"{pos}.json"
    if not expl_path.exists():
        return {"error": f"explanation file not found: {expl_path}"}

    data = json.load(open(expl_path))
    user_content = data["messages"][1]["content"]
    assistant_content = normalize_markdown_for_claims(data["messages"][2]["content"])

    graph_block = gn.extract_task_graph_block(user_content)
    kw_scores = gn.real_keyword_scores_per_node(graph_block)
    claims = gn.extract_node_claims(assistant_content)

    direct_neighbors = [k for k in kw_scores if DIRECT_NEIGHBOR_RE.match(k)]
    direct_neighbors.sort(key=lambda k: int(k.split("-")[1]))
    max_score = {}
    for k in direct_neighbors:
        all_scores = [s for scores in kw_scores[k].values() for s in scores]
        max_score[k] = max(all_scores) if all_scores else float("-inf")

    n = len(direct_neighbors)
    if n == 0:
        return {"position_index": pos, "generation_failed": len(claims) == 0,
                "direct_neighbors": [], "important_set": [], "mentioned": {},
                "n_important": 0, "n_mentioned": 0, "recall": None}

    cutoff_count = math.ceil(n / 2)
    scores_sorted_desc = sorted(max_score.values(), reverse=True)
    boundary_score = scores_sorted_desc[cutoff_count - 1]
    important_set = [k for k in direct_neighbors if max_score[k] >= boundary_score]
    important_set.sort(key=lambda k: (-max_score[k], int(k.split("-")[1])))

    mentioned = {k: (k in claims) for k in important_set}
    n_mentioned = sum(mentioned.values())
    generation_failed = len(claims) == 0
    recall = None if generation_failed else (n_mentioned / len(important_set) if important_set else None)

    return {
        "position_index": pos,
        "generation_failed": generation_failed,
        "direct_neighbors": direct_neighbors,
        "max_score_per_neighbor": max_score,
        "n_total_direct_neighbors": n,
        "cutoff_count_target_50pct": cutoff_count,
        "boundary_score": boundary_score,
        "important_set": important_set,
        "mentioned": mentioned,
        "n_important": len(important_set),
        "n_mentioned": n_mentioned,
        "recall": recall,
    }


def run_graphnarrator_cora_exp3(gn, pos_map):
    """Side-by-side comparison run: the ACTUAL text shown to human survey
    participants for GraphNarrator/Cora is exp_id=3 (confirmed 2026-09-07 by
    exact-phrase matching against cora_explanation_comparison_llama.txt --
    e.g. node 884's survey text contains the verbatim sentence "cryptographic
    limitations in learning boolean formulae", found ONLY in
    generated_expls-3/168.json on this whole filesystem). The existing
    'standardized_run_2026-08-17' precision file instead scored a later,
    freshly-regenerated exp_id=504, which fails outright on 3 of these 4
    nodes and, even for node 510 where it succeeds, produces completely
    different content (different cited keywords, different target class,
    even a hallucinated extra neighbor) than what was actually surveyed.
    This function re-runs the SAME rule-based precision check (gn.check_explanation,
    imported unmodified) plus this script's own recall logic against
    exp_id=3, so the two data sources can be reported side by side. Writes
    to a NEW file only -- does not touch cora_RULEBASED.json."""
    results = {}
    for node_id in CORA_SURVEY:
        pos = pos_map.get(node_id)
        pkl_path = GN_PKL_DIRS["cora"] / f"{pos}.pkl"
        expl_path = GN_CORA_EXP3_DIR / f"{pos}.json"
        if not expl_path.exists():
            results[node_id] = {"error": f"not found: {expl_path}"}
            continue
        precision_res = check_explanation_normalized(gn, pkl_path, expl_path)
        recall_res = graphnarrator_node_recall_normalized(gn, pos_map, GN_CORA_EXP3_DIR, node_id)
        precision = precision_res.get("grounding_precision")
        recall = recall_res.get("recall")
        f1 = None
        if precision is not None and recall is not None and (precision + recall) > 0:
            f1 = 2 * precision * recall / (precision + recall)
        results[node_id] = {
            "precision": precision,
            "n_facts": precision_res.get("n_facts"),
            "n_supported": precision_res.get("n_supported"),
            "n_fallback_facts": precision_res.get("n_fallback_facts"),
            "all_facts_fallback": precision_res.get("all_facts_fallback"),
            **recall_res,
            "f1": f1,
        }
    return results


def graphnarrator_products_source_unconfirmed(precision_data):
    """FIX 2 (2026-09-07), Products half: exp503 (used by the existing
    'GraphNarrator' table above) is the SAME kind of truncated
    use_local_hf=True generation as Cora's exp504 -- confirmed to hard-cut
    the verbalized-graph text at exactly 6000 characters for all 4 Products
    survey nodes too (see memory / prior debug session). Unlike Cora, no
    untruncated ORIGINAL source could be confirmed for Products: filesystem-
    wide exact-phrase searches for each node's real survey text (both its
    "Graph Structure Reconstruction" neighbor titles and its Free-Text
    Explanation prose, from products_explanation_comparison_llama*.txt)
    turned up zero verbatim matches anywhere on disk for 6813 and 1852; the
    closest candidates found for 8438 (generated_expls-501/29.json,
    GraphXAIN_Products/output/graphnarrator_products_regen_6813_1852.json
    for 6813) are confirmed NOT exact matches (different neighbor counts,
    different phrasing -- non-deterministic LLM sampling produces different
    text on every regeneration attempt, so thematic similarity is not
    proof of identity); and node 8766's own survey entry doesn't even
    contain a "Free-Text Explanation" heading to search for. Per the task's
    explicit instruction, these are FLAGGED as unconfirmed rather than
    silently scored against an unverified or known-truncated substitute."""
    results = {}
    for node_id in PRODUCTS_SURVEY:
        prec_entry = precision_data.get(str(node_id), precision_data.get(node_id))
        precision = prec_entry.get("grounding_precision") if isinstance(prec_entry, dict) else None
        results[node_id] = {
            "source_unconfirmed": True,
            "reason": "No untruncated original generation for this node could be verified anywhere on "
                      "disk against products_explanation_comparison_llama*.txt (see docstring) -- recall "
                      "and F1 are intentionally left unset rather than falling back to the truncated "
                      "exp503 source or an unverified candidate file.",
            "precision": precision,
            "precision_source_file": str(GN_PRECISION_FILES["products"]),
            "recall": None,
            "f1": None,
        }
    return results


def run_graphnarrator():
    gn = load_module("gn_precision", str(GN_REPO / "grounding_precision_rulebased.py"))

    precision_data = {}
    for ds, path in GN_PRECISION_FILES.items():
        precision_data[ds] = json.load(open(path))["results"]

    results = {"cora": {}, "products": {}}
    pos_maps = {}
    for ds, survey in (("cora", CORA_SURVEY), ("products", PRODUCTS_SURVEY)):
        pos_map = gn.build_position_map(GN_PKL_DIRS[ds])
        pos_maps[ds] = pos_map
        for node_id in survey:
            rec = graphnarrator_node_recall(gn, pos_map, GN_EXPL_DIRS[ds], node_id)
            prec_entry = precision_data[ds].get(str(node_id), precision_data[ds].get(node_id))
            precision = prec_entry.get("grounding_precision") if isinstance(prec_entry, dict) else None
            recall = rec.get("recall")
            f1 = None
            if precision is not None and recall is not None and (precision + recall) > 0:
                f1 = 2 * precision * recall / (precision + recall)
            rec["precision"] = precision
            rec["precision_source_file"] = str(GN_PRECISION_FILES[ds])
            rec["f1"] = f1
            if isinstance(prec_entry, dict) and "facts" in prec_entry:
                n_fb = sum(1 for f in prec_entry["facts"] if f.get("fallback"))
                rec["n_facts"] = prec_entry.get("n_facts")
                rec["n_fallback_facts"] = n_fb
                rec["all_facts_fallback"] = (n_fb == prec_entry["n_facts"]) if prec_entry.get("n_facts") else None
            results[ds][node_id] = rec

    cora_exp3_results = run_graphnarrator_cora_exp3(gn, pos_maps["cora"])
    return results, cora_exp3_results


# =============================================================================
# GraphXAIN
# =============================================================================

GX_DIR = Path("./graphxain_survey_corrected_2026-08-07")
GX_PRECISION_FILE = GX_DIR / "grounding_precision_rulebased_v2/graphxain_grounding_precision_RULEBASED_v2.json"
GX_SURVEY_JSONL = {
    "cora": GX_DIR / "cora/explainer_and_prompts.jsonl",
    "products_6813_1852": GX_DIR / "products_6813_1852/explainer_and_prompts.jsonl",
    "products_8766_8438": GX_DIR / "products_8766_8438/explainer_and_prompts.jsonl",
}
GX_SURVEY_SCOPE = {"cora": set(CORA_SURVEY), "products": set(PRODUCTS_SURVEY)}


def run_graphxain():
    gx = load_module("gx_precision", str(GX_DIR / "grounding_precision_rulebased.py"))

    precision_data = json.load(open(GX_PRECISION_FILE))  # {node_id_str: {...}}

    records = {}
    for label, path in GX_SURVEY_JSONL.items():
        dataset_label = "cora" if label == "cora" else "products"
        for line in open(path):
            r = json.loads(line)
            node_id = r["target_node"]
            if node_id not in GX_SURVEY_SCOPE[dataset_label]:
                continue  # Cora node 4 excluded, same 8-node scope as precision v2
            records[(dataset_label, node_id)] = r

    results = {"cora": {}, "products": {}}
    for (ds, node_id), r in records.items():
        narrative = r["raw_llm_output"]
        real_feats = r["gnnexplainer_top_features"]  # list of 7 {word, importance, present}
        predicted_class = r["prediction"]["Predicted Class"]

        feat_facts, _, _ = gx.extract_feature_facts(narrative, real_feats, predicted_class)
        mentioned_stems = {f["stem"] for f in feat_facts if f["exists_in_real_top7"]}

        per_feature = []
        n_mentioned = 0
        for feat in real_feats:
            stem = gx.ps.stem(feat["word"].lower())
            is_mentioned = stem in mentioned_stems
            n_mentioned += int(is_mentioned)
            per_feature.append({"word": feat["word"], "stem": stem, "importance": feat["importance"], "mentioned": is_mentioned})

        recall = n_mentioned / len(real_feats) if real_feats else None

        prec_entry = precision_data.get(str(node_id))
        precision = prec_entry.get("grounding_precision") if prec_entry else None
        f1 = None
        if precision is not None and recall is not None and (precision + recall) > 0:
            f1 = 2 * precision * recall / (precision + recall)

        results[ds][node_id] = {
            "real_top7_features": per_feature,
            "n_important": len(real_feats),
            "n_mentioned": n_mentioned,
            "recall": recall,
            "precision": precision,
            "precision_source_file": str(GX_PRECISION_FILE),
            "f1": f1,
        }
    return results


# =============================================================================
# CF-GNNExplainer
# =============================================================================

CF_RUN_DIR = Path("./cf_gnnexplainer_run_2026-08-10")
CF_PRECISION_FILE = CF_RUN_DIR / "grounding_precision_rulebased/cf_gnnexplainer_grounding_precision_RULEBASED.json"
CF_SURVEY_FILES = {
    "cora": CF_RUN_DIR / "survey_nodes/cora_survey_nodes.json",
    "products": CF_RUN_DIR / "survey_nodes/products_survey_nodes.json",
}



# --- FIX 1 (2026-09-07): the ORIGINAL cf.REMOVAL_WORDS (imported unmodified
# from the precision script, kept file-untouched) only covers verb forms
# ("remove"/"removed") and a rigid "lost (the|its) connection" adjacency, so
# it misses real, correct citations debugged by hand:
#   - node 1062: "the removal of the connection between node 1062 and node
#     930" -- "removal" is a noun form; "removed?" never matches it.
#   - node 510: "lost all its connections" -- the inserted word "all" breaks
#     the "lost (the|its) connection" adjacency, and the plural
#     "connections" breaks the original's trailing \b (which expects
#     "connection" to end right there).
# This is a NEW, script-local regex used only for THIS script's recall
# computation -- it does not alter cf.REMOVAL_WORDS or any other part of
# the original precision-adjudication module. remov\w* subsumes remove/
# removed/removes/removing/removal in one alternative; sever\w* likewise
# subsumes severed/severing/severance; connections? tolerates the plural
# throughout; "lost(?:\s+\w+){0,3}?\s+connections?" allows up to 3 filler
# words between "lost" and "connection(s)" (covers "lost all its
# connections", "lost the connections to", etc.) instead of the original's
# fixed "(the |its )?" single-slot adjacency.
REMOVAL_WORDS_FIXED = re.compile(
    r"\b(remov\w*|disconnect\w*|no longer|sever\w*|eliminat\w*|"
    r"lost(?:\s+\w+){0,3}?\s+connections?|"
    r"drop(?:ped)? the (?:edge|connection|link)s?|"
    r"cut (?:the )?(?:edge|connection|link)s?)\b",
    re.IGNORECASE,
)

# --- FIX 1 (2026-09-07), sentence-splitter gap: the original
# r"(?<=[.!?])\s+" never splits when a period is immediately followed by a
# closing quote before whitespace (e.g. `Theory."\n\nHere...`), because the
# character right before the whitespace run is the quote, not the
# punctuation the lookbehind checks for -- confirmed this merged node
# 1062's real removal sentence into one giant multi-paragraph blob. Adding
# an optional quote character between the punctuation and the whitespace
# fixes this without changing behavior for unquoted sentence endings.
SENTENCE_SPLIT_FIXED = re.compile(r"(?<=[.!?])[\"']?\s+")


def cf_edge_recall(cf, entry, removal_words=REMOVAL_WORDS_FIXED, sentence_split=SENTENCE_SPLIT_FIXED):
    """Re-derives check_prose_claims()'s B2 removal/addition sentence
    detection, but returns which SPECIFIC real removed edges were correctly
    cited (both endpoints named together under removal language), instead
    of check_prose_claims()'s single aggregated per-sentence verdict.
    `removal_words`/`sentence_split` default to the FIXED versions above;
    callers can still pass the ORIGINAL cf.REMOVAL_WORDS / the original
    split regex to reproduce the pre-fix numbers for before/after
    comparison (see run_cf_gnnexplainer())."""
    node_id = entry["node_id"]
    raw_output = entry["llm_raw_output"]
    removed_edges = entry["removed_edges_global"]
    removed_pairs = {tuple(sorted(p)) for p in removed_edges}

    factual_class_map = cf.build_node_class_map(entry["factual_graph_description"])
    cf_class_map = cf.build_node_class_map(entry["counterfactual_graph_description"])

    # KNOWN OPEN ISSUE (found 2026-09-07, NOT part of the two requested
    # fixes, left AS-IS): CF-GNNExplainer's raw output often embeds a
    # Python-dict-literal block (`infos = {...}`) with no sentence-ending
    # punctuation between its comma-separated fields, so a fixed sentence
    # boundary never appears until deep inside a quoted string value (e.g.
    # 'Natural_Language_Explanation': '...'). Neither this fix nor the
    # original splitter breaks that block into anything smaller -- the
    # WHOLE dict (which always lists the full real Factual_Target_Node_
    # Neighbors set) becomes one "sentence". If that block also contains
    # removal language ANYWHERE in it (even inside the one specific
    # sentence the model wrote), every real removed edge touching the
    # target gets credited, not just the one the model actually named.
    # Confirmed on node 1062: crediting (930,1062) is a genuine citation
    # ("the removal of the connection between node 1062 and node 930"),
    # but (1062,1323) is also credited purely because 1323 sits in the same
    # dict's neighbor list -- the model never named 1323 specifically. This
    # does NOT affect node 510 (its "lost ALL its connections" claim is a
    # genuine broad claim that legitimately covers each of its 3 factual
    # neighbors). `id_group_size` below records how many real-graph ids
    # were in the matched blob, as a rough signal for how tight vs. diffuse
    # a given credit is -- large groups deserve more scrutiny before trusting
    # the credit at face value.
    mentioned_pairs = set()
    credit_group_size = {}
    for sent in sentence_split.split(raw_output):
        ids_in_sent = [int(x) for x in re.findall(r"\b(\d{1,6})\b", sent)]
        ids_in_sent = [i for i in ids_in_sent if i in factual_class_map or i in cf_class_map or i == node_id]
        if len(ids_in_sent) < 2:
            continue
        removal_hit = removal_words.search(sent)
        addition_hit = cf.ADDITION_WORDS.search(sent)
        if not removal_hit or addition_hit:
            # No removal language, OR addition language present -- an
            # addition-flagged sentence is never a correct removal citation,
            # matching check_prose_claims()'s "supported = False" rule for
            # addition_hit regardless of any co-occurring removal language.
            continue
        pairs_mentioned = {tuple(sorted((a, b))) for i, a in enumerate(ids_in_sent) for b in ids_in_sent[i + 1:]}
        newly_mentioned = pairs_mentioned & removed_pairs
        mentioned_pairs |= newly_mentioned
        for p in newly_mentioned:
            credit_group_size[p] = min(credit_group_size.get(p, 10**9), len(set(ids_in_sent)))

    per_edge = [
        {"edge": list(p), "mentioned": p in mentioned_pairs, "matched_id_group_size": credit_group_size.get(p)}
        for p in sorted(removed_pairs)
    ]
    n_mentioned = len(mentioned_pairs)
    n_total = len(removed_pairs)
    recall = n_mentioned / n_total if n_total else None
    return per_edge, n_mentioned, n_total, recall


def run_cf_gnnexplainer():
    cf = load_module("cf_precision", str(CF_RUN_DIR / "grounding_precision_rulebased/grounding_precision_rulebased.py"))
    precision_data = json.load(open(CF_PRECISION_FILE))

    results = {"cora": {}, "products": {}}
    for ds, path in CF_SURVEY_FILES.items():
        entries = json.load(open(path))
        for entry in entries:
            node_id = entry["node_id"]
            if entry["status"] != "llm_generated":
                results[ds][node_id] = {"status": entry["status"], "skipped": True}
                continue

            per_edge, n_mentioned, n_total, recall = cf_edge_recall(cf, entry)
            # Before-fix numbers, computed with the ORIGINAL cf.REMOVAL_WORDS
            # and the original (unfixed) sentence splitter, for side-by-side
            # reporting -- cf.REMOVAL_WORDS itself is never modified.
            _, n_mentioned_before, _, recall_before = cf_edge_recall(
                cf, entry, removal_words=cf.REMOVAL_WORDS,
                sentence_split=re.compile(r"(?<=[.!?])\s+"),
            )

            prec_entry = precision_data.get(str(node_id))
            precision = prec_entry.get("grounding_precision") if prec_entry else None
            f1 = None
            if precision is not None and recall is not None and (precision + recall) > 0:
                f1 = 2 * precision * recall / (precision + recall)
            f1_before = None
            if precision is not None and recall_before is not None and (precision + recall_before) > 0:
                f1_before = 2 * precision * recall_before / (precision + recall_before)

            results[ds][node_id] = {
                "status": "checked",
                "real_removed_edges": per_edge,
                "n_important": n_total,
                "n_mentioned": n_mentioned,
                "recall": recall,
                "recall_before_fix": recall_before,
                "n_mentioned_before_fix": n_mentioned_before,
                "precision": precision,
                "precision_source_file": str(CF_PRECISION_FILE),
                "f1": f1,
                "f1_before_fix": f1_before,
            }
    return results


# =============================================================================
# Summary + main
# =============================================================================

def mean(vals):
    vals = [v for v in vals if v is not None]
    return sum(vals) / len(vals) if vals else None


def summarize(method_name, results):
    lines = [f"\n=== {method_name} ==="]
    for ds in ("cora", "products"):
        precs, recs, f1s = [], [], []
        for node_id, r in sorted(results[ds].items()):
            if r.get("skipped"):
                lines.append(f"  {ds} node {node_id}: skipped ({r['status']})")
                continue
            precs.append(r.get("precision"))
            recs.append(r.get("recall"))
            f1s.append(r.get("f1"))
            p_str = f"{r['precision']:.3f}" if r.get("precision") is not None else "n/a"
            r_str = f"{r['recall']:.3f}" if r.get("recall") is not None else "n/a"
            f1_str = f"{r['f1']:.3f}" if r.get("f1") is not None else "n/a"
            tag = " [GENERATION FAILED]" if r.get("generation_failed") else ""
            if r.get("source_unconfirmed"):
                tag = " [SOURCE UNCONFIRMED -- recall/F1 intentionally left unset]"
            lines.append(f"  {ds} node {node_id}: precision={p_str}  recall={r_str}  F1={f1_str}{tag}")
        mp, mr, mf1 = mean(precs), mean(recs), mean(f1s)
        mp_str = f"{mp:.3f}" if mp is not None else "n/a"
        mr_str = f"{mr:.3f}" if mr is not None else "n/a"
        mf1_str = f"{mf1:.3f}" if mf1 is not None else "n/a"
        lines.append(f"  -> {ds} mean: precision={mp_str}  recall={mr_str}  F1={mf1_str}")
    return "\n".join(lines), {ds: (mean([r.get("precision") for r in results[ds].values() if not r.get("skipped")]),
                                    mean([r.get("recall") for r in results[ds].values() if not r.get("skipped")]),
                                    mean([r.get("f1") for r in results[ds].values() if not r.get("skipped")]))
                                for ds in ("cora", "products")}


def node510_sanity_check(gn_results):
    node = gn_results["cora"].get(510)
    if not node:
        return "node 510 not found in GraphNarrator cora results"
    lines = ["\n=== GraphNarrator node 510 sanity check ==="]
    lines.append(f"direct (1-hop) neighbors in verbalized graph: {node['direct_neighbors']}")
    lines.append(f"max saliency score per neighbor: {node['max_score_per_neighbor']}")
    lines.append(f"top-50% important set (n={node['n_important']} of {node['n_total_direct_neighbors']} total): {node['important_set']}")
    for k in node["important_set"]:
        lines.append(f"    {k}: mentioned={node['mentioned'][k]}")
    lines.append(f"recall = {node['n_mentioned']}/{node['n_important']} = {node['recall']}")
    lines.append(f"precision (from existing adjudication) = {node['precision']}")
    lines.append(f"F1 = {node['f1']}")
    return "\n".join(lines)


def gn_cora_exp3_comparison_text(gn_results, cora_exp3_results):
    lines = ["\n=== GraphNarrator Cora: side-by-side data-source comparison ==="]
    lines.append("exp_id=504 (existing 'standardized_run_2026-08-17' precision file, cora_RULEBASED.json)")
    lines.append("   vs. exp_id=3 (the ACTUAL text shown to human survey participants -- confirmed by exact")
    lines.append("   phrase matching against cora_explanation_comparison_llama.txt, 2026-09-07)")
    lines.append("")
    lines.append("CAVEAT (found 2026-09-07): the precision checker's PRIMARY test is strict --")
    lines.append("does a quoted \"word\" (score) citation actually exist in the real data. It only")
    lines.append("falls back to a much weaker 'does this claim share any real content word at all'")
    lines.append("test when a claim has NO quoted citation to check. exp_id=3's writing style never")
    lines.append("quotes score citations at all, so ALL of its facts hit the weak fallback path (see")
    lines.append("'fb' column below). exp_id=504's node 510 also happens to be 100% fallback, so")
    lines.append("that ONE row is a fair apples-to-apples comparison (0.4 vs 1.0, both weak-test).")
    lines.append("For 1062/2334/884 there is no prior score to compare against at all (exp_id=504")
    lines.append("failed outright there) -- read exp_id=3's 1.000s there as 'every claim shares a")
    lines.append("real word with its node,' a real but WEAK grounding signal, not literal perfection.")
    lines.append(f"{'node':>6s} | {'exp504 P':>9s} {'exp504 R':>9s} {'exp504 F1':>10s} {'fb':>4s} | {'exp3 P':>7s} {'exp3 R':>7s} {'exp3 F1':>8s} {'fb':>4s}")
    for node_id in CORA_SURVEY:
        a = gn_results["cora"][node_id]
        b = cora_exp3_results.get(node_id, {})

        def fmt(v):
            return f"{v:.3f}" if isinstance(v, (int, float)) else "n/a"

        def fmt_fb(d):
            if d.get("n_facts"):
                return f"{d.get('n_fallback_facts', 0)}/{d['n_facts']}"
            return "n/a"

        tag = " [exp504 GENERATION FAILED]" if a.get("generation_failed") else ""
        lines.append(
            f"{node_id:>6d} | {fmt(a.get('precision')):>9s} {fmt(a.get('recall')):>9s} {fmt(a.get('f1')):>10s} {fmt_fb(a):>4s} | "
            f"{fmt(b.get('precision')):>7s} {fmt(b.get('recall')):>7s} {fmt(b.get('f1')):>8s} {fmt_fb(b):>4s}{tag}"
        )
    return "\n".join(lines)


def cf_before_after_text(cf_results):
    lines = ["\n=== CF-GNNExplainer: REMOVAL_WORDS / sentence-splitter fix, before vs after (FIX 1) ==="]
    lines.append(f"{'node':>6s} {'dataset':>10s} | {'recall before':>14s} {'recall after':>13s} | {'F1 before':>10s} {'F1 after':>9s}")
    for ds in ("cora", "products"):
        for node_id, r in sorted(cf_results[ds].items()):
            if r.get("skipped"):
                lines.append(f"{node_id:>6d} {ds:>10s} | skipped ({r['status']})")
                continue

            def fmt(v):
                return f"{v:.3f}" if isinstance(v, (int, float)) else "n/a"

            changed = " <-- FIXED" if r.get("recall_before_fix") != r.get("recall") else ""
            lines.append(
                f"{node_id:>6d} {ds:>10s} | {fmt(r.get('recall_before_fix')):>14s} {fmt(r.get('recall')):>13s} | "
                f"{fmt(r.get('f1_before_fix')):>10s} {fmt(r.get('f1')):>9s}{changed}"
            )
    return "\n".join(lines)


def main():
    gn_results, cora_exp3_results = run_graphnarrator()
    gx_results = run_graphxain()
    cf_results = run_cf_gnnexplainer()

    precision_data_products = json.load(open(GN_PRECISION_FILES["products"]))["results"]
    products_unconfirmed = graphnarrator_products_source_unconfirmed(precision_data_products)
    gn_corrected = {"cora": cora_exp3_results, "products": products_unconfirmed}

    all_results = {
        "graphnarrator_superseded_truncated_source": gn_results,
        "graphnarrator_corrected": gn_corrected,
        "graphxain": gx_results,
        "cf_gnnexplainer": cf_results,  # includes recall/f1 (after fix) and recall_before_fix/f1_before_fix
    }
    out_json = OUT_DIR / "grounding_recall_f1_results.json"
    with open(out_json, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # cf_results already carries the FIXED recall/f1 as "recall"/"f1"; build
    # a same-shaped view under the ORIGINAL (unfixed) numbers so summarize()
    # can render a before-fix reference section the same way.
    cf_results_before_fix = {
        ds: {
            nid: (r if r.get("skipped") else {**r, "recall": r.get("recall_before_fix"), "f1": r.get("f1_before_fix")})
            for nid, r in cf_results[ds].items()
        }
        for ds in ("cora", "products")
    }

    summary_lines = []
    means = {}

    summary_lines.append("\n########## FIX 1: CF-GNNExplainer REMOVAL_WORDS + sentence-splitter ##########")
    summary_lines.append(cf_before_after_text(cf_results))
    for name, results in (
        ("CF-GNNExplainer [BEFORE FIX, reference only]", cf_results_before_fix),
        ("CF-GNNExplainer [AFTER FIX]", cf_results),
    ):
        text, m = summarize(name, results)
        summary_lines.append(text)
        means[name] = m

    summary_lines.append("\n########## FIX 2: GraphNarrator -- untruncated survey-text source ##########")
    summary_lines.append(node510_sanity_check(gn_results))
    summary_lines.append(gn_cora_exp3_comparison_text(gn_results, cora_exp3_results))
    for name, results in (
        ("GraphNarrator [SUPERSEDED, truncated exp504/exp503 source]", gn_results),
        ("GraphNarrator [CORRECTED: exp_id=3 Cora, Products unconfirmed]", gn_corrected),
    ):
        text, m = summarize(name, results)
        summary_lines.append(text)
        means[name] = m

    text, m = summarize("GraphXAIN", gx_results)
    summary_lines.append(text)
    means["GraphXAIN"] = m

    summary_lines.append(
        "\n\n=== FINAL Summary table: method x dataset (mean precision [unchanged, locked adjudication] "
        "/ mean recall [corrected] / mean F1 [recomputed]) ==="
    )
    summary_lines.append(f"{'method':55s} {'dataset':10s} {'mean_precision':>14s} {'mean_recall':>12s} {'mean_f1':>10s}")
    for name in (
        "GraphNarrator [CORRECTED: exp_id=3 Cora, Products unconfirmed]",
        "GraphXAIN",
        "CF-GNNExplainer [AFTER FIX]",
    ):
        for ds in ("cora", "products"):
            mp, mr, mf1 = means[name][ds]
            if mp is None and mr is None and mf1 is None:
                continue
            mp_str = f"{mp:.3f}" if mp is not None else "n/a"
            mr_str = f"{mr:.3f}" if mr is not None else "n/a"
            mf1_str = f"{mf1:.3f}" if mf1 is not None else "n/a"
            summary_lines.append(f"{name:55s} {ds:10s} {mp_str:>14s} {mr_str:>12s} {mf1_str:>10s}")

    summary_lines.append(
        "\nNote: GraphNarrator/Products recall+F1 are 'n/a' by design (source unconfirmed, see "
        "graphnarrator_products_source_unconfirmed() docstring) -- NOT zero, NOT the old truncated value."
    )

    summary_text = "\n".join(summary_lines)
    print(summary_text)

    out_txt = OUT_DIR / "grounding_recall_f1_summary.txt"
    with open(out_txt, "w") as f:
        f.write(summary_text + "\n")

    print(f"\nWrote {out_json}")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
