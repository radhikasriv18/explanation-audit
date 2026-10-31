#!/usr/bin/env python3
"""Step 1: reference packet per survey node (read-only on all inputs; no model calls).

Sources
- claims:  gspell_grounding_manual_2026-10-10/claims_<ds>_<node>_v4.csv
- title / text / true label: {cora,products}_canonical.pt (raw_text, y, label_names)
- canonical prediction: gnn_preds in GSPELL's data_canonical.pth (= canonical GraphSAGE), same files as
  gspell_grounding_manual_2026-10-10/build_labeling_sheets.py
- hop distance: canonical edge_index made undirected; 1, 2, "not within 2 hops", "does not exist"

Cited nodes = every cited_node_id in the sheet plus every ID matched by the sheets' CITE regex in any claim text.
Target text: first 1000 chars (after the title); cited nodes: first 300 chars, as specified.
Writes packets/packet_<ds>_<node>.json and packets/packet_<ds>_<node>.txt (the text block used in the prompt).
"""
import csv, json, os, re, sys
from collections import deque
import torch
sys.path.insert(0, "./LOGIC2/GSPELL")  # unpickling data_canonical.pth needs GSPELL's modules

R = "./"
OUT = R + "grounding_judge_2026-10-13/packets/"
os.makedirs(OUT, exist_ok=True)
SHEETS = R + "gspell_grounding_manual_2026-10-10/"
G_ = R + "LOGIC2/GSPELL/output/"
PREDS = {"cora": G_ + "cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth",
         "products": G_ + "products-meta-llama/Meta-Llama-3.1-8B-Instruct/data_canonical.pth"}
NODES = {"cora": [510, 2334, 1062, 884], "products": [6813, 1852, 8766, 8438]}
CITE = re.compile(r"(?:Article|Paper|Product|Node)\s*#?\s*(\d+)|\bID\s*[:#]?\s*(\d+)|<<\s*(\d+)\s*>>", re.I)  # = build_labeling_sheets.CITE
csv.field_size_limit(sys.maxsize)


def split_raw(ds, raw):
    """(title, body) from raw_text; title rule = build_labeling_sheets.title()."""
    if ds == "products":
        m = re.search(r"Title:\s*(.*?)\.\s*Content:\s*(.*)", raw, re.S)
    else:
        m = re.search(r"Title:\s*(.*?)\s*\n\s*(?:Abstract:)?\s*(.*)", raw, re.S)
    if not m:
        return re.sub(r"\s+", " ", raw[:150]).strip(), raw
    return re.sub(r"\s+", " ", m.group(1)).strip(), re.sub(r"\s+", " ", m.group(2)).strip()


def hops_from(adj, src, n):
    dist, q = {src: 0}, deque([src])
    while q:
        u = q.popleft()
        if dist[u] == 2:
            continue
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


index = []
for ds, nodes in NODES.items():
    canon = torch.load(R + f"{ds}_canonical.pt", map_location="cpu", weights_only=False)
    preds = torch.load(PREDS[ds], map_location="cpu", weights_only=False)["gnn_preds"].cpu()
    labels = list(canon.label_names)
    N = int(canon.num_nodes)
    assert preds.shape[0] == N
    adj = [[] for _ in range(N)]
    for a, b in canon.edge_index.t().tolist():
        if a != b:
            adj[a].append(b); adj[b].append(a)
    lab = lambda i: labels[int(canon.y[i])]
    prd = lambda i: labels[int(preds[i])]
    for t in nodes:
        rows = list(csv.DictReader(open(SHEETS + f"claims_{ds}_{t}_v4.csv")))
        ids = set()
        for r in rows:
            if r["cited_node_id"] != "":
                ids.add(int(r["cited_node_id"]))
            for m in CITE.finditer(r["claim_text"]):
                ids.add(int(next(g for g in m.groups() if g)))
        ids.discard(t)
        dist = hops_from(adj, t, N)
        ttl, body = split_raw(ds, canon.raw_text[t])
        cited = []
        for i in sorted(ids):
            if i >= N:
                cited.append({"id": i, "hop": "does not exist"}); continue
            h = dist.get(i)
            ci, cb = split_raw(ds, canon.raw_text[i])
            cited.append({"id": i, "hop": h if h in (1, 2) else "not within 2 hops", "title": ci, "text_300": cb[:300],
                          "true_label": lab(i), "canonical_pred": prd(i)})
        pk = {"dataset": ds, "target": {"id": t, "title": ttl, "text_1000": body[:1000], "true_label": lab(t),
                                        "canonical_pred": prd(t)},
              "label_set": labels, "cited": cited}
        # prompt text block
        unit = "paper" if ds == "cora" else "product"
        L = [f"TARGET {unit} {t}", f"  title: {ttl}", f"  text: {body[:1000]}", f"  true label: {lab(t)}",
             f"  GNN (canonical) prediction: {prd(t)}", "",
             f"CITED NODES ({len(cited)}) - every node ID mentioned in the explanation:"]
        for c in cited:
            if c["hop"] == "does not exist":
                L.append(f"- {unit} {c['id']}: DOES NOT EXIST (dataset has {N} nodes, IDs 0-{N - 1})"); continue
            hop = {1: "1-hop (direct neighbor)", 2: "2-hop (neighbor of a neighbor, NOT a direct neighbor)"}.get(c["hop"], "NOT within 2 hops of the target")
            L += [f"- {unit} {c['id']}  [{hop}]", f"    title: {c['title']}", f"    text: {c['text_300']}",
                  f"    true label: {c['true_label']}; GNN prediction: {c['canonical_pred']}"]
        L += ["", f"Valid class labels: {', '.join(labels)}"]
        json.dump(pk, open(OUT + f"packet_{ds}_{t}.json", "w"), indent=1)
        open(OUT + f"packet_{ds}_{t}.txt", "w").write("\n".join(L) + "\n")
        hc = {k: sum(str(c["hop"]) == k for c in cited) for k in ("1", "2", "not within 2 hops", "does not exist")}
        index.append({"dataset": ds, "node": t, "claims": len(rows), "cited_nodes": len(cited), **{f"hop_{k}": v for k, v in hc.items()},
                      "packet_chars": len("\n".join(L))})
        print(index[-1])
with open(OUT + "packet_index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(index[0])); w.writeheader(); w.writerows(index)
