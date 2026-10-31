"""
Phase 1 pilot — atomic-claim extraction with Llama-3.1-8B-Instruct (fp16, greedy
decoding = temperature 0) over the 21 answer-key texts in answer_key_texts.json.

Extraction only: no judging, no scoring, no OpenAI calls.

Per explanation writes extractions/<id>[__full].json with the exact chat prompt
(messages + rendered template string), the raw model output, the parsed claims
(after validation + merge of repeated claims) and parse diagnostics. Also writes
claim_counts.csv comparing the extracted count with the persisted adjudicated count.

GraphNarrator texts are run twice: on the adjudicated scope (Free-Text Explanation
section, primary) and on the full assistant message (suffix __full, secondary).

Run (GPU): venv python from graphnarrCora/GraphNarrator; see run_extract.sbatch.
"""
import argparse
import csv
import json
import re
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

HERE = Path(__file__).resolve().parent
MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"
MAX_NEW_TOKENS = 4096
CLAIM_TYPES = ["content", "structural", "importance", "class_state", "mechanism", "feature", "neighbor"]
ENTITY_KEYS = ["node_ids", "titles", "feature_words", "edges", "classes"]

SYSTEM_PROMPT = """You are a careful information-extraction system. You read an explanation that a model wrote about why a graph neural network (GNN) classified a target node, and you list the atomic factual claims it makes. You do not judge whether claims are true. You output JSON only."""

USER_TEMPLATE = """Extract every atomic factual claim from the EXPLANATION below.

Definitions
- An atomic claim states exactly one checkable fact (one subject, one property or relation). Split sentences that state several facts into several claims. Do not split one fact into pieces.
- Merge repeated claims: if the same fact is stated more than once (for example once in prose and again in a summary or dictionary), output it once.
- Skip: opinions, judgments of quality, hedged or speculative statements ("may", "might", "could", "possibly", "it is likely that"), generic statements about GNNs or datasets that are not about this graph, restatements of the task, and YES/NO votes.
- Dictionary output: if the explanation contains a dictionary such as infos={{...}}, treat EACH field as one claim (e.g. "Factual_Target_Node_Neighbors of node 510 are 192, 356, 519"), including empty fields (e.g. "Counterfactual_Target_Node_Neighbors of node 510 is empty"). Prose that repeats a dictionary field is the same claim; merge it.

claim_type (choose exactly one)
- content: what the TARGET node is about (its topic, title, abstract, product description).
- neighbor: a property of a specific NEIGHBOR node (its topic, title, content or label).
- structural: graph connectivity: which nodes are connected, neighbor lists, number of neighbors, hops, edges added or removed.
- importance: an importance/saliency/attention score, weight, or ranking of a node, edge, word or feature.
- class_state: a class label, predicted class, true class, counterfactual class, or prediction confidence.
- mechanism: a causal claim about how the GNN used specific information to reach or change its prediction (e.g. "removing the edge to node 930 changed the prediction").
- feature: a specific feature/keyword/bag-of-words term being present, absent, or changed for a node.

entities (copy exactly as written in the explanation; use [] when none)
- node_ids: integer node IDs, or labels such as "Node-1" / "Node-1.2" exactly as written.
- titles: paper or product titles quoted or named.
- feature_words: specific words/keywords/features named.
- edges: pairs [a, b] of connected or disconnected nodes named by the claim.
- classes: class/category names.

Output format: a single JSON object and nothing else, no markdown fences:
{{"claims": [{{"claim": "<one atomic claim, self-contained, with the subject node named>", "claim_type": "<type>", "entities": {{"node_ids": [], "titles": [], "feature_words": [], "edges": [], "classes": []}}}}]}}

TARGET NODE: {node}  (dataset: {dataset})

EXPLANATION:
<<<
{text}
>>>"""

# v2 (2026-10-06, approved): three fixes over v1 — (1) prose that restates an infos field is
# merged into that field's claim, (2) stricter skip rule for opinion/evaluative phrasing,
# (3) explicit subject-based typing of target vs neighbor claims. Everything else unchanged.
USER_TEMPLATE_V2 = """Extract every atomic factual claim from the EXPLANATION below.

Definitions
- An atomic claim states exactly one checkable fact (one subject, one property or relation). Split sentences that state several facts into several claims. Do not split one fact into pieces.
- Merge repeated claims: if the same fact is stated more than once, output it once.

Dictionary output and merging (apply when the explanation contains a dictionary such as infos={{...}})
- Output EXACTLY ONE claim per dictionary field, phrased from the field, including empty fields (e.g. "Counterfactual_Target_Node_Neighbors of node 510 is empty").
- Before outputting any prose claim, check it against every field. If the prose states the same fact as a field, even in different words, do NOT output it; the field claim already covers it. Examples of the same fact:
  * "node 510 is connected with nodes 192, 356 and 519" = Factual_Target_Node_Neighbors [192, 356, 519]
  * "node 510 is not connected to any other node in the counterfactual graph" = "node 510 lost all its connections" = Counterfactual_Target_Node_Neighbors []
  * "node 510 is classified as Theory" = Factual_Target_Node_Class 'Theory'
  * "no features changed" = Target_Node_Features_Changed_From_Factual_To_Counterfactual []
- Output a prose claim only if it states a fact that no field states (for example the class of a specific neighbor, or which specific edge was removed).
- Natural_Language_Explanation is one field: output it as one claim (claim_type mechanism).
- Field types: Target_Node_ID -> structural; *_Neighbors -> structural; *_Features and Target_Node_Features_Changed_From_Factual_To_Counterfactual -> feature; *_Class / *_class -> class_state.

Skip rule: output only claims that can be checked against the graph data (node texts, titles, features, edges, labels, predictions, importance scores). Do NOT output:
- opinions or evaluations of relevance, quality, strength or significance: "is crucial", "is essential", "is vital", "plays a key role", "contributes significantly", "lacks strong relevance", "its contribution is minimal", "is well-supported", "strongly supports the classification";
- interpretations of what something indicates or suggests: "indicates a focus on", "suggests that", "reflects", "highlights", "emphasizes the importance of", "reinforces the theme", "is consistent with";
- hedged or speculative statements ("may", "might", "could", "possibly", "likely", "appears to");
- generic statements about GNNs, graphs, datasets or the task, and sentences that only announce a list ("the classification is supported by the following factors");
- YES/NO votes.
- If a sentence mixes a checkable fact with an evaluation, output only the checkable part. Example: "Node-1 discusses backpropagation, which is critical for training neural networks" -> "Node-1 discusses backpropagation".
- An importance claim is kept only if it gives a specific score, weight, rank or ordering (e.g. "smooth has importance 0.67", "Node-1 is the most important neighbor"). A vague "is important / influential" without a score, rank or ordering is skipped.
- A mechanism claim is kept only if it names specific nodes, edges or features AND a specific effect on the prediction.

Typing target vs neighbor: decide by the SUBJECT of the claim.
- The TARGET is node {node}. It may also be called "ROOT", "the target node", "the target paper/product", "this paper/product", or by its own title.
- Any other node is a NEIGHBOR: "Node-1", "Node-2.3", "Node-3.1 to Node-3.4", "Node 192", "its neighbors", "the 2-hop neighbors", or a neighbor's title. In GraphNarrator-style text, ROOT is the target and EVERY "Node-X" / "Node-X.Y" is a neighbor.
- A claim about a neighbor's topic, title, content or label is type neighbor, never content. Use content only when the subject is the target.
- A claim about which nodes are connected is structural, whoever the subject is.

claim_type (choose exactly one)
- content: what the TARGET node is about (its topic, title, abstract, product description).
- neighbor: a property of a NEIGHBOR node or group of neighbors (topic, title, content or label).
- structural: graph connectivity: which nodes are connected, neighbor lists, number of neighbors, hops, edges added or removed, which node is the target.
- importance: an importance/saliency/attention score, weight, rank or ordering of a node, edge, word or feature.
- class_state: a class label, predicted class, true class, counterfactual class, or prediction confidence.
- mechanism: a causal claim about how the GNN used specific information to reach or change its prediction.
- feature: a specific feature/keyword/bag-of-words term being present, absent, or changed for a node.

entities (copy exactly as written in the explanation; use [] when none)
- node_ids: integer node IDs, or labels such as "Node-1" / "Node-1.2" exactly as written.
- titles: paper or product titles quoted or named.
- feature_words: specific words/keywords/features named.
- edges: pairs [a, b] of connected or disconnected nodes named by the claim.
- classes: class/category names.

Output format: a single JSON object and nothing else, no markdown fences:
{{"claims": [{{"claim": "<one atomic claim, self-contained, with the subject node named>", "claim_type": "<type>", "entities": {{"node_ids": [], "titles": [], "feature_words": [], "edges": [], "classes": []}}}}]}}

TARGET NODE: {node}  (dataset: {dataset})

EXPLANATION:
<<<
{text}
>>>"""

# v3 (2026-10-06, approved): v2 + a verbatim source_span per claim (checked in Python by
# span_check.py; failures are flagged unsupported_extraction). Rules otherwise identical to v2.
_V2_FORMAT = """Output format: a single JSON object and nothing else, no markdown fences:
{{"claims": [{{"claim": "<one atomic claim, self-contained, with the subject node named>", "claim_type": "<type>", "entities": {{"node_ids": [], "titles": [], "feature_words": [], "edges": [], "classes": []}}}}]}}"""
_V3_FORMAT = """source_span (required for every claim)
- Copy the exact contiguous words from the EXPLANATION that state this claim, character for character: same spelling, capitalization and punctuation. Do not paraphrase, summarize, fix typos, or join words that are not next to each other in the EXPLANATION.
- Keep it as short as possible while still containing the whole fact. For a dictionary field, copy that field as written (e.g. "Counterfactual_Target_Node_Neighbors: []").

Output format: a single JSON object and nothing else, no markdown fences:
{{"claims": [{{"claim": "<one atomic claim, self-contained, with the subject node named>", "claim_type": "<type>", "source_span": "<exact words copied from the EXPLANATION>", "entities": {{"node_ids": [], "titles": [], "feature_words": [], "edges": [], "classes": []}}}}]}}"""
assert USER_TEMPLATE_V2.count(_V2_FORMAT) == 1
USER_TEMPLATE_V3 = USER_TEMPLATE_V2.replace(_V2_FORMAT, _V3_FORMAT)

TEMPLATES = {"v1": USER_TEMPLATE, "v2": USER_TEMPLATE_V2, "v3": USER_TEMPLATE_V3}


def build_messages(entry, text, version="v1"):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": TEMPLATES[version].format(node=entry["node"], dataset=entry["dataset"], text=text)},
    ]


def first_json_object(s):
    """Return the first balanced {...} block in s (string-aware), or None."""
    s = re.sub(r"^```(?:json)?\s*|\s*```\s*$", "", s.strip())
    start = s.find("{")
    while start != -1:
        depth, in_str, esc = 0, False, False
        for i in range(start, len(s)):
            ch = s[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            elif ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return s[start : i + 1]
        start = s.find("{", start + 1)
    return None


def norm_claim(c):
    return re.sub(r"[^a-z0-9]+", " ", c.lower()).strip()


CLAIM_START = re.compile(r'\{\s*"claim"\s*:')


def balanced_end(s, start):
    """Index just past the balanced {...} starting at s[start], or None if it never closes."""
    depth, in_str, esc = 0, False, False
    for i in range(start, len(s)):
        ch = s[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i + 1
    return None


def recover_claim_objects(raw):
    """Fallback when the top-level JSON is malformed: parse each {"claim": ...} object on
    its own. A segment that fails to parse is retried with up to two closing braces appended
    (the observed Llama failure: the last object's closing brace is omitted). Every repair
    is logged."""
    starts = [m.start() for m in CLAIM_START.finditer(raw)]
    claims, repairs, failures = [], [], []
    for k, st in enumerate(starts):
        nxt = starts[k + 1] if k + 1 < len(starts) else len(raw)
        end = balanced_end(raw, st)
        seg = raw[st:end] if (end is not None and end <= nxt) else raw[st:nxt]
        # candidate bodies: as-is, then with any trailing run of ] } , whitespace removed
        # (an unclosed last object gets "balanced" by the outer array/object closers)
        bodies = [seg, re.sub(r"[\s,\]\}]*$", "", seg)]
        obj = None
        for body in bodies:
            for fix in ["", "}", "}}", "]}}", "\"]}}"]:
                try:
                    obj = json.loads(body + fix)
                except json.JSONDecodeError:
                    continue
                if body != seg or fix:
                    repairs.append({"claim_index": k, "stripped_tail": body != seg, "appended": fix})
                break
            if obj is not None:
                break
        if isinstance(obj, dict) and "claim" in obj:
            claims.append(obj)
        else:
            failures.append({"claim_index": k, "segment_head": seg[:120]})
    return claims, repairs, failures


def parse_output(raw):
    diag = {
        "json_found": False,
        "json_valid": False,
        "parse_mode": None,
        "error": None,
        "n_raw_claims": 0,
        "n_bad_type": 0,
        "n_merged_duplicates": 0,
        "repairs": [],
        "unrecoverable_segments": [],
    }
    raw_claims = None
    blob = first_json_object(raw)
    if blob is not None:
        diag["json_found"] = True
        try:
            obj = json.loads(blob)
            if isinstance(obj, dict) and isinstance(obj.get("claims"), list):
                raw_claims = obj["claims"]
                diag["json_valid"] = True
                diag["parse_mode"] = "strict"
            else:
                diag["error"] = "first balanced JSON object has no top-level 'claims' list (outer object malformed)"
        except json.JSONDecodeError as e:
            diag["error"] = f"JSONDecodeError: {e}"
    else:
        diag["error"] = "no balanced JSON object found"
    if raw_claims is None:
        raw_claims, diag["repairs"], diag["unrecoverable_segments"] = recover_claim_objects(raw)
        diag["parse_mode"] = "recovered_per_object" if raw_claims else "failed"
    diag["n_raw_claims"] = len(raw_claims)
    out, seen = [], set()
    for c in raw_claims:
        if not isinstance(c, dict) or not str(c.get("claim", "")).strip():
            continue
        ctype = str(c.get("claim_type", "")).strip().lower()
        if ctype not in CLAIM_TYPES:
            diag["n_bad_type"] += 1
        ents = c.get("entities") if isinstance(c.get("entities"), dict) else {}
        ents = {k: ents.get(k, []) if isinstance(ents.get(k, []), list) else [ents.get(k)] for k in ENTITY_KEYS}
        key = norm_claim(c["claim"])
        if key in seen:
            diag["n_merged_duplicates"] += 1
            continue
        seen.add(key)
        rec = {"claim": c["claim"].strip(), "claim_type": ctype, "claim_type_valid": ctype in CLAIM_TYPES, "entities": ents}
        if "source_span" in c:
            rec["source_span"] = str(c["source_span"]) if c["source_span"] is not None else ""
        out.append(rec)
    return out, diag


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="restrict to these answer-key ids")
    ap.add_argument("--prompt-version", default="v1", choices=sorted(TEMPLATES))
    ap.add_argument("--no-full", action="store_true", help="skip the secondary GraphNarrator full-message runs")
    args = ap.parse_args()

    entries = json.load(open(HERE / "answer_key_texts.json"))
    if args.only:
        entries = [e for e in entries if e["id"] in set(args.only)]
    jobs = []
    for e in entries:
        jobs.append((e, e["id"], e["text_scored"], e["scored_scope"]))
        if e["method"] == "GraphNarrator" and not args.no_full:
            jobs.append((e, e["id"] + "__full", e["text_full"], "full assistant message (secondary)"))

    tok = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=torch.float16, device_map="cuda:0", attn_implementation="sdpa")
    model.eval()
    print(f"loaded {MODEL_ID} fp16 on {torch.cuda.get_device_name(0)}", flush=True)

    tag = "" if args.prompt_version == "v1" else f"_{args.prompt_version}"
    out_dir = HERE / f"extractions{tag}"
    out_dir.mkdir(exist_ok=True)
    rows = []
    for e, run_id, text, scope in jobs:
        messages = build_messages(e, text, args.prompt_version)
        rendered = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        ids = tok(rendered, return_tensors="pt", add_special_tokens=False).to("cuda:0")
        t0 = time.time()
        with torch.no_grad():
            gen = model.generate(
                **ids,
                max_new_tokens=MAX_NEW_TOKENS,
                do_sample=False,  # greedy == temperature 0
                temperature=None,
                top_p=None,
                pad_token_id=tok.eos_token_id,
            )
        new = gen[0, ids["input_ids"].shape[1] :]
        raw = tok.decode(new, skip_special_tokens=True)
        claims, diag = parse_output(raw)
        diag["n_prompt_tokens"] = int(ids["input_ids"].shape[1])
        diag["n_output_tokens"] = int(new.shape[0])
        diag["hit_max_new_tokens"] = int(new.shape[0]) >= MAX_NEW_TOKENS
        diag["seconds"] = round(time.time() - t0, 1)
        type_counts = {t: sum(c["claim_type"] == t for c in claims) for t in CLAIM_TYPES}
        rec = {
            "run_id": run_id,
            "answer_key_id": e["id"],
            "method": e["method"],
            "dataset": e["dataset"],
            "node": e["node"],
            "source_file": e["source_file"],
            "source_locator": e["source_locator"],
            "text_scope": scope,
            "input_text": text,
            "model": MODEL_ID,
            "prompt_version": args.prompt_version,
            "generation": {"dtype": "float16", "do_sample": False, "temperature": 0, "max_new_tokens": MAX_NEW_TOKENS},
            "prompt_messages": messages,
            "prompt_rendered": rendered,
            "raw_output": raw,
            "claims": claims,
            "n_claims": len(claims),
            "claim_type_counts": type_counts,
            "parse_diagnostics": diag,
            "manual": e["manual"],
        }
        json.dump(rec, open(out_dir / f"{run_id}.json", "w"), indent=1)
        m = e["manual"]
        rows.append(
            {
                "run_id": run_id,
                "method": e["method"],
                "dataset": e["dataset"],
                "node": e["node"],
                "text_scope": scope,
                "n_extracted_claims": len(claims),
                "n_manual_adjudicated": m["n_claims_adjudicated"],
                "manual_supported": m["n_supported"],
                "manual_unsupported": m["n_unsupported"],
                "manual_count_source": m["count_source"],
                "chat_csv_precision": e["chat_csv_precision"],
                "parse_mode": diag["parse_mode"],
                "n_repairs": len(diag["repairs"]),
                "n_unrecoverable": len(diag["unrecoverable_segments"]),
                "n_merged_duplicates": diag["n_merged_duplicates"],
                "n_bad_type": diag["n_bad_type"],
                "hit_max_new_tokens": diag["hit_max_new_tokens"],
                **{f"n_{t}": type_counts[t] for t in CLAIM_TYPES},
            }
        )
        print(f"{run_id:40s} claims={len(claims):3d} manual={m['n_claims_adjudicated']} valid={diag['json_valid']} out_tok={diag['n_output_tokens']} {diag['seconds']}s", flush=True)

    suffix = "" if not args.only else "_subset"
    with open(HERE / f"claim_counts{tag}{suffix}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("done")


if __name__ == "__main__":
    main()
