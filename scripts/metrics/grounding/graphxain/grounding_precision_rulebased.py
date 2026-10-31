"""
RULE-BASED grounding precision for GraphXAIN's survey-node narratives, adapted
from GraphNarrator's grounding_precision_rulebased.py methodology (same repo,
same date convention) to GraphXAIN's structurally different output:

  - GraphNarrator's Free-Text Explanation is a markdown hierarchy with one
    claim line per node key (ROOT, Node-1, Node-1.1, ...) and explicit
    "word" (score) citations -> trivial to decompose into atomic per-node facts.
  - GraphXAIN's narrative is free-flowing prose with NO structural per-node
    breakdown and (per its own prompt rule 6) is explicitly told NOT to quote
    raw importance scores -- so there is nothing to parse into a fixed
    node-key -> claim mapping, and no numeric score to check for plausibility.

Adapted atomic-fact model for GraphXAIN, mirroring the SAME underlying
principle (word existence is the primary criterion; a secondary "concrete
value" check is tracked but folded into one verdict per the task spec, not
kept as a side channel like GraphNarrator's score_plausible):

  1. FEATURE claims: every single-word quote in the narrative ('word' or
     "word") that isn't a fragment of the predicted-class label. Checked via
     Porter-stemmed match against the real top-7 GNNExplainer feature words
     actually fed into that node's prompt (gnnexplainer_top_features).
       existence: does the (stemmed) word appear in the real top-7 set at all?
       value accuracy: if the sentence containing the citation makes an
       explicit presence/absence claim ("absent", "present", "mentioned",
       "does not appear", ...), does it match the real `present` flag for
       that word? A citation that exists but asserts the wrong
       presence/absence is marked Unsupported (this is the "concrete value"
       check the task asks for -- GraphXAIN has no importance number to
       check instead, since its own prompt forbids quoting one).
  2. NEIGHBOR claims: every explicit "Node <id>" citation, and every
     multi-word quoted or Title-Case phrase (a paraphrased/verbatim neighbor
     title), checked against the real 1-hop+2-hop neighbor set actually fed
     into that node's prompt (gnnexplainer_1hop_neighbors +
     gnnexplainer_2hop_neighbors: node id, class, text snippet).
       Node-ID citations: exact id lookup, plus (if present) a class claim
       ("belongs ... to the X class") checked against the real neighbor's
       class field.
       Title citations: token-overlap match against every given neighbor's
       real text snippet (>=3 shared significant tokens, or a normalized
       substring match) -- if no given neighbor matches at all, the neighbor
       is fabricated / pulled from outside the given subgraph (mirrors
       GraphNarrator's "panstik" pretrained-knowledge-leak finding).

INTERPRETIVE LANGUAGE (rule 5 of GraphXAIN's own prompt explicitly instructs
"interpret WHY a feature or connection pushed the prediction in a certain
direction" -- this is by-design behavior, not a factual claim): sentences
containing hedge/causal-gloss markers (suggests, indicates, reveals, likely,
reinforces, further solidifies, ...) are tagged `interpretive_sentence: true`
on any fact extracted from them (still checked and counted -- the underlying
named claim is checkable even if wrapped in interpretive framing) AND listed
separately as "interpretive_passages" for any sentence that carries NO
checkable named citation at all (pure connective/causal narration) -- these
are excluded from the fact count entirely, consistent with
"Total factual (non-interpretive) claims" in the denominator.

Grounding Precision = Supported facts / Total facts, per explanation (single
combined count -- no GraphNarrator-style separate word/score split).
"""
import json
import re
from pathlib import Path

from nltk.stem import PorterStemmer

ps = PorterStemmer()

SURVEY_JSONL = {
    "cora": "./graphxain_survey_corrected_2026-08-07/cora/explainer_and_prompts.jsonl",
    "products_6813_1852": "./graphxain_survey_corrected_2026-08-07/products_6813_1852/explainer_and_prompts.jsonl",
    "products_8766_8438": "./graphxain_survey_corrected_2026-08-07/products_8766_8438/explainer_and_prompts.jsonl",
}

OUT_DIR = Path("./graphxain_survey_corrected_2026-08-07/grounding_precision_rulebased")

INTERPRETIVE_MARKERS = [
    "suggest", "indicat", "impli", "reveal", "likely", " may ", " might ",
    " could ", "presum", "underscor", "reinforc", "solidif", "strengthen",
    "which explains", "this interpretation", "demonstrat", "consistent with",
    "convincing case", "credibility", "nuanced understanding",
    "deep understanding", "reflect", "steered", "telling clue",
]

PRESENCE_MARKERS = ["present in", "presence of", "mentioned within", "is indeed mentioned",
                     "indeed present", "does appear", "found in the", "appears in the"]
ABSENCE_MARKERS = ["absent", "not present", "not mentioned", "does not appear",
                    "missing from", "lacking", "despite being absent"]

STOPWORD_QUOTE = {"beauty", "theory", "neural", "networks", "genetic", "algorithms",
                   "health", "personal", "care", "office", "products", "electronics"}


def sentences(text):
    text = text.replace("\n", " ")
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def is_interpretive(sentence):
    low = sentence.lower()
    return any(m in low for m in INTERPRETIVE_MARKERS)


def sentence_for_offset(text, offset, sents_with_spans):
    for s, start, end in sents_with_spans:
        if start <= offset < end:
            return s
    return text


def spans(text, sents):
    out = []
    pos = 0
    for s in sents:
        start = text.find(s, pos)
        if start == -1:
            start = pos
        end = start + len(s)
        out.append((s, start, end))
        pos = end
    return out


def normalize_tokens(s):
    return {ps.stem(w.lower()) for w in re.findall(r"[A-Za-z]{3,}", s)}


def extract_feature_facts(narrative, real_feats, predicted_class):
    """real_feats: list of {word, importance, present} -- the real top-7 fed to the prompt."""
    real_by_stem = {}
    for r in real_feats:
        real_by_stem.setdefault(ps.stem(r["word"].lower()), []).append(r)

    class_words = {w.lower() for w in re.findall(r"[A-Za-z]+", predicted_class)}

    sents = sentences(narrative)
    sent_spans = spans(narrative, sents)

    facts = []
    seen_positions = set()
    for m in re.finditer(r"[\"']([A-Za-z][A-Za-z\-]{1,20})[,.;:]?[\"']", narrative):
        word = m.group(1)
        low = word.lower()
        if low in class_words or low in STOPWORD_QUOTE:
            continue
        if m.start() in seen_positions:
            continue
        seen_positions.add(m.start())
        stem = ps.stem(low)
        sent = sentence_for_offset(narrative, m.start(), sent_spans)
        sent_low = sent.lower()

        exists = stem in real_by_stem
        claims_present = any(p in sent_low for p in PRESENCE_MARKERS)
        claims_absent = any(a in sent_low for a in ABSENCE_MARKERS)

        value_ok = True
        value_claim = None
        if exists:
            real_present_flags = {r["present"] for r in real_by_stem[stem]}
            if claims_absent and not claims_present:
                value_claim = "absent"
                value_ok = 0 in real_present_flags
            elif claims_present and not claims_absent:
                value_claim = "present"
                value_ok = 1 in real_present_flags

        supported = exists and value_ok
        facts.append({
            "type": "feature",
            "cited_word": word,
            "stem": stem,
            "sentence": sent,
            "exists_in_real_top7": exists,
            "real_present_flags": sorted({r["present"] for r in real_by_stem.get(stem, [])}),
            "value_claim": value_claim,
            "value_accurate": value_ok if value_claim else None,
            "supported": supported,
            "interpretive_sentence": is_interpretive(sent),
        })
    return facts, sent_spans, sents


TITLECASE_NGRAM = re.compile(r"(?:[A-Z][A-Za-z0-9&\-]*\s+){2,}[A-Z][A-Za-z0-9&\-]*")
QUOTED_PHRASE = re.compile(r'["“](?=[A-Z])([^"”]{15,150})["”]')

# Fixed scaffolding/boilerplate vocabulary that recurs in every narrative
# regardless of the specific node -- a Title-Case or quoted match consisting
# ONLY of these terms (plus the predicted-class label, checked separately) is
# not a neighbor citation, just narration about the method/dataset itself.
GENERIC_ML_TERMS = {
    "graph", "neural", "network", "networks", "gnn", "gnnexplainer",
    "model", "bag", "word", "words", "bow", "explainer", "our", "given",
    "predicted", "class", "category", "categories", "product", "products",
    "amazon", "cora", "citation", "purchase", "co", "hop", "feature",
    "features", "node", "nodes", "paper", "papers", "confidence", "score",
}


def extract_neighbor_facts(narrative, node_idx, hop1, hop2, sent_spans, sents, predicted_class, target_text):
    real_neighbors = {r["node"]: r for r in (hop1 + hop2)}
    real_texts_norm = {nid: normalize_tokens(r["text"]) for nid, r in real_neighbors.items()}
    class_norm = normalize_tokens(predicted_class)
    target_norm = normalize_tokens(target_text) if target_text else set()

    facts = []
    handled_spans = []
    handled_texts = set()  # normalized text of class-claim phrases already scored via neighbor_id

    # 1) explicit "Node <id>" citations (exclude self-reference to node_idx)
    real_class_names = {r["class"] for r in real_neighbors.values()}
    for m in re.finditer(r"\bNode[- ](\d+)\b", narrative):
        cited_id = int(m.group(1))
        if cited_id == node_idx:
            continue
        sent = sentence_for_offset(narrative, m.start(), sent_spans)
        exists = cited_id in real_neighbors
        real_class = real_neighbors[cited_id]["class"] if exists else None

        # If the text right after this citation attaches an explicit class
        # claim to this node ("belongs ... to the X class" / "class: X"),
        # check it against the neighbor's real class and fold the result
        # into ONE combined verdict for this citation, and mark that
        # phrase's span as handled so it isn't ALSO scored as a separate
        # (and wrongly-typed) neighbor_title fact via text-overlap against
        # snippet content. Searched in a window right after the citation
        # (absolute narrative offsets throughout, not the extracted
        # sentence string) so span bookkeeping stays simple and correct.
        claimed_class, class_ok = None, None
        window_start = m.end()
        window = narrative[window_start:window_start + 300]
        cue = re.search(r"(?:belongs?(?:\s+instead)?\s+to(?:\s+the)?|classified\s+as|category\s+of|class[:\s]+)\s*[\"']?([A-Za-z][A-Za-z_ &]{2,40}?)[\"']?(?:\s+class|\s+category|[.,]|$)", window)
        if cue:
            candidate = cue.group(1).strip()
            for rc in real_class_names | {predicted_class}:
                if candidate.replace("_", " ").lower() == rc.replace("_", " ").lower():
                    claimed_class = rc
                    break
            if exists and claimed_class:
                class_ok = claimed_class.lower() == real_class.lower()
                cue_start_abs = window_start + cue.start(1)
                handled_spans.append((cue_start_abs, cue_start_abs + len(cue.group(1))))
            if claimed_class:
                handled_texts.add(re.sub(r"[^a-z0-9]", "", candidate.lower()))

        supported = exists and (class_ok is None or class_ok)
        facts.append({
            "type": "neighbor_id",
            "cited_id": cited_id,
            "sentence": sent,
            "exists_in_real_subgraph": exists,
            "real_class": real_class,
            "claimed_class": claimed_class,
            "class_accurate": class_ok,
            "supported": supported,
            "interpretive_sentence": is_interpretive(sent),
        })
        handled_spans.append((m.start(), m.end()))

    # 2) quoted multi-word phrases + Title-Case n-grams, found PER SENTENCE
    # (prevents a capitalized word starting the next sentence from being
    # stitched onto the previous sentence's trailing capitalized phrase).
    for sent, s_start, s_end in sent_spans:
        candidates = []
        for m in QUOTED_PHRASE.finditer(sent):
            candidates.append((m.group(1), s_start + m.start(), s_start + m.end()))
        for m in TITLECASE_NGRAM.finditer(sent):
            candidates.append((m.group(0), s_start + m.start(), s_start + m.end()))

        for text, start, end in candidates:
            if any(hs <= start < he for hs, he in handled_spans):
                continue
            if re.sub(r"[^a-z0-9]", "", text.lower()) in handled_texts:
                continue
            norm = normalize_tokens(text)
            if len(norm) < 2:
                continue
            # Skip boilerplate method/dataset language and bare restatements
            # of the predicted-class label -- not neighbor claims at all.
            if norm <= GENERIC_ML_TERMS or norm <= class_norm:
                continue
            best_nid, best_overlap = None, 0
            for nid, real_norm in real_texts_norm.items():
                overlap = len(norm & real_norm)
                if overlap > best_overlap:
                    best_overlap, best_nid = overlap, nid
            target_overlap = len(norm & target_norm)
            # If this phrase matches the TARGET node's own real text at least
            # as well as any neighbor, it's the model restating what IT is
            # (self-description), not a claim about a connected node --
            # exclude entirely rather than score it as an (un)supported
            # neighbor claim.
            if target_overlap >= 3 and target_overlap >= best_overlap:
                handled_spans.append((start, end))
                continue
            supported = best_overlap >= 3 or (best_overlap >= 2 and best_overlap / max(1, len(norm)) >= 0.5)
            facts.append({
                "type": "neighbor_title",
                "cited_text": text,
                "sentence": sent,
                "best_matched_node": best_nid if supported else None,
                "token_overlap": best_overlap,
                "supported": supported,
                "interpretive_sentence": is_interpretive(sent),
            })
            handled_spans.append((start, end))

    return facts


def interpretive_only_passages(narrative, all_facts, sents, sent_spans):
    fact_sentences = {f["sentence"] for f in all_facts}
    out = []
    for s in sents:
        if s in fact_sentences:
            continue
        if is_interpretive(s):
            out.append(s)
    return out


TARGET_TEXT_RE = re.compile(r"### Target (?:Paper|Product) \(node \d+\):\s*(.+?)\n\n###", re.DOTALL)
TARGET_TITLE_RE = re.compile(r"\*\*Product:\*\*\s*(.+?)\s*\(node \d+\)")


def extract_target_text(prompt):
    m = TARGET_TEXT_RE.search(prompt)
    if m:
        return m.group(1).strip()
    m = TARGET_TITLE_RE.search(prompt)
    return m.group(1).strip() if m else ""


def check_node(node_id, record, dataset_label):
    narrative = record["raw_llm_output"]
    real_feats = record["gnnexplainer_top_features"]
    hop1 = record["gnnexplainer_1hop_neighbors"]
    hop2 = record["gnnexplainer_2hop_neighbors"]
    predicted_class = record["prediction"]["Predicted Class"]
    target_text = extract_target_text(record["prompt"])

    feat_facts, sent_spans, sents = extract_feature_facts(narrative, real_feats, predicted_class)
    nb_facts = extract_neighbor_facts(narrative, node_id, hop1, hop2, sent_spans, sents, predicted_class, target_text)
    all_facts = feat_facts + nb_facts

    interp_passages = interpretive_only_passages(narrative, all_facts, sents, sent_spans)

    n_supported = sum(1 for f in all_facts if f["supported"])
    n_total = len(all_facts)
    precision = n_supported / n_total if n_total else None

    return {
        "dataset": dataset_label,
        "node_id": node_id,
        "predicted_class": predicted_class,
        "n_facts": n_total,
        "n_supported": n_supported,
        "grounding_precision": precision,
        "n_feature_facts": len(feat_facts),
        "n_neighbor_facts": len(nb_facts),
        "facts": all_facts,
        "interpretive_passages": interp_passages,
        "narrative": narrative,
    }


def run():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    all_results = {}
    for label, path in SURVEY_JSONL.items():
        dataset_label = "cora" if label == "cora" else "products"
        for line in open(path):
            r = json.loads(line)
            node_id = r["target_node"]
            res = check_node(node_id, r, dataset_label)
            all_results[node_id] = res

    with open(OUT_DIR / "graphxain_grounding_precision_RULEBASED.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"{'dataset':10s} {'node':>7s} {'facts':>6s} {'supp':>6s} {'precision':>10s}")
    by_dataset = {}
    for node_id, res in sorted(all_results.items(), key=lambda kv: (kv[1]["dataset"], kv[0])):
        p = res["grounding_precision"]
        print(f"{res['dataset']:10s} {node_id:>7d} {res['n_facts']:>6d} {res['n_supported']:>6d} {p if p is None else round(p,3):>10}")
        by_dataset.setdefault(res["dataset"], []).append(p)

    print()
    for ds, precs in by_dataset.items():
        vals = [p for p in precs if p is not None]
        print(f"{ds}: mean grounding precision = {sum(vals)/len(vals):.3f} (n={len(vals)})")

    return all_results


if __name__ == "__main__":
    run()
