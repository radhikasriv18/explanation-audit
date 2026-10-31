"""
Build one reference packet per answer-key text: reference_packets/<id>.md (no model call;
read-only on all sources).

Each packet contains:
  1. the full explanation text (and, for GraphNarrator, which part was scored);
  2. the exact prompt the method's model received, as persisted:
       GraphNarrator  messages (system + user) in the generated_expls JSON
       GraphXAIN      "prompt" field of explainer_and_prompts.jsonl
       CF            "llm_prompt" field of the survey_nodes JSON (full rendered chat template);
  3. the target node: ID, title, canonical text, true class, canonical-SAGE predicted class,
     plus the prediction the method itself recorded;
  4. 1-hop and 2-hop neighbors (IDs, titles, true class) computed from edge_index in the
     canonical .pt (locked decision); 2-hop = nodes at shortest distance exactly 2;
  5. the method's own recorded evidence:
       GraphNarrator  per-token saliency scores for every node in the verbalized subgraph,
                      from the pkl that produced the prompt (outputs/pkls for Cora exp_id=3,
                      outputs/pkls_products for Products; verified: TAG.text() is contained
                      verbatim in each prompt). Node-X labels are rebuilt with the same BFS
                      labelling as tag.neighborhood_corpus.
       GraphXAIN      GNNExplainer top-7 features with importance values and the 1-hop/2-hop
                      GNNExplainer neighbors with edge importance, from the jsonl record.
       CF            factual / counterfactual class, removed edges (global ids), and the
                      factual / counterfactual target dicts.

Run with ~/.conda/envs/graphnarr/bin/python (needs torch_geometric + tag.py).
"""
import json
import re
import sys
from pathlib import Path

import torch

ROOT = Path(".")
GN = ROOT / "graphnarrCora/GraphNarrator"
sys.path.insert(0, str(GN))
from tag import TAG, bfs_edges  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "reference_packets"
AK = json.load(open(HERE / "answer_key_texts.json"))
GN_PKL = {"cora": GN / "outputs/pkls", "products": GN / "outputs/pkls_products"}
PRED = {ds: json.load(open(ROOT / f"production_run_2026-07-27/prediction_agreement/{ds}_canonical_vs_gspell_full.json"))["per_node"] for ds in ["cora", "products"]}
FENCE = "~~~~~~"

data = {ds: torch.load(ROOT / f"{ds}_canonical.pt", weights_only=False) for ds in ["cora", "products"]}
adj = {}
for ds, d in data.items():
    a = [set() for _ in range(d.num_nodes)]
    for s, t in d.edge_index.t().tolist():
        if s != t:
            a[s].add(t)
            a[t].add(s)
    adj[ds] = a


def title_of(ds, nid):
    t = data[ds].raw_text[nid]
    if ds == "cora":
        m = re.search(r"Title:\s*(.*?)\s*(?:\n|Abstract:|$)", t)
    else:
        m = re.search(r"Title:\s*(.*?)(?:\.\s*Content:|\s*Content:|$)", t, re.S)
    return (m.group(1) if m else t[:120]).strip()


def label_of(ds, nid):
    return data[ds].label_names[int(data[ds].y[nid])]


def fence(text):
    assert FENCE not in text
    return f"{FENCE}text\n{text}\n{FENCE}"


def md_cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def neighbor_section(ds, node):
    one = sorted(adj[ds][node])
    two = sorted(set().union(*[adj[ds][u] for u in one]) - set(one) - {node}) if one else []
    out = [f"## 4. Neighbors (canonical `edge_index`, `{ds}_canonical.pt`)", ""]
    for name, ids in [("1-hop", one), ("2-hop (shortest distance exactly 2)", two)]:
        out += [f"### {name}: {len(ids)} nodes", "", "| node id | true class | title |", "|---|---|---|"]
        out += [f"| {i} | {label_of(ds, i)} | {md_cell(title_of(ds, i))} |" for i in ids]
        out.append("")
    return out


def gn_label_mapping(g):
    """Same BFS labelling as tag.neighborhood_corpus: local index -> 'ROOT' / 'Node-1.2'."""
    G = g.to_filtered_networkx(None)
    mapping = {0: "ROOT"}
    old_depth, cur = 0, {}
    for parent, child, depth in bfs_edges(G, source=0):
        if depth != old_depth:
            cur, old_depth = {}, depth
        cur[parent] = cur.get(parent, 0) + 1
        mapping[child] = f"{cur[parent]}" if depth == 1 else f"{mapping[parent]}.{cur[parent]}".replace("ROOT.", "")
    return {k: (v if v == "ROOT" else f"Node-{v}") for k, v in mapping.items()}


def gn_evidence(e):
    pos = int(Path(e["source_file"]).stem)
    pkl = GN_PKL[e["dataset"]] / f"{pos}.pkl"
    g = TAG.load(pkl)
    assert g.root_global_id == e["node"]
    msgs = {m["role"]: m["content"] for m in json.load(open(e["source_file"]))["messages"]}
    assert g.text() in msgs["user"], "pkl does not reproduce the prompt's verbalized graph"
    labels = gn_label_mapping(g)
    order = sorted(labels, key=lambda k: [0] if labels[k] == "ROOT" else [1] + [int(x) for x in labels[k][5:].split(".")])
    out = [
        "## 5. Method evidence: GraphNarrator saliency scores per token",
        "",
        f"Source: `{pkl}` (verified: `TAG.text()` of this pkl appears verbatim in the prompt).",
        f"GraphNarrator's own GNN recorded prediction = **{g.prediction}**, ground truth = **{g.ground_truth}**.",
        "Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals; the prompt shows them as displayed by `to_string()`.",
        "",
        "### Subgraph nodes",
        "",
        "| label | local idx | global id | n tokens | max score |",
        "|---|---|---|---|---|",
    ]
    for k in order:
        nd = g.nodes[k]
        out.append(f"| {labels[k]} | {k} | {g.global_nids[k]} | {len(nd.features)} | {max(nd.importance_scores):.4f} |")
    unl = [k for k in range(len(g.nodes)) if k not in labels]
    if unl:
        out.append(f"\nNodes in the pkl not reached by the BFS labelling (not shown in the prompt): {unl}")
    edges = sorted({(labels.get(s, s), labels.get(t, t)) for s, t in zip(*g.edges)})
    out += ["", f"Subgraph edges (src -> dst, as stored): {', '.join(f'{a}->{b}' for a, b in edges)}", "", "### Tokens and scores"]
    for k in order:
        nd = g.nodes[k]
        toks = " ".join(f"{t} ({s:.4f})" for t, s in zip(nd.features, nd.importance_scores))
        out += ["", f"**{labels[k]}** (global {g.global_nids[k]}):", "", fence(toks)]
    return out, msgs, g.prediction


def gx_evidence(e):
    rec = None
    for line in open(e["source_file"]):
        if line.strip():
            r = json.loads(line)
            if r["target_node"] == e["node"]:
                rec = r
    out = [
        "## 5. Method evidence: GraphXAIN (GNNExplainer)",
        "",
        f"Source: `{e['source_file']}` (record target_node={e['node']}).",
        f"Recorded prediction: `{json.dumps(rec['prediction'])}`",
        "",
        "### Top-7 features (GNNExplainer node mask)",
        "",
        "| rank | word | importance | present in target | dim |",
        "|---|---|---|---|---|",
    ]
    for i, f in enumerate(rec["gnnexplainer_top_features"], 1):
        out.append(f"| {i} | {f['word']} | {f['importance']} | {f.get('present', '')} | {f.get('dim', '')} |")
    for hop in ["1hop", "2hop"]:
        rows = rec.get(f"gnnexplainer_{hop}_neighbors", [])
        out += ["", f"### GNNExplainer {hop[0]}-hop neighbors (edge importance, as given to the model): {len(rows)}", "", "| node | importance | class | text (as given) |", "|---|---|---|---|"]
        out += [f"| {r['node']} | {r.get('importance', '')} | {r.get('class', '')} | {md_cell(r.get('text', ''))[:200]} |" for r in rows]
    return out, {"prompt": rec["prompt"]}, rec["prediction"].get("Predicted Class")


def cf_evidence(e):
    rec = next(r for r in json.load(open(e["source_file"])) if r["node_id"] == e["node"])
    fd, cd = rec["factual_target_dict"], rec["counterfactual_target_dict"]
    out = [
        "## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)",
        "",
        f"Source: `{e['source_file']}` (node_id={e['node']}, explainer_key={rec['explainer_key']}).",
        "",
        f"- Factual class: **{fd['Factual_Target_Node_Class']}**",
        f"- Counterfactual class: **{fd['Counterfactual_Target_Node_class']}**",
        f"- Removed edges (global ids, {len(rec['removed_edges_global'])}): {', '.join(f'({a}, {b})' for a, b in rec['removed_edges_global'])}",
        "",
        "### Factual target dict",
        "",
        "| field | value |",
        "|---|---|",
    ]
    out += [f"| {k} | {md_cell(v)} |" for k, v in fd.items()]
    out += ["", "### Counterfactual target dict", "", "| field | value |", "|---|---|"]
    out += [f"| {k} | {md_cell(v)} |" for k, v in cd.items()]
    return out, {"llm_prompt": rec["llm_prompt"]}, fd["Factual_Target_Node_Class"]


def main():
    OUT.mkdir(exist_ok=True)
    for e in AK:
        ds, node = e["dataset"], e["node"]
        ev, prompt, method_pred = {"GraphNarrator": gn_evidence, "GraphXAIN": gx_evidence, "CF-GNNExplainer": cf_evidence}[e["method"]](e)
        canon = PRED[ds][str(node)]
        lines = [
            f"# Reference packet: {e['id']}",
            "",
            f"- Method: {e['method']}; dataset: {ds}; target node: {node}",
            f"- Explanation source: `{e['source_file']}` ({e['source_locator']})",
            f"- Scored scope (what the claims were extracted from): {e['scored_scope']}",
            "- Built by `build_reference_packets.py` (read-only on all sources, no model call).",
            "",
            "## 1. Explanation (full text)",
            "",
        ]
        if e["method"] == "GraphNarrator":
            lines += ["Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.", ""]
        lines += [fence(e["text_full"]), "", "## 2. Prompt the method's model received (as persisted)", ""]
        if e["method"] == "GraphNarrator":
            sysmsg = {m["role"]: m["content"] for m in json.load(open(e["source_file"]))["messages"]}.get("system", "")
            lines += ["Chat messages from the generation record (`messages`).", "", "**system:**", "", fence(sysmsg), "", "**user:**", "", fence(prompt["user"])]
        elif e["method"] == "GraphXAIN":
            lines += ["`prompt` field of the record (the text passed to the generator).", "", fence(prompt["prompt"])]
        else:
            lines += ["`llm_prompt` field (full rendered Llama-3.1 chat template).", "", fence(prompt["llm_prompt"])]
        lines += [
            "",
            "## 3. Target node",
            "",
            f"- ID: {node}",
            f"- Title: {title_of(ds, node)}",
            f"- True class (canonical `y`): **{label_of(ds, node)}**",
            f"- Predicted class, canonical GraphSAGE (`prediction_agreement/{ds}_canonical_vs_gspell_full.json`): **{canon['canonical_pred']}**",
            f"- Prediction recorded by this method's pipeline: **{method_pred}**",
            "",
            "Canonical text (`raw_text`):",
            "",
            fence(data[ds].raw_text[node]),
            "",
        ]
        assert canon["true_label"] == label_of(ds, node)
        lines += neighbor_section(ds, node)
        lines += ev
        (OUT / f"{e['id']}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{e['id']}.md  {sum(len(l) for l in lines)//1000} kB-ish  1hop={len(adj[ds][node])}")


if __name__ == "__main__":
    main()
