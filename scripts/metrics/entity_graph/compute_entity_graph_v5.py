"""
Entity Graph Complexity v5 -- follow-up to v4 (v4 untouched; new files only).

Three changes this version:

1. Self-reference: "Node 0" / "node 0" / "Node-0" is ALSO collapsed to ROOT
   unconditionally, in addition to matching the row's real target_id.
   Confirmed first (not assumed) across the full corpus: 199/199 GraphNarrator
   Products texts use "Node 0" and 0/199 use literal "ROOT"; 519/519 Cora
   texts use "ROOT" and 0/519 use "Node 0" -- a clean, universal, non-
   overlapping convention split, so this is safe to apply unconditionally
   (it can never fire on Cora, and always means the target on Products).

2. Ranges: "X to Y" between two entity references (e.g. "Node-1 to Node-1.9")
   is now treated as a 2-member enumeration (no X-Y edge; connects to a
   sentence subject if one is found, exactly like other enumeration groups),
   instead of being read as two independently co-occurring entities.

3. Title/brand matching (Products only): brand_word matching is REMOVED
   entirely (the "before" audit showed it mostly firing on generic English
   words -- "ocean", "idea", "comfort", "White" -- coincidentally identical
   to a neighbour's title's first word, not real brand identifiers).
   title_key matching is kept, but a candidate key is now only accepted if
   it contains a run of >= 3 CONSECUTIVE non-stopword words (STOPWORDS
   reused unmodified from grounding_precision_rulebased.py) -- this mainly
   discards the 2-word candidates that used to fall through to this rule.

Everything else (C_cycle = E-N+P, C_state = N-1, bracket/comma-list
enumeration suppression, extended sentence splitting, repetition flagging)
is reused UNMODIFIED from v3/v4 by import.
"""

import argparse
import csv
import glob
import importlib.util
import json
import os
import re
import statistics as stats
import sys

import networkx as nx

sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from tag import TAG  # noqa: E402

GN_REPO = "./graphnarrCora/GraphNarrator"

V3_PATH = "./grounding_recall_f1_2026-09-07/compute_entity_graph_v3.py"
_spec = importlib.util.spec_from_file_location("compute_entity_graph_v3", V3_PATH)
v3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v3)

V2_PATH = "./grounding_recall_f1_2026-09-07/compute_entity_graph_v2.py"
_spec2 = importlib.util.spec_from_file_location("compute_entity_graph_v2", V2_PATH)
v2 = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(v2)

GP_PATH = GN_REPO + "/grounding_precision_rulebased.py"
_spec3 = importlib.util.spec_from_file_location("grounding_precision_rulebased", GP_PATH)
gp = importlib.util.module_from_spec(_spec3)
_spec3.loader.exec_module(gp)

STOPWORDS = gp.STOPWORDS  # reused unmodified

ENTITY_REF_RE = v2.ENTITY_REF_RE
_title_keys = v2._title_keys
sentence_boundaries_v3 = v3.sentence_boundaries_v3
sentence_index_of_v3 = v3.sentence_index_of_v3
detect_repetition = v3.detect_repetition
load_graphnarrator = v3.load_graphnarrator
load_graphxain_json = v3.load_graphxain_json
load_cf_response_json = v3.load_cf_response_json


def _norm_keep_len(s):
    return re.sub(r"[^a-z0-9' ]", " ", s.lower())


# --------------------------------------------------------------------------
# 3. title_key-only matching (brand_word removed), >=3-consecutive-
#    non-stopword-words filter
# --------------------------------------------------------------------------

def _has_three_consecutive_nonstop(key):
    words = key.lower().split()
    run = 0
    for w in words:
        w_clean = re.sub(r"[^a-z0-9']", "", w)
        if w_clean and w_clean not in STOPWORDS:
            run += 1
            if run >= 3:
                return True
        else:
            run = 0
    return False


def extract_entity_spans_v5(text, neighbours=None):
    """Same structure as v2/v3's extract_entity_spans, but: no brand_word
    stage at all, and title_key candidates are filtered to those with a
    run of >=3 consecutive non-stopword words before being tried."""
    spans = []
    consumed = [False] * len(text)

    for m in ENTITY_REF_RE.finditer(text):
        eid = "ROOT" if m.group(2) else m.group(1)
        spans.append((m.start(), m.end(), eid))
        for i in range(m.start(), m.end()):
            consumed[i] = True

    if not neighbours:
        return spans

    tnorm = _norm_keep_len(text)

    for nb in neighbours:
        nid = str(nb["node_id"])
        for m in re.finditer(r"(?<![\d\w.])" + re.escape(nid) + r"(?![\d\w.])", tnorm):
            s, e = m.start(), m.end()
            if any(consumed[s:e]):
                continue
            spans.append((s, e, nid))
            for i in range(s, e):
                consumed[i] = True

    candidates = []
    for nb in neighbours:
        if nb["title"] == "missing":
            continue
        for key in _title_keys(nb["title"]):
            if _has_three_consecutive_nonstop(key):
                candidates.append((len(key), key, str(nb["node_id"])))
        # brand_word: REMOVED entirely (point 3)
    candidates.sort(key=lambda c: -c[0])

    for _, key, nid in candidates:
        pos = 0
        while True:
            idx = tnorm.find(key, pos)
            if idx == -1:
                break
            end = idx + len(key)
            if not any(consumed[idx:end]):
                for i in range(idx, end):
                    consumed[i] = True
                spans.append((idx, end, nid))
            pos = idx + 1

    return spans


# --------------------------------------------------------------------------
# Enumeration detection: brackets, comma/and-lists (>=3), AND "X to Y" ranges
# --------------------------------------------------------------------------

BRACKET_RE = re.compile(r"\[([^\[\]]*)\]")
CONNECTOR_RE = re.compile(
    r"connected\s+to|connected\s+with|linked\s+to|neighbou?rs?\b|including\b|such\s+as\b|"
    r"\bare:|\bis:",
    re.IGNORECASE,
)
LIST_SEP_RE = re.compile(r"^[\s,]*(?:and\b[\s,]*)?&?[\s,]*$", re.IGNORECASE)
RANGE_SEP_RE = re.compile(r"^\s*to\s*$", re.IGNORECASE)  # point 2: "X to Y"


def find_enumeration_groups(sent_text, sent_spans):
    claimed = set()
    enum_groups = []

    for bm in BRACKET_RE.finditer(sent_text):
        b_start, b_end = bm.start(), bm.end()
        members = [i for i, (s, e, eid) in enumerate(sent_spans) if b_start <= s < b_end]
        if len(members) >= 2:
            for i in members:
                claimed.add(i)
            enum_groups.append((members, b_start))

    unclaimed_idx = [i for i in range(len(sent_spans)) if i not in claimed]

    # "X to Y" ranges: adjacent pairs among unclaimed spans separated only by "to"
    range_claimed = set()
    for a, b in zip(unclaimed_idx, unclaimed_idx[1:]):
        if a in range_claimed or b in range_claimed:
            continue
        gap = sent_text[sent_spans[a][1]:sent_spans[b][0]]
        if RANGE_SEP_RE.match(gap):
            claimed.add(a)
            claimed.add(b)
            range_claimed.add(a)
            range_claimed.add(b)
            enum_groups.append(([a, b], sent_spans[a][0]))

    unclaimed_idx = [i for i in range(len(sent_spans)) if i not in claimed]
    run = []
    for i in unclaimed_idx:
        if not run:
            run = [i]
            continue
        prev_i = run[-1]
        gap = sent_text[sent_spans[prev_i][1]:sent_spans[i][0]]
        if LIST_SEP_RE.match(gap):
            run.append(i)
        else:
            if len(run) >= 3:
                for j in run:
                    claimed.add(j)
                enum_groups.append((run, sent_spans[run[0]][0]))
            run = [i]
    if len(run) >= 3:
        for j in run:
            claimed.add(j)
        enum_groups.append((run, sent_spans[run[0]][0]))

    resolved_groups = []
    for members, enum_start in enum_groups:
        subject_eid = None
        best = None
        for i, (s, e, eid) in enumerate(sent_spans):
            if i in claimed:
                continue
            if e <= enum_start:
                if best is None or e > sent_spans[best][1]:
                    best = i
        if best is not None:
            between = sent_text[sent_spans[best][1]:enum_start]
            if CONNECTOR_RE.search(between):
                subject_eid = sent_spans[best][2]
        resolved_groups.append((members, subject_eid))

    free_spans = [sent_spans[i] for i in range(len(sent_spans)) if i not in claimed]
    return resolved_groups, free_spans


# --------------------------------------------------------------------------
# Graph building
# --------------------------------------------------------------------------

def build_graph_v5(text, target_id, neighbours=None):
    spans = extract_entity_spans_v5(text, neighbours)
    cuts = sentence_boundaries_v3(text)

    G = nx.Graph()
    G.add_node("ROOT")

    self_ref_count = 0
    by_sentence_spans = {}
    for start, end, eid in spans:
        if eid == "ROOT":
            continue
        if eid == "0" or (target_id is not None and eid == str(target_id)):  # point 1
            self_ref_count += 1
            continue
        G.add_node(eid)
        G.add_edge("ROOT", eid)
        sidx = sentence_index_of_v3(start, cuts)
        by_sentence_spans.setdefault(sidx, []).append((start, end, eid))

    for sidx, sspans in by_sentence_spans.items():
        sent_start = cuts[sidx]
        sent_text = text[sent_start:cuts[sidx + 1]]
        rel_spans = sorted([(s - sent_start, e - sent_start, eid) for s, e, eid in sspans])

        enum_groups, free_spans = find_enumeration_groups(sent_text, rel_spans)

        free_ents = sorted({eid for _, _, eid in free_spans})
        for i in range(len(free_ents)):
            for j in range(i + 1, len(free_ents)):
                G.add_edge(free_ents[i], free_ents[j])

        for members, subject_eid in enum_groups:
            member_eids = {rel_spans[i][2] for i in members}
            if subject_eid is not None:
                for m in member_eids:
                    if m != subject_eid:
                        G.add_edge(subject_eid, m)

    return G, spans, self_ref_count


def entity_graph_measures_v5(text, target_id, neighbours=None):
    G, spans, self_ref_count = build_graph_v5(text, target_id, neighbours)
    N = G.number_of_nodes()
    E = G.number_of_edges()
    P = nx.number_connected_components(G)

    return {
        "N": N, "E": E, "P": P,
        "C_state": N - 1, "C_fan": E / N, "C_cycle": E - N + P,
        "C_density": E / (N * (N - 1) / 2) if N >= 2 else 0.0,
        "self_reference_count": self_ref_count,
    }, G


def assert_valid(row, method, dataset, node):
    if not (0 <= row["C_density"] <= 1):
        raise AssertionError(f"C_density out of [0,1]: {row['C_density']} "
                              f"(method={method}, dataset={dataset}, node={node})")
    if row["C_cycle"] < 0:
        raise AssertionError(f"C_cycle < 0: {row['C_cycle']} "
                              f"(method={method}, dataset={dataset}, node={node})")


LOADERS = {
    "graphnarrator": load_graphnarrator,
    "graphxain_json": load_graphxain_json,
    "cf_response_json": load_cf_response_json,
}


def parse_inputs(argv):
    inputs = []
    i = 0
    while i < len(argv):
        if argv[i] == "--input":
            method, dataset, fmt, path = argv[i + 1:i + 5]
            i += 5
            pkl_dir = None
            if i < len(argv) and argv[i] == "--pkl-dir":
                pkl_dir = argv[i + 1]
                i += 2
            inputs.append({"method": method, "dataset": dataset, "format": fmt,
                            "path": path, "pkl_dir": pkl_dir})
        else:
            i += 1
    return inputs


def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--neighbor-titles", default=None)
    args, unknown = p.parse_known_args()
    inputs = parse_inputs(sys.argv[1:])
    if not inputs:
        p.error("at least one --input METHOD DATASET FORMAT PATH is required")

    os.makedirs(args.out_dir, exist_ok=True)

    neighbor_titles = {}
    if args.neighbor_titles:
        with open(args.neighbor_titles, encoding="utf-8") as f:
            neighbor_titles = json.load(f)

    for spec_ in inputs:
        method, dataset, fmt, path, pkl_dir = (
            spec_["method"], spec_["dataset"], spec_["format"], spec_["path"], spec_["pkl_dir"]
        )
        loader = LOADERS.get(fmt)
        if loader is None:
            raise ValueError(f"unknown/excluded format '{fmt}' for --input {method} {dataset}")

        records = loader(path, pkl_dir) if fmt == "graphnarrator" else loader(path)
        use_titles = neighbor_titles and dataset.lower() == "products"

        rows = []
        for node, text, neighbours in records:
            if neighbours is None and use_titles:
                neighbours = neighbor_titles.get(str(node), {}).get("neighbors")
            m, _ = entity_graph_measures_v5(text, node, neighbours)
            assert_valid(m, method, dataset, node)
            flagged, detail = detect_repetition(text)
            row = {"method": method, "dataset": dataset, "node": node, **m,
                   "repetition_flagged": flagged, **detail}
            rows.append(row)

        if not rows:
            print(f"WARNING: 0 rows for {method}/{dataset}", file=sys.stderr)
            continue

        out_csv = os.path.join(args.out_dir, f"entity_graph_v5_{method}_{dataset}.csv")
        fieldnames = ["method", "dataset", "node", "N", "E", "P", "C_state", "C_fan", "C_cycle",
                      "C_density", "self_reference_count", "repetition_flagged", "line_repeat",
                      "worst_line_repeat_count", "token_repeat"]
        with open(out_csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        print(f"{method}/{dataset}: n={len(rows)} -> {out_csv}")


if __name__ == "__main__":
    main()
