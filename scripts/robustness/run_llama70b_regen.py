"""Robustness analysis 2: regenerate all three methods' narrations with
Llama-3.1-70B-Instruct (hugging-quants GPTQ-INT4) for the nodes in robustness_subset.json.

Only the model changes relative to each method's Llama-3.1-8B-Instruct reference run:

cf             llm-graph-cf llms_m.py run (jobs 51137055/51137056). Messages, sampling and
               LLM(...) args are imported from run_qwen14b_regen.py, which imports them
               read-only from the repo. Sampling: temperature 0.1, top_p 0.8, top_k 10,
               repetition penalty 1.05, 2048 tokens, seed 42.
graphxain      graphxain_schemaaligned_production_2026-08-16 (HF generate). Prompt verbatim
               from prompts_dump.jsonl as a single user message. Sampling: temperature 1.0,
               top_p 0.95, top_k 50 (HF default), repetition penalty 1.1, 600 tokens, seed 42.
graphnarrator  exp100/101 (FreeTextExpGenerator.gen, use_local_hf=True). User prompt verbatim
               from generated_expls-{100,101}/{pkl_index}.json: already 6000-char truncated,
               and matches a pkl rebuild byte for byte. System message is the one gen() sent.
               Sampling: temperature 0.3, top_p 0.95, top_k 50 (HF default), 2048 tokens, seed 42.

Token-level parity: every prompt goes to vLLM as explicit token IDs, reproducing what each
reference path fed its 8B model. The 8B tokenizer prepends BOS to plain text and the 70B GPTQ
tokenizer does not. Both llms_m.py (text -> vLLM) and gen() (tokenizer(chat_text)) therefore fed
<|begin_of_text|> twice, so the cf and graphnarrator prompts get an extra BOS here.
GraphXAIN's apply_chat_template(tokenize=True) fed it once. --no_bos_parity drops the extra BOS.

Backend note: GraphXAIN and GraphNarrator originally ran on HF transformers; here they run on
vLLM. Sampling parameters match, but random draws cannot match across backends anyway.

Resumable: one JSON per node, existing files are skipped. Each node is written as it finishes,
so a job killed at the 1-hour debug-quad limit can be resubmitted to continue.

Usage:
  python run_llama70b_regen.py --methods cf graphxain graphnarrator --datasets cora products \
      --out_dir llama70b_smoke --nodes cora:1782 products:1958
  python run_llama70b_regen.py --methods cf --datasets cora --out_dir llama70b
"""
import argparse
import datetime
import json
import os
import socket
import time

from run_qwen14b_regen import (  # noqa: E402  (also puts llm-graph-cf on sys.path)
    CHAR_LIMIT,
    DESCRIPTIONS,
    EXPLAINER,
    LLM_ARGS,
    REPO,
    SAMPLING as CF_SAMPLING,
    SEED,
    SUBSET,
    build_messages,
)

import transformers  # noqa: E402
import vllm  # noqa: E402
from huggingface_hub import snapshot_download  # noqa: E402
from transformers import AutoTokenizer  # noqa: E402
from vllm import LLM, SamplingParams  # noqa: E402
from vllm.inputs import TokensPrompt  # noqa: E402

from src.llms_m import set_full_reproducibility  # noqa: E402

MODEL_ID = "hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"
REVISION = "1b0ae7f9d6da8b79f36fdc24912f950ecb2b6e91"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "."
BOS = 128000

SAMPLING = {
    "cf": CF_SAMPLING,
    "graphxain": dict(temperature=1.0, top_p=0.95, top_k=50, repetition_penalty=1.1, max_tokens=600, seed=SEED),
    "graphnarrator": dict(temperature=0.3, top_p=0.95, top_k=50, max_tokens=2048, seed=SEED),
}
EXTRA_BOS = {"cf": True, "graphxain": False, "graphnarrator": True}
GN_SYSTEM = "You are a helpful, reliable and responsible AI assistant."
GN_SOURCE_EXP = {"cora": 100, "products": 101}


def load_inputs(method, ds, nodes):
    """Return {cf_key: messages} for the requested subset nodes."""
    if method == "cf":
        base = f"{REPO}/data/{ds}/{EXPLAINER}/random_seed_{SEED}_"
        fact = json.load(open(base + "factual_graph_descriptions.json"))
        cf = json.load(open(base + "counterfactual_graph_descriptions.json"))
        return {n["cf_key"]: build_messages(ds, n["cf_key"], fact, cf) for n in nodes}
    if method == "graphxain":
        dump = {}
        for line in open(f"{ROOT}/graphxain_schemaaligned_production_2026-08-16/{ds}/prompts_dump.jsonl"):
            rec = json.loads(line)
            dump[rec["target_node"]] = rec["prompt"]
        return {n["cf_key"]: [{"role": "user", "content": dump[n["global_node_id"]]}] for n in nodes}
    if method == "graphnarrator":
        out = {}
        for n in nodes:
            src = f"{ROOT}/graphnarrCora/GraphNarrator/outputs/generated_expls-{GN_SOURCE_EXP[ds]}/{n['cf_key']}.json"
            user = json.load(open(src))["messages"][1]["content"]
            out[n["cf_key"]] = [{"role": "system", "content": GN_SYSTEM}, {"role": "user", "content": user}]
        return out
    raise ValueError(method)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--methods", nargs="+", required=True, choices=list(SAMPLING))
    ap.add_argument("--datasets", nargs="+", default=list(DESCRIPTIONS), choices=list(DESCRIPTIONS))
    ap.add_argument("--out_dir", required=True, help="subfolder of robustness_2026-10-30/")
    ap.add_argument("--nodes", nargs="*", default=None, help="optional ds:global_id list (smoke test)")
    ap.add_argument("--no_bos_parity", action="store_true", help="never add the extra BOS")
    args = ap.parse_args()

    subset = json.load(open(SUBSET))
    wanted = {(s.split(":")[0], int(s.split(":")[1])) for s in args.nodes} if args.nodes else None

    set_full_reproducibility(SEED)
    model_path = snapshot_download(MODEL_ID, revision=REVISION, local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    assert tokenizer.bos_token_id == BOS

    job = os.environ.get("SLURM_JOB_ID", "local")
    settings = {
        "model_id": MODEL_ID, "revision": REVISION, "model_path": model_path,
        "methods": args.methods, "datasets": args.datasets, "nodes": args.nodes,
        "sampling_params": {m: SAMPLING[m] for m in args.methods},
        "extra_bos": {m: EXTRA_BOS[m] and not args.no_bos_parity for m in args.methods},
        "llm_args": LLM_ARGS, "char_limit_cf": CHAR_LIMIT,
        "versions": {"vllm": vllm.__version__, "transformers": transformers.__version__},
        "env": {k: os.environ.get(k) for k in ("VLLM_ENABLE_V1_MULTIPROCESSING", "HF_HUB_OFFLINE", "CC", "CUDA_HOME")},
        "slurm_job_id": job, "host": socket.gethostname(),
        "started": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    out_root = os.path.join(HERE, args.out_dir)
    os.makedirs(out_root, exist_ok=True)
    settings_path = os.path.join(out_root, f"settings_{'-'.join(args.methods)}_{'-'.join(args.datasets)}_{job}.json")
    json.dump(settings, open(settings_path, "w"), indent=2)

    t0 = time.time()
    llm = LLM(model=model_path, **LLM_ARGS)
    settings["model_load_seconds"] = round(time.time() - t0, 1)
    print(f"model loaded in {settings['model_load_seconds']}s", flush=True)

    counts = {}
    for method in args.methods:
        sp = SamplingParams(**SAMPLING[method])
        extra_bos = EXTRA_BOS[method] and not args.no_bos_parity
        for ds in args.datasets:
            nodes = [n for n in subset["datasets"][ds]["nodes"]
                     if wanted is None or (ds, n["global_node_id"]) in wanted]
            if not nodes:
                continue
            out_dir = os.path.join(out_root, method, ds)
            os.makedirs(out_dir, exist_ok=True)
            inputs = load_inputs(method, ds, nodes)
            for n in nodes:
                gid, key = n["global_node_id"], n["cf_key"]
                out_path = os.path.join(out_dir, f"{gid}.json")
                if os.path.exists(out_path):
                    continue
                messages = inputs[key]
                if method == "graphxain":
                    ids = list(tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True))
                    text = tokenizer.decode(ids)
                else:
                    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                    ids = tokenizer(text, add_special_tokens=False).input_ids
                    if extra_bos:
                        ids = [BOS] + ids
                rec = {"method": method, "dataset": ds, "global_node_id": gid, "cf_key": key,
                       "is_survey": n["is_survey"], "messages": messages,
                       "prompt_chars": len(text), "prompt_tokens": len(ids),
                       "leading_bos": ids[:2].count(BOS), "sampling_params": SAMPLING[method],
                       "model_id": MODEL_ID, "revision": REVISION, "slurm_job_id": job}
                if method == "cf" and len(text) > CHAR_LIMIT:
                    rec["status"] = "skipped_char_limit"
                else:
                    try:
                        start = time.time()
                        out = llm.generate([TokensPrompt(prompt_token_ids=ids)], sampling_params=sp)[0]
                        elapsed = time.time() - start
                        o = out.outputs[0]
                        rec.update(status="ok", response=o.text, output_tokens=len(o.token_ids),
                                   finish_reason=o.finish_reason,
                                   hit_max_tokens=len(o.token_ids) >= SAMPLING[method]["max_tokens"],
                                   gen_seconds=round(elapsed, 2),
                                   output_tokens_per_sec=round(len(o.token_ids) / elapsed, 2))
                    except (ValueError, AssertionError, RuntimeError) as e:
                        rec.update(status="error", error=f"{type(e).__name__}: {e}")
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump(rec, f, indent=1)
                counts[rec["status"]] = counts.get(rec["status"], 0) + 1
                print(f"[{method}:{ds}:{gid}] " + json.dumps({k: rec.get(k) for k in (
                    "status", "prompt_tokens", "output_tokens", "finish_reason", "gen_seconds",
                    "output_tokens_per_sec")}), flush=True)

    settings["finished"] = datetime.datetime.now().isoformat(timespec="seconds")
    settings["status_counts_this_job"] = counts
    json.dump(settings, open(settings_path, "w"), indent=2)
    print(f"done: {counts}", flush=True)


if __name__ == "__main__":
    main()
