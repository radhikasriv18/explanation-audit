"""Robustness experiment step 2: regenerate counterfactual-framework narrations
with Qwen2.5-14B-Instruct-GPTQ-Int4 for the nodes in robustness_subset.json.

Only the model changes relative to the Llama-3.1-8B run (jobs 51137055/51137056):
- same factual/counterfactual graph descriptions
  (llm-graph-cf/data/{ds}/cf-gnnexplainer-canonical/random_seed_42_*.json)
- same system prompt (data.kb.get_system_prompt, "adjacency matrix", "node") and
  user prompt (src.prompts.CANONICAL_PROMPT / STANDARD_PROMPT, same branch logic
  as src/llms_m.py), imported from the repo read-only, not copied
- same vLLM LLM(...) and SamplingParams(...) arguments as src/llms_m.py
- prompts rebuilt through Qwen's own chat template (never the stored Llama
  prompt strings)

Deliberate differences from llms_m.py's loop, none of which touch generation:
no OOM retry (llms_m.py's retry silently reloads with max_model_len=4096);
failures are recorded instead. Outputs never overwrite existing files.

Usage:
  python run_qwen14b_regen.py --out_dir smoke_test --nodes cora:1782 products:1958
  python run_qwen14b_regen.py --out_dir production
"""
import argparse
import datetime
import json
import os
import socket
import sys
import time

REPO = "./llm-graph-cf"
HERE = os.path.dirname(os.path.abspath(__file__))
SUBSET = os.path.join(HERE, "robustness_subset.json")
sys.path.insert(0, REPO)

import vllm  # noqa: E402
import transformers  # noqa: E402
from huggingface_hub import snapshot_download  # noqa: E402
from transformers import AutoTokenizer  # noqa: E402
from vllm import LLM, SamplingParams  # noqa: E402

from data.kb import cora_description, products_description, get_system_prompt  # noqa: E402
from src.prompts import CANONICAL_PROMPT, STANDARD_PROMPT  # noqa: E402
from src.llms_m import MODEL_MAPPING, set_full_reproducibility  # noqa: E402

MODEL_KEY = "qwen_14B_Q4_GPTQ"
MODEL_ID = MODEL_MAPPING[MODEL_KEY]  # Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4
REVISION = "08fdbde5eea15cd2aae884125fbfd604dec19818"
EXPLAINER = "cf-gnnexplainer-canonical"
SEED = 42

# Identical to the Llama run: main.py defaults + sbatch flags + llms_m.py hardcodes.
SAMPLING = dict(temperature=0.1, top_p=0.8, repetition_penalty=1.05,
                max_tokens=2048, top_k=10, seed=SEED)
LLM_ARGS = dict(gpu_memory_utilization=0.8, max_model_len=32000, max_num_seqs=1)
CHAR_LIMIT = 200000  # llms_m.py skips templated prompts longer than this
DESCRIPTIONS = {"cora": cora_description, "products": products_description}


def build_messages(ds, key, fact, cf):
    # Same branch logic as llms_m.py, prompt_type == "standard".
    if str(fact[key]).strip().lower().startswith("given the factual graph"):
        user = CANONICAL_PROMPT.format(combined_description=fact[key], kb=DESCRIPTIONS[ds])
    else:
        user = STANDARD_PROMPT.format(fact[key], cf[key], DESCRIPTIONS[ds])
    return [
        {"role": "system", "content": get_system_prompt(perturbation_type="adjacency matrix", task="node")},
        {"role": "user", "content": user},
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_dir", required=True, help="subfolder of robustness_2026-10-30/")
    ap.add_argument("--nodes", nargs="*", default=None,
                    help="optional ds:global_id list (smoke test); default = whole subset")
    args = ap.parse_args()

    out_dir = os.path.join(HERE, args.out_dir)
    os.makedirs(out_dir, exist_ok=True)
    resp_paths = {ds: os.path.join(out_dir, f"qwen14b_gptq_int4_{ds}_Response.json") for ds in DESCRIPTIONS}
    meta_path = os.path.join(out_dir, "per_node_metadata.json")
    settings_path = os.path.join(out_dir, "settings.json")
    for p in list(resp_paths.values()) + [meta_path, settings_path]:
        assert not os.path.exists(p), f"{p} exists; refusing to overwrite"

    subset = json.load(open(SUBSET))
    wanted = None
    if args.nodes:
        wanted = {(s.split(":")[0], int(s.split(":")[1])) for s in args.nodes}
    todo = [(ds, n) for ds in DESCRIPTIONS for n in subset["datasets"][ds]["nodes"]
            if wanted is None or (ds, n["global_node_id"]) in wanted]
    assert wanted is None or len(todo) == len(wanted), "some --nodes not in subset"

    set_full_reproducibility(SEED)
    # Local snapshot path pins the exact revision and avoids hub calls on the compute node.
    model_path = snapshot_download(MODEL_ID, revision=REVISION, local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    sampling_params = SamplingParams(**SAMPLING)

    settings = {
        "model_key": MODEL_KEY, "model_id": MODEL_ID, "revision": REVISION, "model_path": model_path,
        "explainer": EXPLAINER, "prompt_type": "standard", "data_seed_prefix": SEED,
        "sampling_params": SAMPLING, "llm_args": LLM_ARGS, "char_limit": CHAR_LIMIT,
        "full_reproducibility_seed": SEED, "vllm_engine_seed": "default (None -> 0), as in Llama run",
        "versions": {"vllm": vllm.__version__, "transformers": transformers.__version__},
        "env": {k: os.environ.get(k) for k in ("VLLM_ENABLE_V1_MULTIPROCESSING", "HF_HUB_OFFLINE", "CC", "CUDA_HOME")},
        "slurm_job_id": os.environ.get("SLURM_JOB_ID"), "host": socket.gethostname(),
        "started": datetime.datetime.now().isoformat(timespec="seconds"),
        "nodes_requested": [f"{ds}:{n['global_node_id']}" for ds, n in todo],
        "reference_llama_run": "cf_gnnexplainer_run_2026-08-10/llm_gen_{cora,products}.sh (jobs 51137055/51137056)",
    }
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=2)

    t0 = time.time()
    llm = LLM(model=model_path, **LLM_ARGS)
    settings["model_load_seconds"] = round(time.time() - t0, 1)

    data = {}
    for ds in DESCRIPTIONS:
        base = f"{REPO}/data/{ds}/{EXPLAINER}/random_seed_{SEED}_"
        data[ds] = (json.load(open(base + "factual_graph_descriptions.json")),
                    json.load(open(base + "counterfactual_graph_descriptions.json")))

    responses = {ds: {} for ds in DESCRIPTIONS}
    meta = []
    for ds, n in todo:
        key, gid = n["cf_key"], n["global_node_id"]
        fact, cf = data[ds]
        text = tokenizer.apply_chat_template(build_messages(ds, key, fact, cf),
                                             tokenize=False, add_generation_prompt=True)
        rec = {"dataset": ds, "global_node_id": gid, "cf_key": key, "is_survey": n["is_survey"],
               "prompt_chars": len(text),
               "prompt_tokens": len(tokenizer(text, add_special_tokens=False).input_ids)}
        if len(text) > CHAR_LIMIT:
            rec["status"] = "skipped_char_limit"
            meta.append(rec)
            continue
        try:
            start = time.time()
            out = llm.generate([text], sampling_params=sampling_params)[0]
            elapsed = time.time() - start
        except (ValueError, AssertionError, RuntimeError) as e:
            rec.update(status="error", error=f"{type(e).__name__}: {e}")
            meta.append(rec)
            print(f"[{ds}:{gid}] ERROR {rec['error']}", flush=True)
            continue
        o = out.outputs[0]
        rec.update(status="ok", output_tokens=len(o.token_ids), finish_reason=o.finish_reason,
                   hit_max_tokens=len(o.token_ids) >= SAMPLING["max_tokens"],
                   gen_seconds=round(elapsed, 2),
                   output_tokens_per_sec=round(len(o.token_ids) / elapsed, 2))
        responses[ds][key] = (out.prompt, o.text)
        meta.append(rec)
        print(f"[{ds}:{gid}] {json.dumps({k: rec[k] for k in ('prompt_tokens', 'output_tokens', 'finish_reason', 'gen_seconds', 'output_tokens_per_sec')})}", flush=True)

        # Incremental save after every node (small subset; cheap).
        with open(resp_paths[ds], "w", encoding="utf-8") as f:
            json.dump(responses[ds], f, indent=4)
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=2)

    for ds, p in resp_paths.items():
        if responses[ds]:
            with open(p, "w", encoding="utf-8") as f:
                json.dump(responses[ds], f, indent=4)
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    settings["finished"] = datetime.datetime.now().isoformat(timespec="seconds")
    settings["n_ok"] = sum(r["status"] == "ok" for r in meta)
    settings["n_hit_max_tokens"] = sum(r.get("hit_max_tokens", False) for r in meta)
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=2)
    print(f"done: {settings['n_ok']}/{len(todo)} ok, {settings['n_hit_max_tokens']} hit max_tokens", flush=True)


if __name__ == "__main__":
    main()
