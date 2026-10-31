"""
Corrected-prompt regeneration of the full 542-node Cora production run,
isolating the ground-truth-leakage fix as the SOLE variable vs. the
original run_cora_production_with_persistence.py.

Confirmed diff (2026-09-07): run_graphxain_cora_full_eval.py's main()
(untouched by this script -- loaded via importlib exactly as the original
wrapper does) builds pred_info as:

    pred_info = {
        "Target Node":     node_idx,
        "True Class":      label_names[data.y[node_idx].item()],   # LEAKAGE
        "Predicted Class": label_names[pred_cls],
        "Confidence":      round(probs[node_idx, pred_cls].item(), 4),
        "Correct":         label_names[pred_cls] == label_names[data.y[node_idx].item()],  # LEAKAGE
    }

and this dict is rendered verbatim into the prompt's "Model Prediction"
block via json.dumps(pred_info, indent=2) inside build_prompt(). This
matches the corrected 8-node survey script's pred_info exactly (Target
Node / Predicted Class / Confidence only, no True Class or Correct).

This script does NOT edit run_graphxain_cora_full_eval.py (same
non-invasive monkeypatch approach as the original persistence wrapper).
It intercepts build_prompt() and strips the two leakage keys from the
pred_info dict it receives, before handing the (now clean) dict to the
ORIGINAL, unmodified build_prompt() -- every other function (GNNExplainer
call, feature/neighbor extraction, generate_llama's sampling params:
temperature=1.0, top_p=0.95, do_sample=True, repetition_penalty=1.1,
max_new_tokens=600; --top_k_feat/--top_k_1hop/--top_k_2hop CLI defaults;
paper_text[:300] truncation) is exactly the original script's code,
completely untouched. This isolates the leakage removal as the only
difference from the original 2026-07-27 production run.

Writes to a NEW directory -- does not touch run_graphxain_cora_full_eval.py,
run_cora_production_with_persistence.py, or any file under
production_run_2026-07-27/graphxain_cora/ or
production_run_2026-07-27/consolidated/.
"""
import importlib.util
import json
import os
import sys
import time

REPO_FILE = "./GraphXAIN_Cora/run_graphxain_cora_full_eval.py"
OUT_DIR = "./GraphXAIN_Cora/production_corrected_2026-09-07"
os.makedirs(OUT_DIR, exist_ok=True)
PERSIST_PATH = f"{OUT_DIR}/explainer_and_prompts.jsonl"

LEAKAGE_KEYS = ("True Class", "Correct")

spec = importlib.util.spec_from_file_location("gx_cora_full_eval_corrected", REPO_FILE)
gx = importlib.util.module_from_spec(spec)
sys.modules["gx_cora_full_eval_corrected"] = gx
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


def _wrapped_build_prompt(node_idx, paper_text, pred_info, feat_table, rows_1hop, rows_2hop):
    # THE FIX: strip the two leakage keys before the original build_prompt
    # ever sees them / json.dumps()'s them into the prompt. Every other
    # arg and every other line of build_prompt's template is untouched.
    clean_pred_info = {k: v for k, v in pred_info.items() if k not in LEAKAGE_KEYS}
    prompt = _orig_build_prompt(node_idx, paper_text, clean_pred_info, feat_table, rows_1hop, rows_2hop)
    _state["prompt"] = prompt
    _state["pred_info"] = clean_pred_info
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

sys.argv = ["run_graphxain_cora_full_eval.py", "--out_dir", OUT_DIR]
gx.main()
