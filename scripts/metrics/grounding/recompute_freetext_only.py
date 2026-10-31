"""
Read-only recomputation, per user request: GraphNarrator grounding recall,
Cora and Products, recomputed with "mentioned" scoped to ONLY the Free-Text
Explanation section, next to the current pipeline values. Writes new
*_freetext.json/csv files; does not touch any existing file; no model calls.

Finding established first (by direct code trace, confirmed empirically
below): the CURRENT pipeline (grounding_recall_f1.py for Cora,
graphnarrator_products_recall_f1_untruncated.py for Products) ALREADY
scopes "mentioned" to Free-Text Explanation only:
  - grounding_precision_rulebased.py:129-130
        ft_idx = assistant_content.find("Free-Text Explanation")
        tail = assistant_content[ft_idx:] if ft_idx != -1 else assistant_content
    reused unmodified by grounding_recall_f1.py:129,226,281 via
    `gn.extract_node_claims(assistant_content)`.
  - graphnarrator_products_recall_f1_untruncated.py:178
        ft_idx = ac.find("Free-Text Explanation")
    (manual "mentioned" judgment, but the docstring states explicitly this
    manual read was restricted to text after this header.)

So "recompute using only Free-Text Explanation" reproduces the CURRENT
values exactly, by construction. What's actually informative -- and what
this script also computes, as the natural complement -- is the reverse
comparison: what would recall look like if the "mentioned" check were NOT
restricted to Free-Text Explanation, i.e. searched the FULL assistant
response (Reasoning + Free-Text Explanation) instead. This isolates whether
the Free-Text-only scoping decision ever actually mattered.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
import grounding_precision_rulebased as gp  # noqa: E402  (unmodified import, read-only)

# grounding_recall_f1.py itself, imported unmodified, so we call its REAL
# graphnarrator_node_recall_normalized() for the "current" (freetext-only)
# value instead of reimplementing it (avoids subtly-wrong reimplementation).
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "grounding_recall_f1", "./grounding_recall_f1_2026-09-07/grounding_recall_f1.py")
grf1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(grf1)

OUT_DIR = Path("./grounding_recall_f1_2026-09-07")
GN_REPO = Path("./graphnarrCora/GraphNarrator")

# ---------------------------------------------------------------------
# CORA: current value = grf1.graphnarrator_node_recall_normalized() called
# as-is (unmodified). Full-text variant = same function's logic, but with
# extract_node_claims' internal Free-Text-Explanation restriction bypassed
# (claims parsed from the whole normalized assistant_content instead).
# ---------------------------------------------------------------------

CORA_EXPL_DIR = GN_REPO / "outputs/generated_expls-3"
CORA_PKL_DIR = GN_REPO / "outputs/pkls"
CORA_SURVEY_NODES = [510, 2334, 1062, 884]


def extract_node_claims_full_text(text):
    """Identical to gp.extract_node_claims() EXCEPT it does not restrict to
    the Free-Text-Explanation tail first -- parses the whole given text."""
    block = text
    fence_start = block.find("```markdown")
    if fence_start != -1:
        fs = fence_start + len("```markdown")
        fe = block.find("```", fs)
        block = block[fs:fe] if fe != -1 else block[fs:]
    claims = {}
    range_pattern = re.compile(r"^(ROOT|Node-[\d.]+)\s*~\s*(Node-[\d.]+)\s*:\s*(.+)$")
    single_pattern = re.compile(r"^(ROOT|Node-[\d.]+)\s*:\s*(.+)$")
    for line in block.splitlines():
        stripped = line.strip().lstrip("-").strip()
        m_range = range_pattern.match(stripped)
        if m_range:
            for key in gp.expand_node_range(m_range.group(1), m_range.group(2)):
                claims[key] = m_range.group(3)
            continue
        m_single = single_pattern.match(stripped)
        if m_single:
            claims[m_single.group(1)] = m_single.group(2)
    return claims


def cora_node_recall_fulltext(pos_map, expl_dir, node_id):
    """Mirrors grf1.graphnarrator_node_recall_normalized() exactly, except
    claims come from extract_node_claims_full_text() instead of
    gp.extract_node_claims() -- i.e. the ONLY change is removing the
    Free-Text-Explanation-only restriction."""
    import math
    pos = pos_map.get(node_id)
    expl_path = Path(expl_dir) / f"{pos}.json"
    data = json.load(open(expl_path))
    user_content = data["messages"][1]["content"]
    assistant_content = grf1.normalize_markdown_for_claims(data["messages"][2]["content"])

    graph_block = gp.extract_task_graph_block(user_content)
    kw_scores = gp.real_keyword_scores_per_node(graph_block)
    claims = extract_node_claims_full_text(assistant_content)  # <-- the only change

    direct_neighbors = [k for k in kw_scores if grf1.DIRECT_NEIGHBOR_RE.match(k)]
    direct_neighbors.sort(key=lambda k: int(k.split("-")[1]))
    max_score = {}
    for k in direct_neighbors:
        all_scores = [s for scores in kw_scores[k].values() for s in scores]
        max_score[k] = max(all_scores) if all_scores else float("-inf")

    n = len(direct_neighbors)
    if n == 0:
        return {"important_set": [], "mentioned": {}, "n_important": 0, "n_mentioned": 0, "recall": None}

    cutoff_count = math.ceil(n / 2)
    scores_sorted_desc = sorted(max_score.values(), reverse=True)
    boundary_score = scores_sorted_desc[cutoff_count - 1]
    important_set = [k for k in direct_neighbors if max_score[k] >= boundary_score]
    important_set.sort(key=lambda k: (-max_score[k], int(k.split("-")[1])))

    mentioned = {k: (k in claims) for k in important_set}
    n_mentioned = sum(mentioned.values())
    generation_failed = len(claims) == 0
    recall = None if generation_failed else (n_mentioned / len(important_set) if important_set else None)
    return {"important_set": important_set, "mentioned": mentioned,
            "n_important": len(important_set), "n_mentioned": n_mentioned, "recall": recall}


def run_cora():
    pos_map = gp.build_position_map(CORA_PKL_DIR)
    results = {}
    for gid in CORA_SURVEY_NODES:
        r_ft = grf1.graphnarrator_node_recall_normalized(gp, pos_map, CORA_EXPL_DIR, gid)
        r_full = cora_node_recall_fulltext(pos_map, CORA_EXPL_DIR, gid)
        results[str(gid)] = {"freetext_only_CURRENT": r_ft, "full_text_ALTERNATIVE": r_full}
    return results


# ---------------------------------------------------------------------
# PRODUCTS: "mentioned" there is a MANUAL judgment (MENTION_EVIDENCE dict
# in graphnarrator_products_recall_f1_untruncated.py), not a mechanical
# parse -- so it cannot be "recomputed" the same mechanical way. What CAN
# be checked mechanically: does the Reasoning section ever cite an
# important-set neighbor (an explicit "Node N" reference) that is absent
# from the Free-Text Explanation section? If never, the manual judgment's
# explicit claim ("this exclusion didn't change ANY node's result") is
# mechanically corroborated for all 4 nodes, not just the 1 already
# checked by hand (1852).
# ---------------------------------------------------------------------

PRODUCTS_EXPL_DIR = GN_REPO / "outputs/generated_expls-products_untruncated_2026-09-07"
PRODUCTS_NODE_POSITIONS = {6813: 23, 1852: 3, 8766: 33, 8438: 29}
NODE_CITE_RE = re.compile(r"\bNode[\s\-]?(\d+)\b", re.IGNORECASE)


def products_citation_diff():
    out = {}
    for node, pos in PRODUCTS_NODE_POSITIONS.items():
        f = PRODUCTS_EXPL_DIR / f"{pos}.json"
        if not f.exists():
            out[node] = {"error": f"missing file {f}"}
            continue
        data = json.load(open(f))
        assistant_content = [m["content"] for m in data["messages"] if m["role"] == "assistant"][0]
        ft_idx = assistant_content.find("Free-Text Explanation")
        reasoning_part = assistant_content[:ft_idx] if ft_idx != -1 else ""
        freetext_part = assistant_content[ft_idx:] if ft_idx != -1 else assistant_content

        reasoning_cites = set(NODE_CITE_RE.findall(reasoning_part))
        freetext_cites = set(NODE_CITE_RE.findall(freetext_part))
        only_in_reasoning = reasoning_cites - freetext_cites
        out[node] = {
            "reasoning_cites_node_numbers": sorted(reasoning_cites, key=int),
            "freetext_cites_node_numbers": sorted(freetext_cites, key=int),
            "cited_in_reasoning_only": sorted(only_in_reasoning, key=int),
        }
    return out


if __name__ == "__main__":
    cora_results = run_cora()
    products_results = products_citation_diff()

    with open(OUT_DIR / "grounding_recall_cora_freetext.json", "w") as f:
        json.dump(cora_results, f, indent=2)
    with open(OUT_DIR / "grounding_recall_products_citation_diff_freetext.json", "w") as f:
        json.dump(products_results, f, indent=2)

    print("=== CORA: freetext-only (current, via REAL grounding_recall_f1.py function) vs full-text 'mentioned' scope ===")
    ft_recalls, full_recalls = [], []
    for node, r in cora_results.items():
        ft, full = r["freetext_only_CURRENT"], r["full_text_ALTERNATIVE"]
        print(f"  node {node}: freetext recall={ft['recall']:.3f} ({ft['n_mentioned']}/{ft['n_important']})  "
              f"full-text recall={full['recall']:.3f} ({full['n_mentioned']}/{full['n_important']})  "
              f"{'SAME' if ft['mentioned']==full['mentioned'] else 'DIFFERENT'}")
        ft_recalls.append(ft["recall"])
        full_recalls.append(full["recall"])
    import statistics as stats
    print(f"  MEAN freetext-only (CURRENT, should equal 0.958): {stats.mean(ft_recalls):.3f}   MEAN full-text: {stats.mean(full_recalls):.3f}")

    print()
    print("=== PRODUCTS: citations appearing ONLY in Reasoning (never in Free-Text Explanation) ===")
    for node, r in products_results.items():
        print(f"  node {node}: {r}")
