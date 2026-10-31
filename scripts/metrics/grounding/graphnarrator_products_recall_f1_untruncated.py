"""
Grounding RECALL and F1 for GraphNarrator's 4 Products survey nodes
(1852, 6813, 8766, 8438), using the untruncated regeneration data at
outputs/generated_expls-products_untruncated_2026-09-07/, combined with
manually-verified precision (given, not recomputed).

Does NOT modify any existing file -- reads generated_expls-products_untruncated_2026-09-07/
and pkls_products (read-only), writes only to this script and its JSON output.

=== Important-set definition ===
Per design decision (2026-09-07, after the literal flat all-levels tie-inclusive
rule was found to produce a degenerate 100%-of-all-neighbors result on this
data -- see conversation): important items = TOP-LEVEL neighbors only
(Node-1, Node-2, ... -- Node-X.Y sub-children excluded), matching Cora's
original "direct neighbors" definition. Ranked by max single-word saliency
score AS DISPLAYED in that neighbor's own verbalized-graph line (reusing
gp.real_keyword_scores_per_node, the same parsing used throughout this
project -- NOT the pkl's raw unrounded per-token scores, to stay consistent
with how this has always been computed). Top 50% rounded up, ties at the
cutoff boundary included (score >= boundary value).

=== "Mentioned" definition and methodology ===
Unlike Cora's GraphNarrator output (a markdown hierarchy with one claim line
per "Node-X:" header, mechanically parseable), these Products explanations
are free-flowing prose with an separate "### Reasoning" section followed by
a "### Free-Text Explanation" section. Per the task spec, only text AFTER
the "Free-Text Explanation" header counts (matching the same section-scoping
convention gp.extract_node_claims() uses for Cora via
assistant_content.find("Free-Text Explanation")) -- the earlier "### Reasoning"
section is not searched, even though it sometimes contains additional
Node-N citations not repeated in the actual Free-Text Explanation (e.g.
node 1852's Reasoning section cites "Node 1" but so does its Free-Text
Explanation, so this exclusion didn't change ANY node's result here, but is
applied for principled consistency).

A neighbor is scored "mentioned" only if the Free-Text Explanation
specifically and distinguishably corresponds to THAT neighbor -- either an
explicit "Node N" citation paired with an accurate content description, or
content specific enough that a reader could attribute it to that one
neighbor and not equally to several others. Purely GENERIC collective
language that describes the whole neighbor set as a category (e.g. "linked
to other nodes that discuss similar products, such as tanning lotions and
applicators" when every neighbor is a tanning product) does NOT count as
mentioning any specific one of them -- crediting all of them via one shared
generic phrase would repeat the exact over-crediting failure mode already
found and rejected for GraphNarrator/Cora's fallback path and
CF-GNNExplainer's dict-block merging earlier. Likewise, an
overlap with ROOT's OWN described identity (e.g. ROOT's own brand name
happening to also be a neighbor's brand, or ROOT itself being a "baby
bottle" like one neighbor also is) is not credited to that neighbor unless
the text explicitly frames it as being about that neighbor, not just ROOT.

This determination was made by directly reading each node's real
verbalized-graph content against its Free-Text Explanation text (full dumps
in the untruncated output directory) -- documented per-neighbor below as
`mention_evidence`, not produced by a generic mechanical formula, since no
single such formula reliably distinguishes genuine per-neighbor reference
from incidental word overlap on this free-prose data (the same problem
already debugged at length for other methods earlier).
"""
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
import grounding_precision_rulebased as gp  # noqa: E402

EXPL_DIR = Path("./graphnarrCora/GraphNarrator/outputs/generated_expls-products_untruncated_2026-09-07")
OUT_DIR = Path("./grounding_recall_f1_2026-09-07")

NODE_POSITIONS = {6813: 23, 1852: 3, 8766: 33, 8438: 29}

# Manually verified precision (given by user, NOT recomputed here).
MANUAL_PRECISION = {
    1852: 1.000,
    6813: 0.800,
    8766: 0.857,
    8438: 0.750,
}

TOP_LEVEL_RE = re.compile(r"^Node-\d+$")

# Per-neighbor "mentioned" determination, from direct manual reading of each
# node's Free-Text Explanation section against its real verbalized-graph
# content (see module docstring for the criterion). Only neighbors that end
# up in the top-50% important set are looked up from this dict at runtime;
# entries for excluded neighbors are kept here too, for transparency.
MENTION_EVIDENCE = {
    6813: {
        "Node-1": (False, "Sun Goddess sunless tanning glove mitt applicator. Free-Text Explanation only "
                           "says 'linked to other nodes that discuss similar products, such as tanning "
                           "lotions and applicators' -- a generic category description shared by ALL 6 "
                           "neighbors, not a specific reference to Node-1 by number or distinguishing content."),
        "Node-2": (False, "St Moriz self tan applicator mitt. Same generic 'tanning lotions and applicators' "
                           "phrase as Node-1 -- not individually distinguishable."),
        "Node-3": (False, "St Moriz Instant Self Tanning Mousse (dark). No specific reference; covered only "
                           "by the same generic phrase."),
        "Node-4": (False, "Vita Liberata Phenomenal Dark Tan Mousse -- coincidentally shares ROOT's own "
                           "brand ('vita liberata'), and the explanation does discuss 'the brand vita "
                           "liberata', but frames it as ROOT's OWN branding/identity, not as 'another node "
                           "is also this brand'. Not credited: same principle as not crediting a neighbor "
                           "for sharing ROOT's category unless the text specifically says so."),
        "Node-5": (False, "PretendTan bronzing mousse applicator mitt. No specific reference."),
        "Node-6": (False, "Caudalie Divine Legs tinted body lotion. No specific reference."),
    },
    1852: {
        "Node-2": (False, "Texas Instruments compatible ink roller (for calculators). Free-Text Explanation's "
                           "only specific numbered citation is 'calculators (Node 1)' -- Node-1 is NOT in "
                           "this node's top-50% important set (excluded, score -0.0 vs boundary 0.01), so "
                           "this citation doesn't credit any important-set neighbor. 'envelopes' is also "
                           "named generically, but the actual envelope products are sub-nodes (Node-1.4, "
                           "Node-3.5), not any top-level important neighbor."),
        "Node-3": (False, "Nukote calculator ribbon (for Canon MP-11DX). Not mentioned; not an 'envelope' "
                           "or 'calculator' itself, and no other reference made."),
        "Node-4": (False, "Centon 10x4GB USB flash drive multi-pack. Not mentioned anywhere in the text."),
        "Node-5": (False, "v4ink compatible HP toner cartridge. Not mentioned."),
        "Node-6": (False, "Alliance Sterling rubber bands. Not mentioned."),
        "Node-7": (False, "Quartet Prestige cork bulletin board. Not mentioned."),
        "Node-8": (False, "TOPS spiral steno books. Not mentioned."),
    },
    8766: {
        "Node-1": (True, "Max Factor Pan Stik Foundation (bisque ivory). Free-Text Explanation explicitly "
                          "says 'Node 1 contains references to different foundation types' -- accurate, "
                          "specific, numbered citation. Credited."),
        "Node-2": (True, "Max Factor Lasting Performance Make-up (soft beige). Free-Text Explanation "
                          "explicitly says 'Node 2 discusses the lasting performance of makeup' -- matches "
                          "the real product's own name ('Lasting Performance') exactly. Credited."),
        "Node-3": (False, "Max Factor Mastertouch Concealer. No specific reference beyond the generic "
                           "'part of a larger network of beauty products' framing."),
        "Node-4": (False, "Max Factor Miracle Touch Liquid Illusion Foundation (golden). Not specifically "
                           "referenced (shares ROOT's own product line/name -- 'Miracle Touch Liquid "
                           "Illusion Foundation' is literally ROOT's own title with a different shade -- "
                           "but the explanation never distinguishes it from ROOT's own description)."),
        "Node-5": (False, "Max Factor Pan-Stik Ultra-Creamy Makeup. Not mentioned."),
        "Node-6": (False, "Baby banana bendable infant training toothbrush -- thematically unrelated to "
                           "beauty/foundation; not mentioned (correctly, since it's off-topic)."),
        "Node-7": (False, "Max Factor Creme Puff Powder Makeup. Not mentioned."),
        "Node-8": (False, "Shiseido Perfect Foundation Brush. Not mentioned."),
        "Node-9": (False, "Max Factor Creme Puff Compact Powder (translucent). Not mentioned."),
    },
    8438: {
        "Node-2": (True, "KidCo F710 Baby Food Mill. Free-Text Explanation says 'connections to other nodes "
                          "that feature products like probiotics and baby food' -- 'baby food' specifically "
                          "and accurately matches Node-2's real content. Credited."),
        "Node-3": (False, "Zoli two-pack wide-neck baby bottles. ROOT is ALSO described as 'a baby bottle' "
                           "in the first paragraph -- but that describes ROOT's OWN identity, not a claim "
                           "that another node is also a bottle; the text never says 'another node also "
                           "features bottles'. Not credited under the same coincidental-overlap-with-ROOT "
                           "principle applied to node 6813/Node-4."),
        "Node-6": (False, "Born Free silicone teether. Not mentioned anywhere in the text."),
    },
}


def compute_important_set(pos, node_id):
    d = json.load(open(EXPL_DIR / f"{pos}.json"))
    uc = d["messages"][1]["content"]
    ac = d["messages"][2]["content"]
    block = gp.extract_task_graph_block(uc)
    scores = gp.real_keyword_scores_per_node(block)

    top_level = [k for k in scores if TOP_LEVEL_RE.match(k)]
    top_level.sort(key=lambda k: int(k.split("-")[1]))
    max_score = {}
    for k in top_level:
        allsc = [s for v in scores[k].values() for s in v]
        max_score[k] = max(allsc) if allsc else float("-inf")

    n = len(top_level)
    cutoff = math.ceil(n / 2)
    sorted_desc = sorted(max_score.values(), reverse=True)
    boundary = sorted_desc[cutoff - 1]
    important = [k for k in top_level if max_score[k] >= boundary]
    important.sort(key=lambda k: (-max_score[k], int(k.split("-")[1])))

    ft_idx = ac.find("Free-Text Explanation")
    ft_section = ac[ft_idx:] if ft_idx != -1 else ac

    return {
        "n_top_level_neighbors": n,
        "cutoff_count_target_50pct": cutoff,
        "boundary_score": boundary,
        "all_top_level_scores": {k: max_score[k] for k in top_level},
        "important_set": important,
        "free_text_explanation_section": ft_section,
    }


def main():
    results = {}
    for node_id, pos in NODE_POSITIONS.items():
        ranking = compute_important_set(pos, node_id)
        important = ranking["important_set"]
        evidence = MENTION_EVIDENCE[node_id]

        neighbor_detail = []
        n_mentioned = 0
        for k in important:
            mentioned, note = evidence[k]
            n_mentioned += int(mentioned)
            neighbor_detail.append({
                "neighbor": k,
                "max_saliency_score": ranking["all_top_level_scores"][k],
                "mentioned": mentioned,
                "evidence": note,
            })

        n_important = len(important)
        recall = n_mentioned / n_important if n_important else None
        precision = MANUAL_PRECISION[node_id]
        f1 = (2 * precision * recall / (precision + recall)) if recall is not None and (precision + recall) > 0 else None

        results[node_id] = {
            "position_index": pos,
            "n_top_level_neighbors": ranking["n_top_level_neighbors"],
            "cutoff_count_target_50pct": ranking["cutoff_count_target_50pct"],
            "boundary_score": ranking["boundary_score"],
            "important_set_detail": neighbor_detail,
            "n_important": n_important,
            "n_mentioned": n_mentioned,
            "recall": recall,
            "precision_manual": precision,
            "f1": f1,
        }

    out = {
        "method": "GraphNarrator",
        "dataset": "products",
        "source_dir": str(EXPL_DIR),
        "important_set_definition": "top-level neighbors only (Node-X.Y sub-children excluded)",
        "results": results,
    }

    out_path = OUT_DIR / "graphnarrator_products_recall_f1_untruncated.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"{'node':>6s} {'n_imp':>6s} {'n_ment':>7s} {'precision':>10s} {'recall':>8s} {'F1':>8s}")
    precs, recs, f1s = [], [], []
    for node_id, r in results.items():
        p, rc, f1v = r["precision_manual"], r["recall"], r["f1"]
        precs.append(p)
        recs.append(rc)
        f1s.append(f1v)
        print(f"{node_id:>6d} {r['n_important']:>6d} {r['n_mentioned']:>7d} {p:>10.3f} {rc:>8.3f} {f1v:>8.3f}")
    print(f"{'MEAN':>6s} {'':>6s} {'':>7s} {sum(precs)/4:>10.3f} {sum(recs)/4:>8.3f} {sum(f1s)/4:>8.3f}")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
