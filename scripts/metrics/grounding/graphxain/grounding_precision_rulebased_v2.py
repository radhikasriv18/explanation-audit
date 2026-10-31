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

===============================================================================
V2 ADDITIONS (2026-09-03) -- importance-magnitude/rank check
===============================================================================
Everything above this point is UNCHANGED from grounding_precision_rulebased.py
(the original script, left untouched in the same directory). This copy adds
one new, additive check on top of the existing supported/unsupported verdict:
does the narrative's RHETORICAL STRENGTH about a cited feature/neighbor's
importance ("significant", "crucial", "minor", "weak", ...) match where that
item actually ranks by real importance score among the set it was drawn from?

This directly answers the gap flagged in the prior read-only review: the
original script's `supported` verdict only checks (a) does the word/neighbor
exist in the real data, and (b) does an explicit presence/absence or class
claim match -- it never reads the real `importance` value at all, so a claim
like "'function' had a significant impact" is scored identically regardless
of whether `function` is actually the top-ranked or bottom-ranked of the 7
features by score. V2 adds that check as a SEPARATE, additive signal:

  RANK_MISMATCH   -- high-strength language ("significant", "crucial", ...)
                     on an item ranked in the bottom half of its real set, OR
                     low-strength/dismissive language ("minor", "weak", ...)
                     on an item ranked in the top half.
  RANK_CONSISTENT -- strength language present and the rank agrees with it.
  None            -- no rhetorical-strength language in the sentence, or the
                     citation doesn't exist in the real data (rank is
                     meaningless for a fact that's already Unsupported on
                     existence grounds) -- not applicable, not counted either
                     way.

Applied to BOTH claim types:
  - Feature claims: rank = position (1=highest) among the real top-7 by
    `importance`, TOP_HALF = ranks 1-3, BOTTOM_HALF = ranks 4-7 (exactly the
    asymmetric 7-item split specified for this task). A stem matching
    multiple top-7 entries (e.g. "use" appearing at two different TF-IDF
    dimensions, as seen for Products node 8438) takes the BEST (highest-
    importance / lowest rank-number) matching entry -- the most charitable
    reading, so a claim isn't flagged RANK_MISMATCH just because one of
    several real occurrences of that stem happens to rank low.
  - Neighbor claims (neighbor_id and neighbor_title): a real ranking proxy
    DOES exist -- gnnexplainer_1hop_neighbors and gnnexplainer_2hop_neighbors
    each carry a real `importance` (edge-importance) field per neighbor. Rank
    is computed WITHIN its own hop group (1-hop neighbors ranked only against
    other 1-hop neighbors; 2-hop against 2-hop), since the two hops are
    presented as separate lists with separate importance scales in the
    prompt and it would be misleading to rank a 2-hop neighbor against a
    1-hop one on the same scale. Because neighbor-group sizes vary per node
    (unlike the fixed 7-item feature set), TOP_HALF/BOTTOM_HALF is generalized
    as rank <= ceil(N/2) vs rank > ceil(N/2) for a group of size N -- this is
    a deliberate generalization of the task's explicit 7-item 1-3/4-7 split,
    not a literal instruction, and is called out here for that reason.

Revised precision = (supported AND rank_verdict != RANK_MISMATCH) facts /
total facts. This can only ever DOWNGRADE a fact that the original logic
already marked Supported (an already-Unsupported fact stays Unsupported
regardless of its rank_verdict) -- consistent with "keep existing
supported/unsupported logic unchanged; this is additive."
===============================================================================
"""
import json
import math
import re
from pathlib import Path

from nltk.stem import PorterStemmer

ps = PorterStemmer()

SURVEY_JSONL = {
    "cora": "./graphxain_survey_corrected_2026-08-07/cora/explainer_and_prompts.jsonl",
    "products_6813_1852": "./graphxain_survey_corrected_2026-08-07/products_6813_1852/explainer_and_prompts.jsonl",
    "products_8766_8438": "./graphxain_survey_corrected_2026-08-07/products_8766_8438/explainer_and_prompts.jsonl",
}

# Corrected survey node set (decided 2026-09-03): the actual
# survey stimuli file lists a 5th Cora node (global node 4), but it is
# deliberately excluded from this analysis despite that primary
# evidence -- see the report accompanying this run for the full discussion.
# This filter is what enforces the 4+4 = 8 node scope for the v2 rerun.
SURVEY_NODE_FILTER = {
    "cora": {510, 2334, 1062, 884},
    "products": {6813, 1852, 8766, 8438},
}

OUT_DIR = Path("./graphxain_survey_corrected_2026-08-07/grounding_precision_rulebased_v2")

# Rhetorical importance-strength markers (v2). Kept as a SEPARATE list from
# INTERPRETIVE_MARKERS rather than folded into it: INTERPRETIVE_MARKERS
# flags causal/hedge framing ("suggests", "indicates", "likely") -- i.e. HOW
# confidently something is asserted. HIGH/LOW_STRENGTH_MARKERS flag rhetorical
# MAGNITUDE of importance ("significant", "crucial" vs "minor", "weak") -- a
# different axis; a sentence can be both interpretive AND high-strength
# ("this likely played a crucial role"), so keeping them separate lets both
# signals be read off the same sentence independently rather than collapsing
# them into one marker set.
HIGH_STRENGTH_MARKERS = [
    "significant", "significantly", "crucial", "primary", "most decisive",
    "decisive", "key driver", "key factor", "strongest", "major role",
    "major factor", "heavily influenced", "heavily contributed", "critical",
    "essential", "dominant", "central role", "main driver", "substantial",
    "considerable", "strong impact", "strongly", "pivotal", "vital",
]
LOW_STRENGTH_MARKERS = [
    "minor", "less relevant", "weak", "limited role", "marginal",
    "negligible", "small role", "minimal", "little impact",
    "less significant", "less important", "peripherally", "trivial",
    "not as important", "secondary role", "modest",
]

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


def rhetorical_strength(sentence):
    """Returns 'high', 'low', 'mixed' (both marker types present -- treated
    as not-applicable since direction is ambiguous), or None (no strength
    language at all -- rank check doesn't apply to this claim)."""
    low = sentence.lower()
    high = any(m in low for m in HIGH_STRENGTH_MARKERS)
    weak = any(m in low for m in LOW_STRENGTH_MARKERS)
    if high and weak:
        return "mixed"
    if high:
        return "high"
    if weak:
        return "low"
    return None


def ranks_by_importance(items, key="importance"):
    """Returns a list parallel to `items` giving each item's 1-indexed rank
    (1 = highest importance) among the group. Ties broken by original list
    order (stable sort on -importance)."""
    order = sorted(range(len(items)), key=lambda i: -items[i][key])
    rank_of_index = {idx: rank for rank, idx in enumerate(order, start=1)}
    return [rank_of_index[i] for i in range(len(items))]


def rank_verdict(strength, rank, n_total, top_half_cutoff=None):
    """strength: 'high'/'low'/'mixed'/None. rank: 1-indexed real rank or None
    (citation doesn't exist in real data). n_total: size of the ranked group.
    top_half_cutoff: explicit cutoff (e.g. 3 for the 7-item 1-3/4-7 feature
    split); if None, generalized as ceil(n_total/2) for variable-size groups
    (neighbor hop lists)."""
    if strength not in ("high", "low") or rank is None:
        return None
    cutoff = top_half_cutoff if top_half_cutoff is not None else math.ceil(n_total / 2)
    top_half = rank <= cutoff
    if strength == "high" and not top_half:
        return "RANK_MISMATCH"
    if strength == "low" and top_half:
        return "RANK_MISMATCH"
    return "RANK_CONSISTENT"


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

    # v2: rank each real top-7 entry by importance (1 = highest). Keyed by
    # id() since dicts aren't hashable and entries in real_by_stem are the
    # SAME object instances as in real_feats (appended by reference above).
    feat_ranks = ranks_by_importance(real_feats)
    rank_by_id = {id(real_feats[i]): feat_ranks[i] for i in range(len(real_feats))}
    n_feats = len(real_feats)

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

        # v2: rhetorical-strength / real-rank check. Take the BEST (lowest
        # rank number = highest importance) matching entry when a stem has
        # multiple real occurrences -- most charitable reading (see module
        # docstring).
        strength = rhetorical_strength(sent)
        best_rank = min((rank_by_id[id(r)] for r in real_by_stem[stem]), default=None) if exists else None
        rverdict = rank_verdict(strength, best_rank, n_feats, top_half_cutoff=3)
        revised_supported = supported and rverdict != "RANK_MISMATCH"

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
            "rhetorical_strength": strength,
            "real_rank": best_rank,
            "n_ranked_group": n_feats,
            "rank_verdict": rverdict,
            "revised_supported": revised_supported,
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

    # v2: rank each neighbor by real edge `importance`, WITHIN its own hop
    # group (1-hop vs 2-hop use separate importance scales in the prompt --
    # see module docstring). node id -> (rank, group_size).
    nb_rank_info = {}
    for group in (hop1, hop2):
        if not group:
            continue
        gr = ranks_by_importance(group)
        for i, r in enumerate(group):
            nb_rank_info[r["node"]] = (gr[i], len(group))

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

        strength = rhetorical_strength(sent)
        rank, group_n = nb_rank_info.get(cited_id, (None, None))
        rverdict = rank_verdict(strength, rank, group_n) if exists else None
        revised_supported = supported and rverdict != "RANK_MISMATCH"

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
            "rhetorical_strength": strength,
            "real_rank": rank,
            "n_ranked_group": group_n,
            "rank_verdict": rverdict,
            "revised_supported": revised_supported,
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

            matched_nid = best_nid if supported else None
            strength = rhetorical_strength(sent)
            rank, group_n = nb_rank_info.get(matched_nid, (None, None)) if matched_nid is not None else (None, None)
            rverdict = rank_verdict(strength, rank, group_n) if matched_nid is not None else None
            revised_supported = supported and rverdict != "RANK_MISMATCH"

            facts.append({
                "type": "neighbor_title",
                "cited_text": text,
                "sentence": sent,
                "best_matched_node": matched_nid,
                "token_overlap": best_overlap,
                "supported": supported,
                "interpretive_sentence": is_interpretive(sent),
                "rhetorical_strength": strength,
                "real_rank": rank,
                "n_ranked_group": group_n,
                "rank_verdict": rverdict,
                "revised_supported": revised_supported,
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

    # v2: revised precision folds RANK_MISMATCH in as contradicted (can only
    # downgrade a fact the original logic already marked Supported).
    n_revised_supported = sum(1 for f in all_facts if f["revised_supported"])
    revised_precision = n_revised_supported / n_total if n_total else None
    rank_mismatches = [f for f in all_facts if f.get("rank_verdict") == "RANK_MISMATCH"]
    flipped = [f for f in all_facts if f["supported"] and not f["revised_supported"]]

    return {
        "dataset": dataset_label,
        "node_id": node_id,
        "predicted_class": predicted_class,
        "n_facts": n_total,
        "n_supported": n_supported,
        "grounding_precision": precision,
        "n_revised_supported": n_revised_supported,
        "revised_grounding_precision": revised_precision,
        "n_rank_mismatch": len(rank_mismatches),
        "flipped_facts": flipped,
        "n_feature_facts": len(feat_facts),
        "n_neighbor_facts": len(nb_facts),
        "facts": all_facts,
        "interpretive_passages": interp_passages,
        "narrative": narrative,
    }


def run():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    all_results = {}
    skipped = []
    for label, path in SURVEY_JSONL.items():
        dataset_label = "cora" if label == "cora" else "products"
        for line in open(path):
            r = json.loads(line)
            node_id = r["target_node"]
            # v2: enforce the corrected 8-node survey scope (excludes Cora
            # node 4 per explicit user instruction 2026-09-03 -- see report).
            if node_id not in SURVEY_NODE_FILTER[dataset_label]:
                skipped.append((dataset_label, node_id))
                continue
            res = check_node(node_id, r, dataset_label)
            all_results[node_id] = res

    with open(OUT_DIR / "graphxain_grounding_precision_RULEBASED_v2.json", "w") as f:
        json.dump(all_results, f, indent=2)

    if skipped:
        print(f"Excluded from this run (not in corrected survey scope): {skipped}")
        print()

    print(f"{'dataset':10s} {'node':>7s} {'facts':>6s} {'supp':>6s} {'orig_prec':>10s} "
          f"{'rev_supp':>9s} {'rev_prec':>9s} {'mismatch':>9s}")
    by_dataset_orig = {}
    by_dataset_rev = {}
    for node_id, res in sorted(all_results.items(), key=lambda kv: (kv[1]["dataset"], kv[0])):
        p = res["grounding_precision"]
        rp = res["revised_grounding_precision"]
        print(f"{res['dataset']:10s} {node_id:>7d} {res['n_facts']:>6d} {res['n_supported']:>6d} "
              f"{p if p is None else round(p,3):>10} {res['n_revised_supported']:>9d} "
              f"{rp if rp is None else round(rp,3):>9} {res['n_rank_mismatch']:>9d}")
        by_dataset_orig.setdefault(res["dataset"], []).append(p)
        by_dataset_rev.setdefault(res["dataset"], []).append(rp)

    print()
    for ds in by_dataset_orig:
        ov = [p for p in by_dataset_orig[ds] if p is not None]
        rv = [p for p in by_dataset_rev[ds] if p is not None]
        print(f"{ds}: mean ORIGINAL precision = {sum(ov)/len(ov):.3f} (n={len(ov)})  |  "
              f"mean REVISED precision = {sum(rv)/len(rv):.3f} (n={len(rv)})")

    return all_results


if __name__ == "__main__":
    run()
