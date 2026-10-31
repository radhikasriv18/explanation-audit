#!/usr/bin/env python3
"""Report for runs/gemini_full (no model calls). New file.

Joins Gemini judgments with the hand labels:
  GSPELL   : runs/gemini_full/gspell/judgments.csv  x  "./gspell_grounding_verdicts (1).csv" (column verdict)
  3 methods: runs/gemini_full/3methods/judgments.csv x answer_key_3methods_labeled.csv (not_a_claim rows were never judged)
Per method and overall: n, agreement, Cohen's kappa (4 verdicts; compare.kappa), the same on rows hand-labelled
supported/contradicted, 4x4 confusion. PARSE_FAIL rows are counted and left out.

Disagreement type (first rule that applies; a heuristic, not a hand classification):
  duplicate_vs_content : exactly one side says duplicate
  loop_R1_vs_R6        : claim looks like a repetition loop (>1500 chars, or >400 chars with one word >= 6 times)
                         and one side says unverifiable
  title_abstract_R5    : hand note or judge reason invokes R5 / a title-abstract mismatch
  unverifiable_vs_content : one side says unverifiable (R4/R6 vs a content verdict)
  supported_vs_contradicted : both content verdicts, opposite
Writes runs/gemini_full/: report.txt, report.json, disagreements.csv, run_info.json.
"""
import csv, json, os, re, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from compare import kappa  # noqa: E402

csv.field_size_limit(sys.maxsize)
RD = os.path.join(HERE, "runs/gemini_full")
V = ["supported", "contradicted", "unverifiable", "duplicate"]
PRICE_IN, PRICE_OUT = 0.75, 3.75   # USD / 1M tokens; third-party-reported introductory rate, NOT confirmed on Google's page
METHODS = ["GraphNarrator", "GraphXAIN", "CF-GNNExplainer", "GSPELL"]


def looks_loop(t):
    if len(t) > 1500:
        return True
    words = re.findall(r"[a-z]{3,}", t.lower())
    return len(t) > 400 and bool(words) and Counter(words).most_common(1)[0][1] >= 6


def dtype(h, j, text, hnote, jreason):
    if (h == "duplicate") != (j == "duplicate"):
        return "duplicate_vs_content"
    if looks_loop(text) and "unverifiable" in (h, j):
        return "loop_R1_vs_R6"
    if re.search(r"\bR5\b|title.{0,40}abstract|abstract.{0,40}title|mismatch", f"{hnote} {jreason}", re.I):
        return "title_abstract_R5"
    if "unverifiable" in (h, j):
        return "unverifiable_vs_content"
    return "supported_vs_contradicted"


def load():
    rows = []
    hand = {r["claim_id"]: r for r in csv.DictReader(open("./gspell_grounding_verdicts (1).csv", encoding="utf-8-sig"))}
    for r in csv.DictReader(open(os.path.join(RD, "gspell/judgments.csv"), encoding="utf-8")):
        h = hand[r["claim_id"]]
        rows.append({"method": "GSPELL", "dataset": r["dataset"], "node": r["node"], "claim_id": r["claim_id"],
                     "claim_kind": r["claim_kind"], "hand": h["verdict"].strip(), "hand_note": h.get("reason", ""),
                     "judge": r["judge_verdict"], "judge_reason": r["judge_reason"], "claim_text": r["claim_text"]})
    key = {r["claim_id"]: r for r in csv.DictReader(open(
        "./grounding_answer_key_3methods_2026-10-13/answer_key_3methods_labeled.csv", encoding="utf-8"))}
    for r in csv.DictReader(open(os.path.join(RD, "3methods/judgments.csv"), encoding="utf-8")):
        h = key[r["claim_id"]]
        rows.append({"method": r["method"], "dataset": r["dataset"], "node": r["node"], "claim_id": r["claim_id"],
                     "claim_kind": "", "hand": h["verdict"], "hand_note": h["note"], "judge": r["judge_verdict"],
                     "judge_reason": r["judge_reason"], "claim_text": r["claim_text"]})
    return rows


def stats(sub):
    ok = [r for r in sub if r["judge"] != "PARSE_FAIL"]
    pairs = [(r["hand"], r["judge"]) for r in ok]
    sc = [(h, j) for h, j in pairs if h in ("supported", "contradicted")]
    c = Counter(pairs)
    return {"n": len(sub), "parse_fail": len(sub) - len(ok), "compared": len(pairs),
            "agreement": sum(h == j for h, j in pairs) / len(pairs) if pairs else float("nan"), "kappa": kappa(pairs, V),
            "sc_n": len(sc), "sc_agreement": sum(h == j for h, j in sc) / len(sc) if sc else float("nan"), "sc_kappa": kappa(sc, V),
            "confusion": {h: {j: c[(h, j)] for j in V} for h in V},
            "disagreement_types": dict(Counter(r["dtype"] for r in ok if r["hand"] != r["judge"]))}


def main():
    rows = load()
    for r in rows:
        r["dtype"] = dtype(r["hand"], r["judge"], r["claim_text"], r["hand_note"], r["judge_reason"]) if (
            r["judge"] != "PARSE_FAIL" and r["hand"] != r["judge"]) else ""
    res = {m: stats([r for r in rows if r["method"] == m]) for m in METHODS}
    res["ALL"] = stats(rows)
    res["ALL_except_GSPELL"] = stats([r for r in rows if r["method"] != "GSPELL"])

    calls = [json.loads(l) for p in ("gspell/raw.jsonl", "3methods/raw.jsonl") for l in open(os.path.join(RD, p))]
    tok = {k: sum(c["usage"].get(k, 0) for c in calls) for k in ("prompt", "output", "thoughts", "total")}
    cost = (tok["prompt"] * PRICE_IN + (tok["output"] + tok["thoughts"]) * PRICE_OUT) / 1e6
    info = {"date": datetime.now(timezone.utc).isoformat(timespec="seconds"), "model": "gemini-3.8-flash",
            "model_versions_seen": sorted({c.get("model_version") for c in calls if c.get("model_version")}),
            "settings": "temperature 0, JSON output, batches of 10, one retry, no hybrid (judge_gemini.py prompt unchanged)",
            "calls": len(calls), "retries": sum(c["attempt"] == 2 for c in calls),
            "failed_batches": sum(c["status"] == "failed" for c in calls), "tokens": tok,
            "price_usd_per_1M": {"input": PRICE_IN, "output_incl_thinking": PRICE_OUT,
                                 "note": "third-party-reported introductory rate; not confirmed on Google's pricing page"},
            "cost_usd_estimate": round(cost, 3),
            "timestamps": [min(c["timestamp"] for c in calls), max(c["timestamp"] for c in calls)]}
    json.dump(info, open(os.path.join(RD, "run_info.json"), "w"), indent=1)
    json.dump(res, open(os.path.join(RD, "report.json"), "w"), indent=1)
    with open(os.path.join(RD, "disagreements.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["method", "dataset", "node", "claim_id", "claim_kind", "dtype", "hand", "judge",
                                          "judge_reason", "hand_note", "claim_text"], extrasaction="ignore")
        w.writeheader(); w.writerows(r for r in rows if r["dtype"])

    L = [f"Gemini judge vs hand labels  ({info['model']}, versions {info['model_versions_seen']}, {info['date']})", ""]
    L.append(f"{'method':18s} {'n':>5s} {'pf':>3s} {'agree':>6s} {'kappa':>6s} | {'n_SC':>5s} {'agree':>6s} {'kappa':>6s}")
    for m in METHODS + ["ALL_except_GSPELL", "ALL"]:
        s = res[m]
        L.append(f"{m:18s} {s['n']:5d} {s['parse_fail']:3d} {s['agreement']:6.1%} {s['kappa']:6.3f} | {s['sc_n']:5d} {s['sc_agreement']:6.1%} {s['sc_kappa']:6.3f}")
    for m in METHODS + ["ALL"]:
        s = res[m]; L += ["", f"== {m}: confusion (rows = hand, cols = judge)", "hand \\ judge".rjust(14) + "".join(f"{v[:12]:>13s}" for v in V)]
        L += [f"{h:>14s}" + "".join(f"{s['confusion'][h][j]:13d}" for j in V) for h in V]
        L.append("   disagreement types: " + ", ".join(f"{k}={v}" for k, v in sorted(s["disagreement_types"].items(), key=lambda x: -x[1])))
    L += ["", f"tokens: {tok} | calls {info['calls']} | retries {info['retries']} | failed batches {info['failed_batches']}",
          f"estimated cost: ${cost:.3f} at ${PRICE_IN}/1M in, ${PRICE_OUT}/1M out incl. thinking (unconfirmed third-party rate)"]
    open(os.path.join(RD, "report.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
