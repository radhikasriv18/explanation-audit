"""
Manual-labeling sheets for the 21 answer-key texts (GraphNarrator 8, GraphXAIN 8, CF-GNNExplainer 5).

Read-only on every existing file; writes only into this folder.
Run:  PYTHONDONTWRITEBYTECODE=1 ~/.conda/envs/graphnarr/bin/python build_labeling_sheets.py

Inputs
  claims        grounding_judge_pilot/claim_answer_key_v4.csv (262 claims)
  references    the same sources grounding_judge_pilot/build_reference_packets.py used for
                reference_packets/<id>.md (imported, not re-implemented): canonical .pt graphs,
                GraphNarrator pkls, GraphXAIN explainer_and_prompts.jsonl, CF survey_nodes JSON,
                canonical predictions (prediction_agreement/*_canonical_vs_gspell_full.json)
  carried-over  GraphXAIN_cora_2334: graphxain_grounding_precision_RULEBASED_v2.json facts
  recall set G  (as scored in Table 14)
                GraphNarrator Cora      grounding_recall_cora_freetext.json  [freetext_only_CURRENT].important_set
                GraphNarrator Products  graphnarrator_products_recall_f1_untruncated.json  important_set_detail
                GraphXAIN               grounding_recall_f1_results.json [graphxain].real_top7_features,
                                        duplicate words collapsed (grounding_recall_verified_per_node.csv)
                CF-GNNExplainer         grounding_recall_f1_results.json [cf_gnnexplainer].real_removed_edges

Outputs (this folder)
  claims_<method>_<ds>_<node>.csv   one row per claim; reference columns; suggested_verdict/suggest_reason
                                    only where mechanical; verdict/corrected_type/note blank for labeling
  G_<method>_<ds>_<node>.csv        recall set G with the Table-14 "mentioned" flag and a blank
                                    mentioned_relabel column
  summary.csv                       per-text counts
"""
import csv
import json
import re
import sys
from collections import deque
from pathlib import Path

import pandas as pd
from nltk.stem import PorterStemmer

ROOT = Path(".")
PILOT = ROOT / "grounding_judge_pilot"
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(PILOT))
import build_reference_packets as brp  # noqa: E402  (loads canonical graphs, tag.py, predictions)

STEM = PorterStemmer().stem
RECALL = ROOT / "grounding_recall_f1_2026-09-07"
KEEP = ["claim_id", "claim_text", "source_span", "claim_type", "span_check"]

claims = pd.read_csv(PILOT / "claim_answer_key_v4.csv", dtype=str).fillna("")
AK = {e["id"]: e for e in brp.AK}


# ------------------------------------------------------------------ graph helpers
def hop_distance(ds, src, dst, limit=6):
    if src == dst:
        return 0
    seen, q = {src}, deque([(src, 0)])
    while q:
        u, d = q.popleft()
        if d >= limit:
            continue
        for v in brp.adj[ds][u]:
            if v == dst:
                return d + 1
            if v not in seen:
                seen.add(v)
                q.append((v, d + 1))
    return None  # > limit or disconnected


# canonical SAGE prediction for every node (predict_canonical_allnodes.py; identical to the
# persisted eval-node predictions on all 542 Cora / 200 Products nodes)
CANON_ALL = {ds: json.load(open(OUT / f"canonical_pred_allnodes/{ds}_canonical_pred_allnodes.json"))["canonical_pred"]
             for ds in ["cora", "products"]}


def node_info(ds, nid):
    return {"title": brp.title_of(ds, nid), "true": brp.label_of(ds, nid), "canon": CANON_ALL[ds][nid]}


def within2(ds, node):
    one = set(brp.adj[ds][node])
    two = set().union(*[brp.adj[ds][u] for u in one]) - one - {node} if one else set()
    return one | two


def norm(s):
    s = s.lower().replace("&amp;", "&").replace("&", " and ").replace("_", " ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ------------------------------------------------------------------ per-method evidence
def gn_context(e):
    pos = int(Path(e["source_file"]).stem)
    g = brp.TAG.load(brp.GN_PKL[e["dataset"]] / f"{pos}.pkl")
    assert g.root_global_id == e["node"]
    labels = brp.gn_label_mapping(g)  # local idx -> 'ROOT' / 'Node-1.2'
    by_label = {v: k for k, v in labels.items()}
    return {"g": g, "labels": labels, "by_label": by_label, "pred": g.prediction}


def gx_context(e):
    rec = None
    for line in open(e["source_file"]):
        if line.strip():
            r = json.loads(line)
            if r["target_node"] == e["node"]:
                rec = r
    return {"top": rec["gnnexplainer_top_features"], "pred": rec["prediction"].get("Predicted Class"),
            "conf": rec["prediction"].get("Confidence")}


def cf_context(e):
    rec = next(r for r in json.load(open(e["source_file"])) if r["node_id"] == e["node"])
    fd = rec["factual_target_dict"]
    return {"fact": fd["Factual_Target_Node_Class"], "cf": fd["Counterfactual_Target_Node_class"],
            "removed": [tuple(x) for x in rec["removed_edges_global"]], "pred": fd["Factual_Target_Node_Class"]}


# ------------------------------------------------------------------ cited nodes
GN_REF = re.compile(r"\bNodes?[- ]?(\d+(?:\.\d+)*)(?:\s*(?:to|through|-|–)\s*(?:Node[- ]?)?(\d+(?:\.\d+)*))?", re.I)


def gn_cited(text, ctx, target):
    """Node-X / Node X / 'Nodes 8 to 10' / ROOT. 'Node 0' and ROOT are the target, not citations."""
    out = []
    for m in GN_REF.finditer(text):
        a, b = m.group(1), m.group(2)
        refs = [a]
        if b:  # range: same parent, last component increments
            pa, pb = a.split("."), b.split(".")
            if len(pa) == len(pb) and pa[:-1] == pb[:-1] and int(pb[-1]) > int(pa[-1]):
                refs = [".".join(pa[:-1] + [str(i)]) for i in range(int(pa[-1]), int(pb[-1]) + 1)]
            else:
                refs = [a, b]
        for r in refs:
            if r == "0":
                continue
            lab = f"Node-{r}"
            loc = ctx["by_label"].get(lab)
            gid = int(ctx["g"].global_nids[loc]) if loc is not None else None
            if gid == target:
                continue
            if lab not in [c["ref"] for c in out]:
                out.append({"ref": lab, "id": gid, "via": "label"})
    return out


def numeric_cited(text, ents, target):
    ids = []
    try:
        ent_ids = {int(x) for x in ents.get("node_ids", []) if str(x).lstrip("-").isdigit()}
    except (TypeError, ValueError):
        ent_ids = set()
    for m in re.finditer(r"(?<![\d.])(\d+)(?![\d.%])", text):
        n = int(m.group(1))
        if n in ent_ids and n != target and n not in ids:
            ids.append(n)
    return [{"ref": str(n), "id": n, "via": "id"} for n in ids]


def title_cited(text, ents, ds, target):
    """Titles the claim quotes, resolved only by exact normalized containment against the
    target's <=2-hop neighbourhood (paraphrases are left unresolved, never guessed)."""
    out, cand = [], within2(ds, target)
    ntext = norm(text)
    for t in ents.get("titles", []):
        nt = norm(t)
        if len(nt) < 12 or nt not in ntext:
            continue
        hits = [n for n in cand if nt in norm(brp.title_of(ds, n))]
        if not hits and nt in norm(brp.title_of(ds, target)):
            continue  # the target's own title
        if len(hits) == 1:
            out.append({"ref": f"title:{t}", "id": hits[0], "via": "title"})
        else:
            out.append({"ref": f"title:{t}", "id": None, "via": f"title not resolved ({len(hits)} exact title matches within 2 hops)"})
    return out


# ------------------------------------------------------------------ features
def gx_feature_ref(words, ctx):
    rows = []
    for w in words:
        for tok in re.findall(r"[a-z]+", w.lower()):
            if len(tok) < 3:
                continue
            hit = None
            for i, f in enumerate(ctx["top"], 1):
                fw = f["word"].lower()
                if tok.startswith(fw) or STEM(tok) == fw or STEM(tok).startswith(fw) or (len(tok) >= 4 and fw.startswith(tok)):
                    hit = (i, f)
                    break
            if hit:
                i, f = hit
                rows.append(f"{tok}->{f['word']} (rank {i}/7, imp {f['importance']}, present={f.get('present', '')})")
            else:
                rows.append(f"{tok}: not in top-7")
    return "; ".join(dict.fromkeys(rows))


def gn_feature_ref(words, ctx, cited_locals):
    g = ctx["g"]
    nodes = cited_locals or [0]
    rows = []
    for w in words:
        for tok in re.findall(r"[a-z0-9]+", w.lower()):
            if len(tok) < 3:
                continue
            st = STEM(tok)
            for loc in nodes:
                nd = g.nodes[loc]
                toks = [re.sub(r"[^a-z0-9]", "", t.lower()) for t in nd.features]
                parts = [[p for p in re.split(r"[^a-z0-9]+", t.lower()) if p] for t in nd.features]
                scores = list(nd.importance_scores)
                idx = [i for i, t in enumerate(toks) if t and (t == tok or STEM(t) == st or any(p == tok or STEM(p) == st for p in parts[i]))]
                lab = ctx["labels"].get(loc, f"local{loc}")
                if not idx:
                    rows.append(f"{tok}@{lab}: not a token")
                    continue
                best = max(scores[i] for i in idx)
                rank = 1 + sum(1 for s in scores if s > best)
                rows.append(f"{tok}@{lab}: max saliency {best:.4f} (rank {rank}/{len(scores)}, n={len(idx)})")
    return "; ".join(dict.fromkeys(rows))


# ------------------------------------------------------------------ class claims
CLASS_VERB = re.compile(r"classif|class\b|categor|belong|falls? (under|into)|label|predict", re.I)
# the class must be stated as the node's class, not just mentioned as a topic or a category of items
TGT_CLASS = re.compile(r"classif|predict|belongs? to|falls? (under|into)|class\b|class of|category (is|of)|labell?ed", re.I)
NEI_CLASS = re.compile(r"(classified|labell?ed|predicted) as|belongs? to|falls? (under|into)|class(es)? (is|are|of)|categor(y|ies) (is|are|of)", re.I)
TARGET_CLASS_STRONG = re.compile(r"classification of (the )?(ROOT|target|node \d+|Node 0)[^.]*?\b(into|as)\b|(ROOT|Node 0|target node(?: \d+)?|node \d+)[^.,]{0,20}?(to be |is |was )?(re)?classified (as|into|under)|_Class\b", re.I)
EVALUATIVE = re.compile(r"support|well|explain|credib|confiden|strong|due to|because|reinforc|consistent", re.I)
NEG = re.compile(r"\bnot\b|n't|rather than|instead of|no longer|unlike|\bnor\b", re.I)
NEIGHBOR_SUBJ = re.compile(r"neighbo|connect|linked|\bedge|\bhop|these (products|nodes|papers|items)|all of these|other (nodes|products|papers|items)|\bpapers\b|\bitems\b|\bnodes\b", re.I)
FACTUAL = re.compile(r"(?<!counter)factual", re.I)
COUNTER = re.compile(r"counterfactual|reclassif", re.I)
TRUE_ROLE = re.compile(r"\btrue\b|ground[- ]truth|\bactual\b|real label|correct label", re.I)


def labels_in(text, ds):
    nt = " " + norm(text) + " "
    found = []
    for lab in brp.data[ds].label_names:
        nl = norm(lab)
        pos = nt.find(" " + nl + " ")
        if nl and pos >= 0:
            found.append((pos, lab))
    return [lab for _, lab in sorted(found)]


def class_check(row, ds, target, tgt, ctx, method, cited):
    """Returns (check_text, verdict or '') following the 'stated class vs recorded value' rule."""
    text = row["claim_text"]
    labs = labels_in(text, ds)
    if not labs or not CLASS_VERB.search(text):
        return "", ""
    if NEG.search(text):
        return f"mentions {labs}; negated phrasing, not checked", ""
    eq = lambda a, b: norm(a) == norm(b)  # noqa: E731
    pred = ctx["pred"]
    about_target = mentions_target(text, method, target)

    if cited and not about_target:  # neighbour class: stated class vs BOTH true and canonical
        if len(labs) != 1 or any(c["id"] is None for c in cited) or not NEI_CLASS.search(text):
            return "", ""
        L = labs[0]
        parts, vs = [], set()
        for c in cited:
            inf = node_info(ds, c["id"])
            parts.append(f"{c['id']}: true={inf['true']}, canon={inf['canon']}")
            m_t, m_c = eq(L, inf["true"]), eq(L, inf["canon"])
            vs.add("supported" if (m_t and m_c) else "contradicted" if (not m_t and not m_c) else "split")
        chk = f"stated '{L}' for cited node(s) | " + "; ".join(parts)
        if vs == {"supported"}:
            return chk, "" if EVALUATIVE.search(text) else "supported"
        if "contradicted" in vs and "supported" not in vs and "split" not in vs:
            return chk, "contradicted"
        return chk, ""

    if not about_target and NEIGHBOR_SUBJ.search(text):
        return "", ""
    # a claim that also talks about neighbours counts only if the class is explicitly the target's
    if (cited or NEIGHBOR_SUBJ.search(text)) and not TARGET_CLASS_STRONG.search(text):
        return "", ""
    if not TGT_CLASS.search(text):
        return "", ""

    # target class. 'supported' only for a plain class_state claim (the class is the whole claim);
    # a wrong stated class makes any claim type contradicted.
    def verdict(ok):
        if not ok:
            return "contradicted"
        return "supported" if row["claim_type"] == "class_state" and not EVALUATIVE.search(text) else ""

    m = re.search(r"from (.+?) to (.+)", text, re.I)
    if m and len(labs) == 2 and method == "CF-GNNExplainer":
        a, b = labs
        chk = f"stated factual '{a}' (recorded {ctx['fact']}), counterfactual '{b}' (recorded {ctx['cf']})"
        return chk, verdict(eq(a, ctx["fact"]) and eq(b, ctx["cf"]))
    if len(labs) != 1:
        return f"mentions {labs}; not a single stated class", ""
    L = labs[0]
    has_f, has_c = bool(FACTUAL.search(text)), bool(COUNTER.search(text))
    if method == "CF-GNNExplainer" and has_f and has_c:  # 'in both the factual and counterfactual graphs'
        ok = eq(L, ctx["fact"]) and eq(L, ctx["cf"])
        return f"stated '{L}' for factual AND counterfactual (recorded {ctx['fact']} / {ctx['cf']})", verdict(ok)
    if method == "CF-GNNExplainer" and has_c:
        return f"stated counterfactual '{L}' (recorded {ctx['cf']})", verdict(eq(L, ctx["cf"]))
    if TRUE_ROLE.search(text):
        return f"stated true '{L}' (recorded {tgt['true']})", verdict(eq(L, tgt["true"]))
    if method == "CF-GNNExplainer" and not has_f and re.search(r"counterfactual", row["source_span"], re.I):
        return f"stated '{L}'; role unclear (span mentions counterfactual)", ""
    rec = ctx["fact"] if method == "CF-GNNExplainer" else pred
    role = "factual/predicted" if method == "CF-GNNExplainer" else "predicted"
    return f"stated {role} '{L}' (recorded {rec})", verdict(eq(L, rec))


# ------------------------------------------------------------------ hop rules
DIRECT = re.compile(r"connected (to|with)|\bdirect|1-hop|one[- ]hop|neighbo|linked|edge between|adjacent|\bcites?\b|\bcited\b", re.I)
NOT_DIRECT = re.compile(r"2-hop|two[- ]hop|two hops|2 hops|second[- ]degree|indirect|within two|neighbors of neighbors", re.I)


def mentions_target(text, method, target):
    if re.search(rf"\b{target}\b", text):
        return True
    if re.search(r"\btarget\b|\bROOT\b|\bNode 0\b|\bthe (paper|product|bottle)\b", text, re.I):
        return True
    return False


# ------------------------------------------------------------------ G sets (Table 14)
gn_cora = json.load(open(RECALL / "grounding_recall_cora_freetext.json"))
gn_prod = json.load(open(RECALL / "graphnarrator_products_recall_f1_untruncated.json"))["results"]
rf = json.load(open(RECALL / "grounding_recall_f1_results.json"))
t14 = {}
for r in csv.DictReader(open(ROOT / "grounding_per_node_from_chat.csv")):
    if r["method"] == "GraphNarrator":
        t14[(r["method"], r["dataset"], int(r["node"]))] = r["recall"]
for r in csv.DictReader(open(ROOT / "grounding_recall_verified_per_node.csv")):
    t14[(r["method"], r["dataset"], int(r["node"]))] = r["recall"]


def build_G(e, ctx):
    m, ds, node = e["method"], e["dataset"], e["node"]
    rows = []
    if m == "GraphNarrator":
        if ds == "cora":
            r = gn_cora[str(node)]["freetext_only_CURRENT"]
            items = [(lab, r["max_score_per_neighbor"][lab], r["mentioned"][lab]) for lab in r["important_set"]]
        else:
            items = [(x["neighbor"], x["max_saliency_score"], x["mentioned"]) for x in gn_prod[str(node)]["important_set_detail"]]
        for lab, sc, men in items:
            gid = int(ctx["g"].global_nids[ctx["by_label"][lab]])
            inf = node_info(ds, gid)
            rows.append({"element": lab, "global_id": gid, "title": inf["title"], "true_label": inf["true"],
                         "canonical_pred": inf["canon"], "hop": hop_distance(ds, node, gid),
                         "score": sc, "score_kind": "max saliency as displayed in prompt (2 dp)",
                         "mentioned_table14": men, "mentioned_relabel": ""})
    elif m == "GraphXAIN":
        seen = {}
        for i, f in enumerate(rf["graphxain"][ds][str(node)]["real_top7_features"], 1):
            w = f["word"]
            top = ctx["top"][i - 1]
            assert top["word"] == w, (e["id"], w, top["word"])
            if w in seen:
                seen[w]["ranks"] += f",{i}"
                seen[w]["mentioned_table14"] = seen[w]["mentioned_table14"] or f["mentioned"]
                continue
            seen[w] = {"element": w, "ranks": str(i), "score": f["importance"], "score_kind": "GNNExplainer node-mask importance (first occurrence)",
                       "present_in_target": top.get("present", ""), "mentioned_table14": f["mentioned"], "mentioned_relabel": ""}
        rows = list(seen.values())
    else:
        for x in rf["cf_gnnexplainer"][ds][str(node)]["real_removed_edges"]:
            a, b = x["edge"]
            other = b if a == node else a if b == node else None
            inf = node_info(ds, other) if other is not None else {"title": "", "true": "", "canon": ""}
            rows.append({"element": f"({a}, {b})", "touches_target": other is not None,
                         "other_endpoint": other if other is not None else "", "other_title": inf["title"],
                         "other_true_label": inf["true"], "mentioned_table14": x["mentioned"],
                         "matched_id_group_size": x["matched_id_group_size"], "mentioned_relabel": ""})
        assert sorted(tuple(x["edge"]) for x in rf["cf_gnnexplainer"][ds][str(node)]["real_removed_edges"]) == sorted(tuple(sorted(r)) for r in ctx["removed"])
    n_men = sum(bool(r["mentioned_table14"]) for r in rows)
    recall = n_men / len(rows) if rows else None
    tab = t14.get((m, ds, node), "")
    assert tab == "" or abs(float(tab) - recall) < 6e-4, (e["id"], tab, recall)
    return rows, recall, tab


# ------------------------------------------------------------------ carried-over verdicts
gx_rb = json.load(open(ROOT / "graphxain_survey_corrected_2026-08-07/grounding_precision_rulebased_v2/graphxain_grounding_precision_RULEBASED_v2.json"))


def carried_over(e, sheet):
    """GraphXAIN_cora_2334 only. Rule-based v2 facts are per cited word; a claim gets a
    carried verdict only if it cites exactly the words of facts that share one source sentence."""
    if e["id"] != "GraphXAIN_cora_2334":
        return {}
    facts = gx_rb["2334"]["facts"]
    out = {}
    for i, r in sheet.iterrows():
        ents = json.loads(claims.loc[claims.claim_id == r["claim_id"], "entities"].iloc[0])
        words = {w.lower() for w in ents.get("feature_words", [])}
        hit = [f for f in facts if f["cited_word"] in words]
        if hit and {f["cited_word"] for f in hit} == words and len({f["sentence"] for f in hit}) == 1:
            v = "supported" if all(f["supported"] for f in hit) else "contradicted"
            out[i] = (v, "carried over: graphxain_grounding_precision_RULEBASED_v2.json node 2334 facts "
                         + ", ".join(f"'{f['cited_word']}' supported={f['supported']}" for f in hit)
                         + " (binary rule-based check, same source sentence)")
    return out


# ------------------------------------------------------------------ main
def main():
    summary = []
    for tid, grp in claims.groupby(claims.method + "_" + claims.dataset + "_" + claims.node, sort=False):
        e = AK[tid]
        m, ds, node = e["method"], e["dataset"], e["node"]
        ctx = {"GraphNarrator": gn_context, "GraphXAIN": gx_context, "CF-GNNExplainer": cf_context}[m](e)
        canon = brp.PRED[ds][str(node)]
        tgt = {"true": brp.label_of(ds, node), "canon": canon["canonical_pred"]}
        sheet = grp[KEEP].reset_index(drop=True).copy()
        cols = {k: [] for k in ["cited_refs", "cited_ids", "cited_titles", "cited_true_labels", "cited_canonical_preds",
                                "cited_hops", "feature_evidence", "class_check", "suggested_verdict", "suggest_reason"]}
        seen_norm = {}
        for i, r in sheet.iterrows():
            ents = json.loads(grp.iloc[i]["entities"])
            text = r["claim_text"]
            if m == "GraphNarrator":
                cited = gn_cited(text, ctx, node)
                if not cited:  # e.g. 'calculators (Node 1) ...' kept only in the span; use it if the extractor's entities name it
                    ent_refs = {str(x).replace("Node-", "").replace("Node ", "") for x in ents.get("node_ids", [])}
                    cited = [dict(c, via="label", ref_src="span") for c in gn_cited(r["source_span"], ctx, node) if c["ref"][5:] in ent_refs]
            else:
                cited = numeric_cited(text, ents, node) + title_cited(text, ents, ds, node)
                if not cited:
                    cited = [dict(c, ref_src="span") for c in numeric_cited(r["source_span"], ents, node)]
            infos = []
            for c in cited:
                if c["id"] is None or not (0 <= c["id"] < brp.data[ds].num_nodes):
                    infos.append(None)
                else:
                    inf = node_info(ds, c["id"])
                    inf["hop"] = hop_distance(ds, node, c["id"])
                    infos.append(inf)
            hopstr = lambda h: ">6/none" if h is None else str(h)  # noqa: E731
            cols["cited_refs"].append(" | ".join(c["ref"] + (" (from source_span)" if c.get("ref_src") == "span" else "") for c in cited))
            cols["cited_ids"].append(" | ".join("" if c["id"] is None else str(c["id"]) for c in cited))
            cols["cited_titles"].append(" | ".join(i_["title"] if i_ else "(not resolved)" for i_ in infos))
            cols["cited_true_labels"].append(" | ".join(i_["true"] if i_ else "" for i_ in infos))
            cols["cited_canonical_preds"].append(" | ".join(i_["canon"] if i_ else "" for i_ in infos))
            cols["cited_hops"].append(" | ".join(hopstr(i_["hop"]) if i_ else ("label not in prompt subgraph" if c["via"] == "label" else c["via"]) for c, i_ in zip(cited, infos)))

            # features
            words = [w for w in ents.get("feature_words", []) if isinstance(w, str)]
            words += re.findall(r"['\"‘’“”]([A-Za-z][A-Za-z\- ]{1,30})['\"‘’“”]", text)
            class_names = {norm(x) for x in brp.data[ds].label_names}
            words = list(dict.fromkeys(w.strip() for w in words if w.strip() and norm(w) not in class_names))
            fe = ""
            if (r["claim_type"] == "feature" or words) and words:
                if m == "GraphXAIN":
                    fe = gx_feature_ref(words, ctx)
                elif m == "GraphNarrator":
                    locs = [ctx["by_label"][c["ref"]] for c in cited if c["ref"] in ctx["by_label"]]
                    fe = gn_feature_ref(words, ctx, locs)
            cols["feature_evidence"].append(fe)

            # mechanical suggestions
            sv, why = [], []
            key = norm(text)
            if key in seen_norm:
                sv.append("duplicate")
                why.append(f"exact repeat of {seen_norm[key]}")
            else:
                seen_norm[key] = r["claim_id"]
            for c, i_ in zip(cited, infos):
                if c["via"] == "label" and c["id"] is None:
                    sv.append("contradicted"); why.append(f"{c['ref']} does not exist in the prompt subgraph")
                elif c["via"] == "id" and i_ is None:
                    sv.append("contradicted"); why.append(f"node {c['ref']} does not exist in {ds}")
                elif i_ is not None and (i_["hop"] is None or i_["hop"] > 2):
                    sv.append("contradicted"); why.append(f"{c['ref']} (id {c['id']}) is {hopstr(i_['hop'])} hops from {node}, not within 2")
            if mentions_target(text, m, node) and DIRECT.search(text) and not NOT_DIRECT.search(text):
                for c, i_ in zip(cited, infos):
                    if i_ is not None and i_["hop"] == 2:
                        sv.append("contradicted"); why.append(f"{c['ref']} (id {c['id']}) is a 2-hop node described as directly connected")
            chk, cv = class_check(r, ds, node, tgt, ctx, m, [c for c in cited if c["id"] is not None] if cited else [])
            cols["class_check"].append(chk)
            if cv:
                sv.append(cv); why.append(chk)
            final = "duplicate" if "duplicate" in sv else "contradicted" if "contradicted" in sv else "supported" if "supported" in sv else ""
            cols["suggested_verdict"].append(final)
            cols["suggest_reason"].append("; ".join(dict.fromkeys(why)) if final else "")
        for k, v in cols.items():
            sheet[k] = v
        sheet.insert(5, "target_id", node)
        sheet.insert(6, "target_true_label", tgt["true"])
        sheet.insert(7, "target_recorded_pred", ctx["pred"])
        sheet.insert(8, "target_canonical_pred", tgt["canon"])
        if m == "GraphXAIN":
            sheet.insert(9, "gx_confidence", ctx["conf"])
        if m == "CF-GNNExplainer":
            sheet.insert(9, "cf_factual_class", ctx["fact"])
            sheet.insert(10, "cf_counterfactual_class", ctx["cf"])
            sheet.insert(11, "cf_removed_edges", "; ".join(f"({a}, {b})" for a, b in ctx["removed"]))
            ids = [x for x in sheet["cited_ids"]]
            rem = {n for edge in ctx["removed"] for n in edge} - {node}
            sheet.insert(12, "cited_in_removed_edges", [" | ".join(("yes" if s and int(s) in rem else "no") if s else "" for s in x.split(" | ")) if x else "" for x in ids])
        sheet["corrected_type"] = ""
        sheet["verdict"] = ""
        sheet["verdict_source"] = ""
        sheet["note"] = ""
        for i, (v, src) in carried_over(e, sheet).items():
            sheet.at[i, "verdict"] = v
            sheet.at[i, "verdict_source"] = src
        sheet.to_csv(OUT / f"claims_{tid}.csv", index=False)

        G, rec, tab = build_G(e, ctx)
        pd.DataFrame(G).to_csv(OUT / f"G_{tid}.csv", index=False)

        sv = sheet["suggested_verdict"]
        n_carried = int((sheet["verdict"] != "").sum())
        manual = int(((sv == "") & (sheet["verdict"] == "")).sum())
        summary.append({"text": tid, "method": m, "dataset": ds, "node": node, "n_claims": len(sheet),
                        "prefill_contradicted": int((sv == "contradicted").sum()), "prefill_supported": int((sv == "supported").sum()),
                        "prefill_duplicate": int((sv == "duplicate").sum()), "carried_over_verdicts": n_carried,
                        "rows_for_manual_review": manual, "G_size": len(G), "G_mentioned_table14": sum(bool(x["mentioned_table14"]) for x in G),
                        "recall_from_G": round(rec, 3), "recall_table14": tab})
        print(summary[-1])
    pd.DataFrame(summary).to_csv(OUT / "summary.csv", index=False)


if __name__ == "__main__":
    main()
