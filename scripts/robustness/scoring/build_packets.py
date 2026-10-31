"""Reference packets for the robustness texts: packets/<text id>.md, one per text in texts.json.

Same layout and helpers as grounding_judge_pilot/build_reference_packets.py (title_of, label_of,
fence, md_cell, neighbor_section, gn_label_mapping, canonical data/adjacency and PRED are imported
from it unchanged). Sections: 1 explanation (full text), 2 prompt the model received,
3 target node, 4 canonical 1-hop / 2-hop neighbors, 5 the method's own evidence.
Only the evidence sources differ from the survey packets, because these texts come from the
production / robustness runs:
  GraphNarrator  pkls_cora_eval / pkls_products at the pkl index (= cf_key), the pkls behind
                 exp100/101. The prompts are 6000-char truncated, so the check is that the
                 truncated verbalized graph appears verbatim in the persisted user prompt. Labels
                 visible in that prompt are marked.
  GraphXAIN      top-7 features parsed from the locked schema-aligned prompt (prompts_dump.jsonl);
                 GNNExplainer neighbors are in the prompt itself (section 2).
  CF             llm-graph-cf/data/<ds>/cf-gnnexplainer-canonical/random_seed_42_* files:
                 factual / counterfactual target dicts and removed edges (global ids).
Section 1 differs per configuration; sections 2-5 are identical for the 3 configurations of a
method at a node. GraphNarrator's section 2 shows the system message gen() actually sent
(exp100/101 files record save()'s default string instead).

Run with ~/.conda/envs/graphnarr/bin/python (torch_geometric + tag.py).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "./grounding_judge_pilot")
import build_reference_packets as brp  # noqa: E402  (module import only reads sources)
from build_reference_packets import TAG, adj, data, fence, gn_label_mapping, label_of, md_cell, neighbor_section, title_of  # noqa: E402

R = Path(".")
HERE = Path(__file__).resolve().parent
OUT = HERE / "packets"
GN_PKL = {"cora": R / "graphnarrCora/GraphNarrator/outputs/pkls_cora_eval",
          "products": R / "graphnarrCora/GraphNarrator/outputs/pkls_products"}
GN_PROMPT = {"cora": R / "graphnarrCora/GraphNarrator/outputs/generated_expls-100",
             "products": R / "graphnarrCora/GraphNarrator/outputs/generated_expls-101"}
GN_SYSTEM = "You are a helpful, reliable and responsible AI assistant."
GX_DUMP = {ds: {json.loads(l)["target_node"]: json.loads(l) for l in open(R / f"graphxain_schemaaligned_production_2026-08-16/{ds}/prompts_dump.jsonl")}
           for ds in ("cora", "products")}
CF_DIR = R / "llm-graph-cf/data"
CF_MSG = R / "robustness_2026-10-30/llama70b/cf"
GX_FEAT_RE = re.compile(r"word='([^']*)', importance=([0-9.]+), present_in_\w+=(\d)")


def gn_evidence(e):
    pkl = GN_PKL[e["dataset"]] / f"{e['cf_key']}.pkl"
    g = TAG.load(pkl)
    assert str(g.root_global_id) == e["node"], (pkl, g.root_global_id, e["node"])
    user = json.load(open(GN_PROMPT[e["dataset"]] / f"{e['cf_key']}.json"))["messages"][1]["content"]
    doc = g.text(style="document", masker="", with_score=True)
    assert doc[:6000] in user, "pkl does not reproduce the prompt's verbalized graph"
    labels = gn_label_mapping(g)
    shown = doc[:6000]
    order = sorted(labels, key=lambda k: [0] if labels[k] == "ROOT" else [1] + [int(x) for x in labels[k][5:].split(".")])
    visible = lambda lab: re.search(rf"(?m)^{re.escape(lab)}:", shown) is not None
    out = [
        "## 5. Method evidence: GraphNarrator saliency scores per token",
        "",
        f"Source: `{pkl}` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).",
        f"GraphNarrator's own GNN recorded prediction = **{g.prediction}**, ground truth = **{g.ground_truth}**.",
        f"The verbalized graph is {len(doc)} characters; the model saw the first 6000"
        + (" (the whole graph)." if len(doc) <= 6000 else ", so nodes marked 'no' below were cut from its prompt."),
        "Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.",
        "",
        "### Subgraph nodes",
        "",
        "| label | local idx | global id | n tokens | max score | in prompt |",
        "|---|---|---|---|---|---|",
    ]
    for k in order:
        nd = g.nodes[k]
        out.append(f"| {labels[k]} | {k} | {g.global_nids[k]} | {len(nd.features)} | {max(nd.importance_scores):.4f} | "
                   f"{'yes' if visible(labels[k]) else 'no'} |")
    unl = [k for k in range(len(g.nodes)) if k not in labels]
    if unl:
        out.append(f"\nNodes in the pkl not reached by the BFS labelling (not shown in the prompt): {unl}")
    edges = sorted({(labels.get(s, s), labels.get(t, t)) for s, t in zip(*g.edges)})
    out += ["", f"Subgraph edges (src -> dst, as stored): {', '.join(f'{a}->{b}' for a, b in edges)}", "", "### Tokens and scores"]
    for k in order:
        nd = g.nodes[k]
        toks = " ".join(f"{t} ({s:.4f})" for t, s in zip(nd.features, nd.importance_scores))
        out += ["", f"**{labels[k]}** (global {g.global_nids[k]}):", "", fence(toks)]
    prompt = ("Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; "
              f"user message verbatim from `{GN_PROMPT[e['dataset']]}/{e['cf_key']}.json`).",
              [("system", GN_SYSTEM), ("user", user)])
    return out, prompt, g.prediction, {labels[k]: g.global_nids[k] for k in labels}


def gx_evidence(e):
    rec = GX_DUMP[e["dataset"]][int(e["node"])]
    feats = GX_FEAT_RE.findall(rec["prompt"])
    assert len(feats) == 7, (e["id"], len(feats))
    out = [
        "## 5. Method evidence: GraphXAIN (GNNExplainer)",
        "",
        f"Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/{e['dataset']}/prompts_dump.jsonl`, target_node={e['node']}).",
        f"Recorded prediction: `{json.dumps(rec['prediction'])}`",
        f"Recorded graph stats: `{json.dumps(rec['graph_stats'])}`",
        "",
        "### Top-7 features (GNNExplainer node mask), as given to the model",
        "",
        "| rank | word | importance | present in target |",
        "|---|---|---|---|",
    ]
    out += [f"| {i} | {w} | {imp} | {p} |" for i, (w, imp, p) in enumerate(feats, 1)]
    out += ["", "The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2)."]
    prompt = ("`prompt` field of the record (sent as the single user message).", [("user", rec["prompt"])])
    return out, prompt, rec["prediction"].get("Predicted Class"), {}


def cf_evidence(e):
    ds, key = e["dataset"], e["cf_key"]
    base = CF_DIR / ds / "cf-gnnexplainer-canonical/random_seed_42_"
    fd = json.load(open(str(base) + "factual_target_dict_repr.json"))[key]
    cd = json.load(open(str(base) + "counterfactual_target_dict_repr.json"))[key]
    removed = json.load(open(str(base) + "cf_removed_edges.json"))[key]
    assert str(fd["Target_Node_ID"]) == e["node"], (e["id"], fd["Target_Node_ID"])
    msgs = json.load(open(CF_MSG / ds / f"{e['node']}.json"))["messages"]
    fclass = fd.get("Factual_Target_Node_Class")
    cclass = fd.get("Counterfactual_Target_Node_class", cd.get("Counterfactual_Target_Node_class"))
    out = [
        "## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)",
        "",
        f"Source: `{base}*` (key={key}).",
        "",
        f"- Factual class: **{fclass}**",
        f"- Counterfactual class: **{cclass}**",
        f"- Removed edges (global ids, {len(removed)}): {', '.join(f'({a}, {b})' for a, b in removed)}",
        "",
        "### Factual target dict",
        "",
        "| field | value |",
        "|---|---|",
    ]
    out += [f"| {k} | {md_cell(v)} |" for k, v in fd.items()]
    out += ["", "### Counterfactual target dict", "", "| field | value |", "|---|---|"]
    out += [f"| {k} | {md_cell(v)} |" for k, v in cd.items()]
    prompt = ("Chat messages (system + user) built by llm-graph-cf's prompt code; identical for every CF configuration.",
              [(m["role"], m["content"]) for m in msgs])
    return out, prompt, fclass, {}


def main():
    OUT.mkdir(exist_ok=True)
    texts = json.load(open(HERE / "texts.json"))
    gn_maps = {}
    for e in texts:
        ds, node = e["dataset"], int(e["node"])
        ev, (pdesc, pmsgs), method_pred, labmap = {"GraphNarrator": gn_evidence, "GraphXAIN": gx_evidence,
                                                    "CF-GNNExplainer": cf_evidence}[e["method"]](e)
        if e["method"] == "GraphNarrator":
            gn_maps[f"{ds}:{node}"] = labmap
        canon = brp.PRED[ds][str(node)]
        assert canon["true_label"] == label_of(ds, node)
        lines = [
            f"# Reference packet: {e['id']}",
            "",
            f"- Method: {e['method']}; configuration: {e['config']}; dataset: {ds}; target node: {node}",
            f"- Explanation source: `{e['source_file']}` ({e['source_locator']})",
            f"- Scored scope (what the claims were extracted from): {e['scored_scope']}",
            "- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).",
            "",
            "## 1. Explanation (full text)",
            "",
        ]
        if e["method"] == "GraphNarrator":
            lines += ["Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.", ""]
        lines += [fence(e["text_full"]), "", "## 2. Prompt the method's model received", "", pdesc, ""]
        for role, content in pmsgs:
            lines += [f"**{role}:**", "", fence(content), ""]
        lines += [
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
        lines += neighbor_section(ds, node)
        lines += ev
        (OUT / f"{e['id']}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    json.dump(gn_maps, open(HERE / "gn_label_maps.json", "w"), indent=1)
    print(f"{len(texts)} packets written to {OUT}; GraphNarrator label maps for {len(gn_maps)} nodes")


if __name__ == "__main__":
    main()
