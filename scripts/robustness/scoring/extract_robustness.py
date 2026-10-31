"""Claim extraction for the robustness texts (texts.json) with the frozen pilot extractor.

Imported unchanged from grounding_judge_pilot/extract_claims.py: MODEL_ID (Llama-3.1-8B-Instruct),
MAX_NEW_TOKENS (4096), build_messages + TEMPLATES["v3"] (the v3 prompt the answer key was built
from) and parse_output. The generate() call repeats extract_claims.main() argument for argument:
fp16, SDPA, greedy (do_sample=False), chat template rendered then tokenized without special tokens.
Only the input list and output folder differ. One JSON per text, existing files are skipped,
--shard/--nshards split the work across jobs.
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "./grounding_judge_pilot")
import extract_claims as ec  # noqa: E402

import torch  # noqa: E402
from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: E402

HERE = Path(__file__).resolve().parent
PROMPT_VERSION = "v3"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--nshards", type=int, default=1)
    ap.add_argument("--judge-first", nargs="*", default=None,
                    help="method__config ids: restrict to these configurations on the judge subset (judge_subset.json)")
    args = ap.parse_args()

    entries = json.load(open(HERE / "texts.json"))
    if args.judge_first is not None:
        js = json.load(open(HERE / "judge_subset.json"))["datasets"]
        keep = {(ds, str(n["global_node_id"])) for ds, ns in js.items() for n in ns}
        entries = [e for e in entries if f"{e['method']}__{e['config']}" in args.judge_first and (e["dataset"], e["node"]) in keep]
    out_dir = HERE / "extractions_v3"
    out_dir.mkdir(exist_ok=True)
    # texts with no scored text (GraphNarrator output without a Free-Text section) have nothing to extract
    todo = [e for i, e in enumerate(entries) if i % args.nshards == args.shard and e["text_scored"]
            and not (out_dir / f"{e['id']}.json").exists()]
    print(f"shard {args.shard}/{args.nshards}: {len(todo)} texts to extract", flush=True)
    if not todo:
        return

    tok = AutoTokenizer.from_pretrained(ec.MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(ec.MODEL_ID, torch_dtype=torch.float16, device_map="cuda:0", attn_implementation="sdpa")
    model.eval()
    print(f"loaded {ec.MODEL_ID} fp16 on {torch.cuda.get_device_name(0)}", flush=True)

    for e in todo:
        text = e["text_scored"]
        messages = ec.build_messages(e, text, PROMPT_VERSION)
        rendered = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        ids = tok(rendered, return_tensors="pt", add_special_tokens=False).to("cuda:0")
        t0 = time.time()
        with torch.no_grad():
            gen = model.generate(
                **ids,
                max_new_tokens=ec.MAX_NEW_TOKENS,
                do_sample=False,  # greedy == temperature 0
                temperature=None,
                top_p=None,
                pad_token_id=tok.eos_token_id,
            )
        new = gen[0, ids["input_ids"].shape[1]:]
        raw = tok.decode(new, skip_special_tokens=True)
        claims, diag = ec.parse_output(raw)
        diag["n_prompt_tokens"] = int(ids["input_ids"].shape[1])
        diag["n_output_tokens"] = int(new.shape[0])
        diag["hit_max_new_tokens"] = int(new.shape[0]) >= ec.MAX_NEW_TOKENS
        diag["seconds"] = round(time.time() - t0, 1)
        rec = {
            "run_id": e["id"], "method": e["method"], "config": e["config"], "dataset": e["dataset"],
            "node": e["node"], "source_file": e["source_file"], "source_locator": e["source_locator"],
            "text_scope": e["scored_scope"], "input_text": text, "text_scored_sha256_16": e["text_scored_sha256_16"],
            "model": ec.MODEL_ID, "prompt_version": PROMPT_VERSION,
            "generation": {"dtype": "float16", "do_sample": False, "temperature": 0, "max_new_tokens": ec.MAX_NEW_TOKENS},
            "gpu": torch.cuda.get_device_name(0),
            "versions": {"torch": torch.__version__, "transformers": __import__("transformers").__version__},
            "prompt_messages": messages, "prompt_rendered": rendered, "raw_output": raw,
            "claims": claims, "n_claims": len(claims), "parse_diagnostics": diag,
        }
        tmp = out_dir / f".{e['id']}.json.tmp"
        json.dump(rec, open(tmp, "w"), indent=1)
        tmp.rename(out_dir / f"{e['id']}.json")
        print(f"{e['id']:55s} claims={len(claims):3d} valid={diag['json_valid']} out_tok={diag['n_output_tokens']} "
              f"cap={diag['hit_max_new_tokens']} {diag['seconds']}s", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
