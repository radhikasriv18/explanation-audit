#!/usr/bin/env python3
"""
Manual grounding labeling sheets for GSPELL (standardized embedding-path runs) on the 8 survey nodes.
  Cora     job 51247846  LOGIC2/GSPELL/output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-08-16-23-39-47/GSPELL_explanations.pt
  Products job 50765167  LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt

1. Extract every batch in order (neighbour IDs given in the prompt + generated text); join exactly
   like gspell_metrics_2026-10-09/final/stage_a_extract.py (strip only the leading "assistant"
   header, join non-empty batches with "\\n\\n") and check against the scored text.
2. Table 13 aggregation: mean of per-node F1 vs F1 of mean P / mean R, from the per-node CSVs.
3. Claim rows, rule-based (no LLM):
   - inside a neighbour block (headed "Article N:" / "Product N:"):
       neighbor_exists   the header line (the text asserts N is a neighbour)
       feature           each <<BEGIN KEYWORDS>> ... <<END KEYWORDS>> list
       neighbor_content  each "Summary:" line; any other sentence that cites another ID
       support_verdict   each "Support:" line (verdict + justification)
       other             remaining lines of >= 4 words
   - outside neighbour blocks (preamble / closing paragraph), sentence by sentence:
       neighbor_content  one row per ID cited in the sentence
       class             sentences naming a class label or "classif"/"category"
       other             remaining sentences of >= 4 words
   Pre-fill: in_batch (ID in that batch's prompt list), is_1hop / is_2hop (canonical edge_index;
   is_2hop = exactly 2 hops, i.e. within 2 hops and not 1-hop), true_title / true_label from
   {cora,products}_canonical.pt, canonical_pred from data_canonical.pth gnn_preds (= canonical
   GraphSAGE; the prediction_agreement/*_canonical_vs_gspell_full.json files only cover target
   nodes and are used to cross-check those). Class rows (no cited ID) carry the TARGET's
   true_label / canonical_pred. verdict and notes are left blank.
4. Per node: G = 1-hop neighbours given to GSPELL across its batches (+ title, label, pred).
Run in the GSPELL narratives venv. Read-only; writes only into this folder. No model calls.
"""
import csv, json, re, sys
sys.path.insert(0, "./LOGIC2/GSPELL")
import torch
from torch_geometric.utils import k_hop_subgraph, is_undirected, to_undirected

R = "./"
G_ = R + "LOGIC2/GSPELL/"
OUT = R + "gspell_grounding_manual_2026-10-10/"
RUNS = {
    "cora": ("51247846", G_ + "output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-08-16-23-39-47/GSPELL_explanations.pt",
             G_ + "output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth", [510, 2334, 1062, 884]),
    "products": ("50765167", G_ + "output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt",
                 G_ + "output/products-meta-llama/Meta-Llama-3.1-8B-Instruct/data_canonical.pth", [6813, 1852, 8766, 8438]),
}
ROLE = re.compile(r"^\s*assistant\s*\n+", re.I)                          # = stage_a_extract.ROLE
HEADER = re.compile(r"^[\s\-#*]*(?:Article|Product|Paper|Node)\s+#?(\d+)\s*[:*]", re.I)
CITE = re.compile(r"(?:Article|Paper|Product|Node)\s*#?\s*(\d+)|\bID\s*[:#]?\s*(\d+)|<<\s*(\d+)\s*>>", re.I)
KW = re.compile(r"<<\s*BEGIN(?: TARGET)? KEYWORDS\s*>>.*?(?:<<\s*END(?: TARGET)? KEYWORDS\s*>>|\Z)", re.S | re.I)
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(*\[])|\n+")
FIELDS = ["node", "dataset", "batch_idx", "claim_id", "claim_text", "source_span", "claim_kind", "cited_node_id",
          "in_batch", "is_1hop", "is_2hop", "true_title", "true_label", "canonical_pred", "verdict", "notes"]
lines_out = []
P = lambda s="": (print(s), lines_out.append(s))


def title(ds, raw):
    m = re.search(r"Title:\s*(.*?)\.\s*Content:", raw, re.S) if ds == "products" else re.search(r"Title:\s*(.*?)\s*\n", raw)
    return re.sub(r"\s+", " ", (m.group(1) if m else raw[:150])).strip()


def cited_ids(s):
    return [int(next(g for g in m.groups() if g)) for m in CITE.finditer(s)]


# ---------------------------------------------------------------- 2. Table 13 aggregation
P("== 2. Table 13 aggregation (per-node CSVs: grounding_per_node_from_chat.csv precision; recall overlaid from "
  "grounding_recall_verified_per_node.csv for GraphXAIN / CF-GNNExplainer, as in part_a_heatmap.load_grounding)")
pn = {}
for r in csv.DictReader(open(R + "grounding_per_node_from_chat.csv")):
    pn[(r["method"], r["dataset"], r["node"])] = {"p": float(r["precision"]) if r["precision"] else None,
                                                   "r": float(r["recall"]) if r["recall"] else None}
for r in csv.DictReader(open(R + "grounding_recall_verified_per_node.csv")):
    pn.setdefault((r["method"], r["dataset"], r["node"]), {"p": None, "r": None})["r"] = float(r["recall"]) if r["recall"] else None
f1 = lambda p, r: 0.0 if p + r == 0 else 2 * p * r / (p + r)
agg = []
for (m, ds) in sorted({(k[0], k[1]) for k in pn}):
    v = [x for k, x in pn.items() if k[:2] == (m, ds) and x["p"] is not None and x["r"] is not None]
    mp, mr = sum(x["p"] for x in v) / len(v), sum(x["r"] for x in v) / len(v)
    mf = sum(f1(x["p"], x["r"]) for x in v) / len(v)
    agg.append({"method": m, "dataset": ds, "n_nodes": len(v), "mean_precision": mp, "mean_recall": mr,
                "mean_of_per_node_f1": mf, "f1_of_mean_p_mean_r": f1(mp, mr)})
    P(f"   {m:16s} {ds:9s} n={len(v)}  meanP={mp:.3f} meanR={mr:.3f} | mean(per-node F1)={mf:.3f} | F1(meanP,meanR)={f1(mp, mr):.3f}")
gn = next(a for a in agg if a["method"] == "GraphNarrator" and a["dataset"] == "products")
P(f"   GraphNarrator Products: mean of per-node F1 = {gn['mean_of_per_node_f1']:.4f}; F1 of means = {gn['f1_of_mean_p_mean_r']:.4f} "
  f"-> 0.204 comes from {'mean of per-node F1' if round(gn['mean_of_per_node_f1'], 3) == 0.204 else 'F1 of means' if round(gn['f1_of_mean_p_mean_r'], 3) == 0.204 else 'neither'}")
P("   code: grounding_recall_f1.py:676-706 mean() over per-node precision, recall and per-node f1 (f1 computed per node at :351-353)")
with open(OUT + "table13_aggregation_check.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(agg[0])); w.writeheader(); w.writerows(agg)

# ---------------------------------------------------------------- 1, 3, 4
scored = {(r["dataset"], r["node"]): r["text"] for r in json.load(open(R + "gspell_metrics_2026-10-09/final/gspell_per_node_records.json"))}
allrows, summary = [], []
P("\n== 1. Survey nodes present / batches / text identical to scored text")
for ds, (job, pt, dc, nodes) in RUNS.items():
    canon = torch.load(R + f"{ds}_canonical.pt", map_location="cpu", weights_only=False)
    preds = torch.load(dc, map_location="cpu", weights_only=False)["gnn_preds"].cpu()
    agree = json.load(open(R + f"production_run_2026-07-27/prediction_agreement/{ds}_canonical_vs_gspell_full.json"))["per_node"]
    ei = canon.edge_index if is_undirected(canon.edge_index) else to_undirected(canon.edge_index)
    P(f"{ds}: edge_index undirected as stored: {is_undirected(canon.edge_index)}")
    labels = list(canon.label_names)
    lab = lambda i: labels[int(canon.y[i])]
    prd = lambda i: labels[int(preds[i])]
    run = {n[0]["target_node"]: n for n in torch.load(pt, map_location="cpu", weights_only=False)}
    for node in nodes:
        assert node in run, f"{ds} {node} missing"
        a = agree[str(node)]
        assert a["true_label"] == lab(node) and a["canonical_pred"] == prd(node), (node, a)
        batches = run[node]
        h1 = set(k_hop_subgraph(node, 1, ei, num_nodes=canon.num_nodes)[0].tolist()) - {node}
        h2 = set(k_hop_subgraph(node, 2, ei, num_nodes=canon.num_nodes)[0].tolist()) - {node} - h1
        texts = [ROLE.sub("", b.get("explanation") or "", count=1).strip() for b in batches]
        joined = "\n\n".join(t for t in texts if t)
        same = joined == scored[(ds, node)]
        given = [n for b in batches for n in b["neighbors"]]
        P(f"   {ds} {node}: present, {len(batches)} batches, {len(given)} neighbour IDs given "
          f"({len(set(given) & h1)} 1-hop, {len(set(given) & h2)} 2-hop); joined text == scored text: {same}")
        assert same
        json.dump({"dataset": ds, "job": job, "node": node, "true_label": lab(node), "canonical_pred": prd(node),
                   "batches": [{"batch_idx": i, "neighbors": b["neighbors"], "text": t} for i, (b, t) in enumerate(zip(batches, texts))],
                   "joined_text": joined}, open(OUT + f"batches_{ds}_{node}.json", "w"), indent=1)
        open(OUT + f"joined_text_{ds}_{node}.txt", "w").write(joined + "\n")

        def info(n):
            if n is None or n >= canon.num_nodes:
                return {"true_title": "" if n is None else "(no such node)", "true_label": "", "canonical_pred": ""}
            return {"true_title": title(ds, canon.raw_text[n]), "true_label": lab(n), "canonical_pred": prd(n)}

        rows, k = [], [0]

        def add(bi, kind, text, span, cid, batch_ids, target_info=False):
            k[0] += 1
            r = {"node": node, "dataset": ds, "batch_idx": bi, "claim_id": f"{ds}-{node}-b{bi}-c{k[0]:03d}",
                 "claim_text": re.sub(r"\s+", " ", text).strip(), "source_span": span, "claim_kind": kind,
                 "cited_node_id": "" if cid is None else cid,
                 "in_batch": "" if cid is None else cid in batch_ids,
                 "is_1hop": "" if cid is None else cid in h1, "is_2hop": "" if cid is None else cid in h2,
                 **(info(cid) if cid is not None else ({"true_title": "", "true_label": lab(node), "canonical_pred": prd(node)}
                                                       if target_info else {"true_title": "", "true_label": "", "canonical_pred": ""})),
                 "verdict": "", "notes": ""}
            rows.append(r)

        def prose(bi, seg, batch_ids):
            for s in (x.strip() for x in SENT.split(seg)):
                if not s:
                    continue
                ids = [i for i in dict.fromkeys(cited_ids(s))]
                for kwm in KW.finditer(s):
                    add(bi, "feature", kwm.group(0), kwm.group(0), None, batch_ids)
                s_nokw = KW.sub("", s).strip()
                if ids:
                    for i in ids:
                        add(bi, "neighbor_content", s, s, i, batch_ids)
                elif any(l.lower() in s.lower() for l in labels) or re.search(r"classif|categor", s, re.I):
                    add(bi, "class", s, s, None, batch_ids, target_info=True)
                elif len(s_nokw.split()) >= 4:
                    add(bi, "other", s, s, None, batch_ids)

        for bi, (b, t) in enumerate(zip(batches, texts)):
            batch_ids = set(map(int, b["neighbors"]))
            blines = t.split("\n")
            starts = [j for j, l in enumerate(blines) if HEADER.match(l)]
            # preamble
            prose(bi, "\n".join(blines[:starts[0]] if starts else blines), batch_ids)
            for si, j in enumerate(starts):
                end = starts[si + 1] if si + 1 < len(starts) else len(blines)
                block = blines[j:end]
                cid = int(HEADER.match(blines[j]).group(1))
                # closing paragraph: after the last Support line, separated by a blank line
                tail = []
                if si + 1 == len(starts):
                    sup = [x for x, l in enumerate(block) if re.search(r"Support\s*:", l, re.I)]
                    if sup:
                        after = block[sup[-1] + 1:]
                        blank = next((x for x, l in enumerate(after) if not l.strip()), None)
                        if blank is not None:
                            tail = after[blank:]
                            block = block[:sup[-1] + 1 + blank]
                add(bi, "neighbor_exists", f"{'Article' if ds == 'cora' else 'Product'} {cid} is a neighbour of the target",
                    blines[j].strip(), cid, batch_ids)
                body = "\n".join(block[1:]) if HEADER.match(blines[j]).end() >= len(blines[j].rstrip()) else \
                    blines[j][HEADER.match(blines[j]).end():] + "\n" + "\n".join(block[1:])
                for kwm in KW.finditer(body):
                    add(bi, "feature", kwm.group(0), kwm.group(0), cid, batch_ids)
                body = KW.sub("\n", body)
                for l in (x.strip() for x in body.split("\n")):
                    if not l:
                        continue
                    if re.match(r"[\W_]*Summary\s*:", l, re.I):
                        add(bi, "neighbor_content", l, l, cid, batch_ids)
                        for i in dict.fromkeys(cited_ids(l)):
                            if i != cid:
                                add(bi, "neighbor_content", l, l, i, batch_ids)
                    elif re.match(r"[\W_]*Support\s*:", l, re.I):
                        add(bi, "support_verdict", l, l, cid, batch_ids)
                    else:
                        ids = [i for i in dict.fromkeys(cited_ids(l)) if i != cid]
                        for i in ids:
                            add(bi, "neighbor_content", l, l, i, batch_ids)
                        if not ids and len(l.split()) >= 4:
                            add(bi, "other", l, l, cid, batch_ids)
                if tail:
                    prose(bi, "\n".join(tail), batch_ids)

        with open(OUT + f"claims_{ds}_{node}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
        allrows += rows
        # 4. G
        G = sorted(dict.fromkeys(n for n in given if n in h1))
        with open(OUT + f"G_{ds}_{node}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["neighbor_id", "title", "true_label", "canonical_pred", "batches"])
            w.writeheader()
            for n in G:
                w.writerow({"neighbor_id": n, "title": title(ds, canon.raw_text[n]), "true_label": lab(n), "canonical_pred": prd(n),
                            "batches": " ".join(str(i) for i, b in enumerate(batches) if n in b["neighbors"])})
        kinds = {}
        for r in rows:
            kinds[r["claim_kind"]] = kinds.get(r["claim_kind"], 0) + 1
        summary.append({"dataset": ds, "node": node, "job": job, "true_label": lab(node), "canonical_pred": prd(node),
                        "n_batches": len(batches), "n_ids_given": len(given), "G_size_1hop_given": len(G),
                        "true_1hop_total": len(h1), "1hop_not_given": " ".join(map(str, sorted(h1 - set(given)))),
                        "n_claims": len(rows), **{f"n_{k}": kinds.get(k, 0) for k in
                        ("neighbor_exists", "neighbor_content", "class", "feature", "support_verdict", "other")},
                        "n_claims_citing_id_not_in_batch": sum(r["in_batch"] is False for r in rows),
                        "n_claims_citing_non_neighbor": sum(r["cited_node_id"] != "" and not r["is_1hop"] and not r["is_2hop"] for r in rows)})

with open(OUT + "claims_all_nodes.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(allrows)
with open(OUT + "node_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(summary[0])); w.writeheader(); w.writerows(summary)
P("\n== 3/4. Claims per node")
for s in summary:
    P(f"   {s['dataset']:9s}{s['node']:6d}  claims {s['n_claims']:4d} | exists {s['n_neighbor_exists']}, content {s['n_neighbor_content']}, "
      f"class {s['n_class']}, feature {s['n_feature']}, verdict {s['n_support_verdict']}, other {s['n_other']} | "
      f"G {s['G_size_1hop_given']}/{s['true_1hop_total']} 1-hop | cited ID not in batch {s['n_claims_citing_id_not_in_batch']}, "
      f"not within 2 hops {s['n_claims_citing_non_neighbor']}")
P(f"   total claims {len(allrows)}")
open(OUT + "results.txt", "w").write("\n".join(lines_out) + "\n")
