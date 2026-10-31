import argparse
import csv
import json
import random
from datetime import datetime
from pathlib import Path

import networkx as nx
import numpy as np
import regex as re
import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.utils import subgraph, to_networkx
from tqdm import tqdm

from dataset import CORA, Encoder
from log import logger
from models.joint_model import LM_GNN_Joint_Model
from tag import TAG, bfs_edges


LABELS = [
    "Case_Based",
    "Genetic_Algorithms",
    "Neural_Networks",
    "Probabilistic_Methods",
    "Reinforcement_Learning",
    "Rule_Learning",
    "Theory",
]


def save_metrics_summary(exp_dir: Path, metrics, num_requested: int):
    avg_fid = np.mean(metrics["fidelity_scores"]) if metrics["fidelity_scores"] else 0.0
    avg_size = np.mean(metrics["sizes"]) if metrics["sizes"] else 0.0
    drop_comp = np.mean(np.array(metrics["prob_orig"]) - np.array(metrics["prob_comp"])) if metrics["prob_orig"] else 0.0
    drop_rand = np.mean(np.array(metrics["prob_orig"]) - np.array(metrics["prob_rand"])) if metrics["prob_orig"] else 0.0
    drop_align = np.mean(np.array(metrics["prob_orig"]) - np.array(metrics["prob_align"])) if metrics["prob_orig"] else 0.0

    metrics_dir = Path("outputs/metrics")
    metrics_dir.mkdir(parents=True, exist_ok=True)

    run_tag = exp_dir.name
    timestamp = datetime.now().isoformat(timespec="seconds")
    summary = {
        "timestamp": timestamp,
        "exp_dir": str(exp_dir),
        "run_tag": run_tag,
        "num_requested": num_requested,
        "num_evaluated": len(metrics["fidelity_scores"]),
        "fidelity_sufficiency": float(avg_fid),
        "explanation_size": float(avg_size),
        "comprehensiveness_drop": float(drop_comp),
        "random_baseline_drop": float(drop_rand),
        "alignment_drop": float(drop_align),
    }

    json_path = metrics_dir / f"gspell_summary-{run_tag}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    csv_path = metrics_dir / "gspell_summary.csv"
    csv_columns = list(summary.keys())
    file_exists = csv_path.exists()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        if not file_exists:
            writer.writeheader()
        writer.writerow(summary)

    logger.info("Saved GSPELL summary JSON: %s", json_path)
    logger.info("Appended GSPELL summary CSV: %s", csv_path)

    return summary


def build_local_label_maps(tag_graph: TAG):
    # Build a directed graph from TAG edges
    data = Data(
        num_nodes=len(tag_graph.nodes),
        edge_index=torch.tensor(tag_graph.edges, dtype=torch.long),
        is_undirected=False,
    )
    G = to_networkx(data)

    mapping = {0: "ROOT"}
    old_depth = 0
    cur_depth_count = {}

    for parent, child, depth in list(bfs_edges(G, source=0)):
        if depth != old_depth:
            cur_depth_count = {}
            old_depth = depth

        cur_depth_count[parent] = cur_depth_count.get(parent, 0) + 1

        if depth == 1:
            mapping[child] = f"{cur_depth_count[parent]}"
        else:
            mapping[child] = f"{mapping[parent]}.{cur_depth_count[parent]}"

    label_to_local = {v: k for k, v in mapping.items() if v != "ROOT"}
    local_to_label = {k: v for k, v in mapping.items()}
    return label_to_local, local_to_label


def extract_support_nodes_from_explanation(explanation_text, label_to_local):
    # GraphNarrator explanations usually reference nodes as "Node-1", "Node-1.2", etc.
    pattern = re.compile(r"Node-([0-9]+(?:\\.[0-9]+)*)")
    matches = pattern.findall(explanation_text)

    supports_local = []
    for label in matches:
        if label in label_to_local:
            supports_local.append(label_to_local[label])

    return list(sorted(set(supports_local)))


def get_gnn_prediction_prob(model, data, text, subset_list, target_node_idx, original_pred_class, encoder, device):
    if len(subset_list) == 0:
        return 0.0

    subset_sorted = torch.tensor(sorted(list(subset_list)), dtype=torch.long, device=device)
    edge_index_sub, _ = subgraph(subset_sorted, data.edge_index, relabel_nodes=True)

    target_mapping = (subset_sorted == target_node_idx).nonzero(as_tuple=True)[0]
    if len(target_mapping) == 0:
        return 0.0
    idx_in_batch = target_mapping.item()

    # Compute embeddings for subset nodes
    embs = torch.concat(
        [encoder.encode(text[i]).detach().cpu() for i in subset_sorted.tolist()], dim=0
    ).to(device)

    with torch.no_grad():
        logits = model.forward_gnn(embs, edge_index_sub.to(device))
        probs = F.softmax(logits, dim=-1)
        target_prob = probs[idx_in_batch, original_pred_class].item()

    return target_prob


def evaluate(
    exp_dir,
    pkl_dir,
    gnn_ckpt,
    cora_data_path,
    num_eval_samples,
    device,
):
    # Load dataset and graph
    data, text, _ = CORA.load(seed=42, data_path=cora_data_path)
    data = data.to(device)
    G_full = to_networkx(data, to_undirected=True)

    # Load GNN
    encoder = Encoder()
    model = LM_GNN_Joint_Model(lm_model_name="bert-base-uncased", gnn_model_name="SAGE", out_dim=7).to(device)
    try:
        state_dict = torch.load(gnn_ckpt, map_location=device, weights_only=True)
    except TypeError:
        state_dict = torch.load(gnn_ckpt, map_location=device)
    model.gnn.load_state_dict(state_dict)
    model.eval()

    exp_dir = Path(exp_dir)
    pkl_dir = Path(pkl_dir)
    exp_files = sorted(exp_dir.glob("*.json"))
    if num_eval_samples is not None:
        exp_files = exp_files[:num_eval_samples]

    metrics = {
        "fidelity_scores": [],
        "prob_orig": [],
        "prob_suff": [],
        "prob_comp": [],
        "prob_rand": [],
        "prob_align": [],
        "sizes": [],
    }

    for exp_file in tqdm(exp_files, desc="Evaluating GraphNarrator (GSPELL metrics)"):
        sample_id = exp_file.stem
        tag_path = pkl_dir / f"{sample_id}.pkl"
        if not tag_path.exists():
            logger.warning("Missing TAG file: %s", tag_path)
            continue

        graph = TAG.load(tag_path)

        # Load explanation text
        with open(exp_file, "r", encoding="utf-8") as f:
            payload = json.load(f)
        explanation_text = payload["messages"][-1]["content"]

        # Resolve mappings
        label_to_local, _ = build_local_label_maps(graph)
        supports_local = extract_support_nodes_from_explanation(explanation_text, label_to_local)

        if graph.global_nids is None:
            logger.warning("TAG missing global_nids; skipping %s", sample_id)
            continue

        # Map local -> global
        supports_global = [graph.global_nids[i] for i in supports_local if i < len(graph.global_nids)]

        # Target node global id
        target_global = graph.root_global_id if graph.root_global_id is not None else graph.global_nids[0]

        # 2-hop ego graph around target
        ego_graph = nx.ego_graph(G_full, target_global, radius=2)
        all_neighbors = set(ego_graph.nodes)

        s_plus_set = set([n for n in supports_global if n in all_neighbors])
        s_minus_set = set()  # GraphNarrator explanations don't label "NO" nodes

        # Original prediction class
        try:
            orig_pred_class = LABELS.index(graph.prediction)
        except ValueError:
            logger.warning("Unknown prediction label %s for %s", graph.prediction, sample_id)
            continue

        subset_orig = list(all_neighbors)
        p_orig = get_gnn_prediction_prob(
            model, data, text, subset_orig, target_global, orig_pred_class, encoder, device
        )

        s_list = list(s_plus_set)
        try:
            selected_nodes = list(nx.algorithms.approximation.steinertree.steiner_tree(ego_graph, s_list).nodes)
        except Exception:
            selected_nodes = []
        if len(selected_nodes) == 0:
            selected_nodes = s_list

        subset_suff = selected_nodes
        metrics["sizes"].append(len(subset_suff))

        # Fidelity
        subset_sorted = torch.tensor(sorted(subset_suff), dtype=torch.long, device=device)
        edge_index_sub, _ = subgraph(subset_sorted, data.edge_index, relabel_nodes=True)

        target_idx = (subset_sorted == target_global).nonzero(as_tuple=True)
        if len(target_idx[0]) == 0:
            metrics["fidelity_scores"].append(False)
        else:
            with torch.no_grad():
                embs = torch.concat(
                    [encoder.encode(text[i]).detach().cpu() for i in subset_sorted.tolist()], dim=0
                ).to(device)
                out = model.forward_gnn(embs, edge_index_sub.to(device))
                out_class = out.argmax(dim=-1)
                metrics["fidelity_scores"].append(out_class[target_idx[0].item()].item() == orig_pred_class)

        p_suff = get_gnn_prediction_prob(
            model, data, text, subset_suff, target_global, orig_pred_class, encoder, device
        )

        # Comprehensiveness
        nodes_to_remove = s_plus_set - {target_global}
        subset_comp = list(all_neighbors - nodes_to_remove)
        p_comp = get_gnn_prediction_prob(
            model, data, text, subset_comp, target_global, orig_pred_class, encoder, device
        )

        # Random baseline
        num_to_remove = len(nodes_to_remove)
        candidates_to_remove = list(all_neighbors - {target_global})
        if len(candidates_to_remove) >= num_to_remove:
            random_remove = set(random.sample(candidates_to_remove, num_to_remove))
            subset_rand = list(all_neighbors - random_remove)
        else:
            subset_rand = list(all_neighbors)
        p_rand = get_gnn_prediction_prob(
            model, data, text, subset_rand, target_global, orig_pred_class, encoder, device
        )

        # Alignment (no "NO" nodes in GraphNarrator explanations)
        nodes_to_remove_align = s_minus_set - {target_global}
        subset_align = list(all_neighbors - nodes_to_remove_align)
        p_align = get_gnn_prediction_prob(
            model, data, text, subset_align, target_global, orig_pred_class, encoder, device
        )

        metrics["prob_orig"].append(p_orig)
        metrics["prob_suff"].append(p_suff)
        metrics["prob_comp"].append(p_comp)
        metrics["prob_rand"].append(p_rand)
        metrics["prob_align"].append(p_align)

    summary = save_metrics_summary(exp_dir=exp_dir, metrics=metrics, num_requested=len(exp_files))

    logger.info("--- Evaluation Results (GSPELL-style) ---")
    logger.info("Fidelity (Sufficiency): %.4f", summary["fidelity_sufficiency"])
    logger.info("Explanation Size: %.4f", summary["explanation_size"])
    logger.info("Comprehensiveness (Prob Drop removing Expl): %.4f", summary["comprehensiveness_drop"])
    logger.info("Random Baseline (Prob Drop removing Random): %.4f", summary["random_baseline_drop"])
    logger.info("Alignment Check (Prob Drop removing 'NO' nodes): %.4f", summary["alignment_drop"])

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp_dir", type=str, required=True, help="Path to generated explanations dir")
    parser.add_argument("--pkl_dir", type=str, default="outputs/pkls", help="Path to TAG pkls")
    parser.add_argument("--gnn_ckpt", type=str, required=True, help="Path to GNN checkpoint")
    parser.add_argument("--cora_data_path", type=str, required=True, help="Path to cora_canonical.pt")
    parser.add_argument("--num_eval_samples", type=int, default=50)
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()

    evaluate(
        exp_dir=args.exp_dir,
        pkl_dir=args.pkl_dir,
        gnn_ckpt=args.gnn_ckpt,
        cora_data_path=args.cora_data_path,
        num_eval_samples=args.num_eval_samples,
        device=args.device,
    )
