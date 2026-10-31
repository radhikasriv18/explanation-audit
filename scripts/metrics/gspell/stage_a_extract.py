#!/usr/bin/env python3
"""
Stage A (GSPELL narratives venv: torch + networkx; textstat 0.7.13 appended from the
user site only because compute_entity_graph_v5 imports it).

Builds one text per node for the standardized GSPELL embedding-path runs:
  Cora     job 51247846  output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-08-16-23-39-47
  Products job 50765167  output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05 (July 27 production, Summary prompt)
Each node's batch outputs are joined in batch order ("\\n\\n"); the leading chat role
header "assistant" that starts every batch is stripped (template artefact, not model
text). Flags: empty, no "Support:" line, repetition loop (v3.detect_repetition, the
flag used by the v5 tables), per-batch empties / missing Support.
Correctness = canonical GraphSAGE prediction (gnn_preds in data_canonical.pth, verified
identical to sage_canonical.pt) vs y in {cora,products}_canonical.pt.
Entity graph = compute_entity_graph_v5.entity_graph_measures_v5, imported unmodified;
Products passes neighbor_titles_full.json neighbours, exactly as for the other methods.
(final sources; Sept-vs-July comparison section kept from the first version for reference.)
Read-only; writes into gspell_metrics_2026-10-09/ only. No model calls.
"""
import csv, hashlib, importlib.util, json, os, re, statistics as st, sys
sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))  # textstat 0.7.13 (pure python)
sys.path.insert(0, "./LOGIC2/GSPELL")                   # unpickle data_canonical datasets
sys.path.insert(0, "./graphnarrCora/GraphNarrator")      # v5 imports `tag`
import numpy as np, torch
import textstat

R = "./"
G = R + "LOGIC2/GSPELL/"
OUT = R + "gspell_metrics_2026-10-09/final/"
_s = importlib.util.spec_from_file_location("v5", R + "grounding_recall_f1_2026-09-07/compute_entity_graph_v5.py")
v5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(v5)
assert textstat.__version__ == (0, 7, 13), textstat.__version__

RUNS = {
    "cora": {"job": "51247846", "pt": G + "output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-08-16-23-39-47/GSPELL_explanations.pt",
             "data": G + "output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth"},
    "products": {"job": "50765167", "pt": G + "output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt",
                 "data": G + "output/products-meta-llama/Meta-Llama-3.1-8B-Instruct/data_canonical.pth"},
}
JULY = G + "output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt"
ROLE = re.compile(r"^\s*assistant\s*\n+", re.I)
SUPPORT = re.compile(r"Support\s*:", re.I)
CITE = re.compile(r"(?:Article|Paper|Product|Node)\s*#?\s*(\d+)")
titles_full = json.load(open(R + "production_run_2026-07-27/consolidated/neighbor_titles_full.json"))
lines = []
P = lambda s="": (print(s), lines.append(s))


def batch_text(b):
    return ROLE.sub("", b.get("explanation") or "", count=1).strip()


def node_text(batches):
    return "\n\n".join(t for t in (batch_text(b) for b in batches) if t)


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


# ---- 0. environment check: v5 here reproduces the existing CF-GNNExplainer v5 rows
for ds in ["cora", "products"]:
    old = {r["node"]: r for r in csv.DictReader(open(R + f"grounding_recall_f1_2026-09-07/entity_graph_v5_output/entity_graph_v5_CF-GNNExplainer_{ds}.csv"))}
    resp = json.load(open(R + f"llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{ds}_standard_Response.json"))
    td = json.load(open(R + f"llm-graph-cf/data/{ds}/cf-gnnexplainer-canonical/random_seed_42_factual_target_dict_repr.json"))
    ok = 0
    for k, v in resp.items():
        node = str(td[k]["Target_Node_ID"])
        nb = titles_full.get(node, {}).get("neighbors") if ds == "products" else None
        m, _ = v5.entity_graph_measures_v5(v[1], node, nb)
        ok += int(int(old[node]["C_state"]) == m["C_state"] and int(old[node]["C_cycle"]) == m["C_cycle"])
    P(f"env check: v5 reproduces existing CF-GNNExplainer {ds} rows {ok}/{len(old)}")

# ---- 1. per-node records
lex = {(r["dataset"], r["global_node_id"]): r["correct"] for r in csv.DictReader(open(R + "lexical_complexity_results.csv"))
       if r["method"] == "graphxain"}
records = []
for ds, cfg in RUNS.items():
    canon = torch.load(R + f"{ds}_canonical.pt", map_location="cpu", weights_only=False)
    preds = torch.load(cfg["data"], map_location="cpu", weights_only=False)["gnn_preds"].cpu()
    pt = torch.load(cfg["pt"], map_location="cpu", weights_only=False)
    split = np.load(G + f"{ds}_splits_seed42.npz")
    ref = (split["test_idx"] if ds == "cora" else split["eval_idx"]).tolist()
    targets = [n[0]["target_node"] for n in pt]
    P(f"\n{ds} job {cfg['job']}: {len(pt)} nodes, {sum(len(n) for n in pt)} batches; targets == "
      f"{'test_idx' if ds == 'cora' else 'eval_idx'} in order: {targets == ref}")
    agree = 0
    for nb in pt:
        node = int(nb[0]["target_node"])
        text = node_text(nb)
        bts = [batch_text(b) for b in nb]
        pred, true = int(preds[node]), int(canon.y[node])
        rep, rep_d = v5.detect_repetition(text)
        allowed = set(map(int, [n for b in nb for n in b["neighbors"]])) | {node}
        cited = [int(c) for c in CITE.findall(text)]
        rec = {"dataset": ds, "job": cfg["job"], "node": node, "n_batches": len(nb),
               "n_empty_batches": sum(t == "" for t in bts),
               "n_batches_without_support": sum(not SUPPORT.search(t) for t in bts),
               "empty": text == "", "has_support": bool(SUPPORT.search(text)),
               "repetition_flagged": rep, **{f"rep_{k}": v for k, v in rep_d.items()},
               "malformed": text != "" and (not SUPPORT.search(text) or rep),
               "pred": canon.label_names[pred], "true": canon.label_names[true], "correct": pred == true,
               "n_cited_ids": len(cited), "n_cited_outside_batches": sum(c not in allowed for c in cited),
               "fk_with_role_header": textstat.flesch_kincaid_grade("\n\n".join((b.get("explanation") or "").strip() for b in nb)),
               "text": text}
        if (ds, str(node)) in lex:
            agree += int(str(rec["correct"]) == lex[(ds, str(node))])
        if text:
            m, _ = v5.entity_graph_measures_v5(text, str(node), titles_full.get(str(node), {}).get("neighbors") if ds == "products" else None)
            rec.update({"C_state": m["C_state"], "C_cycle": m["C_cycle"], "eg_N": m["N"], "eg_E": m["E"], "eg_P": m["P"]})
        records.append(rec)
    s = [r for r in records if r["dataset"] == ds]
    P(f"   correctness agrees with lexical_complexity_results.csv (GraphXAIN rows, same canonical model): {agree}/{len(s)}")
    P(f"   empty {sum(r['empty'] for r in s)} | no Support line {sum(not r['has_support'] and not r['empty'] for r in s)} | "
      f"repetition loop {sum(r['repetition_flagged'] for r in s)} (line {sum(r['rep_line_repeat'] for r in s)}, token {sum(r['rep_token_repeat'] for r in s)}) | "
      f"malformed (non-empty, no Support or repetition) {sum(r['malformed'] for r in s)}")
    P(f"   batches: empty {sum(r['n_empty_batches'] for r in s)} / {sum(r['n_batches'] for r in s)}, "
      f"without Support line {sum(r['n_batches_without_support'] for r in s)}; nodes with >=1 empty batch "
      f"{sum(r['n_empty_batches'] > 0 for r in s)}")
    P(f"   cited IDs outside the node's batches: {sum(r['n_cited_outside_batches'] for r in s)}/{sum(r['n_cited_ids'] for r in s)}")

# ---- 2. Products: Sept 54238808 vs July 27 production 50765167
P("\n== Products: job 54238808 (Sept 15) vs job 50765167 (July 27 production)")
SEPT = G + "output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-09-15-14-57-20/GSPELL_explanations.pt"
sep, jul = (torch.load(p, map_location="cpu", weights_only=False) for p in (SEPT, JULY))
same_t = [a[0]["target_node"] for a in sep] == [b[0]["target_node"] for b in jul]
same_nb = sum([x["neighbors"] for x in a] == [y["neighbors"] for y in b] for a, b in zip(sep, jul))
P(f"targets identical & same order: {same_t}; neighbour batches identical for {same_nb}/200 nodes; "
  f"batches {sum(map(len, sep))} vs {sum(map(len, jul))}")
cmp_rows = []
for tag, run in (("sep_54238808", sep), ("jul_50765167", jul)):
    bt = [batch_text(b) for n in run for b in n]
    nt = [node_text(n) for n in run]
    words = [len(t.split()) for t in bt]
    cited = out = 0
    for n in run:
        allowed = set(map(int, [x for b in n for x in b["neighbors"]])) | {int(n[0]["target_node"])}
        c = [int(x) for x in CITE.findall(node_text(n))]
        cited += len(c); out += sum(x not in allowed for x in c)
    row = {"run": tag,
           "empty_batches": sum(t == "" for t in bt),
           "batches_without_support": sum(not SUPPORT.search(t) for t in bt),
           "nodes_without_support": sum(not SUPPORT.search(t) for t in nt),
           "batches_with_Summary_field": sum(bool(re.search(r"Summary\s*:", t)) for t in bt),
           "batches_with_KEYWORDS_block": sum("BEGIN KEYWORDS" in t for t in bt),
           "batches_ending_mid_sentence": sum(bool(t) and not re.search(r"[.!?)\]*\"'`>]\s*$", t) for t in bt),
           "nodes_repetition_flagged": sum(v5.detect_repetition(t)[0] for t in nt),
           "median_words_per_batch": st.median(words), "max_words_per_batch": max(words),
           "cited_ids": cited, "cited_outside_batches_pct": round(100 * out / cited, 1)}
    cmp_rows.append(row)
    P("   " + json.dumps(row))
P(f"identical batch texts between runs: {sum(batch_text(x) == batch_text(y) for a, b in zip(sep, jul) for x, y in zip(a, b))}")
pj = lambda t: G + f"pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct-{t}/projector.pth"
P(f"projector md5: Sept {md5(pj('2026-09-15-14-57-20'))} | July {md5(pj('2026-07-27-12-21-05'))}")

# ---- write
with open(OUT + "gspell_per_node_records.json", "w") as f:
    json.dump(records, f)
keys = [k for k in records[0] if k != "text"] + ["C_state", "C_cycle", "eg_N", "eg_E", "eg_P"]
keys = list(dict.fromkeys(keys))
with open(OUT + "gspell_per_node_flags.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore"); w.writeheader(); w.writerows(records)
with open(OUT + "products_sep_vs_july_comparison.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(cmp_rows[0])); w.writeheader(); w.writerows(cmp_rows)
open(OUT + "stage_a_results.txt", "w").write("\n".join(lines) + "\n")
