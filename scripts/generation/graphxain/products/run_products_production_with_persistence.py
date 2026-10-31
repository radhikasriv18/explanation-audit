"""
Additive persistence wrapper around GraphXAIN Products' unmodified pipeline
(run_graphxain_products_full_eval.py). See run_cora_production_with_persistence.py
in GraphXAIN_Cora/ for the rationale -- identical approach, applied to the
Products script's equivalent functions.
"""
import importlib.util
import json
import os
import sys
import time

REPO_FILE = "./GraphXAIN_Products/run_graphxain_products_full_eval.py"
PROD_DIR = "./production_run_2026-07-27/graphxain_products"
os.makedirs(PROD_DIR, exist_ok=True)
PERSIST_PATH = f"{PROD_DIR}/explainer_and_prompts.jsonl"

spec = importlib.util.spec_from_file_location("gx_products_full_eval", REPO_FILE)
gx = importlib.util.module_from_spec(spec)
sys.modules["gx_products_full_eval"] = gx
spec.loader.exec_module(gx)

_orig_extract_top_features = gx.extract_top_features
_orig_extract_neighbors_by_hop = gx.extract_neighbors_by_hop
_orig_build_prompt = gx.build_prompt
_orig_generate_llama = gx.generate_llama

_state = {}


def _wrapped_extract_top_features(node_mask, node_features, vocab, top_k, raw_text=""):
    rows, top_dims = _orig_extract_top_features(node_mask, node_features, vocab, top_k, raw_text=raw_text)
    _state["feat_table"] = rows
    return rows, top_dims


def _wrapped_extract_neighbors_by_hop(node_idx, global_edge_index, edge_mask, data, label_names, top_k_1hop, top_k_2hop):
    rows_1hop, rows_2hop = _orig_extract_neighbors_by_hop(
        node_idx, global_edge_index, edge_mask, data, label_names, top_k_1hop, top_k_2hop
    )
    _state["node_idx"] = node_idx
    _state["rows_1hop"] = rows_1hop
    _state["rows_2hop"] = rows_2hop
    return rows_1hop, rows_2hop


def _wrapped_build_prompt(node_idx, product_text, pred_info, feat_table, rows_1hop, rows_2hop):
    prompt = _orig_build_prompt(node_idx, product_text, pred_info, feat_table, rows_1hop, rows_2hop)
    _state["prompt"] = prompt
    _state["pred_info"] = pred_info
    return prompt


def _wrapped_generate_llama(prompt, tokenizer, model):
    narrative = _orig_generate_llama(prompt, tokenizer, model)
    record = {
        "target_node": _state.get("node_idx"),
        "gnnexplainer_top_features": _state.get("feat_table"),
        "gnnexplainer_1hop_neighbors": _state.get("rows_1hop"),
        "gnnexplainer_2hop_neighbors": _state.get("rows_2hop"),
        "prediction": _state.get("pred_info"),
        "prompt": prompt,
        "raw_llm_output": narrative,
        "timestamp": time.time(),
    }
    with open(PERSIST_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")
    return narrative


gx.extract_top_features = _wrapped_extract_top_features
gx.extract_neighbors_by_hop = _wrapped_extract_neighbors_by_hop
gx.build_prompt = _wrapped_build_prompt
gx.generate_llama = _wrapped_generate_llama

sys.argv = ["run_graphxain_products_full_eval.py", "--out_dir", PROD_DIR]
gx.main()
