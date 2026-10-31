"""
GraphXAIN full evaluation for Cora (2-hop prompts)
===================================================
Runs GNNExplainer + Llama-3.1-8B on all 542 test_idx nodes from
cora_splits_seed42.npz, with separate 1-hop and 2-hop neighbor sections
in the Llama prompt (matching the Products full-eval script format).

Upgrades vs the original run_graphxain_cora.py:
  - Prompt includes separate 1-hop and 2-hop neighbor tables
  - Checkpointing: skips already-processed nodes on resume

Outputs (all keyed by global node ID string):
  output/graphxain_cora_dims_full.json                    {node_id: [top_k_dims]}
  output/graphxain_cora_llama_2hop_narratives_full.json   {node_id: narrative}
"""

import os
import sys
import json
import re
import argparse

import torch
import torch.nn.functional as F
import numpy as np
from nltk.stem import PorterStemmer
from torch_geometric.explain import Explainer, GNNExplainer
from torch_geometric.utils import k_hop_subgraph

_ps = PorterStemmer()

def _destem(stem, raw_text):
    """Return the first real word from raw_text that Porter-stems to `stem`."""
    for word in re.findall(r'[a-zA-Z]+', raw_text.lower()):
        if _ps.stem(word) == stem:
            return word
    return stem

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "utils"))
from gnn_model import GraphSAGE


# ── paths ─────────────────────────────────────────────────────────────────────
CORA_PT     = "./cora_canonical.pt"
GNN_CKPT    = "./llm-graph-cf/pretrained/sage_canonical.pt"
VOCAB_JSON  = "./llm-graph-cf/data/cora_vocab.json"
SPLITS_NPZ  = "./graphnarrCora/GraphNarrator/cora_splits_seed42.npz"
LLAMA_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"

# ── hyperparams ───────────────────────────────────────────────────────────────
TOP_K_FEAT     = 7
TOP_K_1HOP     = 7
TOP_K_2HOP     = 10
NUM_HOPS       = 2
GNNEXPL_EPOCHS = 100
SEED           = 42

# ── LLM context strings ───────────────────────────────────────────────────────
ML_TASK_INFO = (
    "Multi-class node classification task that predicts the research area of an academic "
    "computer science paper. The model classifies each paper into one of 7 categories: "
    "Case_Based, Genetic_Algorithms, Neural_Networks, Probabilistic_Methods, "
    "Reinforcement_Learning, Rule_Learning, or Theory."
)
DATASET_INFO = (
    "The Cora citation network contains 2,708 academic computer science papers. "
    "Each paper (node) is represented as a bag-of-words feature vector of 1,433 unique "
    "Porter-stemmed words derived from the paper's title and abstract — each feature is "
    "binary (1 = word present, 0 = absent). Edges represent undirected citation links "
    "between papers. The task is to classify each paper into its research sub-area based "
    "on its content and the content of papers it cites or is cited by."
)


def load_model(ckpt, nf, nc, dev):
    m = GraphSAGE(in_channels=nf, hidden_channels=768, out_channels=nc,
                  num_layers=2, dropout=0.0).to(dev)
    m.load_state_dict(torch.load(ckpt, map_location=dev, weights_only=True))
    m.eval()
    return m


def extract_top_features(node_mask, node_features, vocab, top_k, raw_text=""):
    mask = node_mask.squeeze()
    topk = torch.topk(mask, min(top_k, mask.numel()))
    rows = []
    for d, imp in zip(topk.indices.tolist(), topk.values.tolist()):
        stem = vocab[d]
        present = int(node_features[d].item())
        word = _destem(stem, raw_text) if present == 1 and raw_text else stem
        rows.append({
            "word":       word,
            "dim":        d,
            "importance": round(imp, 4),
            "present":    present,
        })
    return rows, topk.indices.tolist()


def extract_neighbors_by_hop(node_idx, global_edge_index, edge_mask, data, label_names,
                              top_k_1hop, top_k_2hop):
    src, dst = global_edge_index

    hop1_imp = {}
    for mask in [(dst == node_idx), (src == node_idx)]:
        for ei in mask.nonzero(as_tuple=True)[0].tolist():
            nb = src[ei].item() if dst[ei].item() == node_idx else dst[ei].item()
            if nb == node_idx:
                continue
            imp = edge_mask[ei].item()
            if nb not in hop1_imp or imp > hop1_imp[nb]:
                hop1_imp[nb] = imp

    hop1_nodes = set(hop1_imp.keys())

    hop2_imp = {}
    n_edges = src.shape[0]
    for ei in range(n_edges):
        s, d = src[ei].item(), dst[ei].item()
        if s == node_idx or d == node_idx:
            continue
        imp = edge_mask[ei].item()
        for nb1, nb2 in [(s, d), (d, s)]:
            if nb1 in hop1_nodes and nb2 not in hop1_nodes and nb2 != node_idx:
                if nb2 not in hop2_imp or imp > hop2_imp[nb2]:
                    hop2_imp[nb2] = imp

    def make_rows(imp_dict, top_k):
        rows = []
        for nb, imp in sorted(imp_dict.items(), key=lambda x: x[1], reverse=True)[:top_k]:
            rows.append({
                "node":       nb,
                "importance": round(imp, 4),
                "class":      label_names[data.y[nb].item()],
                "text":       data.raw_text[nb][:200] if hasattr(data, 'raw_text') else "",
            })
        return rows

    return make_rows(hop1_imp, top_k_1hop), make_rows(hop2_imp, top_k_2hop)


def build_prompt(node_idx, paper_text, pred_info, feat_table, rows_1hop, rows_2hop):
    feat_str = "\n".join(
        f"  word='{r['word']}', importance={r['importance']}, present_in_paper={r['present']}"
        for r in feat_table
    )

    def fmt_rows(rows):
        if not rows:
            return "  (none)"
        return "\n".join(
            f"  Node {r['node']} | edge_importance={r['importance']} | "
            f"class={r['class']} | {r['text']}"
            for r in rows
        )

    return f"""Your goal is to generate a textual narrative explaining why a GNN model made a certain prediction for a target node, based on the output of a GNNExplainer.

### Machine Learning Task:
{ML_TASK_INFO}

### Dataset:
{DATASET_INFO}

### Target Paper (node {node_idx}):
{paper_text}

### Model Prediction:
{json.dumps(pred_info, indent=2)}

### Top-{TOP_K_FEAT} Most Important BOW Features (GNNExplainer node mask):
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
{feat_str}

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance):
These are papers directly cited by or citing the target paper.
{fmt_rows(rows_1hop)}

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask):
These papers are not directly connected to the target but are linked through shared citation partners.
{fmt_rows(rows_2hop)}

Generate a fluent, cohesive narrative explaining the prediction. Rules:

**Format rules:**
1) Start the explanation immediately — no preamble.
2) Limit the entire answer to 8 sentences or fewer.
3) Do not use tables or bullet lists — write a single cohesive paragraph.
4) Do NOT reference specific node IDs (e.g., "Node 4") — describe papers by their topic or title instead.

**Content rules:**
1) State clearly what class the model predicted and with what confidence.
2) Discuss how the top BOW features contributed — note whether each high-importance word is actually present or absent in the paper.
3) Discuss how the most influential direct (1-hop) citation neighbors shaped the prediction, describing them by topic or title.
4) Mention how 2-hop neighbors reinforce the pattern if relevant.
5) Interpret WHY a feature or connection pushed the prediction in a certain direction.
6) Do not quote raw importance numbers; use relative language (e.g., "most influential", "strongly associated").
7) Use clear language that a general audience can understand.
"""


def generate_llama(prompt, tokenizer, model):
    messages = [{"role": "user", "content": prompt}]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    with torch.no_grad():
        out_ids = model.generate(
            inputs, max_new_tokens=600, temperature=1.0,
            top_p=0.95, do_sample=True, repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id,
        )
    new_tokens = out_ids[0][inputs.shape[-1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cora_pt",        default=CORA_PT)
    parser.add_argument("--gnn_ckpt",       default=GNN_CKPT)
    parser.add_argument("--vocab",          default=VOCAB_JSON)
    parser.add_argument("--splits",         default=SPLITS_NPZ)
    parser.add_argument("--out_dir",        default=os.path.join(os.path.dirname(__file__), "output"))
    parser.add_argument("--llama_model",    default=LLAMA_MODEL)
    parser.add_argument("--top_k_feat",     type=int, default=TOP_K_FEAT)
    parser.add_argument("--top_k_1hop",     type=int, default=TOP_K_1HOP)
    parser.add_argument("--top_k_2hop",     type=int, default=TOP_K_2HOP)
    parser.add_argument("--gnnexpl_epochs", type=int, default=GNNEXPL_EPOCHS)
    parser.add_argument("--seed",           type=int, default=SEED)
    parser.add_argument("--max_nodes",        type=int, default=None,
                        help="Process only the first N test nodes (for testing)")
    parser.add_argument("--skip_llm",         action="store_true",
                        help="Only run GNNExplainer (dims), skip Llama narrative generation")
    parser.add_argument("--regen_narratives", action="store_true",
                        help="Re-run Llama for all nodes (re-runs GNNExplainer too; keeps existing dims)")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    os.makedirs(args.out_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    print("Loading Cora data ...")
    data = torch.load(args.cora_pt, map_location="cpu", weights_only=False)
    label_names = data.label_names
    n_features  = data.x.shape[1]
    n_classes   = len(label_names)

    with open(args.vocab) as f:
        vocab = json.load(f)
    assert len(vocab) == n_features, f"Vocab mismatch: {len(vocab)} vs {n_features}"

    splits = np.load(args.splits)
    test_idx = sorted(splits["test_idx"].tolist())
    if args.max_nodes:
        test_idx = test_idx[:args.max_nodes]
    print(f"  Nodes={data.num_nodes}  Features={n_features}  Classes={n_classes}")
    print(f"  test_idx: {len(test_idx)} nodes, range {min(test_idx)}-{max(test_idx)}")

    print("Loading GNN ...")
    model = load_model(args.gnn_ckpt, n_features, n_classes, device)
    with torch.no_grad():
        logits = model(data.x.to(device), data.edge_index.to(device))
        probs  = F.softmax(logits, dim=-1).cpu()
    test_acc = (probs[test_idx].argmax(dim=-1) == data.y[test_idx]).float().mean()
    print(f"  test_idx accuracy: {test_acc:.4f}")

    explainer = Explainer(
        model=model,
        algorithm=GNNExplainer(epochs=args.gnnexpl_epochs),
        explanation_type="model",
        node_mask_type="common_attributes",
        edge_mask_type="object",
        model_config=dict(
            mode="multiclass_classification",
            task_level="node",
            return_type="raw",
        ),
    )

    if not args.skip_llm:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        print(f"Loading Llama ({args.llama_model}) ...")
        llm_tokenizer = AutoTokenizer.from_pretrained(args.llama_model)
        llm_model = AutoModelForCausalLM.from_pretrained(
            args.llama_model, torch_dtype=torch.float16, device_map="auto"
        )
        llm_model.eval()
        print(f"  Llama on: {next(llm_model.parameters()).device}")
    else:
        llm_tokenizer = llm_model = None
        print("Skipping Llama (--skip_llm)")

    dims_path = os.path.join(args.out_dir, "graphxain_cora_dims_full.json")
    narr_path = os.path.join(args.out_dir, "graphxain_cora_llama_2hop_narratives_full.json")

    dims_map:   dict = {}
    narratives: dict = {}
    if os.path.exists(dims_path):
        with open(dims_path) as f:
            dims_map = json.load(f)
        print(f"  Resuming dims: {len(dims_map)} already done")
    if os.path.exists(narr_path) and not args.skip_llm:
        with open(narr_path) as f:
            narratives = json.load(f)
        print(f"  Resuming narr: {len(narratives)} already done")

    if args.regen_narratives:
        todo = [n for n in test_idx if str(n) not in narratives]
    else:
        todo = [n for n in test_idx if str(n) not in dims_map]
    print(f"\nProcessing {len(todo)} nodes ...")

    def save():
        with open(dims_path, "w") as f:
            json.dump(dims_map, f, indent=2)
        if not args.skip_llm:
            with open(narr_path, "w") as f:
                json.dump(narratives, f, indent=2)

    for i, node_idx in enumerate(todo):
        key = str(node_idx)
        print(f"[{i+1}/{len(todo)}] node {node_idx} ...", end=" ", flush=True)

        try:
            subset, edge_index_sub, mapping, _ = k_hop_subgraph(
                node_idx=node_idx,
                num_hops=NUM_HOPS,
                edge_index=data.edge_index,
                relabel_nodes=True,
                num_nodes=data.num_nodes,
                flow="target_to_source",
            )
            x_sub = data.x[subset].to(device)
            edge_index_sub_dev = edge_index_sub.to(device)
            local_target = mapping.item()

            expl = explainer(x_sub, edge_index_sub_dev, index=local_target)
            node_mask       = expl.node_mask.squeeze().cpu()
            edge_mask       = expl.edge_mask.cpu()
            edge_index_cpu  = edge_index_sub.cpu()
            global_edge_idx = subset[edge_index_cpu]

            paper_text = data.raw_text[node_idx] if hasattr(data, 'raw_text') else ""
            feat_table, top_dims = extract_top_features(
                node_mask, data.x[node_idx], vocab, args.top_k_feat, raw_text=paper_text
            )
            rows_1hop, rows_2hop = extract_neighbors_by_hop(
                node_idx, global_edge_idx, edge_mask, data, label_names,
                args.top_k_1hop, args.top_k_2hop,
            )
            pred_cls = probs[node_idx].argmax().item()
            pred_info = {
                "Target Node":     node_idx,
                "True Class":      label_names[data.y[node_idx].item()],
                "Predicted Class": label_names[pred_cls],
                "Confidence":      round(probs[node_idx, pred_cls].item(), 4),
                "Correct":         label_names[pred_cls] == label_names[data.y[node_idx].item()],
            }

            dims_map[key] = top_dims

        except Exception as e:
            print(f"EXPLAIN_ERROR: {e}")
            continue

        if not args.skip_llm and key not in narratives:
            try:
                prompt = build_prompt(node_idx, paper_text[:300], pred_info,
                                      feat_table, rows_1hop, rows_2hop)
                narrative = generate_llama(prompt, llm_tokenizer, llm_model)
                narratives[key] = narrative
                print(f"OK  class={pred_info['Predicted Class']}")
            except Exception as e:
                print(f"LLM_ERROR (dims saved): {e}")
        else:
            print(f"dims_only  class={pred_info['Predicted Class']}")

        if (i + 1) % 10 == 0:
            save()

    save()
    print(f"\nDone. {len(dims_map)} dims, {len(narratives)} narratives saved.")
    print(f"  Dims      : {dims_path}")
    print(f"  Narratives: {narr_path}")


if __name__ == "__main__":
    main()
