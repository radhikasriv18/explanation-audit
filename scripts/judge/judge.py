#!/usr/bin/env python3
"""Step 2: LLM grounding judge over the v4 claim sheets.

  python judge.py --backend llama  --nodes cora:884 --run-dir runs/llama_884
  python judge.py --backend llama  --run-dir runs/llama_all          (all 8 nodes)

Backends
  llama : meta-llama/Meta-Llama-3.1-8B-Instruct from ~/.cache/huggingface (offline), fp16, greedy decoding.

Per call: the node's reference packet (packets/packet_<ds>_<node>.txt), the node's previous claims (all earlier rows of
the sheet, for duplicate checks) and BATCH=10 claims (id + text). The judge sees no claim_kind, cited id or pre-filled
verdict. Output = JSON. A batch whose output fails to parse or validate (every id exactly once, verdict in the 4 labels)
is retried once with a correction turn; if it fails again it is logged as a failure and its rows get verdict PARSE_FAIL.

--hybrid: code decides support_verdict, neighbor_exists, class rows, any row citing an ID outside 2 hops, and
neighbor_content / feature / other rows that restate an earlier row (see code_decide, find_duplicate); the model judges only the remaining rows (neighbor_content, feature, other), in batches of 10 with the
same prompt; "previous claims" are still all earlier rows of the sheet. Code decisions go to code_decisions.csv.

Outputs in --run-dir: raw.jsonl (every call: prompt, raw output, attempt, status, seconds), judgments.csv,
failures.csv, run_info.json. Re-running with the same --run-dir skips batches already judged.
"""
import argparse, csv, json, os, re, sys, time

csv.field_size_limit(sys.maxsize)
HERE = os.path.dirname(os.path.abspath(__file__))
SHEETS = "./gspell_grounding_manual_2026-10-10/"
ALL_NODES = [("cora", 510), ("cora", 2334), ("cora", 1062), ("cora", 884),
             ("products", 6813), ("products", 1852), ("products", 8766), ("products", 8438)]
BATCH = 10
MAX_CLAIM_CHARS = 2000   # repetition-loop rows run to 4.6k chars; the cut is marked in the text
MAX_PREV_CHARS = 300     # previous claims are shown for duplicate checks only
VERDICTS = ("supported", "contradicted", "unverifiable", "duplicate")
LLAMA_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"
# local snapshot path: transformers 4.57's tokenizer loader calls the Hub API for repo ids even with HF_HUB_OFFLINE=1
LLAMA_PATH = os.path.expanduser("~/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-8B-Instruct/snapshots/"
                                "0e9e39f249a16976918f6564b8830bc894c89659")

RULES = """- Supported only if the reference confirms it; contradicted if the reference shows
  it is false; unverifiable if it cannot be checked (opinions, headings, procedure,
  YES/NO support judgments, generic advice, loops/boilerplate).
- Citing a node not within 2 hops, or that does not exist, is contradicted.
  Calling a 2-hop node a direct neighbor is contradicted.
- A keyword list is one claim: contradicted if most keywords do not fit the node.
- "X is a <class> paper / more related to <class>" is a class claim about X,
  checked against X's true label.
- A claim repeating an earlier claim about the same thing is duplicate.
- If a node's title and abstract disagree, a description matching either half plus
  the true label is supported.
- Products: supported if it names the right product type or a category the product
  clearly belongs to; contradicted if it names a different product type."""

SYSTEM = f"""You are a strict fact-checker. You check claims taken from an explanation that a language model wrote about
why a graph neural network (GNN) classified a target node. Each node is a paper (Cora citation graph) or a product
(Amazon co-purchase graph). You are given a REFERENCE with the ground truth: the target node and every node ID the
explanation mentions, with its title, text, true label, GNN prediction and hop distance from the target.
Judge each claim ONLY against the REFERENCE.

Verdicts: supported / contradicted / unverifiable / duplicate.
Rules:
{RULES}

Output JSON only, no other text, in exactly this form, one entry per claim, in the given order:
{{"verdicts": [{{"id": "<claim id>", "verdict": "supported|contradicted|unverifiable|duplicate", "reason": "<one line>"}}]}}"""


def user_msg(packet, prev, batch):
    L = ["REFERENCE", packet.rstrip(), "", "PREVIOUS CLAIMS of this explanation (for duplicate checks only; do not judge these):"]
    L += [f"[{r['claim_id']}] {r['claim_text'][:MAX_PREV_CHARS]}{' ...' if len(r['claim_text']) > MAX_PREV_CHARS else ''}"
          for r in prev] or ["(none)"]
    L += ["", f"CLAIMS TO JUDGE ({len(batch)}):"]
    for r in batch:
        t = r["claim_text"]
        L.append(f"[{r['claim_id']}] {t[:MAX_CLAIM_CHARS]}{' ...[truncated]' if len(t) > MAX_CLAIM_CHARS else ''}")
    L += ["", f"Return JSON only with {len(batch)} verdicts, ids: " + ", ".join(r["claim_id"] for r in batch)]
    return "\n".join(L)


def parse(raw, ids):
    s = raw.strip()
    s = re.sub(r"^```(?:json)?\s*|\s*```$", "", s)
    i, j = s.find("{"), s.rfind("}")
    if i < 0 or j < 0:
        return None, "no JSON object"
    try:
        obj = json.loads(s[i:j + 1])
    except json.JSONDecodeError as e:
        return None, f"JSON error: {e}"
    v = obj.get("verdicts") if isinstance(obj, dict) else None
    if not isinstance(v, list):
        return None, "no 'verdicts' list"
    out = {}
    for e in v:
        if not isinstance(e, dict) or str(e.get("id")) not in ids:
            return None, f"unknown id {e.get('id') if isinstance(e, dict) else e!r}"
        vd = str(e.get("verdict", "")).strip().lower()
        if vd not in VERDICTS:
            return None, f"bad verdict {vd!r} for {e.get('id')}"
        if str(e["id"]) in out:
            return None, f"duplicate id {e['id']}"
        out[str(e["id"])] = (vd, str(e.get("reason", "")).replace("\n", " ").strip())
    missing = [x for x in ids if x not in out]
    if missing:
        return None, f"missing ids {missing}"
    return out, "ok"


class Llama:
    def __init__(self, max_new):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        self.torch = torch
        self.tok = AutoTokenizer.from_pretrained(LLAMA_PATH)
        self.model = AutoModelForCausalLM.from_pretrained(LLAMA_PATH, torch_dtype=torch.float16, device_map="cuda").eval()
        self.max_new = max_new
        self.name = LLAMA_ID + " fp16 greedy"

    def __call__(self, messages):
        ids = self.tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to("cuda")
        with self.torch.no_grad():
            out = self.model.generate(ids, max_new_tokens=self.max_new, do_sample=False, temperature=None, top_p=None,
                                      pad_token_id=self.tok.eos_token_id)
        return self.tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True), int(ids.shape[1])




CITE = re.compile(r"(?:Article|Paper|Product|Node)\s*#?\s*(\d+)|\bID\s*[:#]?\s*(\d+)|<<\s*(\d+)\s*>>", re.I)  # = build_labeling_sheets.CITE
DIRECT = re.compile(r"\bdirect(ly)?\b|\b1-hop\b|\bone-hop\b|\bfirst[- ]order\b|\bimmediate\b", re.I)  # = build_v2.DIRECT
lnorm = lambda s: re.sub(r"[\s_]+", " ", s).strip().lower()


def class_labels(text, labels):
    """Labels named in the text, longest first, skipping labels contained in one already found (= build_v2)."""
    t, found = lnorm(text), []
    for lab in sorted(labels, key=len, reverse=True):
        if lnorm(lab) in t and not any(lnorm(lab) in lnorm(f) for f in found):
            found.append(lab)
    return found


DUP_KINDS = ("neighbor_content", "feature", "other")
# duplicate-detector settings; DUP_PRESETS["spec"] is the default (the 2026-10-13 request), "strict" the tighter variant
DUP_PRESETS = {"spec":   {"jaccard": 0.8, "same_id_kinds": DUP_KINDS, "same_id_skip_target": False},
               "strict": {"jaccard": 0.8, "same_id_kinds": ("neighbor_content", "feature"), "same_id_skip_target": True}}
DUP = dict(DUP_PRESETS["spec"])
NEG_SUPPORT = re.compile(r"\b(?:not|n't|never|no longer)\b[^.;]{0,40}\bsupport|\bunsupported\b|\bnot\b[^.;]{0,25}\b(?:correct|accurate|justified)\b", re.I)
# R3 topic test (= gspell_grounding_manual_2026-10-10/build_v3.py)
TOPIC = re.compile(r"\b(?:focus(?:es|ed)? on|connection to|related to|relates to|relevance to|relevant to|"
                   r"associated with|discuss(?:es)?|about)\b\s*(.*)", re.I)
STOP = set("""a an and are as at be but by category categories classification classify classified connection
different does doesn't focus for from has have in indicate indicates into is it its keywords keyword more not of
on or product products article articles paper target that the their these this those to which with suggest
suggests strong which supports support supporting supported class align aligns aligned is also than other""".split())
stems = lambda s: {w[:5] for w in re.findall(r"[a-z][a-z\-']+", s.lower()) if w not in STOP and len(w) > 2}
toks = lambda s: set(re.findall(r"[a-z0-9]+", s.lower()))


def find_duplicate(i, rows, target, far):
    """Reason string if rows[i] (kind neighbor_content / feature / other) restates an earlier row of the node, else None.
    (a) token Jaccard >= DUP["jaccard"] with an earlier row of these kinds;
    (b) same cited ID + same claim_kind as an earlier row (kinds DUP["same_id_kinds"]; target's own ID skipped if
        DUP["same_id_skip_target"]);
    (c) R3, only for rows citing an ID outside 2 hops (far=True), as in build_v3: an 'other' row whose topic restates the
        closest preceding Summary row of the same block (same batch_idx and cited_node_id; >= 50% of topic stems, >= 1)."""
    r = rows[i]
    if r["claim_kind"] not in DUP_KINDS:
        return None
    tr = toks(r["claim_text"])
    for e in rows[:i]:
        if e["claim_kind"] in DUP_KINDS and tr:
            te = toks(e["claim_text"])
            if len(tr & te) / len(tr | te) >= DUP["jaccard"]:
                return f"code: duplicate of {e['claim_id']} (token overlap {len(tr & te) / len(tr | te):.2f})"
    if r["cited_node_id"] and r["claim_kind"] in DUP["same_id_kinds"] and not (DUP["same_id_skip_target"] and int(r["cited_node_id"]) == target):
        e = next((e for e in rows[:i] if e["cited_node_id"] == r["cited_node_id"] and e["claim_kind"] == r["claim_kind"]), None)
        if e:
            return f"code: duplicate of {e['claim_id']} (same cited id {r['cited_node_id']} and claim_kind)"
    if far and r["claim_kind"] == "other" and r["cited_node_id"]:
        summ = next((rows[j] for j in range(i - 1, -1, -1) if rows[j]["batch_idx"] == r["batch_idx"]
                     and rows[j]["cited_node_id"] == r["cited_node_id"] and rows[j]["claim_kind"] == "neighbor_content"
                     and re.match(r"[\W_]*Summary\s*:", rows[j]["claim_text"], re.I)), None)
        if summ:
            m = TOPIC.search(r["claim_text"])
            topic = re.split(r",\s*which\b|\bwhich\b", m.group(1) if m else r["claim_text"])[0]
            tw, hit = stems(topic), stems(topic) & stems(summ["claim_text"])
            if hit and len(hit) / len(tw) >= 0.5:
                return f"code: restates summary row {summ['claim_id']} (R3, topic overlap {len(hit) / len(tw):.2f})"
    return None


def code_decide(rows, pk):
    """Hybrid mode: {claim_id: (verdict, reason)} for the rows code decides; the rest go to the model.
    Precedence (v2 rules, 2026-10-13; v1 = judge_hybrid_v1.py):
      1. support_verdict -> unverifiable
      2. neighbor_content / feature / other restating an earlier row (find_duplicate) -> duplicate
         (before the range check: duplicate wins over contradicted)
      3. a cited ID (cited_node_id or an ID in the text) not within 2 hops or nonexistent -> contradicted
      4. neighbor_exists -> target itself contradicted, 2-hop called direct contradicted, else supported
      5. class -> first class row of the node: names the canonical prediction but says it is not supported -> unverifiable;
         names the prediction -> supported; names another label -> contradicted; no label -> unverifiable.
         Later class rows -> duplicate."""
    t = pk["target"]["id"]
    hop = {c["id"]: c["hop"] for c in pk["cited"]}
    pred, labels = pk["target"]["canonical_pred"], pk["label_set"]
    dec, first_class = {}, None
    for i, r in enumerate(rows):
        kind = r["claim_kind"]
        cids = ([int(r["cited_node_id"])] if r["cited_node_id"] else []) + \
               [int(next(g for g in m.groups() if g)) for m in CITE.finditer(r["claim_text"])]
        far = [c for c in dict.fromkeys(cids) if c != t and hop.get(c) not in (1, 2)]
        dup = find_duplicate(i, rows, t, bool(far))
        if kind == "support_verdict":
            dec[r["claim_id"]] = ("unverifiable", "code: YES/NO support judgment")
        elif dup:
            dec[r["claim_id"]] = ("duplicate", dup)
        elif far:
            c = far[0]
            dec[r["claim_id"]] = ("contradicted", f"code: cited id {c} " + ("does not exist" if hop.get(c) == "does not exist"
                                                                          else "is not within 2 hops of the target"))
        elif kind == "neighbor_exists":
            c = int(r["cited_node_id"])
            if c == t:
                dec[r["claim_id"]] = ("contradicted", "code: target cited as its own neighbour")
            elif hop[c] == 2 and DIRECT.search(r["claim_text"]):
                dec[r["claim_id"]] = ("contradicted", f"code: {c} is 2-hop but the text calls it direct")
            else:
                dec[r["claim_id"]] = ("supported", f"code: {c} is a {hop[c]}-hop neighbour")
        elif kind == "class":
            if first_class is not None:
                dec[r["claim_id"]] = ("duplicate", f"code: later class statement (first is {first_class})")
                continue
            first_class = r["claim_id"]
            found = class_labels(r["claim_text"], labels)
            if pred in found and NEG_SUPPORT.search(r["claim_text"]):
                dec[r["claim_id"]] = ("unverifiable", f"code: first class statement names '{pred}' but says it is not supported")
            elif pred in found:
                dec[r["claim_id"]] = ("supported", f"code: first class statement names '{pred}' = canonical prediction"
                                      + (f" (also names {[f for f in found if f != pred]})" if len(found) > 1 else ""))
            elif found:
                dec[r["claim_id"]] = ("contradicted", f"code: first class statement names {found}; canonical prediction is '{pred}'")
            else:
                dec[r["claim_id"]] = ("unverifiable", "code: first class statement names no class label")
    return dec


def plan(ds, node, hybrid):
    """rows of the sheet, code decisions, and model batches [(batch_idx, batch_rows, previous_rows)]."""
    rows = list(csv.DictReader(open(SHEETS + f"claims_{ds}_{node}_v4.csv")))
    if not hybrid:
        return rows, {}, [(b // BATCH, rows[b:b + BATCH], rows[:b]) for b in range(0, len(rows), BATCH)]
    dec = code_decide(rows, json.load(open(os.path.join(HERE, f"packets/packet_{ds}_{node}.json"))))
    pos = {r["claim_id"]: i for i, r in enumerate(rows)}
    rest = [r for r in rows if r["claim_id"] not in dec]
    return rows, dec, [(b // BATCH, rest[b:b + BATCH], rows[:pos[rest[b]["claim_id"]]]) for b in range(0, len(rest), BATCH)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["llama"], required=True)
    ap.add_argument("--nodes", default="all", help="'all' or comma list like cora:884,products:6813")
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--max-new-tokens", type=int, default=1536)
    ap.add_argument("--hybrid", action="store_true", help="code decides support/exists/class/out-of-range/duplicate rows; model the rest")
    ap.add_argument("--dup-preset", choices=sorted(DUP_PRESETS), default="spec", help="duplicate-detector settings (hybrid only)")
    a = ap.parse_args()
    DUP.update(DUP_PRESETS[a.dup_preset])
    nodes = ALL_NODES if a.nodes == "all" else [(x.split(":")[0], int(x.split(":")[1])) for x in a.nodes.split(",")]
    rd = a.run_dir if os.path.isabs(a.run_dir) else os.path.join(HERE, a.run_dir)
    os.makedirs(rd, exist_ok=True)
    raw_path = os.path.join(rd, "raw.jsonl")
    done = {}
    if os.path.exists(raw_path):
        for line in open(raw_path):
            e = json.loads(line)
            if e["status"] in ("ok", "failed"):
                done[(e["node"], e["batch"])] = e
    plans = {(ds, node): plan(ds, node, a.hybrid) for ds, node in nodes}
    if a.hybrid:
        with open(os.path.join(rd, "code_decisions.csv"), "w", newline="") as f:
            w = csv.writer(f); w.writerow(["dataset", "node", "claim_id", "claim_kind", "cited_node_id", "verdict", "reason", "claim_text"])
            for (ds, node), (rows, dec, _) in plans.items():
                for r in rows:
                    if r["claim_id"] in dec:
                        w.writerow([ds, node, r["claim_id"], r["claim_kind"], r["cited_node_id"], *dec[r["claim_id"]], r["claim_text"]])
    llm = Llama(a.max_new_tokens)
    t0 = time.time()
    for ds, node in nodes:
        packet = open(os.path.join(HERE, f"packets/packet_{ds}_{node}.txt")).read()
        for bi, batch, prev in plans[(ds, node)][2]:
            if (node, bi) in done:
                continue
            ids = [r["claim_id"] for r in batch]
            msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user_msg(packet, prev, batch)}]
            for attempt in (1, 2):
                ts = time.time()
                raw, n_in = llm(msgs)
                res, why = parse(raw, ids)
                status = "ok" if res else ("retry" if attempt == 1 else "failed")
                e = {"dataset": ds, "node": node, "batch": bi, "attempt": attempt, "status": status, "why": why,
                     "input_tokens": n_in, "seconds": round(time.time() - ts, 2), "ids": ids,
                     "messages": msgs, "raw_output": raw, "verdicts": res}
                with open(raw_path, "a") as f:
                    f.write(json.dumps(e) + "\n")
                print(f"{ds} {node} batch {bi} attempt {attempt}: {status} ({why}) in={n_in} {e['seconds']}s", flush=True)
                if res:
                    break
                msgs = msgs + [{"role": "assistant", "content": raw},
                               {"role": "user", "content": f"Your output was not valid ({why}). Return JSON only, in the exact "
                                                           f"format given, with one verdict for each of these ids: {', '.join(ids)}"}]
    run_seconds = time.time() - t0

    # collect final verdicts (last ok/failed entry per batch)
    final = {}
    for line in open(raw_path):
        e = json.loads(line)
        if e["status"] in ("ok", "failed"):
            final[(e["node"], e["batch"])] = e
    out, fails = [], []
    for ds, node in nodes:
        rows, dec, batches = plans[(ds, node)]
        got = {}
        for bi, batch, _ in batches:
            e = final.get((node, bi))
            if e and e["status"] == "failed":
                fails.append({"dataset": ds, "node": node, "batch": bi, "why": e["why"], "ids": " ".join(e["ids"])})
            for r in batch:
                got[r["claim_id"]] = (bi, *(e["verdicts"][r["claim_id"]] if e and e["status"] == "ok"
                                            else ("PARSE_FAIL", e["why"] if e else "not run")))
        for r in rows:
            bi, v, why = ("", *dec[r["claim_id"]]) if r["claim_id"] in dec else got[r["claim_id"]]
            row = {"dataset": ds, "node": node, "batch": bi, "claim_id": r["claim_id"], "claim_kind": r["claim_kind"],
                   "cited_node_id": r["cited_node_id"], "judge_verdict": v, "judge_reason": why, "claim_text": r["claim_text"]}
            if a.hybrid:
                row["decided_by"] = "code" if r["claim_id"] in dec else "model"
            out.append(row)
    with open(os.path.join(rd, "judgments.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    with open(os.path.join(rd, "failures.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["dataset", "node", "batch", "why", "ids"]); w.writeheader(); w.writerows(fails)
    calls = [json.loads(l) for l in open(raw_path)]
    info = {"backend": a.backend, "model": llm.name, "hybrid": a.hybrid, "dup_preset": a.dup_preset if a.hybrid else None, "nodes": [f"{d}:{n}" for d, n in nodes], "batch_size": BATCH,
            "max_new_tokens": a.max_new_tokens, "claims": len(out), "code_decided": sum(len(p[1]) for p in plans.values()),
            "model_rows": len(out) - sum(len(p[1]) for p in plans.values()), "batches": len(final),
            "calls": len(calls), "retries": sum(c["attempt"] == 2 for c in calls), "failed_batches": len(fails),
            "seconds_this_invocation": round(run_seconds, 1), "seconds_sum_of_calls": round(sum(c["seconds"] for c in calls), 1),
            "slurm_job_id": os.environ.get("SLURM_JOB_ID")}
    json.dump(info, open(os.path.join(rd, "run_info.json"), "w"), indent=1)
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
