"""
RULE-BASED (not LLM-judge) grounding precision for GraphNarrator's final Stage 4b
explanations, survey nodes only. FActScore-style: decompose each explanation into
one atomic fact per hierarchy node (ROOT, Node-1, Node-1.1, ...) -- what that node
is claimed to be/contain -- then check each fact's claimed content words against
that SAME node's real keyword list, extracted from the exact verbalized-graph text
used to build the Stage 1/2 prompt (embedded in the '## Task' section of the same
JSON file's user message).

This is explicitly the fast rule-based pass. A follow-up LLM-as-judge (true
FActScore) run across the full eval set is a separate, later task -- do not
conflate the two. All outputs from this script are prefixed/suffixed RULEBASED.
"""
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from tag import TAG  # noqa: E402

REPO = Path("./graphnarrCora/GraphNarrator")

# Boilerplate words present in every node's keyword list regardless of actual
# content (LM_GNN_Joint_Model's fixed prompt scaffolding: "product", "amazon",
# "title", "content", etc.) -- these carry no discriminating evidence, so they
# don't count as support for a claim either way.
BOILERPLATE = {
    "product", "amazon", "platform", "title", "content", "160",
}
STOPWORDS = {
    "a", "an", "the", "is", "are", "this", "that", "of", "to", "and", "or", "as",
    "by", "its", "own", "for", "with", "in", "on", "further", "also", "another",
    "supporting", "reinforcing", "confirming", "collectively", "affirming",
    "context", "category", "classification", "beauty", "books", "sports",
    "outdoors", "keywords", "keyword", "node", "root", "direct", "indirect",
    "neighbor", "neighbors", "hop", "hops", "quintessentially", "clearly",
    "identify", "identifies", "product,", "products",
    "all", "these", "those", "some", "same", "such", "several", "other",
    "others", "each", "any", "more", "most", "several", "various", "multiple",
}


def normalize(word):
    w = re.sub(r"[^a-z0-9]", "", word.lower())
    if len(w) > 4 and w.endswith("s"):
        w = w[:-1]
    return w


def real_keywords_per_node(task_graph_block):
    """Parses '<verbalized-graph>...' lines into {node_key: set(real words)}."""
    per_node = {}
    for line in task_graph_block.splitlines():
        line = line.strip()
        m = re.match(r"^(ROOT|Node-[\d.]+):\s*(.+)$", line)
        if not m:
            continue
        node_key, rest = m.group(1), m.group(2)
        # allow trailing punctuation between the word and its score paren, e.g. "folders,(-0.01)"
        words = re.findall(r"([a-zA-Z][a-zA-Z0-9'\-.]*)[,;:\"')]*\(", rest)
        norm_words = {normalize(w) for w in words}
        norm_words = {w for w in norm_words if w and w not in BOILERPLATE and len(w) > 1}
        per_node[node_key] = norm_words
    return per_node


def real_keyword_scores_per_node(task_graph_block):
    """Parses '<verbalized-graph>...' lines into {node_key: {normalized_word: [real scores]}}
    -- keeps ALL occurrences' scores (a word can appear multiple times with different
    scores), for citation-level score-plausibility checking."""
    per_node = {}
    for line in task_graph_block.splitlines():
        line = line.strip()
        m = re.match(r"^(ROOT|Node-[\d.]+):\s*(.+)$", line)
        if not m:
            continue
        node_key, rest = m.group(1), m.group(2)
        # Includes boilerplate words on purpose: citation checks need TRUE
        # existence+score data even for generic words like "product" -- if the
        # model cites one with a specific score, that's a checkable claim.
        pairs = re.findall(r"([a-zA-Z][a-zA-Z0-9'\-.]*)[,;:\"')]*\(([-\d.]+)\)", rest)
        scores = {}
        for w, s in pairs:
            nw = normalize(w)
            if not nw or len(nw) <= 1:
                continue
            scores.setdefault(nw, []).append(float(s))
        per_node[node_key] = scores
    return per_node


def extract_cited_keywords(claim_text):
    """Extracts the model's own quoted '"word" (score)' citations from a claim line
    -- these are the atomic, checkable evidence units, not the loose descriptive phrase."""
    pairs = re.findall(r'"([a-zA-Z][a-zA-Z0-9\'\-]*)"\s*\(([-\d.]+)\)', claim_text)
    return [(normalize(w), float(s)) for w, s in pairs if normalize(w)]


def extract_task_graph_block(user_content):
    task_idx = user_content.find("## Task")
    assert task_idx != -1, "no ## Task section found"
    graph_start = user_content.find("<verbalized-graph>", task_idx)
    graph_end = user_content.find("</verbalized-graph>", graph_start)
    return user_content[graph_start + len("<verbalized-graph>") : graph_end]


def expand_node_range(start_key, end_key):
    """'Node-1.1' ~ 'Node-1.6' -> [Node-1.1, Node-1.2, ..., Node-1.6] (same prefix, last component is the range)."""
    start_parts = start_key.split(".")
    end_parts = end_key.split(".")
    if len(start_parts) != len(end_parts) or start_parts[:-1] != end_parts[:-1]:
        return [start_key, end_key]  # not a simple same-prefix range, don't guess
    prefix = ".".join(start_parts[:-1])
    try:
        lo, hi = int(start_parts[-1]), int(end_parts[-1])
    except ValueError:
        return [start_key, end_key]
    return [f"{prefix}.{i}" for i in range(lo, hi + 1)]


def extract_node_claims(assistant_content):
    """Parses the Free-Text Explanation section into {node_key: claim_line_text}.
    Handles both single-node lines ('Node-1.1: ...') and range lines
    ('Node-1.1 ~ Node-1.6: ...', matching the few-shot template's own batching
    style for summarizing multiple children in one sentence) -- the same claim
    text is checked against EACH individual node in the range."""
    ft_idx = assistant_content.find("Free-Text Explanation")
    tail = assistant_content[ft_idx:] if ft_idx != -1 else assistant_content
    # Bound to the fenced ```markdown ... ``` block only. Some generations
    # (observed on Cora) don't stop cleanly after closing the fence and
    # continue producing a spurious second copy of the '## Task' prompt --
    # unbounded parsing would treat that garbage's ROOT:/Node-X: lines as
    # real claims. If no closing fence is found, fall back to the full tail.
    fence_start = tail.find("```markdown")
    if fence_start != -1:
        fence_content_start = fence_start + len("```markdown")
        fence_end = tail.find("```", fence_content_start)
        block = tail[fence_content_start:fence_end] if fence_end != -1 else tail[fence_content_start:]
    else:
        block = tail
    claims = {}
    range_pattern = re.compile(r"^(ROOT|Node-[\d.]+)\s*~\s*(Node-[\d.]+)\s*:\s*(.+)$")
    single_pattern = re.compile(r"^(ROOT|Node-[\d.]+)\s*:\s*(.+)$")
    for line in block.splitlines():
        stripped = line.strip().lstrip("-").strip()
        m_range = range_pattern.match(stripped)
        if m_range:
            for key in expand_node_range(m_range.group(1), m_range.group(2)):
                claims[key] = m_range.group(3)
            continue
        m_single = single_pattern.match(stripped)
        if m_single:
            claims[m_single.group(1)] = m_single.group(2)
    return claims


def claim_content_words(claim_text):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9'\-]*", claim_text)
    norm = {normalize(w) for w in words}
    return {w for w in norm if w and len(w) > 2 and w not in STOPWORDS and w not in BOILERPLATE}


SCORE_TOLERANCE = 0.05


def check_explanation(pkl_path, expl_json_path):
    """
    Atomic fact = each individual '"keyword" (score)' citation the model makes
    for a given hierarchy node (its own stated evidence), checked against that
    SAME node's real keyword/score data from the verbalized graph.

    Supported: the cited keyword genuinely occurs in that node's real text
    (regardless of exact score -- word existence is the primary criterion).
    Unsupported: the cited keyword never occurs for that node at all --
    fabricated evidence.
    'score_plausible' is tracked separately for keyword-existent citations:
    whether the cited score is within SCORE_TOLERANCE of ANY real occurrence
    of that word for that node (a word can appear multiple times with
    different scores). A citation can be word-supported but score-fabricated.

    Falls back to the looser whole-claim topic-word overlap ONLY when a node's
    claim contains no quoted citations at all (e.g. some ROOT phrasings) --
    these are flagged separately (fallback=True) since they're a weaker check.
    """
    graph = TAG.load(pkl_path)
    data = json.load(open(expl_json_path))
    user_content = data["messages"][1]["content"]
    assistant_content = data["messages"][2]["content"]

    real_kw = real_keywords_per_node(extract_task_graph_block(user_content))
    real_kw_scores = real_keyword_scores_per_node(extract_task_graph_block(user_content))
    claims = extract_node_claims(assistant_content)

    facts = []
    for node_key, claim_text in claims.items():
        if node_key not in real_kw:
            continue

        cited = extract_cited_keywords(claim_text)
        if cited:
            for kw, cited_score in cited:
                word_exists = kw in real_kw_scores[node_key]
                score_plausible = None
                found_in_other_node = None
                if word_exists:
                    real_scores = real_kw_scores[node_key].get(kw, [])
                    score_plausible = any(abs(cited_score - rs) <= SCORE_TOLERANCE for rs in real_scores)
                else:
                    # Word doesn't belong to the claimed node -- check whether it
                    # belongs to a SIBLING node instead (cross-node misattribution,
                    # a more precise failure mode than "invented from nothing").
                    for other_key, other_scores in real_kw_scores.items():
                        if other_key != node_key and kw in other_scores:
                            found_in_other_node = {"node": other_key, "real_scores": other_scores[kw]}
                            break
                facts.append(
                    {
                        "node_key": node_key,
                        "claim": claim_text,
                        "cited_keyword": kw,
                        "cited_score": cited_score,
                        "supported": word_exists,
                        "score_plausible": score_plausible,
                        "real_scores_for_word": real_kw_scores[node_key].get(kw, []),
                        "found_in_other_node": found_in_other_node,
                        "fallback": False,
                    }
                )
        else:
            # no quoted citations in this claim -- fall back to loose topic-word check
            real_words = real_kw[node_key]
            claim_words = claim_content_words(claim_text)
            matched = claim_words & real_words
            facts.append(
                {
                    "node_key": node_key,
                    "claim": claim_text,
                    "supported": len(matched) > 0,
                    "matched_words": sorted(matched),
                    "fallback": True,
                }
            )

    unmatched_node_refs = [k for k in claims if k not in real_kw]

    n_supported = sum(1 for f in facts if f["supported"])
    precision = n_supported / len(facts) if facts else None
    n_score_implausible = sum(1 for f in facts if f.get("score_plausible") is False)

    return {
        "root_global_id": graph.root_global_id,
        "prediction": graph.prediction,
        "n_facts": len(facts),
        "n_supported": n_supported,
        "grounding_precision": precision,
        "n_score_implausible_among_supported": n_score_implausible,
        "facts": facts,
        "unmatched_node_refs_in_claims": unmatched_node_refs,
    }


def build_position_map(pkl_dir):
    mapping = {}
    for f in glob.glob(str(Path(pkl_dir) / "*.pkl")):
        idx = int(Path(f).stem)
        g = TAG.load(f)
        mapping[g.root_global_id] = idx
    return mapping


def run_dataset(dataset_name, pkl_dir, expl_dir, survey_nodes):
    pos_map = build_position_map(pkl_dir)
    results = {}
    for node in survey_nodes:
        pos = pos_map.get(node)
        if pos is None:
            results[node] = {"error": "node not found in pkl_dir position map"}
            continue
        pkl_path = Path(pkl_dir) / f"{pos}.pkl"
        expl_path = Path(expl_dir) / f"{pos}.json"
        if not expl_path.exists():
            results[node] = {"error": f"explanation file not found: {expl_path}"}
            continue
        results[node] = check_explanation(pkl_path, expl_path)
        results[node]["position_index"] = pos
    return results


if __name__ == "__main__":
    PRODUCTS_SURVEY = [6813, 1852, 8766, 8438]
    CORA_SURVEY = [4, 510, 2334, 1062, 884]

    out = {"dataset": "products", "results": run_dataset(
        "products",
        REPO / "outputs/pkls_standardized_run_2026-08-17_products",
        REPO / "outputs/generated_expls-503",
        PRODUCTS_SURVEY,
    )}

    out_path = REPO / "outputs/standardized_run_2026-08-17/grounding_precision_rulebased/products_RULEBASED.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")

    precisions = [r["grounding_precision"] for r in out["results"].values() if isinstance(r, dict) and r.get("grounding_precision") is not None]
    print(f"Products survey nodes: n={len(precisions)}, mean grounding precision = {sum(precisions)/len(precisions):.3f}")
    for node, r in out["results"].items():
        if isinstance(r, dict) and "grounding_precision" in r:
            print(f"  node {node}: {r['n_supported']}/{r['n_facts']} = {r['grounding_precision']:.3f}")

    # Cora: targeted 5-survey-node generation (exp_id=504), not the full 542-node
    # batch (exp_id=502) -- run separately once ready.
    out_cora = {"dataset": "cora", "results": run_dataset(
        "cora",
        REPO / "outputs/pkls_standardized_run_2026-08-17_cora",
        REPO / "outputs/generated_expls-504",
        CORA_SURVEY,
    )}

    out_path_cora = REPO / "outputs/standardized_run_2026-08-17/grounding_precision_rulebased/cora_RULEBASED.json"
    with open(out_path_cora, "w") as f:
        json.dump(out_cora, f, indent=2)
    print(f"Wrote {out_path_cora}")

    precisions_cora = [r["grounding_precision"] for r in out_cora["results"].values() if isinstance(r, dict) and r.get("grounding_precision") is not None]
    print(f"Cora survey nodes: n={len(precisions_cora)}, mean grounding precision = {sum(precisions_cora)/len(precisions_cora):.3f}")
    for node, r in out_cora["results"].items():
        if isinstance(r, dict) and r.get("grounding_precision") is not None:
            print(f"  node {node}: {r['n_supported']}/{r['n_facts']} = {r['grounding_precision']:.3f}")
        elif isinstance(r, dict) and r.get("n_facts") == 0:
            print(f"  node {node}: generation failed (no parseable explanation, 0 facts)")
        else:
            print(f"  node {node}: {r}")
