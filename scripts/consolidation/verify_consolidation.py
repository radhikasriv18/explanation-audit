import json
import random

import numpy as np
import torch

random.seed(0)

CORA_SPLIT = set(np.load("./LOGIC2/GSPELL/cora_splits_seed42.npz")["test_idx"].tolist())
PRODUCTS_SPLIT = set(np.load("./LOGIC2/GSPELL/products_splits_seed42.npz")["eval_idx"].tolist())

C = "./production_run_2026-07-27/consolidated"

EXPECTED = {
    "graphxain_cora.json": (542, CORA_SPLIT),
    "graphxain_products.json": (200, PRODUCTS_SPLIT),
    "gspell_cora.json": (542, CORA_SPLIT),
    "gspell_products_embedding.json": (200, PRODUCTS_SPLIT),
    "gspell_products_textfallback.json": (200, PRODUCTS_SPLIT),
    "graphnarrator_cora.json": (542, CORA_SPLIT),
    "graphnarrator_products.json": (200, PRODUCTS_SPLIT),
    "llmgraphcf_cora.json": (407, CORA_SPLIT),
    "llmgraphcf_products.json": (177, PRODUCTS_SPLIT),
}

print("=== 1. Key validity + coverage ===")
for fname, (expected_n, split) in EXPECTED.items():
    with open(f"{C}/{fname}") as f:
        d = json.load(f)
    keys = [int(k) for k in d.keys()]
    n = len(keys)
    all_valid = all(k in split for k in keys)
    all_unique = len(set(keys)) == n
    status = "OK" if (n == expected_n and all_valid and all_unique) else "MISMATCH"
    print(f"{fname:38s} n={n:4d} expected={expected_n:4d} all_keys_in_split={all_valid} unique={all_unique} [{status}]")

print("\n=== 2. Spot-check byte-identity (3 nodes/file) ===")


def spotcheck_graphxain(fname, jsonl_path):
    with open(f"{C}/{fname}") as f:
        cons = json.load(f)
    native = {}
    with open(jsonl_path) as f:
        for line in f:
            rec = json.loads(line)
            native[str(rec["target_node"])] = rec
    keys = random.sample(list(cons.keys()), 3)
    for k in keys:
        ok_expl = cons[k]["explanation_text"] == native[k]["raw_llm_output"]
        ok_prompt = cons[k]["prompt"] == native[k]["prompt"]
        print(f"  {fname} node {k}: explanation_match={ok_expl} prompt_match={ok_prompt}")


def spotcheck_gspell_cora():
    with open(f"{C}/gspell_cora.json") as f:
        cons = json.load(f)
    pt = torch.load(
        "./LOGIC2/GSPELL/output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-14-17-08/GSPELL_explanations.pt",
        weights_only=False,
    )
    native = {}
    for node_batches in pt:
        nid = str(node_batches[0]["target_node"])
        native.setdefault(nid, []).extend(b["explanation"] for b in node_batches)
    keys = random.sample(list(cons.keys()), 3)
    for k in keys:
        native_concat_substrings_present = all(e in cons[k]["explanation_text"] for e in native[k])
        print(f"  gspell_cora.json node {k}: all {len(native[k])} native batch explanation(s) present verbatim in consolidated text = {native_concat_substrings_present}")


def spotcheck_gspell_products_embedding():
    with open(f"{C}/gspell_products_embedding.json") as f:
        cons = json.load(f)
    pt = torch.load(
        "./LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt",
        weights_only=False,
    )
    native = {}
    for node_batches in pt:
        nid = str(node_batches[0]["target_node"])
        native.setdefault(nid, []).extend(b["explanation"] for b in node_batches)
    keys = random.sample(list(cons.keys()), 3)
    for k in keys:
        ok = all(e in cons[k]["explanation_text"] for e in native[k])
        print(f"  gspell_products_embedding.json node {k}: all native batch explanation(s) present verbatim = {ok}; prompt is None = {cons[k]['prompt'] is None}")


def spotcheck_gspell_products_textfallback():
    with open(f"{C}/gspell_products_textfallback.json") as f:
        cons = json.load(f)
    pt = torch.load(
        "./LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-28-11-08-30/LLM_explanations.pkl",
        weights_only=False,
    )
    native = {}
    for node_batches in pt:
        nid = str(node_batches[0]["target_node"])
        for b in node_batches:
            msgs = {m["role"]: m["content"] for m in b["explanation"]}
            native.setdefault(nid, {"assistant": [], "user": []})
            native[nid]["assistant"].append(msgs.get("assistant", ""))
            native[nid]["user"].append(msgs.get("user", ""))
    keys = random.sample(list(cons.keys()), 3)
    for k in keys:
        ok_expl = all(e in cons[k]["explanation_text"] for e in native[k]["assistant"])
        ok_prompt = all(p in cons[k]["prompt"] for p in native[k]["user"])
        print(f"  gspell_products_textfallback.json node {k}: explanation_match={ok_expl} prompt_match={ok_prompt}")


def spotcheck_graphnarrator(fname, exp_dir, mapping_path):
    with open(f"{C}/{fname}") as f:
        cons = json.load(f)
    with open(mapping_path) as f:
        mapping = json.load(f)["mapping"]
    global_to_local = {v["root_global_id"]: int(k) for k, v in mapping.items()}
    keys = random.sample(list(cons.keys()), 3)
    for k in keys:
        local_idx = global_to_local[int(k)]
        with open(f"{exp_dir}/{local_idx}.json") as f:
            native = json.load(f)
        msgs = {m["role"]: m["content"] for m in native["messages"]}
        ok_expl = cons[k]["explanation_text"] == msgs.get("assistant", "")
        ok_prompt = cons[k]["prompt"] == msgs.get("user", "")
        print(f"  {fname} node {k} (local_idx={local_idx}): explanation_match={ok_expl} prompt_match={ok_prompt}")


def spotcheck_llmgraphcf(fname, response_path, target_dict_path):
    with open(f"{C}/{fname}") as f:
        cons = json.load(f)
    with open(response_path) as f:
        responses = json.load(f)
    with open(target_dict_path) as f:
        target_dict = json.load(f)
    global_to_seqkey = {v["Target_Node_ID"]: k for k, v in target_dict.items() if k in responses}
    keys = random.sample(list(cons.keys()), 3)
    for k in keys:
        seqkey = global_to_seqkey[int(k)]
        prompt, text = responses[seqkey]
        ok_expl = cons[k]["explanation_text"] == text
        ok_prompt = cons[k]["prompt"] == prompt
        print(f"  {fname} node {k} (seqkey={seqkey}): explanation_match={ok_expl} prompt_match={ok_prompt}")


spotcheck_graphxain("graphxain_cora.json", "./production_run_2026-07-27/graphxain_cora/explainer_and_prompts.jsonl")
spotcheck_graphxain("graphxain_products.json", "./production_run_2026-07-27/graphxain_products/explainer_and_prompts.jsonl")
spotcheck_gspell_cora()
spotcheck_gspell_products_embedding()
spotcheck_gspell_products_textfallback()
spotcheck_graphnarrator(
    "graphnarrator_cora.json",
    "./graphnarrCora/GraphNarrator/outputs/generated_expls-100",
    "./production_run_2026-07-27/graphnarrator_cora/index_to_global_node_id_mapping.json",
)
spotcheck_graphnarrator(
    "graphnarrator_products.json",
    "./graphnarrCora/GraphNarrator/outputs/generated_expls-101",
    "./production_run_2026-07-27/graphnarrator_products/index_to_global_node_id_mapping.json",
)
spotcheck_llmgraphcf(
    "llmgraphcf_cora.json",
    "./llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json",
    "./llm-graph-cf/data/cora/cf-gnnfeatures-canonical-production-2026-07-27/random_seed_42_factual_target_dict_repr.json",
)
spotcheck_llmgraphcf(
    "llmgraphcf_products.json",
    "./llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json",
    "./llm-graph-cf/data/products/cf-gnnfeatures-canonical-production-2026-07-27/random_seed_42_factual_target_dict_repr.json",
)

print("\n=== 3. Nodes present in native output but missing from consolidated ===")


def native_node_set_graphxain(jsonl_path):
    s = set()
    with open(jsonl_path) as f:
        for line in f:
            s.add(str(json.loads(line)["target_node"]))
    return s


def check_missing(fname, native_set):
    with open(f"{C}/{fname}") as f:
        cons_set = set(json.load(f).keys())
    missing = native_set - cons_set
    print(f"{fname}: native={len(native_set)} consolidated={len(cons_set)} missing_from_consolidated={sorted(missing) if missing else 'none'}")


check_missing("graphxain_cora.json", native_node_set_graphxain("./production_run_2026-07-27/graphxain_cora/explainer_and_prompts.jsonl"))
check_missing("graphxain_products.json", native_node_set_graphxain("./production_run_2026-07-27/graphxain_products/explainer_and_prompts.jsonl"))

pt_cora = torch.load("./LOGIC2/GSPELL/output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-14-17-08/GSPELL_explanations.pt", weights_only=False)
check_missing("gspell_cora.json", {str(b["target_node"]) for nb in pt_cora for b in nb})

pt_prod_emb = torch.load("./LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt", weights_only=False)
check_missing("gspell_products_embedding.json", {str(b["target_node"]) for nb in pt_prod_emb for b in nb})

pt_prod_text = torch.load("./LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-28-11-08-30/LLM_explanations.pkl", weights_only=False)
check_missing("gspell_products_textfallback.json", {str(b["target_node"]) for nb in pt_prod_text for b in nb})

with open("./production_run_2026-07-27/graphnarrator_cora/index_to_global_node_id_mapping.json") as f:
    m = json.load(f)["mapping"]
check_missing("graphnarrator_cora.json", {str(v["root_global_id"]) for v in m.values() if v["root_global_id"] is not None})

with open("./production_run_2026-07-27/graphnarrator_products/index_to_global_node_id_mapping.json") as f:
    m = json.load(f)["mapping"]
check_missing("graphnarrator_products.json", {str(v["root_global_id"]) for v in m.values() if v["root_global_id"] is not None})

with open("./llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json") as f:
    resp = json.load(f)
with open("./llm-graph-cf/data/cora/cf-gnnfeatures-canonical-production-2026-07-27/random_seed_42_factual_target_dict_repr.json") as f:
    td = json.load(f)
check_missing("llmgraphcf_cora.json", {str(td[k]["Target_Node_ID"]) for k in resp})

with open("./llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json") as f:
    resp = json.load(f)
with open("./llm-graph-cf/data/products/cf-gnnfeatures-canonical-production-2026-07-27/random_seed_42_factual_target_dict_repr.json") as f:
    td = json.load(f)
check_missing("llmgraphcf_products.json", {str(td[k]["Target_Node_ID"]) for k in resp})
