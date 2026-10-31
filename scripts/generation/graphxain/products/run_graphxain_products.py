"""
GraphXAIN for Amazon Products (ogbn-products)
==============================================
Adapted from GraphXAIN (Cedro & Martens, 2025) for the Amazon Products graph.

Pipeline:
  1. Load products_canonical.pt + sage_products_canonical.pt + products_vocab.json
  2. For each of the first 200 test nodes, run GNNExplainer to get:
       - node_mask  : importance per BOW feature dim (→ top-K vocab words)
       - edge_mask  : importance per co-purchase edge (→ top-K neighbor products)
  3. Build a structured prompt and call GPT-4o or Llama
  4. Save two output files:
       output/graphxain_products_{gpt4o|llama}_narratives.json  {node_id: narrative_text}
       output/graphxain_products_dims.json                      {node_id: [top_k_dims]}
       (the dims file feeds directly into unified_eval_products.py)

Usage:
    python run_graphxain_products.py                          # GPT-4o, 200 nodes
    python run_graphxain_products.py --llm_backend llama      # Llama, 200 nodes
    python run_graphxain_products.py --max_nodes 5            # quick smoke-test
"""

import os
import sys
import json
import argparse

import torch
import torch.nn.functional as F
from torch_geometric.explain import Explainer, GNNExplainer
from torch_geometric.utils import k_hop_subgraph

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "utils"))
from gnn_model import GraphSAGE


# ── paths ─────────────────────────────────────────────────────────────────────
PRODUCTS_PT = "./products_canonical.pt"
GNN_CKPT    = "./sage_products_canonical.pt"
VOCAB_JSON  = "./llm-graph-cf/data/products_vocab.json"

# ── hyperparams ───────────────────────────────────────────────────────────────
TOP_K_FEATURES  = 7
TOP_K_NEIGHBORS = 7
SENTENCE_LIMIT  = 8
GPT_MODEL       = "gpt-4o"
LLAMA_MODEL     = "meta-llama/Meta-Llama-3.1-8B-Instruct"
SEED            = 42
NUM_HOPS        = 2
GNNEXPL_EPOCHS  = 100
MAX_NODES       = 200   # match the 200-node subset used by all other methods

# ── LLM context strings ───────────────────────────────────────────────────────
ML_TASK_INFO = (
    "Multi-class node classification task that predicts the product category of an Amazon "
    "product. The model classifies each product into one of 47 top-level Amazon categories "
    "such as Home & Kitchen, Electronics, Books, Sports & Outdoors, Beauty, and others."
)
DATASET_INFO = (
    "The Amazon Products dataset (ogbn-products) is a large-scale co-purchase graph of "
    "54,025 Amazon products. Each product (node) is represented as a 2,000-dimensional "
    "bag-of-words feature vector derived from the product's title and description — each "
    "feature is binary (1 = word present, 0 = absent). Edges connect products that are "
    "frequently co-purchased together (customers who bought one also bought the other). "
    "The task is to classify each product into its Amazon top-level category."
)
NODE_DESC = "Amazon product listing"
EDGE_DESC = "co-purchase links between Amazon products"


# ── model ─────────────────────────────────────────────────────────────────────

def load_model(ckpt_path, n_features, n_classes, device):
    model = GraphSAGE(
        in_channels=n_features,
        hidden_channels=768,
        out_channels=n_classes,
        num_layers=2,
        dropout=0.0,
    ).to(device)
    state = torch.load(ckpt_path, map_location=device, weights_only=True)
    model.load_state_dict(state)
    model.eval()
    return model


# ── explanation helpers ───────────────────────────────────────────────────────

def get_prediction(model, data, node_idx, device, label_names):
    with torch.no_grad():
        logits = model(data.x.to(device), data.edge_index.to(device))
        probs  = F.softmax(logits, dim=-1)
    pred_cls = probs[node_idx].argmax().item()
    return {
        "Target Node":     node_idx,
        "Predicted Class": label_names[pred_cls],
        "Confidence":      round(probs[node_idx, pred_cls].item(), 4),
    }


def extract_top_features(node_mask, node_features, vocab, top_k):
    mask = node_mask.squeeze()
    topk = torch.topk(mask, min(top_k, mask.numel()))
    dims = topk.indices.tolist()
    imps = topk.values.tolist()
    table = [
        {
            "word":               vocab[d],
            "feature_dim":        d,
            "feature_importance": round(imp, 4),
            "present_in_product": int(node_features[d].item()),
        }
        for d, imp in zip(dims, imps)
    ]
    return table, dims


def extract_top_neighbors(node_idx, edge_index, edge_mask, data, label_names, top_k):
    src, dst = edge_index
    nb_importance = {}
    for direction_mask in [(dst == node_idx), (src == node_idx)]:
        indices = direction_mask.nonzero(as_tuple=True)[0]
        for ei in indices.tolist():
            nb = src[ei].item() if dst[ei].item() == node_idx else dst[ei].item()
            imp = edge_mask[ei].item()
            if nb == node_idx:
                continue
            if nb not in nb_importance or imp > nb_importance[nb]:
                nb_importance[nb] = imp
    sorted_nbs = sorted(nb_importance.items(), key=lambda x: x[1], reverse=True)[:top_k]
    rows = []
    for nb, imp in sorted_nbs:
        rows.append({
            "Source Node":      nb,
            "Destination Node": node_idx,
            "Importance":       round(imp, 4),
            "Neighbor Class":   label_names[data.y[nb].item()],
            "Neighbor Text":    data.raw_text[nb][:200],
        })
    return rows


# ── prompt builder ────────────────────────────────────────────────────────────

def build_prompt(node_idx, product_text, pred_info, feat_table, nb_rows,
                 label_names, top_k_feat, sentence_limit):

    feat_str = "\n".join(
        f"  word='{r['word']}', importance={r['feature_importance']}, "
        f"present_in_product={r['present_in_product']}"
        for r in feat_table
    )

    nb_str = "\n".join(
        f"  Node {r['Source Node']} | edge_importance={r['Importance']} | "
        f"category={r['Neighbor Class']} | {r['Neighbor Text']}"
        for r in nb_rows
    ) if nb_rows else "  (no influential neighbors found)"

    return f"""Your goal is to generate a textual narrative explaining why a GNN model made a certain prediction for a target node, based on the output of a GNNExplainer.

### Machine Learning Task:
{ML_TASK_INFO}

### Dataset:
{DATASET_INFO}

### Target Product (node {node_idx}):
{product_text}

### Model Prediction:
{json.dumps(pred_info, indent=2)}

### Top-{top_k_feat} Most Important BOW Features (GNNExplainer node mask):
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the product description (1=yes, 0=no).
{feat_str}

### Most Influential Co-purchased Products (GNNExplainer edge mask, descending importance):
Each entry: neighbor node | edge importance | product category | product title/description excerpt.
{nb_str}

Generate a fluent, cohesive narrative explaining the prediction. Rules:

**Format rules:**
1) Start the explanation immediately — no preamble.
2) Limit the entire answer to {sentence_limit} sentences or fewer.
3) Do not use tables or bullet lists — write a narrative/story.

**Content rules:**
1) State clearly what category the model predicted for node {node_idx} and with what confidence.
2) Discuss how the top BOW features contributed — note whether each high-importance word is actually present or absent in the product listing.
3) Discuss how the most influential co-purchased products (neighbors) shaped the prediction.
4) Interpret WHY a feature or connection pushed the prediction in a certain direction.
5) Do not quote raw importance numbers; describe relative importance (e.g., "most influential", "second most important").
6) Keep in mind the target node is a {NODE_DESC} and edges are {EDGE_DESC}.
7) Use clear language that a general audience can understand.
"""


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_pt",      default=PRODUCTS_PT)
    parser.add_argument("--gnn_ckpt",     default=GNN_CKPT)
    parser.add_argument("--vocab",        default=VOCAB_JSON)
    parser.add_argument("--out_dir",      default=os.path.join(os.path.dirname(__file__), "output"))
    parser.add_argument("--top_k_feat",   type=int, default=TOP_K_FEATURES)
    parser.add_argument("--top_k_nb",     type=int, default=TOP_K_NEIGHBORS)
    parser.add_argument("--max_nodes",    type=int, default=MAX_NODES,
                        help="Number of test nodes to process (default 200 to match other methods)")
    parser.add_argument("--gpt_model",    default=GPT_MODEL)
    parser.add_argument("--seed",         type=int, default=SEED)
    parser.add_argument("--gnnexpl_epochs", type=int, default=GNNEXPL_EPOCHS,
                        help="GNNExplainer optimization epochs. Use 10-20 for CPU smoke tests.")
    parser.add_argument("--llm_backend",  default="openai", choices=["openai", "llama"],
                        help="LLM backend: 'openai' uses GPT-4o API; 'llama' uses transformers locally.")
    parser.add_argument("--llama_model",  default=LLAMA_MODEL)
    parser.add_argument("--split_path",   default=None,
                        help="Path to .npz split file; if provided, uses eval_idx instead of first max_nodes test nodes.")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    os.makedirs(args.out_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # ── load data ──────────────────────────────────────────────────────────
    print("Loading Products data ...")
    data = torch.load(args.data_pt, map_location="cpu", weights_only=False)
    label_names = data.label_names
    n_features  = data.x.shape[1]
    n_classes   = len(label_names)
    test_nodes  = data.test_mask.nonzero(as_tuple=True)[0].tolist()
    print(f"  Nodes={data.num_nodes}  Features={n_features}  Classes={n_classes}  "
          f"Test nodes={len(test_nodes)} (using first {args.max_nodes})")

    with open(args.vocab) as f:
        vocab = json.load(f)
    assert len(vocab) == n_features, f"Vocab mismatch: {len(vocab)} vs {n_features}"
    print(f"  Vocabulary: {len(vocab)} Porter-stemmed words")

    # ── load GNN ───────────────────────────────────────────────────────────
    print("Loading GNN (sage_products_canonical.pt) ...")
    model = load_model(args.gnn_ckpt, n_features, n_classes, device)
    with torch.no_grad():
        logits = model(data.x.to(device), data.edge_index.to(device))
        preds  = logits.argmax(dim=-1).cpu()
    test_acc = (preds[data.test_mask] == data.y[data.test_mask]).float().mean()
    print(f"  Test accuracy: {test_acc:.4f}")

    # ── GNNExplainer ───────────────────────────────────────────────────────
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

    # ── LLM backend ────────────────────────────────────────────────────────
    if args.llm_backend == "openai":
        from openai import OpenAI
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("WARNING: OPENAI_API_KEY not set — LLM calls will fail.")
        llm_client = OpenAI(api_key=api_key)
        print(f"LLM backend: OpenAI ({args.gpt_model})")
    else:
        import torch as _torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        print(f"LLM backend: Llama via transformers ({args.llama_model})")
        llm_tokenizer = AutoTokenizer.from_pretrained(args.llama_model)
        llm_client = AutoModelForCausalLM.from_pretrained(
            args.llama_model,
            torch_dtype=_torch.float16,
            device_map="auto",
        )
        llm_client.eval()
        print(f"  Llama loaded on: {next(llm_client.parameters()).device}")

    # ── resume support ─────────────────────────────────────────────────────
    narr_suffix = "llama" if args.llm_backend == "llama" else "gpt4o"
    narr_path = os.path.join(args.out_dir, f"graphxain_products_{narr_suffix}_narratives.json")
    dims_path = os.path.join(args.out_dir, "graphxain_products_dims.json")

    narratives: dict = {}
    dims_map:   dict = {}
    if os.path.exists(narr_path):
        with open(narr_path) as f:
            narratives = json.load(f)
        print(f"  Resuming: {len(narratives)} nodes already processed")
    if os.path.exists(dims_path):
        with open(dims_path) as f:
            dims_map = json.load(f)

    if args.split_path:
        import numpy as np
        splits = np.load(args.split_path)
        nodes_to_run = sorted(splits["eval_idx"].tolist())
        print(f"Using split eval_idx: {len(nodes_to_run)} nodes, range {min(nodes_to_run)}-{max(nodes_to_run)}")
    else:
        nodes_to_run = test_nodes[:args.max_nodes]
    todo = [n for n in nodes_to_run if str(n) not in narratives]
    print(f"\nProcessing {len(todo)} nodes ...")

    def save():
        with open(narr_path, "w") as f:
            json.dump(narratives, f, indent=2)
        with open(dims_path, "w") as f:
            json.dump(dims_map, f, indent=2)

    # ── main loop ──────────────────────────────────────────────────────────
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
            edge_index_sub = edge_index_sub.to(device)
            local_target = mapping.item()

            expl = explainer(x_sub, edge_index_sub, index=local_target)
            node_mask = expl.node_mask.squeeze().cpu()
            edge_mask = expl.edge_mask.cpu()
            edge_index_cpu = edge_index_sub.cpu()

            feat_table, top_dims = extract_top_features(
                node_mask, data.x[node_idx], vocab, args.top_k_feat
            )
            global_edge_index = subset[edge_index_cpu]
            nb_rows = extract_top_neighbors(
                node_idx, global_edge_index, edge_mask, data, label_names, args.top_k_nb
            )
            pred_info = get_prediction(model, data, node_idx, device, label_names)

            dims_map[key] = top_dims

        except Exception as e:
            print(f"EXPLAIN_ERROR: {e}")
            continue

        try:
            prompt = build_prompt(
                node_idx, data.raw_text[node_idx],
                pred_info, feat_table, nb_rows,
                label_names, args.top_k_feat, SENTENCE_LIMIT,
            )

            if args.llm_backend == "openai":
                narrative = llm_client.chat.completions.create(
                    model=args.gpt_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=1.0,
                ).choices[0].message.content.strip()
            else:
                import torch as _torch
                messages = [{"role": "user", "content": prompt}]
                inputs = llm_tokenizer.apply_chat_template(
                    messages, tokenize=True, add_generation_prompt=True,
                    return_tensors="pt"
                ).to(llm_client.device)
                with _torch.no_grad():
                    out_ids = llm_client.generate(
                        inputs, max_new_tokens=512, temperature=1.0,
                        top_p=0.95, do_sample=True, repetition_penalty=1.1,
                        pad_token_id=llm_tokenizer.eos_token_id,
                    )
                new_tokens = out_ids[0][inputs.shape[-1]:]
                narrative = llm_tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

            narratives[key] = narrative
            print(f"OK  category={pred_info['Predicted Class']}")

        except Exception as e:
            print(f"LLM_ERROR (dims saved): {e}")

        if (i + 1) % 10 == 0:
            save()

    save()
    print(f"\nDone. {len(narratives)} narratives saved.")
    print(f"  Narratives : {narr_path}")
    print(f"  Dims (eval): {dims_path}")


if __name__ == "__main__":
    main()
