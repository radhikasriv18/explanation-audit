"""
Phase 1 v3 post-processing (no model call). Reads extractions_v3/<id>.json and writes
cleaned_v3/<id>.json + cleanup_log_v3.csv + span_check_failures_v3.csv.

Step 0  span check: every claim's source_span must appear verbatim in the input text after
        collapsing whitespace (only whitespace is normalized; case, punctuation and spelling
        must match). Empty/missing spans fail. Failures get span_check="fail" and
        unsupported_extraction=True. Failing claims are NOT removed; they go to the sheet.
Step 1  relabel by subject (logged):
        - subject is a neighbor (any Node-X / Node-X.Y / "Nodes 8 to 10", a numeric node id other
          than the target, "the neighbor nodes", "its/the (direct|2-hop) neighbors") and type is
          content / feature / class_state -> neighbor. structural, importance and mechanism are
          kept, because those types describe WHAT is claimed (a connection, a score, a causal
          effect), whoever the subject is.
        - subject is the target (ROOT, "the target node/paper/product", "node <target>") and
          type is neighbor -> content.
        - invalid type naming the Natural_Language_Explanation field -> mechanism.
Step 2  drop evaluation-only claims (logged): the claim matches an evaluative/hedge pattern
        (causal verbs such as affect/influence/contribute are NOT treated as evaluative)
        AND names nothing checkable besides its subject (no feature words, titles, classes,
        edges, other node ids, numbers, rank words, or a factual predicate such as
        discusses / contains / mentions / is linked to). Mixed fact+evaluation claims are kept.
Step 3  CF merge (logged, CF-GNNExplainer only): a prose claim is merged into an infos-field
        claim (one whose text/span names a field) when both name the same entity set
        (node ids other than the target, feature words, classes). The field's set is parsed
        from the field claim's own source_span value (fallback: its entities). Empty-set
        prose is matched only by an explicit rule (lost/no connections -> an empty
        *_Neighbors field; no features changed -> an empty Features_Changed field;
        "target node is N" -> Target_Node_ID). Ties between Factual_* and Counterfactual_*
        go to Counterfactual_* only if the prose says "counterfactual". Any remaining tie is
        logged as ambiguous and not merged. Guards (added after reviewing the first log):
        Natural_Language_Explanation is never a merge target; the prose claim's type must fit
        the field (Neighbors/ID -> structural, Features -> feature, Class -> class_state);
        prose with causal/explanatory wording (influence, affect, suggest, because, ...) or
        naming another dict key (Edge_Differences, Node_Differences) is never merged.
GraphNarrator target alias: GraphNarrator verbalizes the target as local node 0, so a claim
whose subject is "Node 0" is a target claim (ROOT is already handled).
span_check_failures_v3.csv also gives a diagnostic cause per failure (markdown-only,
punctuation/case/quotes-only, or words not in text); the pass/fail rule itself is unchanged.
"""
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
IN_DIR = HERE / "extractions_v3"
OUT_DIR = HERE / "cleaned_v3"
CLAIM_TYPES = ["content", "structural", "importance", "class_state", "mechanism", "feature", "neighbor"]

FIELD_NAMES = [
    "Target_Node_Features_Changed_From_Factual_To_Counterfactual",
    "Counterfactual_Target_Node_Neighbors",
    "Counterfactual_Target_Node_Features",
    "Counterfactual_Target_Node_class",
    "Factual_Target_Node_Neighbors",
    "Factual_Target_Node_Features",
    "Factual_Target_Node_Class",
    "Natural_Language_Explanation",
    "Target_Node_ID",
]
FIELD_RE = re.compile("|".join(FIELD_NAMES).replace("_class", "_[Cc]lass").replace("_Class", "_[Cc]lass"), re.I)

EVAL_RE = re.compile(
    r"\b(crucial|essential|vital|key role|critical|significant(ly)?|minimal|well[- ]supported|"
    r"support(s|ed|ing)?|reinforc\w*|strengthen\w*|adds? weight|relevan\w*|"
    r"indicat\w*|suggest\w*|reflect\w*|highlight\w*|emphasi[sz]\w* the importance|consistent with|credib\w*|"
    r"likely|may|might|could|possibly|appears? to|seems?|"
    r"important|influential|strong(ly)?|plays? an? \w+ role|valuable|insight\w*)\b",
    re.I,
)
# a factual predicate means the claim states something checkable even if it also evaluates it
FACT_PRED_RE = re.compile(
    r"\b(discuss\w*|contain\w*|mention\w*|touch\w* on|focus\w* on|address\w*|references?|cites?|"
    r"is (titled|about|linked to|connected to|classified as)|are (linked|connected) to|has (further )?connections|"
    r"connections? to|links? to|belongs? to)\b",
    re.I,
)
RANK_RE = re.compile(r"\b(most|least|highest|lowest|top|second|third|rank\w*|first)\b|\d", re.I)


def norm_ws(s):
    return re.sub(r"\s+", " ", s or "").strip()


def norm_class(s):
    return re.sub(r"[^a-z0-9]+", "_", str(s).lower()).strip("_")


def ints_in(s):
    return {m for m in re.findall(r"(?<![\w.-])\d+(?![\w.])", s or "")}


def span_fail_cause(span, text):
    """Diagnostic only; does not change pass/fail."""
    if not span or not norm_ws(span):
        return "empty span"
    md = lambda x: norm_ws(re.sub(r"[*_`#]", "", x))
    lo = lambda x: re.sub(r"[^a-z0-9]+", " ", x.lower()).strip()
    if md(span) in md(text):
        return "markdown only (** removed)"
    if lo(span) in lo(text):
        return "punctuation/case/quotes only"
    return "words not in text (paraphrase/merge/invented)"


# ---------------------------------------------------------------- subject detection
def subject_kind(claim, target, target_aliases=()):
    c = claim.strip()
    c_l = re.sub(r"^(the|a|an)\s+", "", c, flags=re.I)
    if re.match(r"(root\b|target\b|this (paper|product)\b)", c_l, re.I):
        return "target", set()
    for a in target_aliases:
        if re.match(re.escape(a) + r"(?![\d.])", c_l, re.I):
            return "target", set()
    m = re.match(r"node\s*-?\s*(\d+)\b(?!\.\d)", c_l, re.I)
    if m and not re.match(r"node-", c_l, re.I):
        return ("target", set()) if m.group(1) == str(target) else ("neighbor", {m.group(1)})
    if re.match(r"nodes?-\d+(\.\d+)?", c_l, re.I):
        return "neighbor", set(re.findall(r"(?<=node-)\d+(?:\.\d+)?", c_l[:40], re.I))
    m = re.match(r"nodes\s+(\d+(?:\.\d+)?(?:\s*(?:,|and|to|-|through)\s*(?:node-?\s*)?\d+(?:\.\d+)?)+)", c_l, re.I)
    if m:
        ids = set(re.findall(r"\d+(?:\.\d+)?", m.group(1)))
        return ("target", set()) if ids == {str(target)} else ("neighbor", ids - {str(target)})
    if re.match(r"(its|their)?\s*(direct\s+|1-hop\s+|2-hop\s+|first-hop\s+|second-hop\s+)*(neighbou?r(ing)?\s+(nodes?|papers?|products?)|neighbou?rs)\b", c_l, re.I):
        ids = set(re.findall(r"\b\d+\b", c_l[:80])) - {str(target)}
        return "neighbor", ids
    return "other", set()


# ---------------------------------------------------------------- entity sets for merge
def claim_entity_set(c, target):
    e = c["entities"]
    s = set()
    for x in e.get("node_ids", []) + [y for pair in e.get("edges", []) if isinstance(pair, list) for y in pair]:
        if re.fullmatch(r"\d+", str(x).strip()):
            s.add(str(x).strip())
    s |= ints_in(c["claim"])
    s.discard(str(target))
    s |= {f"w:{str(w).strip().lower()}" for w in e.get("feature_words", []) if str(w).strip()}
    s |= {f"c:{norm_class(k)}" for k in e.get("classes", []) if str(k).strip()}
    return frozenset(s)


def field_of(c):
    text = (c.get("source_span") or "") + " " + c["claim"]
    m = FIELD_RE.search(text)
    if not m:
        return None
    name = m.group(0)
    for f in FIELD_NAMES:
        if f.lower() == name.lower():
            return f
    return None


def field_value_set(c, field, target):
    """Parse the field's value from its source_span (e.g. 'Factual_Target_Node_Neighbors: [192, 356]')."""
    span = c.get("source_span") or ""
    m = re.search(re.escape(field).replace("_class", "_[Cc]lass").replace("_Class", "_[Cc]lass") + r"['\"]?\s*[:=]\s*(.*)", span, re.I | re.S)
    if not m:
        return claim_entity_set(c, target), "entities"
    val = re.sub(r"\s*#.*$", "", m.group(1).strip().split("\n")[0]).strip().rstrip(",")
    if field == "Target_Node_ID":
        return frozenset(), "span"
    if field == "Natural_Language_Explanation":
        return None, "span"
    if val.startswith("["):
        items = [x.strip().strip("'\"") for x in val.strip("[]").split(",") if x.strip().strip("'\"")]
        if "Neighbors" in field:
            return frozenset(x for x in items if re.fullmatch(r"\d+", x)) - {str(target)}, "span"
        return frozenset(f"w:{x.lower()}" for x in items), "span"
    v = val.strip("'\" ")
    if "lass" in field:
        return (frozenset({f"c:{norm_class(v)}"}) if v else frozenset()), "span"
    return claim_entity_set(c, target), "entities"


# a prose claim is only a restatement if it states the field's fact, not a causal or explanatory claim about it
MERGE_BLOCK_RE = re.compile(r"\b(influenc\w*|affect\w*|impact\w*|suggest\w*|explanation|leading to|because|due to|caus\w*)\b", re.I)
OTHER_KEY_RE = re.compile(r"\b(Edge_Differences|Node_Differences)\b")
FIELD_COMPAT = {"neighbors": {"structural"}, "id": {"structural", "content"}, "features": {"feature"}, "class": {"class_state"}}


def field_family(f):
    if "Neighbors" in f:
        return "neighbors"
    if f == "Target_Node_ID":
        return "id"
    if "Features" in f:
        return "features"
    return "class"


EMPTY_NEIGH_RE = re.compile(r"\b(lost|no|not|none|any|empty|isolated|without)\b.*\b(connect\w*|neighbou?r\w*|edges?)\b|\b(connect\w*|neighbou?r\w*)\b.*\b(empty|none)\b", re.I)
EMPTY_FEAT_RE = re.compile(r"\b(no|not|none|empty|unchanged|did not change|remain\w* the same)\b.*\bfeature|\bfeature\w*.*\b(no|not|none|empty|unchanged|same)\b", re.I)
ID_RE = re.compile(r"\btarget node (id )?is (node )?\d+\s*\.?$", re.I)


def merge_candidates(prose, pset, fields, target):
    text = prose["claim"]
    if pset:
        cands = [f for f in fields if f["set"] is not None and f["set"] == pset]
    else:
        if ID_RE.search(text):
            cands = [f for f in fields if f["field"] == "Target_Node_ID"]
        elif EMPTY_FEAT_RE.search(text):
            cands = [f for f in fields if f["field"] == "Target_Node_Features_Changed_From_Factual_To_Counterfactual" and f["set"] == frozenset()]
        elif EMPTY_NEIGH_RE.search(text):
            cands = [f for f in fields if "Neighbors" in f["field"] and f["set"] == frozenset()]
        else:
            cands = []
    if len({f["field"] for f in cands}) > 1:
        want_cf = bool(re.search(r"counterfactual", text, re.I))
        pref = [f for f in cands if f["field"].startswith("Counterfactual") == want_cf and f["field"] != "Target_Node_Features_Changed_From_Factual_To_Counterfactual"]
        if len({f["field"] for f in pref}) == 1:
            cands = pref
    return cands


def process(rec):
    target = rec["node"]
    text = rec["input_text"]
    ntext = norm_ws(text)
    log = []
    claims = [dict(c) for c in rec["claims"]]
    # GraphNarrator verbalizes the target as local node 0 ("Node 0" in Products prose, ROOT in Cora)
    aliases = ("Node 0", "Node-0") if rec["method"] == "GraphNarrator" else ()

    # Step 0 span check
    for i, c in enumerate(claims):
        c["extraction_index"] = i + 1
        c["extracted_type"] = c["claim_type"]
        span = c.get("source_span")
        ok = bool(span and norm_ws(span)) and norm_ws(span) in ntext
        c["span_check"] = "pass" if ok else "fail"
        c["unsupported_extraction"] = not ok
        if not ok:
            log.append({"action": "span_check_fail", "claim_index": i + 1, "claim": c["claim"], "detail": f"source_span={span!r}"})

    # Step 1 relabel by subject
    for c in claims:
        kind, _ = subject_kind(c["claim"], target, aliases)
        old = c["claim_type"]
        new = old
        if old not in CLAIM_TYPES and re.search(r"natural_language_explanation", old + c["claim"], re.I):
            new = "mechanism"
        elif kind == "neighbor" and old in ("content", "feature", "class_state"):
            new = "neighbor"
        elif kind == "target" and old == "neighbor":
            new = "content"
        if new != old:
            c["claim_type"] = new
            log.append({"action": "relabel", "claim_index": c["extraction_index"], "claim": c["claim"], "detail": f"{old} -> {new} (subject={kind})"})

    # Step 2 drop evaluation-only
    kept = []
    for c in claims:
        kind, subj_ids = subject_kind(c["claim"], target, aliases)
        e = c["entities"]
        other_nodes = {re.sub(r"^node-?\s*", "", str(x).strip(), flags=re.I) for x in e.get("node_ids", [])}
        other_nodes -= subj_ids | {str(target), "ROOT", "root", ""} | ({"0"} if aliases else set())
        claim_wo_subject = re.sub(r"^(the\s+)?(node-?\s*\d+(\.\d+)?|nodes\s+[\d.,\s]+(and|to)\s+[\d.]+|root( node)?|target node)", "", c["claim"], flags=re.I)
        residue = bool(e.get("feature_words") or e.get("titles") or e.get("classes") or e.get("edges") or other_nodes or RANK_RE.search(claim_wo_subject) or FACT_PRED_RE.search(claim_wo_subject))
        m = EVAL_RE.search(c["claim"])
        if m and not residue and field_of(c) is None:
            log.append({"action": "drop_evaluation_only", "claim_index": c["extraction_index"], "claim": c["claim"], "detail": f"matched {m.group(0)!r}; no checkable entity besides subject"})
            continue
        kept.append(c)
    claims = kept

    # Step 3 CF prose -> infos field merge
    if rec["method"] == "CF-GNNExplainer":
        fields = []
        for c in claims:
            f = field_of(c)
            if f:
                s, how = field_value_set(c, f, target)
                c["infos_field"] = f
                if f != "Natural_Language_Explanation":  # free-text field: never a merge target
                    fields.append({"field": f, "set": s, "claim": c, "parsed_from": how})
        kept = []
        for c in claims:
            if c.get("infos_field"):
                kept.append(c)
                continue
            pset = claim_entity_set(c, target)
            blocker = MERGE_BLOCK_RE.search(c["claim"]) or OTHER_KEY_RE.search(c["claim"] + " " + (c.get("source_span") or ""))
            if blocker:
                kept.append(c)
                continue
            cands = [f for f in merge_candidates(c, pset, fields, target) if c["claim_type"] in FIELD_COMPAT[field_family(f["field"])]]
            if not cands:
                kept.append(c)
                continue
            if len({f["field"] for f in cands}) > 1:
                log.append({"action": "merge_ambiguous_kept", "claim_index": c["extraction_index"], "claim": c["claim"], "detail": f"candidate fields {sorted({f['field'] for f in cands})}"})
                kept.append(c)
                continue
            tgt = cands[0]
            tgt["claim"].setdefault("merged_from", []).append({"extraction_index": c["extraction_index"], "claim": c["claim"], "source_span": c.get("source_span"), "span_check": c["span_check"]})
            log.append(
                {
                    "action": "merge_into_field",
                    "claim_index": c["extraction_index"],
                    "claim": c["claim"],
                    "detail": f"-> {tgt['field']} (claim {tgt['claim']['extraction_index']}); entity set {sorted(pset) or '{} (rule)'}; field set parsed from {tgt['parsed_from']}",
                }
            )
        claims = kept

    return claims, log


def main():
    OUT_DIR.mkdir(exist_ok=True)
    order = [e["id"] for e in json.load(open(HERE / "answer_key_texts.json"))]
    all_log, fails, summary = [], [], []
    for rid in order:
        rec = json.load(open(IN_DIR / f"{rid}.json"))
        final, log = process(rec)
        extracted = rec["claims"]
        n_fail = sum(1 for l in log if l["action"] == "span_check_fail")
        out = {
            "id": rid,
            "method": rec["method"],
            "dataset": rec["dataset"],
            "node": rec["node"],
            "source_file": rec["source_file"],
            "n_extracted": len(extracted),
            "n_final": len(final),
            "n_span_fail_extracted": n_fail,
            "n_span_fail_final": sum(c["span_check"] == "fail" for c in final),
            "claims_final": final,
            "cleanup_log": log,
        }
        json.dump(out, open(OUT_DIR / f"{rid}.json", "w"), indent=1)
        for l in log:
            all_log.append({"id": rid, **l})
            if l["action"] == "span_check_fail":
                c = rec["claims"][l["claim_index"] - 1]
                final_ids = {x["extraction_index"] for x in final}
                fate = "kept" if l["claim_index"] in final_ids else next((x["action"] for x in log if x["claim_index"] == l["claim_index"] and x["action"] != "span_check_fail"), "?")
                fails.append(
                    {
                        "claim_id": f"{rid}_c{l['claim_index']:02d}",
                        "cause": span_fail_cause(c.get("source_span"), rec["input_text"]),
                        "in_final_csv": fate,
                        "claim": c["claim"],
                        "source_span": c.get("source_span", ""),
                    }
                )
        summary.append(out)
        acts = {}
        for l in log:
            acts[l["action"]] = acts.get(l["action"], 0) + 1
        print(f"{rid:32s} extracted={len(extracted):3d} final={len(final):3d} span_fail={n_fail:2d} {acts}")
    with open(HERE / "cleanup_log_v3.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "action", "claim_index", "claim", "detail"])
        w.writeheader()
        w.writerows(all_log)
    with open(HERE / "span_check_failures_v3.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["claim_id", "cause", "in_final_csv", "claim", "source_span"])
        w.writeheader()
        w.writerows(fails)


if __name__ == "__main__":
    main()
