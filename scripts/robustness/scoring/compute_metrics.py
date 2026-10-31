"""Per-text and aggregate metrics for the robustness texts on the judge subset (judge_subset.json:
12 nodes per dataset, fixed before any judging) -- every metric, every configuration. One table of
method x configuration x dataset with precision, recall, F1, FK, lexical and entity-graph complexity
and claim counts.

Precision  On the judge subset only (judge_subset.json: 12 nodes per dataset, fixed before judging; F1 likewise).
           S / (S + C) over the judge verdicts of the text's claims (unverifiable, duplicate excluded),
           as grounding_judge_2026-10-13/compare.py. Reported on all claims and on span-check-passing
           claims only. NaN when S + C = 0 or when the configuration was not judged.
Recall     rule-based "mentioned" against the main paper's method-specific reference sets, using the
           paper's functions from grounding_recall_f1_2026-09-07/grounding_recall_f1.py unchanged:
             GraphNarrator  graphnarrator_node_recall_normalized: top-50% (ceil, boundary ties in) of the
                            direct Node-X neighbors in the prompt's verbalized graph by max token saliency;
                            mentioned = key found by extract_node_claims() in the Free-Text section.
             GraphXAIN      top-7 GNNExplainer words from the prompt, duplicate words collapsed (as Table 14);
                            mentioned = Porter stem among the quoted citations extract_feature_facts() finds
                            in the real top-7 (existence only).
             CF             removed-edge set; mentioned = cf_edge_recall (REMOVAL_WORDS_FIXED /
                            SENTENCE_SPLIT_FIXED).
F1         2PR/(P+R); 0 when P or R is NaN or both are 0 (compare.py convention).
Text metrics (FK grade, Flesch ease, Halstead lexical complexity, entity-graph C_state/C_fan/C_cycle/C_density)
           readability / halstead / entity_measures imported unchanged from
           readability_analysis/text_metrics/compute_text_metrics.py, word_count = Halstead N as there,
           neighbours = neighbor_titles_full.json for Products and none for Cora (the production metrics
           convention). Computed on clean_text() of the scored text, identical for all 9 configurations:
             - drop code-fence lines (```...), drop markdown heading markers, bullet / numbered-list markers
               and blockquote markers, remove **, __, inline backticks and single * emphasis;
             - every bullet or heading line counts as one sentence (a period is appended when the line
               does not already end in . ! or ?); lines are then joined with spaces.
           CF sensitivity: the same metrics on the prose after the infos = {...} block
           (readability_checks_2026-10-05/cf_nonempty_recompute.clean), suffix _prose.
Aggregates: mean of per-text values, NaN skipped (compare.py convention); claim counts summed.
Run with graphnarrCora/GraphNarrator/venv (textstat 0.7.13, nltk, torch_geometric).
"""
import csv
import importlib.util
import json
import math
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

R = Path(".")
HERE = Path(__file__).resolve().parent
csv.field_size_limit(sys.maxsize)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rf = load_module("rf", R / "grounding_recall_f1_2026-09-07/grounding_recall_f1.py")
gn = load_module("gn_precision", rf.GN_REPO / "grounding_precision_rulebased.py")
gx = load_module("gx_precision", rf.GX_DIR / "grounding_precision_rulebased.py")
cfm = load_module("cf_precision", rf.CF_RUN_DIR / "grounding_precision_rulebased/grounding_precision_rulebased.py")
tm = load_module("tm", R / "readability_analysis/text_metrics/compute_text_metrics.py")


def cfclean(r):  # verbatim copy of readability_checks_2026-10-05/cf_nonempty_recompute.clean (that script has no
    i = r.find("{")  # __main__ guard, so loading it would rerun it and rewrite its output files)
    if i < 0:
        return r.strip()
    d = 0
    for j in range(i, len(r)):
        if r[j] == "{":
            d += 1
        elif r[j] == "}":
            d -= 1
            if d == 0:
                return r[j + 1:].strip()
    return r

GN_PROMPT = {"cora": rf.GN_REPO / "outputs/generated_expls-100", "products": rf.GN_REPO / "outputs/generated_expls-101"}
GX_DUMP = {ds: {json.loads(l)["target_node"]: json.loads(l) for l in open(R / f"graphxain_schemaaligned_production_2026-08-16/{ds}/prompts_dump.jsonl")}
           for ds in ("cora", "products")}
GX_FEAT_RE = re.compile(r"word='([^']*)', importance=([0-9.]+), present_in_\w+=(\d)")
CF_DATA = R / "llm-graph-cf/data"
NEIGHBOURS = {"cora": {}, "products": json.load(open(R / "production_run_2026-07-27/consolidated/neighbor_titles_full.json"))}

BULLET = re.compile(r"^\s*(?:[-*+•]|\d+[.)])\s+")
HEADING = re.compile(r"^\s*#{1,6}\s*")


def clean_text(text):
    out = []
    for line in text.splitlines():
        if re.match(r"^\s*```", line):
            continue
        is_item = bool(BULLET.match(line) or HEADING.match(line))
        s = HEADING.sub("", line)
        s = BULLET.sub("", s)
        s = re.sub(r"^\s*>\s?", "", s)
        s = s.replace("**", "").replace("__", "").replace("`", "")
        s = re.sub(r"(?<!\w)\*(\S[^*]*?)\*(?!\w)", r"\1", s)
        s = s.strip()
        if not s:
            continue
        if is_item and s[-1] not in ".!?":
            s += "."
        out.append(s)
    return " ".join(out)


def text_metrics(text, ds, node, suffix=""):
    t = clean_text(text) if text else ""  # failed generation: no scored text, no metrics
    if not t:
        return {}
    h = tm.halstead(t)
    nb = NEIGHBOURS[ds].get(str(node), {}).get("neighbors")
    e = tm.entity_measures(t, nb, h["length_N"])
    out = {**tm.readability(t), **h, **e, "words": len(t.split())}
    return {k + suffix: v for k, v in out.items()}


def gn_recall(e):
    user = json.load(open(GN_PROMPT[e["dataset"]] / f"{e['cf_key']}.json"))["messages"][1]["content"]
    with tempfile.TemporaryDirectory() as d:
        json.dump({"messages": [{"role": "system", "content": ""}, {"role": "user", "content": user},
                                {"role": "assistant", "content": e["text_full"]}]}, open(Path(d) / "0.json", "w"))
        r = rf.graphnarrator_node_recall_normalized(gn, {int(e["node"]): 0}, d, int(e["node"]))
    return r["recall"], r["n_important"], r["n_mentioned"], r.get("generation_failed")


def gx_recall(e):
    rec = GX_DUMP[e["dataset"]][int(e["node"])]
    feats = [{"word": w, "importance": float(i), "present": int(p)} for w, i, p in GX_FEAT_RE.findall(rec["prompt"])]
    assert len(feats) == 7
    facts, _, _ = gx.extract_feature_facts(e["text_full"], feats, rec["prediction"]["Predicted Class"])
    stems = {f["stem"] for f in facts if f["exists_in_real_top7"]}
    seen = {}
    for f in feats:  # duplicate words collapsed, as the Table 14 recall set G
        seen.setdefault(f["word"], gx.ps.stem(f["word"].lower()) in stems)
    return sum(seen.values()) / len(seen), len(seen), sum(seen.values()), None


def cf_recall(e):
    base = str(CF_DATA / e["dataset"] / "cf-gnnexplainer-canonical/random_seed_42_")
    k = e["cf_key"]
    entry = {"node_id": int(e["node"]), "llm_raw_output": e["text_full"],
             "removed_edges_global": json.load(open(base + "cf_removed_edges.json"))[k],
             "factual_graph_description": json.load(open(base + "factual_graph_descriptions.json"))[k],
             "counterfactual_graph_description": json.load(open(base + "counterfactual_graph_descriptions.json"))[k]}
    _, n_m, n_t, rec = rf.cf_edge_recall(cfm, entry)
    return rec, n_t, n_m, None


def nanmean(xs):
    xs = [x for x in xs if x is not None and x == x]
    return sum(xs) / len(xs) if xs else float("nan")


def main():
    js = json.load(open(HERE / "judge_subset.json"))["datasets"]
    in_subset = {(ds, str(n["global_node_id"])) for ds, ns in js.items() for n in ns}
    # every metric is computed on the judge subset only (12 nodes per dataset, fixed before judging)
    texts = [e for e in json.load(open(HERE / "texts.json")) if (e["dataset"], e["node"]) in in_subset]
    claims = defaultdict(list)
    if (HERE / "claims.csv").exists():
        for r in csv.DictReader(open(HERE / "claims.csv", encoding="utf-8")):
            claims[r["text_id"]].append(r)
    verdicts, judged_cfgs = {}, {}
    jdir = HERE / "judge_run"
    if (jdir / "judgments.csv").exists():
        for r in csv.DictReader(open(jdir / "judgments.csv", encoding="utf-8")):
            verdicts[r["claim_id"]] = r["judge_verdict"]
    if (jdir / "run_status.json").exists():
        judged_cfgs = {k: v.get("state") for k, v in json.load(open(jdir / "run_status.json"))["configs"].items()}

    rows = []
    for e in texts:
        cfg = f"{e['method']}__{e['config']}"
        sub = (e["dataset"], e["node"]) in in_subset
        fully = judged_cfgs.get(cfg) == "fully judged" and sub  # precision / F1 only on the judge subset
        cl = claims.get(e["id"], [])
        row = {"text_id": e["id"], "method": e["method"], "config": e["config"], "dataset": e["dataset"], "node": e["node"],
               "is_survey": e["is_survey"], "valid": bool(e["text_scored"]), "in_judge_subset": sub,
               "judged": fully, "n_claims": len(cl) if cl else None,
               "n_span_fail": sum(c["span_check"] == "fail" for c in cl) if cl else None}
        for tag, keep in (("", lambda c: True), ("_spanpass", lambda c: c["span_check"] == "pass")):
            v = [verdicts.get(c["claim_id"]) for c in cl if keep(c)] if fully else []
            s, c_ = v.count("supported"), v.count("contradicted")
            row[f"S{tag}"], row[f"C{tag}"] = (s, c_) if fully else (None, None)
            row[f"U{tag}"], row[f"D{tag}"] = (v.count("unverifiable"), v.count("duplicate")) if fully else (None, None)
            row[f"parse_fail{tag}"] = v.count("PARSE_FAIL") if fully else None
            row[f"precision{tag}"] = (s / (s + c_) if s + c_ else float("nan")) if fully else float("nan")
        rec, n_g, n_m, gen_failed = {"GraphNarrator": gn_recall, "GraphXAIN": gx_recall, "CF-GNNExplainer": cf_recall}[e["method"]](e)
        if not row["valid"]:
            # Failed generation (no Free-Text section). extract_node_claims() falls back to the whole response when
            # the section is missing, and here that is the copied input graph, so its Node-X lines would count as
            # "mentioned". Recall is undefined instead.
            rec, n_m = None, None
        row.update(recall=rec if rec is not None else float("nan"), G_size=n_g, G_mentioned=n_m, gn_no_node_claims=gen_failed)
        for tag in ("", "_spanpass"):
            p, r_ = row[f"precision{tag}"], row["recall"]
            row[f"f1{tag}"] = (0.0 if (p != p or r_ != r_ or p + r_ == 0) else 2 * p * r_ / (p + r_)) if fully else float("nan")
        row.update(text_metrics(e["text_scored"], e["dataset"], e["node"]))
        if e["method"] == "CF-GNNExplainer":
            row.update(text_metrics(cfclean(e["text_scored"]), e["dataset"], e["node"], "_prose"))
        rows.append(row)

    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(HERE / "metrics_per_text.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)

    MEAN = ["precision", "precision_spanpass", "recall", "f1", "f1_spanpass", "fk_grade", "fk_grade_prose", "flesch_ease",
            "volume_V", "volume_per_word", "vocabulary_n", "length_N", "C_state", "C_fan", "C_cycle", "C_density",
            "C_state_per100w", "C_cycle_per100w", "words"]
    order = {(m, c): i for i, (m, c) in enumerate(dict.fromkeys((e["method"], e["config"]) for e in texts))}
    groups = defaultdict(list)
    for r in rows:
        groups[(r["method"], r["config"], r["dataset"])].append(r)
    keyorder = lambda kv: (order[kv[0][:2]], kv[0][2])  # noqa: E731

    def aggregate(m, c, ds, g_all):
        """Failed generations (no scored text) are reported, not averaged: n_texts counts valid texts only."""
        g = [x for x in g_all if x["valid"]]
        t = {"method": m, "config": c, "dataset": ds, "n_texts": len(g),
             "failed_nodes": " ".join(sorted((x["node"] for x in g_all if not x["valid"]), key=int)),
             "judged": all(x["judged"] for x in g if x["in_judge_subset"]),
             "n_judge_subset": sum(x["in_judge_subset"] for x in g),
             "n_claims_judged": sum(x["n_claims"] or 0 for x in g if x["judged"]) if any(x["judged"] for x in g) else None,
             "n_claims": sum(x["n_claims"] or 0 for x in g) if all(x["n_claims"] is not None for x in g) else None,
             "n_span_fail": sum(x["n_span_fail"] or 0 for x in g) if all(x["n_span_fail"] is not None for x in g) else None,
             "n_precision_defined": sum(x["precision"] == x["precision"] for x in g)}
        for k in MEAN:
            t[k] = nanmean([x.get(k) for x in g]) if any(k in x for x in g) else None
        return t

    table = [aggregate(m, c, ds, g) for (m, c, ds), g in sorted(groups.items(), key=keyorder)]

    # Matched comparison: for each method x dataset where any configuration has failed generations,
    # every configuration of that method restricted to the nodes valid in all of them.
    matched = []
    for m, ds in dict.fromkeys((t["method"], t["dataset"]) for t in table):
        cfgs = [(k, g) for k, g in sorted(groups.items(), key=keyorder) if k[0] == m and k[2] == ds]
        if not any(not x["valid"] for _, g in cfgs for x in g):
            continue
        common = set.intersection(*({x["node"] for x in g if x["valid"]} for _, g in cfgs))
        for (_, c, _), g in cfgs:
            t = aggregate(m, c, ds, [x for x in g if x["node"] in common])
            t["matched_nodes"] = " ".join(sorted(common, key=int))
            matched.append(t)

    for name, data in (("results_table.csv", table), ("results_table_matched.csv", matched)):
        if data:
            with open(HERE / name, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)

    fmt = lambda v: "  n/a" if v is None or v != v else f"{v:5.3f}" if abs(v) < 10 else f"{v:5.1f}"  # noqa: E731
    for title, data in (("ALL VALID TEXTS", table), ("MATCHED NODES (method x dataset slices with failed generations)", matched)):
        if not data:
            continue
        print(f"\n== {title}")
        print(f"{'method':16s}{'config':13s}{'ds':9s}{'n':>4s}{'judged':>7s}{'claims':>7s}{'P':>7s}{'P_sp':>7s}{'R':>7s}{'F1':>7s}"
              f"{'FK':>7s}{'Vol/w':>7s}{'Cst':>7s}{'Cfan':>7s}{'Ccyc':>7s}{'Cden':>7s}{'Pclaims':>8s}  failed")
        for t in data:
            print(f"{t['method']:16s}{t['config']:13s}{t['dataset']:9s}{t['n_texts']:4d}{str(t['judged']):>7s}{str(t['n_claims']):>7s}"
                  + "".join(f"{fmt(t[k]):>7s}" for k in ("precision", "precision_spanpass", "recall", "f1", "fk_grade",
                                                        "volume_per_word", "C_state", "C_fan", "C_cycle", "C_density"))
                  + f"{str(t['n_claims_judged']):>8s}  {t['failed_nodes']}")


if __name__ == "__main__":
    main()
