# CF-GNNExplainer implementation + production run — 2026-08-10

## What this is

The `llm-graph-cf` counterfactual narration framework's README states its
data comes from two explainers, CF-GNNExplainer and CF-GNNFeatures, but
neither is included in the repo. The existing local `src/cf_gnnfeatures.py`
only perturbs node features, never edges, which is why every prior
`Factual_Target_Node_Neighbors` / `Counterfactual_Target_Node_Neighbors`
pair was identical and `removed_edges`-type fields were always empty. This
run implements the missing CF-GNNExplainer (edge-removal counterfactuals)
and re-runs the framework's unchanged LLM narration prompt against it.

## Implementation

`llm-graph-cf/src/cf_gnnexplainer.py` — see its module docstring for full
detail. Summary:
- Followed Lucic et al., "CF-GNNExplainer: Counterfactual Explanations for
  Graph Neural Networks" (AISTATS 2022, arXiv:2102.03322), using the public
  reference implementation (https://github.com/a-lucic/cf-gnnexplainer) as
  the model: a single learned per-edge deletion mask over a node's
  computation-graph subgraph, sigmoid-relaxed for gradient descent, with a
  parallel hard-thresholded forward pass used to check whether the
  prediction has actually flipped.
- **Documented deviation #1 (architecture):** the reference code targets a
  from-scratch 3-layer GCN. Our canonical checkpoints are a frozen 2-layer
  GraphSAGE (mean aggregator, separate self/neighbor weights). Re-derived
  the perturbed propagation rule for SAGEConv's `lin_l(mean_j x_j) +
  lin_r(x_i)` instead of GCN's symmetric-normalized adjacency, using the
  checkpoint's own frozen weights — only the edge mask is ever trained.
- **Documented deviation #2 (minimality mechanism):** the reference loss
  adds an L1/L2 "distance loss" directly into the optimized objective so
  gradient descent both searches for a flip and shrinks the edit at the
  same time. Empirically here that badly hurt coverage: with Adam, the
  optimizer's per-parameter step-size normalization makes step size ~lr
  regardless of how small the regularization weight is, so regularization
  always won once a flip was found (coverage on a 40-node dev sample:
  alpha=beta=0.5 -> 1/40, 0.05 -> 5/40, 0.01 -> 10/40, 0.0 -> 21/40). Plain
  SGD (as the reference code actually uses) made even less progress here
  (0-1/40) because the raw pred_loss gradient on this frozen model is tiny
  relative to a 20-40 edge subgraph's aggregate regularization pull.
  Resolution: run pure existence search (Adam, no distance loss) to find
  *a* flip, then enforce minimality with an exact, deterministic
  `greedy_prune` pass (try restoring each removed edge one at a time; keep
  it restored whenever the prediction still flips without it; repeat to a
  fixed point). This reaches the same "minimal edge set" goal without the
  optimizer instability.
- Same subgraph extraction (`k_hop_subgraph`, 2 hops, matching the model's
  2 layers) and output JSON schema as `cf_gnnfeatures.py`, so `--explainer
  cf-gnnexplainer-canonical` is a drop-in for `main.py` / `llms_m.py`. Its
  name deliberately does not contain the substring `cf-gnnfeatures`, so
  `llms_m.py`'s existing `"node features" if "cf-gnnfeatures" in explainer
  else "adjacency matrix"` check picks the correct system-prompt wording
  automatically — no framework code was touched.
- Bugs found and fixed during development (see git history / this log):
  `torch.triu_indices` device mismatch on GPU; an assertion that assumed
  the class reached at first discovery survives `greedy_prune` pruning
  (it doesn't always — a smaller edit can land on a different alternate
  class; fixed by recomputing the final class from the pruned edge set).

## Production run

Seed 42 throughout (`fix_seed`, matching `cf_gnnfeatures.py`'s convention).
Slurm jobs on `gpu-exp` partition (V100-32G), account <ACCOUNT>.

| Stage | Cora (542 eval nodes) | Products (200 eval nodes) |
|---|---|---|
| CF-GNNExplainer search | job 51136895, 6m22s | job 51136896, 2m58s |
| LLM narration (Llama-3.1-8B, `main.py --prompt_type standard`, unchanged prompt) | job 51137055, 2h02m | job 51137056, 31m |

**Coverage (nodes where CF-GNNExplainer found an edge set that flips the
prediction):**
- Cora: **198 / 542 (36.5%)**
- Products: **60 / 200 (30.0%)**

For comparison, CF-GNNFeatures (feature-removal) found counterfactuals for
409/542 (75.5%) Cora and 177/200 (88.5%) Products nodes
(`production_run_2026-07-27/standardization_notes.md` §7). CF-GNNExplainer's
much lower coverage is expected, not a bug: removing edges only changes a
node's prediction *indirectly*, through 1-2 hops of mean-aggregated
neighbor influence, whereas CF-GNNFeatures can zero out the target's own
bag-of-words features directly — a far more direct lever for a GraphSAGE
classifier that leans heavily on each node's own text content.

**LLM-generation-stage coverage** (of the above, how many got a narration —
`llms_m.py`'s existing, unmodified `max_model_len=32000` guard skips prompts
that don't fit, same mechanism that skipped 2/409 in the original
CF-GNNFeatures Cora production run):
- Cora: 184 / 198 (14 skipped, prompt too long — up to ~51k tokens for
  large 2-hop subgraphs)
- Products: 60 / 60 (none skipped)

**Survey nodes** (Cora 510, 2334, 1062, 884; Products 6813, 1852, 8766,
8438) — all fall inside the eval splits CF-GNNExplainer ran over, so no
separate run was needed:
- Found + narrated: Cora 510, 2334, 1062; Products 1852, 8438 (5/8)
- No CF-GNNExplainer counterfactual found within budget: Cora 884; Products
  6813, 8766 (3/8)
- Persisted separately (explainer output + prompt + raw LLM output) at
  `survey_nodes/{cora,products}_survey_nodes.json`, including explicit
  `status` fields for the not-found nodes.

## Output locations (new, nothing pre-existing was touched)

- `llm-graph-cf/data/cora/cf-gnnexplainer-canonical/` — 5 JSON files
  (factual/counterfactual graph descriptions, factual/counterfactual target
  dicts, `random_seed_42_cf_removed_edges.json`)
- `llm-graph-cf/data/products/cf-gnnexplainer-canonical/` — same 5 files
- `llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_{cora,products}_standard_Response.json`
  — raw (prompt, generated_text) pairs, keyed the same as the explainer
  output
- `survey_nodes/{cora,products}_survey_nodes.json` — the 8 survey nodes'
  full artifacts (or not-found status)
- `edge_accuracy_audit.json` — full per-node audit backing the section below
- Existing `data/{cora,products}/cf-gnnfeatures-canonical*/` and the
  human-survey stimuli files were never opened for writing by this run
  (verified: no `cf-gnnfeatures` path appears anywhere in
  `cf_gnnexplainer.py`'s write logic).

## Does the generated text accurately describe the edges CF-GNNExplainer removed?

Audit script: `edge_accuracy_audit.py` (methodology also embedded in
`edge_accuracy_audit.json`). For every node with a found counterfactual AND
a narration (244 = 184 Cora + 60 Products), checked whether the raw LLM
output names at least one of the actually-removed edge's *other* endpoint
(excluding the target ID, which appears everywhere trivially) within 200
characters of removal-indicating language ("removed", "no longer",
"disconnected", "severed", "eliminated", "dropped/cut the edge/connection").
Separately flagged any use of edge-*addition* language ("new edge",
"introduced a connection", "added a connection") — a factual inversion by
construction, since this method only ever deletes edges from the existing
adjacency.

**Counts:**

| | Cora (n=184) | Products (n=60) | Total (n=244) |
|---|---|---|---|
| Accurately names >=1 removed edge | 26 | 8 | **34** |
| ...and no addition-contradiction elsewhere | — | — | 33 |
| Silent/vague on which edge(s) changed | 158 | 52 | **210** |
| Contains an edge-addition claim (wrong) | 15 | 2 | **17** |

So **34/244 (14%)** of narrations correctly name a specific edge that was
actually removed; the large majority (210/244, 86%) never name the correct
endpoint even though the model is told explicitly (via the same "adjacency
matrix" system-prompt wording used for this explainer type) that it's
looking at an edge-removal counterfactual.

Splitting by whether the removed edge(s) touch the target node directly
vs. only affect its 2-hop neighborhood (i.e. a neighbor-of-a-neighbor's
edge, which still changes the target's prediction through the 2nd
GraphSAGE layer but never shows up in the target's own
`Factual/Counterfactual_Target_Node_Neighbors` fields):
- Direct (touches target): 211 nodes, 28 accurately described (13%)
- Indirect only (2-hop, never touches target): 33 nodes, 6 accurately
  described (18%)

Accuracy is low even in the "easy" direct case, where the target's own
neighbor list literally differs between the factual/counterfactual text
blocks the model is given.

**A concrete, representative failure mode** (Cora key `2`, target node 11):
the actually-removed edges were `(163, 624)` and `(163, 659)` — two edges
between a non-target node and its neighbors, 2 hops from the target.
Node 11's own direct neighbors (624, 659) were untouched. The LLM's output
instead invented `Edge_Differences = [(11, 624), (11, 659)]` — i.e. it
hallucinated that the target's *own* edges were the ones removed, producing
a structurally plausible but factually wrong story. This matches the
project's earlier finding that CF-GNNFeatures' LLM narrations fabricated
edge-removal claims (since that explainer never touches edges at all); here,
even when a real edge removal exists, the model frequently attributes it to
the wrong edge, usually collapsing a subtler 2-hop change into a simpler
"target's own connection was cut" narrative.

**Caveat on the audit's strictness:** the ID+removal-language-window
heuristic is a precision-oriented lower bound, not a full read of every
narration. E.g. Cora key `0` (target 1, single removed edge to node 344)
says "node 1 is not connected to any other nodes" in the counterfactual
graph — substantively correct — but never re-states "344" near a removal
word, so it's counted as "silent" here. This kind of under-count is
real but doesn't change the overall picture: the great majority of
narrations, especially for the common case of >1 removed edge or an
indirect 2-hop change, do not correctly identify which specific edge(s)
changed.
