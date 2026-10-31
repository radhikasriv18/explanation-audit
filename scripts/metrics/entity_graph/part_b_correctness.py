"""
Part B: grounding vs GraphSAGE prediction correctness.
Correct = {2334, 884, 6813, 8766}, Incorrect = {510, 1062, 1852, 8438} --
confirmed directly against "GNN PREDICTION: CORRECT/INCORRECT" labels in the
three survey .txt files before running anything below.

Reads entity_graph_v5_output/part_a_per_explanation.csv (already has
precision/recall/f1 per method/node). Writes new outputs only.
"""
import csv
import os
import statistics as stats

from scipy.stats import mannwhitneyu

OUT_DIR = "./grounding_recall_f1_2026-09-07/entity_graph_v5_output"
IN_PATH = os.path.join(OUT_DIR, "part_a_per_explanation.csv")

CORRECT = {"2334", "884", "6813", "8766"}
INCORRECT = {"510", "1062", "1852", "8438"}

rows = list(csv.DictReader(open(IN_PATH)))
for r in rows:
    for k in ["precision", "recall", "f1"]:
        r[k] = float(r[k]) if r[k] not in (None, "") else None
    r["correctness"] = "correct" if r["node"] in CORRECT else "incorrect"

METHODS = ["GraphNarrator", "GraphXAIN", "CF-GNNExplainer"]
MEASURES = ["precision", "recall", "f1"]

# ---- Part B.1: per method and pooled means ----
summary_rows = []


def group_stats(subset, measure):
    vals = [r[measure] for r in subset if r[measure] is not None]
    if not vals:
        return None, 0
    return stats.mean(vals), len(vals)


print(f"{'method':17s} {'grp':9s}", "".join(f"{m:>14s}" for m in MEASURES))
for method in METHODS + ["POOLED"]:
    for grp, label in [(CORRECT, "correct"), (INCORRECT, "incorrect")]:
        subset = [r for r in rows if (method == "POOLED" or r["method"] == method) and r["node"] in grp]
        line = f"{method:17s} {label:9s}"
        entry = {"method": method, "correctness": label}
        for m in MEASURES:
            mean_v, n = group_stats(subset, m)
            entry[f"{m}_mean"] = mean_v
            entry[f"{m}_n"] = n
            line += f"  {mean_v:.3f}(n={n})" if mean_v is not None else f"  n/a(n={n})"
        summary_rows.append(entry)
        print(line)

out_summary = os.path.join(OUT_DIR, "part_b_correctness_summary.csv")
with open(out_summary, "w", newline="") as f:
    fieldnames = ["method", "correctness"] + [f"{m}_{s}" for m in MEASURES for s in ("mean", "n")]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(summary_rows)
print(f"\n-> {out_summary}")

# ---- Part B.2: pooled Mann-Whitney U per measure ----
print("\n=== Pooled Mann-Whitney U (correct vs incorrect), per measure ===")
mw_rows = []
for m in MEASURES:
    correct_vals = [r[m] for r in rows if r["node"] in CORRECT and r[m] is not None]
    incorrect_vals = [r[m] for r in rows if r["node"] in INCORRECT and r[m] is not None]
    if len(correct_vals) < 1 or len(incorrect_vals) < 1:
        print(f"  {m}: insufficient data (n_correct={len(correct_vals)}, n_incorrect={len(incorrect_vals)})")
        continue
    U, p = mannwhitneyu(correct_vals, incorrect_vals, alternative="two-sided")
    print(f"  {m}: U={U:.1f}  p={p:.4f}  n_correct={len(correct_vals)}  n_incorrect={len(incorrect_vals)}")
    mw_rows.append({"measure": m, "U": U, "p": p, "n_correct": len(correct_vals), "n_incorrect": len(incorrect_vals)})

out_mw = os.path.join(OUT_DIR, "part_b_mannwhitney.csv")
with open(out_mw, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["measure", "U", "p", "n_correct", "n_incorrect"])
    w.writeheader()
    w.writerows(mw_rows)
print(f"-> {out_mw}")
