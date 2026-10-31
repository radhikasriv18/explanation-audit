"""
Additive, corrected re-evaluation of already-generated GSPELL_explanations.pt
files. Does NOT modify eval_utils.py -- eval_llm_explanations() and every
function it calls (extract_neighbor_support, get_gnn_prediction_prob,
get_characterization) are reused completely unmodified, imported from the
real eval_utils module. This file only adds a corrected metrics loop and
persistence around them.

Bug being fixed (index-to-node-ID mapping, NOT the post-hoc filter):
eval_llm_explanations() iterates `for i in range(num_eval_samples)` and uses
that loop position i directly as a graph node ID (nx.ego_graph(G, i, ...),
gnn_preds[i], ...). This is correct only when generation ran over literal
node IDs 0..N-1 in order, which is what upstream's generate_exp_by_llm always
does (`for node_idx in range(max_num_eval_nodes)` -- no scattered-split
support exists upstream). Our repo added scattered-split support
(--split_path / node_ids) to generate_exp_by_llm, but never updated
eval_llm_explanations to match: it still treats list position as node ID.
Every entry in a saved GSPELL_explanations.pt already carries the REAL node
ID in entry['target_node'] -- this module uses that instead of position.

Post-hoc filter (Section 4.3 "Po"): NOT reimplemented here. It is upstream,
unmodified, verbatim code (extract_neighbor_support's regex parse +
`if s in neighbors` membership check inside eval_llm_explanations). This
module calls extract_neighbor_support directly and additionally persists
what it discards, which eval_llm_explanations computes but throws away.
"""
import json
import os

import networkx as nx
import numpy as np
import torch
import torch.nn.functional as F
from networkx.algorithms.approximation import steiner_tree
from torch_geometric.data import Data
from torch_geometric.utils import to_networkx, subgraph
from tqdm import tqdm

import eval_utils as eu


def corrected_eval_llm_explanations(dataset, gnn, gnn_preds, generated_exps, device, out_dir):
    """
    Faithful reproduction of eval_utils.eval_llm_explanations's logic, with
    the loop index replaced by each entry's real target_node, and
    per-node/per-batch raw parse + filtered result + removed (hallucinated)
    set persisted to prefilter_postfilter_removed.jsonl.
    """
    os.makedirs(out_dir, exist_ok=True)
    parse_log_path = os.path.join(out_dir, "prefilter_postfilter_removed.jsonl")

    data = dataset._data.to(device)
    gnn.eval()
    _, _, node_type = eu.get_characterization(dataset, 0, 0)

    # parsed_explanations keyed by REAL target_node, not list position.
    parsed_explanations = {}
    n_raw_total = 0
    n_removed_total = 0

    with open(parse_log_path, "w") as plog:
        for entry_list in generated_exps:
            if not entry_list:
                continue
            target_node = entry_list[0]["target_node"]
            support_papers = [target_node]
            not_support_papers = []

            for entry in entry_list:
                explanation = entry["explanation"]
                if not isinstance(explanation, str):
                    explanation = explanation[-1]["content"]

                neighbors = entry["neighbors"]
                # Raw parse -- exactly extract_neighbor_support's return value,
                # BEFORE the membership filter. This is what
                # eval_llm_explanations computes and immediately discards.
                raw_support, raw_not_support = eu.extract_neighbor_support(
                    explanation, node_type, threshold=dataset.num_samples
                )

                filt_support = [s for s in raw_support if s in neighbors]
                filt_not_support = [ns for ns in raw_not_support if ns in neighbors]

                removed_support = [s for s in raw_support if s not in neighbors]
                removed_not_support = [ns for ns in raw_not_support if ns not in neighbors]

                n_raw_total += len(raw_support) + len(raw_not_support)
                n_removed_total += len(removed_support) + len(removed_not_support)

                plog.write(json.dumps({
                    "target_node": target_node,
                    "batch_neighbors": list(neighbors),
                    "raw_support": raw_support,
                    "raw_not_support": raw_not_support,
                    "filtered_support": filt_support,
                    "filtered_not_support": filt_not_support,
                    "removed_support_hallucinated": removed_support,
                    "removed_not_support_hallucinated": removed_not_support,
                }) + "\n")

                support_papers.extend(filt_support)
                not_support_papers.extend(filt_not_support)

            parsed_explanations[target_node] = (support_papers, not_support_papers)

    G = to_networkx(data, to_undirected=True)

    metrics = {
        "fidelity_scores": [], "prob_orig": [], "prob_suff": [],
        "prob_comp": [], "prob_rand": [], "prob_align": [], "sizes": [],
    }

    for target_node in tqdm(parsed_explanations.keys(), desc="Corrected eval"):
        ego_graph = nx.ego_graph(G, target_node, radius=2)
        all_neighbors = set(ego_graph.nodes)

        supports, not_supports = parsed_explanations[target_node]
        s_plus_set = set(n for n in supports if n in all_neighbors)
        s_minus_set = set(n for n in not_supports if n in all_neighbors)

        subset_orig = list(all_neighbors)
        orig_pred_class = gnn_preds[target_node].item()
        p_orig = eu.get_gnn_prediction_prob(gnn, data, subset_orig, target_node, orig_pred_class)

        s_list = list(s_plus_set)
        try:
            selected_nodes = list(steiner_tree(ego_graph, s_list).nodes)
        except Exception:
            selected_nodes = []
        if len(selected_nodes) == 0:
            selected_nodes = s_list

        subset_suff = selected_nodes
        metrics["sizes"].append(len(subset_suff))

        subset_sorted = torch.tensor(sorted(subset_suff), dtype=torch.long, device=device)
        edge_index_sub, _ = subgraph(subset_sorted, data.edge_index, relabel_nodes=True)
        target_idx = (subset_sorted == target_node).nonzero(as_tuple=True)[0].item()

        with torch.no_grad():
            out, _ = gnn(batch=Data(x=data.x[subset_sorted], edge_index=edge_index_sub))
            out_class = out.argmax(dim=-1)
            metrics["fidelity_scores"].append(out_class[target_idx].item() == orig_pred_class)

        p_suff = eu.get_gnn_prediction_prob(gnn, data, subset_suff, target_node, orig_pred_class)

        nodes_to_remove = s_plus_set - {target_node}
        subset_comp = list(all_neighbors - nodes_to_remove)
        p_comp = eu.get_gnn_prediction_prob(gnn, data, subset_comp, target_node, orig_pred_class)

        num_to_remove = len(nodes_to_remove)
        candidates_to_remove = list(all_neighbors - {target_node})
        if len(candidates_to_remove) >= num_to_remove:
            import random
            random_remove = set(random.sample(candidates_to_remove, num_to_remove))
            subset_rand = list(all_neighbors - random_remove)
        else:
            subset_rand = list(all_neighbors)
        p_rand = eu.get_gnn_prediction_prob(gnn, data, subset_rand, target_node, orig_pred_class)

        nodes_to_remove_align = s_minus_set - {target_node}
        subset_align = list(all_neighbors - nodes_to_remove_align)
        p_align = eu.get_gnn_prediction_prob(gnn, data, subset_align, target_node, orig_pred_class)

        metrics["prob_orig"].append(p_orig)
        metrics["prob_suff"].append(p_suff)
        metrics["prob_comp"].append(p_comp)
        metrics["prob_rand"].append(p_rand)
        metrics["prob_align"].append(p_align)

    summary = {
        "n_nodes_evaluated": len(parsed_explanations),
        "fidelity": float(np.mean(metrics["fidelity_scores"])),
        "size": float(np.mean(metrics["sizes"])),
        "comprehensiveness": float(np.mean(np.array(metrics["prob_orig"]) - np.array(metrics["prob_comp"]))),
        "random_baseline": float(np.mean(np.array(metrics["prob_orig"]) - np.array(metrics["prob_rand"]))),
        "alignment": float(np.mean(np.array(metrics["prob_orig"]) - np.array(metrics["prob_align"]))),
        "n_raw_citations_total": n_raw_total,
        "n_removed_hallucinated_total": n_removed_total,
        "hallucination_rate": (n_removed_total / n_raw_total) if n_raw_total else None,
    }
    with open(os.path.join(out_dir, "corrected_metrics.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))
    return summary
