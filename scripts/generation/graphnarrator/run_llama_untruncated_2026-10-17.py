"""
Full-eval-set GraphNarrator generation with BASE meta-llama/Meta-Llama-3.1-8B-Instruct,
6000-char truncation REMOVED, for Cora (pkls_cora_eval, 542) or Products (pkls_products, 200).
The survey nodes are all inside these eval sets:
  Cora     4->1, 510->85, 2334->463, 1062->203, 884->168
  Products 6813->23, 1852->3, 8766->33, 8438->29

Follows run_products_untruncated_local_2026-09-07.py (same TAG load, graph.text() call,
template/example versions, FreeTextExpGenerator.gen() decoding: max_new_tokens=2048,
do_sample=True, temperature=0.3, top_p=0.95, and FreeTextExpGenerator.save()).
free_text_explanation.py is NOT modified.

Two additions, both aimed at the 19/200 OOMs of the 2026-09-07 run:

1. lm_head last-position slice. transformers 4.44.2's LlamaForCausalLM.forward runs lm_head
   over every prompt position and then calls .float() (15k tokens x 128256 vocab x 4B ~ 7.7 GB),
   but generate() only reads logits[:, -1, :]. Wrapping lm_head to project only the last
   position gives identical sampled tokens with the memory spike removed. The 09-07 OOM sizes
   scaled linearly with doc length (14.23 GiB @57k chars, 7.86 GiB @30k), which matches this
   cause rather than quadratic attention.
2. 4-bit fallback pass. Nodes that still OOM in fp16 are retried after reloading the model in
   4-bit NF4 (FreeTextExpGenerator's own use_4bit config). Nodes that fail both passes go to
   oom_nodes.json. Per-node precision is recorded in run_manifest.json.

Usage: python run_llama_untruncated_2026-10-17.py --dataset cora|products
"""
import argparse
import gc
import json
import sys
import time
import traceback
from pathlib import Path

import torch

ROOT = Path("./graphnarrCora/GraphNarrator")
sys.path.insert(0, str(ROOT))
from tag import TAG  # noqa: E402
from free_text_explanation import FreeTextExpGenerator  # noqa: E402
from log import logger  # noqa: E402

MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"
SEED = 42
PKL_DIRS = {
    "cora": ROOT / "outputs/pkls_cora_eval",
    "products": ROOT / "outputs/pkls_products",
}
SURVEY = {
    "cora": {4: 1, 510: 85, 2334: 463, 1062: 203, 884: 168},
    "products": {6813: 23, 1852: 3, 8766: 33, 8438: 29},
}


class LastPositionHead(torch.nn.Module):
    """Wraps lm_head so the forward pass projects only the last sequence position."""

    def __init__(self, head):
        super().__init__()
        self.head = head

    def forward(self, hidden_states):
        return self.head(hidden_states[:, -1:, :])


def patch_lm_head(generator):
    llm = generator._hf_model
    if not isinstance(llm.lm_head, LastPositionHead):
        llm.lm_head = LastPositionHead(llm.lm_head)


def free_model(generator):
    generator._hf_model = None
    generator._hf_tokenizer = None
    generator._hf_model_id = None
    gc.collect()
    torch.cuda.empty_cache()


def run_pass(generator, indexs, pkl_dir, exp_dir, template_version, example_version, use_4bit, manifest, failed):
    for i, index in enumerate(indexs):
        output_file = exp_dir / f"{index}.json"
        if output_file.exists():
            continue

        try:
            graph = TAG.load(pkl_dir / f"{index}.pkl")
        except FileNotFoundError:
            logger.error(f"{pkl_dir / f'{index}.pkl'} does not exists!")
            continue

        start = time.time()
        label = graph.prediction
        try:
            document = graph.text(style="document", masker="", with_score=True)
        except Exception as e:
            logger.error("stringify graph-%d failed! Error: %s", index, e)
            continue

        # no 6000-char truncation (intentional, see module docstring)

        torch.manual_seed(SEED + index)
        try:
            prompt, response = generator.gen(
                model=MODEL_ID,
                label=label,
                document=document,
                template_version=template_version,
                example_version=example_version,
                use_local_hf=True,
                use_4bit=use_4bit,
            )
        except torch.cuda.OutOfMemoryError as e:
            torch.cuda.empty_cache()
            failed[str(index)] = {"doc_len": len(document), "precision": "4bit" if use_4bit else "fp16",
                                  "error": str(e)[:300]}
            print(f"[{i+1}/{len(indexs)}] node {index} (doc_len={len(document)}) OOM in "
                  f"{'4bit' if use_4bit else 'fp16'}", flush=True)
            continue
        except Exception:
            failed[str(index)] = {"doc_len": len(document), "precision": "4bit" if use_4bit else "fp16",
                                  "error": traceback.format_exc()[-300:]}
            logger.error("generation failed for node %d:\n%s", index, traceback.format_exc())
            continue

        FreeTextExpGenerator.save(prompt, response, output_file)
        failed.pop(str(index), None)
        manifest["nodes"][str(index)] = {"precision": "4bit" if use_4bit else "fp16", "doc_len": len(document),
                                         "prediction": label, "seconds": round(time.time() - start, 1)}
        print(f"[{i+1}/{len(indexs)}] node {index} (doc_len={len(document)}) OK "
              f"{'4bit' if use_4bit else 'fp16'} class={label} time={time.time()-start:.1f}s", flush=True)


def _load(generator, use_4bit):
    # Same from_pretrained args as FreeTextExpGenerator.gen(use_local_hf=True); filling its cache
    # fields means gen() reuses this (patched) model instead of loading its own.
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_fast=True)
    if use_4bit:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
        )
        llm = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="auto", quantization_config=bnb_config)
    else:
        llm = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=torch.float16, device_map="auto")
    generator._hf_model = llm
    generator._hf_tokenizer = tokenizer
    generator._hf_model_id = MODEL_ID
    generator._hf_4bit = use_4bit
    patch_lm_head(generator)
    print(f"Loaded {MODEL_ID} ({'4bit' if use_4bit else 'fp16'}), attn={llm.config._attn_implementation}, "
          f"lm_head patched to last position", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["cora", "products"], required=True)
    args = ap.parse_args()

    pkl_dir = PKL_DIRS[args.dataset]
    exp_dir = ROOT / f"outputs/generated_expls-{args.dataset}_llama_untruncated_2026-10-17"
    exp_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = exp_dir / "run_manifest.json"
    oom_path = exp_dir / "oom_nodes.json"

    template_version = "v_products" if args.dataset == "products" else "v6"
    example_version = "v_products" if args.dataset == "products" else "v1"

    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {
        "model": MODEL_ID, "dataset": args.dataset, "pkl_dir": str(pkl_dir), "truncation": "none",
        "decoding": "FreeTextExpGenerator.gen local-HF defaults: max_new_tokens=2048, do_sample=True, "
                    "temperature=0.3, top_p=0.95",
        "seed": f"torch.manual_seed({SEED} + pkl_index) before each node",
        "template_version": template_version, "example_version": example_version,
        "survey_nodes_global_to_pkl_index": SURVEY[args.dataset],
        "nodes": {},
    }
    failed = json.loads(oom_path.read_text()) if oom_path.exists() else {}

    indexs = sorted(int(p.stem) for p in pkl_dir.glob("*.pkl"))
    # survey nodes first so they are guaranteed even if the job hits its time limit
    survey_idx = sorted(SURVEY[args.dataset].values())
    indexs = survey_idx + [i for i in indexs if i not in survey_idx]
    print(f"Processing {len(indexs)} nodes from {pkl_dir} -> {exp_dir}", flush=True)

    generator = FreeTextExpGenerator()

    def checkpoint():
        manifest_path.write_text(json.dumps(manifest, indent=2))
        oom_path.write_text(json.dumps(failed, indent=2))

    try:
        _load(generator, use_4bit=False)
        run_pass(generator, indexs, pkl_dir, exp_dir, template_version, example_version, False, manifest, failed)
        checkpoint()

        retry = [int(k) for k in failed]
        if retry:
            print(f"\n4-bit fallback pass for {len(retry)} nodes: {retry}", flush=True)
            free_model(generator)
            _load(generator, use_4bit=True)
            run_pass(generator, retry, pkl_dir, exp_dir, template_version, example_version, True, manifest, failed)
    finally:
        checkpoint()

    n_done = len(list(exp_dir.glob("[0-9]*.json")))
    print(f"\nDone. {n_done}/{len(indexs)} generated, {len(failed)} failed both passes. Output: {exp_dir}")


if __name__ == "__main__":
    main()
