"""
Additive persistence wrapper around GSPELL's unmodified Cora pipeline.

Does NOT change eval_utils.py or main.py. Monkeypatches
eval_utils.build_inputs_cora_bow at import time so every exact prompt (decoded
from the real tokens handed to model.generate -- not a reconstruction) is
logged to prompts_raw.jsonl as it's built, then runs main.py's own
__main__ block unmodified via runpy so all of GSPELL's own logic (GNN
loading, projector, generation loop, resume-from-checkpoint, output saving)
is untouched.

GSPELL's own generate_exp_by_llm already persists neighbor lists + raw LLM
output (the "explanation" field is the undecoded model output) inside
GSPELL_explanations.pt -- this wrapper only adds the missing piece: the
exact prompt text.
"""
import json
import os
import sys
import time

REPO = "./LOGIC2/GSPELL"
PROD_DIR = "./production_run_2026-07-27/gspell_cora"
os.makedirs(PROD_DIR, exist_ok=True)
PROMPT_LOG_PATH = f"{PROD_DIR}/prompts_raw.jsonl"

os.chdir(REPO)
sys.path.insert(0, REPO)

sys.argv = [
    "main.py",
    "-cff", "./config/cora.yaml",
    "-m", "gspell",
    "-wno",
    "--cora_data_path", "./cora_canonical.pt",
    "--split_path", "./cora_splits_seed42.npz",
    "-pgp", "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/sage.pth",
    "-pdp", "./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth",
    "-ppp", "./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-23-12-28/projector.pth",
    "--seed", "42",
]

import eval_utils  # noqa: E402

_orig_build_inputs_cora_bow = eval_utils.build_inputs_cora_bow


def _instrumented(gnn_preds, target_node, selected_neighbors, dataset, tokenizer, with_chat_template, device):
    tokens = _orig_build_inputs_cora_bow(
        gnn_preds, target_node, selected_neighbors, dataset, tokenizer, with_chat_template, device
    )
    prompt_text = tokenizer.decode(tokens.input_ids[0], skip_special_tokens=False)
    predicted_label = dataset._data.label_info[str(gnn_preds[target_node].item())]
    record = {
        "target_node": target_node,
        "neighbors": list(selected_neighbors),
        "predicted_category_in_prompt": predicted_label,
        "prompt": prompt_text,
        "timestamp": time.time(),
    }
    with open(PROMPT_LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")
    return tokens


eval_utils.build_inputs_cora_bow = _instrumented

import runpy  # noqa: E402

runpy.run_path("main.py", run_name="__main__")
