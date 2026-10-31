"""
CF-GNNExplainer Grounding Precision (rule-based) -- mirrors the methodology
established for GraphNarrator
(graphnarrCora/GraphNarrator/outputs/standardized_run_2026-08-17/grounding_precision_rulebased/)
and adapted for GraphXAIN
(graphxain_survey_corrected_2026-08-07/grounding_precision_rulebased/),
applied to CF-GNNExplainer's structured-dict-plus-prose narration output.

No LLM judge -- rule-based extraction and exact/set-equality checks against
the real explainer data already persisted in
cf_gnnexplainer_run_2026-08-10/survey_nodes/{cora,products}_survey_nodes.json
(itself sourced from data/{cora,products}/cf-gnnexplainer-canonical/, the
same ground truth the paper's own TNI/CCI/FTNF/CFTNF/FTNN/CFTNN metrics
would be computed against).

Atomic facts, two families:

A. Structured dict-field facts (up to 7 per node) -- the LLM's own stated
   Target_Node_ID / Factual_Target_Node_Class / Counterfactual_Target_Node_class
   / Factual_Target_Node_Neighbors / Counterfactual_Target_Node_Neighbors /
   Factual_Target_Node_Features / Counterfactual_Target_Node_Features lines,
   parsed out of the raw output text and checked by exact value (ID, class)
   or set equality (neighbors, features) against the real target dict.
   A field the model never stated a parseable value for is logged as
   `not_stated` and excluded from the fact count (no claim made = nothing to
   verify), not counted as Contradicted.

B. Free-text explanation claims -- three sub-types:
   B1. node_class_claim: "node <id> ... is classified as <X>" for a
       non-target node id, checked against that node's real class in the
       graph description context it appears in (factual/counterfactual).
   B2. edge_change_claim: sentences with removal- or addition-indicating
       language naming specific node ids, checked against the real
       cf_removed_edges for that node (reuses/extends the edge-accuracy
       audit already run at the corpus level; here re-derived
       per-sentence for these 5 survey nodes specifically). Addition-
       language is always Contradicted by construction (this method only
       ever deletes edges).
   B3. target_feature_change_claim: explicit assertions that the target's
       own features changed/stayed the same, checked against the real fact
       that CF-GNNExplainer never touches features (always "unchanged" here
       by construction).

Verdict: Supported / Contradicted (binary, matching the terminology
requested for this task -- GraphNarrator/GraphXAIN used Supported/
Unsupported; same meaning).

Grounding Precision = Supported / Total facts, per explanation (single
combined score, same convention as the other two tonight).

Also computes the paper's own literal TNI/CCI/FTNF/CFTNF/FTNN/CFTNN
(Section 3.3 definitions, verified against the actual paper text this
session) side by side, to check for redundancy with grounding precision.
"""
import json
import re

RUN_DIR = "./cf_gnnexplainer_run_2026-08-10"
SURVEY_FILES = {
    "cora": f"{RUN_DIR}/survey_nodes/cora_survey_nodes.json",
    "products": f"{RUN_DIR}/survey_nodes/products_survey_nodes.json",
}

REMOVAL_WORDS = re.compile(
    r"\b(removed?|no longer|disconnect\w*|lost (the |its )?connection|severed?|eliminat\w*|"
    r"drop(?:ped)? the (?:edge|connection|link)|cut (?:the )?(?:edge|connection|link))\b",
    re.IGNORECASE,
)
ADDITION_WORDS = re.compile(
    r"\b(new edge|new connection|introduc\w+ (?:a |an |new )?(?:edge|connection|link)|"
    r"added? (?:a |an |new )?(?:edge|connection|link)|strengthen\w* the connection\w*|"
    r"gained (?:an |a )?(?:edge|connection|link))\b",
    re.IGNORECASE,
)
FEATURE_CHANGE_WORDS = re.compile(
    r"\b(features? (?:remain|stay|are)\s+(?:the same|unchanged)|"
    r"(?:lost|gained|changed|modified) (?:its |the )?features?|"
    r"features? (?:remain|stay|are) identical)\b",
    re.IGNORECASE,
)


def parse_field_int(text, field):
    # Field names are sometimes dict-key-quoted ('Target_Node_ID': 510) and
    # sometimes bare (Target_Node_ID = 510) -- inconsistently, even within
    # the same output. Tolerate an optional quote on either side of the key.
    m = re.search(rf"[\'\"]?{field}[\'\"]?\s*[=:]\s*[\'\"]?(\d+)[\'\"]?", text)
    return int(m.group(1)) if m else None


def parse_field_str(text, field):
    # `*` not `+`: an explicitly empty '' value (seen in real output, e.g.
    # node 510's Counterfactual_Target_Node_class: '') is itself a claim --
    # empty is not the same as "field never mentioned" and must be checked
    # (empty != a real non-empty class -> Contradicted), not silently
    # skipped as if no claim were made.
    m = re.search(rf"[\'\"]?{field}[\'\"]?\s*[=:]\s*[\'\"]([^\'\"]*)[\'\"]", text)
    if m:
        return m.group(1).strip()
    # Also accept an UNQUOTED value (seen in bullet-list-style output, e.g.
    # "- Factual_Target_Node_Class: Home & Kitchen" with no quotes at all)
    # -- read to end of line, strip a trailing "# comment" or list marker.
    m = re.search(rf"[\'\"]?{field}[\'\"]?\s*[=:]\s*([^\n#]+)", text)
    if m:
        val = m.group(1).strip().rstrip(",").strip()
        return val if val else None
    return None


def parse_field_list(text, field):
    m = re.search(rf"[\'\"]?{field}[\'\"]?\s*[=:]\s*\[([^\]]*)\]", text)
    if not m:
        return None
    inner = m.group(1).strip()
    if not inner:
        return set()
    items = re.findall(r"[\'\"]?([^,\'\"]+)[\'\"]?", inner)
    return {x.strip() for x in items if x.strip()}


def norm_class(s):
    if s is None:
        return None
    return s.strip().lower().replace(" ", "_").replace("-", "_")


def real_neighbor_set(csv_str):
    if not csv_str or not csv_str.strip():
        return set()
    return {int(x.strip()) for x in csv_str.split(",") if x.strip()}


def real_feature_set(csv_str):
    if not csv_str or not csv_str.strip():
        return set()
    return {x.strip().lower() for x in csv_str.split(",") if x.strip()}


def build_node_class_map(graph_desc_text):
    """Parse 'The node X ... is classified as Y' for every node in a
    factual/counterfactual graph-description block -> {node_id: class}."""
    out = {}
    for m in re.finditer(r"[Tt]he node (\d+)\b.*?it is classified as (\w+)", graph_desc_text, re.DOTALL):
        nid, cls = int(m.group(1)), m.group(2)
        # DOTALL greedy risk: keep only the *nearest* match span, re.finditer
        # with non-greedy .*? already prevents cross-node bleed since the
        # next "The node" starts a fresh sentence boundary before it.
        out[nid] = cls
    return out


def check_dict_fields(node_id, ft, raw_output):
    """Type A: 7 structured-dict-field facts."""
    facts = []

    llm_tid = parse_field_int(raw_output, "Target_Node_ID")
    if llm_tid is not None:
        facts.append({"type": "target_node_id", "claimed": llm_tid, "real": node_id,
                       "supported": llm_tid == node_id})

    llm_fc = parse_field_str(raw_output, "Factual_Target_Node_Class")
    real_fc = ft["Factual_Target_Node_Class"]
    if llm_fc is not None:
        facts.append({"type": "factual_class", "claimed": llm_fc, "real": real_fc,
                       "supported": norm_class(llm_fc) == norm_class(real_fc)})

    llm_cc = parse_field_str(raw_output, "Counterfactual_Target_Node_class")
    if llm_cc is None:
        llm_cc = parse_field_str(raw_output, "Counterfactual_Target_Node_Class")
    real_cc = ft["Counterfactual_Target_Node_class"]
    if llm_cc is not None:
        facts.append({"type": "counterfactual_class", "claimed": llm_cc, "real": real_cc,
                       "supported": norm_class(llm_cc) == norm_class(real_cc)})

    llm_fn = parse_field_list(raw_output, "Factual_Target_Node_Neighbors")
    real_fn = real_neighbor_set(ft["Factual_Target_Node_Neighbors"])
    if llm_fn is not None:
        llm_fn_int = {int(x) for x in llm_fn if str(x).strip().lstrip("-").isdigit()}
        facts.append({"type": "factual_neighbors", "claimed": sorted(llm_fn_int), "real": sorted(real_fn),
                       "supported": llm_fn_int == real_fn})

    llm_cn = parse_field_list(raw_output, "Counterfactual_Target_Node_Neighbors")
    real_cn = real_neighbor_set(ft["Counterfactual_Target_Node_Neighbors"])
    if llm_cn is not None:
        llm_cn_int = {int(x) for x in llm_cn if str(x).strip().lstrip("-").isdigit()}
        facts.append({"type": "counterfactual_neighbors", "claimed": sorted(llm_cn_int), "real": sorted(real_cn),
                       "supported": llm_cn_int == real_cn})

    llm_ff = parse_field_list(raw_output, "Factual_Target_Node_Features")
    real_ff = real_feature_set(ft["Factual_Target_Node_Features"])
    if llm_ff is not None:
        llm_ff_norm = {x.strip().lower() for x in llm_ff}
        facts.append({"type": "factual_features", "claimed": sorted(llm_ff_norm), "real": sorted(real_ff),
                       "supported": llm_ff_norm == real_ff})

    llm_cf = parse_field_list(raw_output, "Counterfactual_Target_Node_Features")
    real_cf = real_feature_set(ft["Counterfactual_Target_Node_Features"])
    if llm_cf is not None:
        llm_cf_norm = {x.strip().lower() for x in llm_cf}
        facts.append({"type": "counterfactual_features", "claimed": sorted(llm_cf_norm), "real": sorted(real_cf),
                       "supported": llm_cf_norm == real_cf})

    return facts


def check_prose_claims(node_id, entry, raw_output):
    """Type B: free-text explanation claims (B1 node-class, B2 edge-change, B3 feature-change)."""
    facts = []
    removed_edges = entry["removed_edges_global"]
    removed_pairs = {tuple(sorted(p)) for p in removed_edges}
    real_removed_neighbor_ids = {n for pair in removed_edges for n in pair if n != node_id}
    also_removed_between_others = {tuple(sorted(p)) for p in removed_edges if node_id not in p}

    factual_class_map = build_node_class_map(entry["factual_graph_description"])
    cf_class_map = build_node_class_map(entry["counterfactual_graph_description"])

    # --- B1: node <id> ... classified as <X> ---
    for m in re.finditer(r"\bnode[s]?\s+(\d+)\b[^.]*?\bclassified as\s+([A-Za-z_& ]+?)[.,;\n]", raw_output, re.IGNORECASE):
        nid, cls = int(m.group(1)), m.group(2).strip()
        if nid == node_id:
            continue  # target's own class already covered by Type A
        real_here = factual_class_map.get(nid) or cf_class_map.get(nid)
        if real_here is None:
            continue  # node not in this subgraph at all -- can't verify, skip rather than guess
        facts.append({
            "type": "node_class_claim", "node": nid, "claimed_class": cls, "real_class": real_here,
            "sentence": raw_output[max(0, m.start() - 60):m.end()],
            "supported": norm_class(cls) == norm_class(real_here),
        })

    # --- B2: edge-change language ---
    seen_sentences = set()
    for sent in re.split(r"(?<=[.!?])\s+", raw_output):
        ids_in_sent = [int(x) for x in re.findall(r"\b(\d{1,6})\b", sent)]
        ids_in_sent = [i for i in ids_in_sent if i in factual_class_map or i in cf_class_map or i == node_id]
        if len(ids_in_sent) < 2:
            continue
        removal_hit = REMOVAL_WORDS.search(sent)
        addition_hit = ADDITION_WORDS.search(sent)
        if not removal_hit and not addition_hit:
            continue
        key = sent.strip()
        if key in seen_sentences:
            continue
        seen_sentences.add(key)
        # does any pair of mentioned ids correspond to a real removed edge?
        pairs_mentioned = {tuple(sorted((a, b))) for i, a in enumerate(ids_in_sent) for b in ids_in_sent[i + 1:]}
        real_hit = bool(pairs_mentioned & removed_pairs)
        if addition_hit:
            supported = False  # method only ever deletes edges -- any addition claim is false by construction
        else:
            supported = real_hit
        facts.append({
            "type": "edge_change_claim", "ids_mentioned": ids_in_sent,
            "addition_language": bool(addition_hit), "removal_language": bool(removal_hit),
            "matches_real_removed_edge": real_hit, "sentence": sent.strip(),
            "supported": supported,
        })

    # --- B3: target's own feature-change assertions ---
    for m in FEATURE_CHANGE_WORDS.finditer(raw_output):
        sent_start = raw_output.rfind(".", 0, m.start()) + 1
        sent_end = raw_output.find(".", m.end())
        sent = raw_output[sent_start: sent_end if sent_end != -1 else len(raw_output)].strip()
        claims_changed = bool(re.search(r"\b(lost|gained|changed|modified)\b", m.group(0), re.IGNORECASE))
        # CF-GNNExplainer never perturbs features -- real answer is always "unchanged"
        supported = not claims_changed
        facts.append({
            "type": "target_feature_change_claim", "sentence": sent,
            "claims_changed": claims_changed, "supported": supported,
        })

    # --- B5: "no classification change" claim (the complement of B4 --
    # some outputs never state a from/to transition and instead assert
    # nothing changed at all, e.g. node 1852: "there is no change in
    # classification for the target node"). Checkable against whether the
    # real factual and counterfactual classes actually differ.
    no_change_re = re.compile(
        r"(no change in classification|classification .{0,40}remains? (?:the same|unchanged)|"
        r"remains? classified as [A-Za-z_ ]+ in both)",
        re.IGNORECASE,
    )
    real_fc = entry["factual_target_dict"]["Factual_Target_Node_Class"]
    real_cc = entry["factual_target_dict"]["Counterfactual_Target_Node_class"]
    seen_no_change = False
    for m in no_change_re.finditer(raw_output):
        if seen_no_change:
            continue
        seen_no_change = True
        sent_start = raw_output.rfind(".", 0, m.start()) + 1
        sent_end = raw_output.find(".", m.end())
        sent = raw_output[sent_start: sent_end if sent_end != -1 else len(raw_output)].strip()
        facts.append({
            "type": "no_classification_change_claim", "sentence": sent,
            "real_factual_class": real_fc, "real_counterfactual_class": real_cc,
            # A "no change" claim is only true if the real classes are
            # actually identical; here they never are, by construction,
            # for every node CF-GNNExplainer found a counterfactual for
            # (a found counterfactual means the class DID flip).
            "supported": norm_class(real_fc) == norm_class(real_cc),
        })

    # --- B4: "classification changed from <X> to <Y>" narrative for the
    # TARGET's own transition -- distinct from the structured dict-field
    # claims (Type A), since the model sometimes states one thing in prose
    # and a different, contradictory thing in its own infos={} block (seen
    # on node 1062: prose correctly says "from Neural_Networks to Theory",
    # the infos dict wrongly says Factual class is 'Theory' too) -- both
    # are separately checkable claims and are scored independently.
    seen_transitions = set()
    for m in re.finditer(
        r"classif(?:ication|ied)[^.]*?\bfrom\s+([A-Za-z_][A-Za-z_ ]*?)\s+to\s+([A-Za-z_][A-Za-z_ ]*?)[.,;\n]",
        raw_output,
    ):
        claimed_from, claimed_to = m.group(1).strip(), m.group(2).strip()
        # The model frequently repeats the identical explanation sentence
        # verbatim (once in prose, again inside its own infos={} dict) --
        # dedupe identical (from,to) pairs so a repeated sentence doesn't
        # inflate the fact count (mirrors the B2 seen_sentences dedup).
        key = (norm_class(claimed_from), norm_class(claimed_to))
        if key in seen_transitions:
            continue
        seen_transitions.add(key)
        real_from = entry["factual_target_dict"]["Factual_Target_Node_Class"]
        real_to = entry["factual_target_dict"]["Counterfactual_Target_Node_class"]
        facts.append({
            "type": "target_class_transition_claim",
            "claimed_from": claimed_from, "claimed_to": claimed_to,
            "real_from": real_from, "real_to": real_to,
            "sentence": raw_output[max(0, m.start() - 40):m.end()],
            "supported": norm_class(claimed_from) == norm_class(real_from) and norm_class(claimed_to) == norm_class(real_to),
        })

    return facts


def paper_metrics(node_id, ft, raw_output):
    """Literal TNI/CCI/FTNF/CFTNF/FTNN/CFTNN, Section 3.3 definitions (verified
    against the actual paper text: exact match between the LLM's stated
    value and the real value, 0/1 each)."""
    llm_tid = parse_field_int(raw_output, "Target_Node_ID")
    tni = int(llm_tid == node_id) if llm_tid is not None else 0

    llm_cc = parse_field_str(raw_output, "Counterfactual_Target_Node_class")
    if llm_cc is None:
        llm_cc = parse_field_str(raw_output, "Counterfactual_Target_Node_Class")
    cci = int(norm_class(llm_cc) == norm_class(ft["Counterfactual_Target_Node_class"])) if llm_cc is not None else 0

    llm_ff = parse_field_list(raw_output, "Factual_Target_Node_Features")
    real_ff = real_feature_set(ft["Factual_Target_Node_Features"])
    ftnf = int({x.lower() for x in llm_ff} == real_ff) if llm_ff is not None else 0

    llm_cf = parse_field_list(raw_output, "Counterfactual_Target_Node_Features")
    real_cf = real_feature_set(ft["Counterfactual_Target_Node_Features"])
    cftnf = int({x.lower() for x in llm_cf} == real_cf) if llm_cf is not None else 0

    llm_fn = parse_field_list(raw_output, "Factual_Target_Node_Neighbors")
    real_fn = real_neighbor_set(ft["Factual_Target_Node_Neighbors"])
    ftnn = int({int(x) for x in llm_fn if str(x).strip().lstrip('-').isdigit()} == real_fn) if llm_fn is not None else 0

    llm_cn = parse_field_list(raw_output, "Counterfactual_Target_Node_Neighbors")
    real_cn = real_neighbor_set(ft["Counterfactual_Target_Node_Neighbors"])
    cftnn = int({int(x) for x in llm_cn if str(x).strip().lstrip('-').isdigit()} == real_cn) if llm_cn is not None else 0

    return {"TNI": tni, "CCI": cci, "FTNF": ftnf, "CFTNF": cftnf, "FTNN": ftnn, "CFTNN": cftnn}


def main():
    results = {}
    for ds, path in SURVEY_FILES.items():
        entries = json.load(open(path))
        for entry in entries:
            node_id = entry["node_id"]
            if entry["status"] != "llm_generated":
                results[str(node_id)] = {"dataset": ds, "node_id": node_id, "status": entry["status"]}
                continue
            ft = entry["factual_target_dict"]
            raw = entry["llm_raw_output"]

            type_a = check_dict_fields(node_id, ft, raw)
            type_b = check_prose_claims(node_id, entry, raw)
            all_facts = type_a + type_b
            n_supported = sum(1 for f in all_facts if f["supported"])

            results[str(node_id)] = {
                "dataset": ds,
                "node_id": node_id,
                "status": "checked",
                "n_facts": len(all_facts),
                "n_supported": n_supported,
                "grounding_precision": (n_supported / len(all_facts)) if all_facts else None,
                "n_dict_field_facts": len(type_a),
                "n_prose_claim_facts": len(type_b),
                "paper_metrics": paper_metrics(node_id, ft, raw),
                "facts": all_facts,
            }

    out_path = f"{RUN_DIR}/grounding_precision_rulebased/cf_gnnexplainer_grounding_precision_RULEBASED.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved -> {out_path}\n")

    for node_id, r in results.items():
        if r["status"] != "checked":
            print(f"node {node_id} ({r['dataset']}): {r['status']}")
            continue
        pm = r["paper_metrics"]
        gp_str = f"{r['grounding_precision']:.3f}" if r["grounding_precision"] is not None else "n/a (0 facts)"
        print(f"node {node_id} ({r['dataset']}): {r['n_supported']}/{r['n_facts']} = {gp_str}  "
              f"| paper metrics: TNI={pm['TNI']} CCI={pm['CCI']} FTNF={pm['FTNF']} CFTNF={pm['CFTNF']} FTNN={pm['FTNN']} CFTNN={pm['CFTNN']} "
              f"(mean={sum(pm.values())/6:.3f})")


if __name__ == "__main__":
    main()
