"""From extractions_v3/ to judge inputs, fully automated (no hand pass), same steps as the answer key:

  1. cleanup_v3.process (grounding_judge_pilot, imported unchanged): span check, relabel by subject,
     drop evaluation-only claims, CF prose -> infos-field merge.
  2. span_check_v4.span_check (imported unchanged) against the scored text -> span_check pass/fail.
  3. cited nodes per claim with build_labeling_sheets.gn_cited / numeric_cited / title_cited
     (imported unchanged) and the same fallback to source_span, as for the answer-key sheets.
  4. packets_full/<id>.md = packets/<id>.md + FULL NODE TEXT section. full_text_section / load_graph / hops
     are verbatim copies from grounding_judge_2026-10-13/judge_gemini_3methods.py (that module imports
     google-genai, which this torch environment does not have).
Outputs: claims.csv (one row per claim, sheet order) and packets_full/. Texts without an extraction
file yet are skipped and counted.

Run with ~/.conda/envs/graphnarr/bin/python.
"""
import csv
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, "./grounding_judge_pilot")
sys.path.insert(0, "./grounding_answer_key_3methods_2026-10-13")
import cleanup_v3  # noqa: E402
from span_check_v4 import span_check  # noqa: E402
import build_labeling_sheets as bls  # noqa: E402  (module import only reads sources)
import torch  # noqa: E402

HERE = Path(__file__).resolve().parent
CANON = {"cora": "./cora_canonical.pt", "products": "./products_canonical.pt"}
GN_PKL = {"cora": Path("./graphnarrCora/GraphNarrator/outputs/pkls_cora_eval"),
          "products": Path("./graphnarrCora/GraphNarrator/outputs/pkls_products")}


# ---- verbatim from judge_gemini_3methods.py ----
def load_graph(ds):
    g = torch.load(CANON[ds], weights_only=False)
    ei = g.edge_index
    adj = {}
    for a, b in zip(ei[0].tolist(), ei[1].tolist()):
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    return g, adj


def hops(adj, t):
    h1 = adj.get(t, set()); h2 = set().union(*(adj.get(x, set()) for x in h1)) - h1 - {t}
    return lambda n: 0 if n == t else 1 if n in h1 else 2 if n in h2 else "not within 2 hops"


def full_text_section(ds, node, g, adj, cited):
    hop = hops(adj, node)
    names = g.label_names
    order = [node] + sorted(adj.get(node, set())) + sorted(c for c in cited if c != node and c not in adj.get(node, set()))
    L = ["", "FULL NODE TEXT (complete canonical raw_text, no truncation; true label and hop distance from the target):"]
    for n in OrderedDict.fromkeys(order):
        if not (0 <= n < g.num_nodes):
            L.append(f"- node {n}: DOES NOT EXIST"); continue
        h = hop(n)
        role = "TARGET" if n == node else ("1-hop (direct neighbor)" if h == 1 else f"{h}-hop" if h == 2 else str(h))
        L.append(f"- node {n} [{role}] true label: {names[int(g.y[n])]}")
        L.append("    " + re.sub(r"\s+", " ", g.raw_text[n]).strip())
    return "\n".join(L)
# ---- end verbatim ----


def gn_ctx(ds, cf_key, node):
    g = bls.brp.TAG.load(GN_PKL[ds] / f"{cf_key}.pkl")
    assert int(g.root_global_id) == node
    labels = bls.brp.gn_label_mapping(g)
    return {"g": g, "labels": labels, "by_label": {v: k for k, v in labels.items()}, "pred": g.prediction}


def cited_for(method, claim, ctx, ds, node):
    """Same per-method logic and source_span fallback as build_labeling_sheets.main()."""
    ents = claim.get("entities") or {}
    text = claim["claim"]
    if method == "GraphNarrator":
        cited = bls.gn_cited(text, ctx, node)
        if not cited:
            ent_refs = {str(x).replace("Node-", "").replace("Node ", "") for x in ents.get("node_ids", [])}
            cited = [dict(c, via="label", ref_src="span") for c in bls.gn_cited(claim.get("source_span") or "", ctx, node) if c["ref"][5:] in ent_refs]
    else:
        cited = bls.numeric_cited(text, ents, node) + bls.title_cited(text, ents, ds, node)
        if not cited:
            cited = [dict(c, ref_src="span") for c in bls.numeric_cited(claim.get("source_span") or "", ents, node)]
    return cited


def main():
    texts = json.load(open(HERE / "texts.json"))
    graphs = {ds: load_graph(ds) for ds in CANON}
    (HERE / "packets_full").mkdir(exist_ok=True)
    rows, skipped, per_text = [], [], []
    for e in texts:
        f = HERE / "extractions_v3" / f"{e['id']}.json"
        if not f.exists():
            skipped.append(e["id"]); continue
        rec = json.load(open(f))
        assert rec["text_scored_sha256_16"] == e["text_scored_sha256_16"], e["id"]
        final, log = cleanup_v3.process(rec)
        ds, node = e["dataset"], int(e["node"])
        ctx = gn_ctx(ds, e["cf_key"], node) if e["method"] == "GraphNarrator" else None
        all_cited = set()
        n_fail = 0
        for c in final:
            sc = span_check(c.get("source_span"), e["text_scored"])
            n_fail += sc == "fail"
            cited = cited_for(e["method"], c, ctx, ds, node)
            ids = [x["id"] for x in cited if x["id"] is not None]
            all_cited.update(ids)
            rows.append({"text_id": e["id"], "method": e["method"], "config": e["config"], "dataset": ds, "node": node,
                         "claim_id": f"{e['id']}_c{c['extraction_index']:02d}", "claim_text": c["claim"],
                         "claim_type": c["claim_type"], "source_span": c.get("source_span") or "", "span_check": sc,
                         "cited_refs": " | ".join(x["ref"] for x in cited), "cited_ids": " | ".join(str(i) for i in ids),
                         "entities": json.dumps(c.get("entities") or {}, ensure_ascii=False, separators=(",", ":"))})
        g, adj = graphs[ds]
        packet = (HERE / "packets" / f"{e['id']}.md").read_text(encoding="utf-8").rstrip() + "\n" + full_text_section(ds, node, g, adj, all_cited)
        (HERE / "packets_full" / f"{e['id']}.md").write_text(packet, encoding="utf-8")
        d = rec["parse_diagnostics"]
        per_text.append({"text_id": e["id"], "method": e["method"], "config": e["config"], "dataset": ds, "node": node,
                         "n_extracted": len(rec["claims"]), "n_final": len(final), "n_span_fail": n_fail,
                         "n_dropped": sum(l["action"].startswith("drop") for l in log),
                         "n_merged": sum(l["action"] == "merge_into_field" for l in log),
                         "hit_max_new_tokens": d["hit_max_new_tokens"], "parse_mode": d.get("parse_mode"),
                         "packet_chars": len(packet)})
    for name, data in (("claims.csv", rows), ("extraction_summary.csv", per_text)):
        with open(HERE / name, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
    print(f"{len(per_text)} texts prepared, {len(rows)} claims, {sum(p['n_span_fail'] for p in per_text)} span-check fails, "
          f"{sum(p['hit_max_new_tokens'] for p in per_text)} hit the 4096 cap; {len(skipped)} texts not extracted yet")


if __name__ == "__main__":
    main()
