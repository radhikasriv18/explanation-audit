# Verification addendum (2026-08-16)

Follow-up audit against the actual paper (arXiv:2102.03322v4, AISTATS 2022
proceedings PDF) and the actual reference code
(github.com/a-lucic/cf-gnnexplainer, commit on `main` as of 2026-08-16:
`src/cf_explanation/gcn_perturb.py`, `cf_explainer.py`, `main_explain.py`),
fetched and read directly rather than recalled from memory. Corrects/extends
the original README's "documented deviations" section with exact numbers
and code-level citations. See chat transcript for the full component-by-
component table and the read-only diagnostics (isolation test, weight-norm
comparison, sample prompts, addition-language cases) backing this.

## Paper's actual reported numbers (Table 1 & 2)
Datasets: TREE-CYCLES, TREE-GRID, BA-SHAPES — all from Ying et al. 2019
(GNNExplainer), all synthetic, motif-detection tasks. BA-SHAPES has **no
node features at all**; classification is 100% structure-driven by
construction. Never evaluated on Cora/CiteSeer/Products.

| | Tree-Cycles | Tree-Grid | BA-Shapes |
|---|---|---|---|
| Avg node degree | 2.27 | 2.77 | 5.87 |
| Avg edges in subgraph (A_v) | 18.99 | 33.94 | 1106.24 |
| Fidelity (low = good) | 0.21 | 0.07 | 0.39 |
| **Coverage ≈ 1 − Fidelity** | **~0.79** | **~0.93** | **~0.61** |
| Explanation size (edges removed) | 2.09 | 1.47 | 2.39 |
| Accuracy (vs ground-truth motif, in-motif nodes only) | 0.94 | 0.96 | 0.96 |

Their own densest dataset (BA-Shapes, avg degree 5.87) already drops to 61%
coverage, well below the other two — the paper's own results show coverage
falling as graph density rises, even with a from-scratch, purely
structure-driven GCN.

## Exact hyperparameter search space and winner (paper §6.4)
K ∈ {100,300,500}; β ∈ {0.1,0.5}; **α is the learning rate** (not a second
regularization weight) ∈ {0.005,0.01,0.1,1}; momentum ∈ {0,0.5,0.7,0.9};
optimizers {Adam, SGD, AdaDelta} all tested. Winner for all three datasets:
**SGD, K=500, β=0.5, α(lr)=0.1**, momentum 0 (tree-cycles/grid) or 0.9
(BA-shapes).

## Reference loss (gcn_perturb.py `loss()`, confirmed from source)
```
pred_same = (y_pred_new_actual == y_pred_orig).float()
loss_pred = -F.nll_loss(output, y_pred_orig)          # = log P(y_orig)
loss_graph_dist = sum(sum(abs(cf_adj - self.adj))) / 2  # edges changed, L1 only
loss_total = pred_same * loss_pred + self.beta * loss_graph_dist
```
Single L1 distance term (not L1+L2 as my first implementation attempt used),
single β weight, gated by the HARD (thresholded) prediction exactly as I
inferred and implemented in my gating fix. Gradient clipped to max-norm 2.0
(`clip_grad_norm(cf_model.parameters(), 2.0)`) — not implemented on our
side. `cf_explainer.py.explain()` runs the full `num_epochs` (500) for
**every** node regardless of whether a CF was already found, tracking the
lowest-total-loss valid CF seen across the whole trajectory — different
from our final algorithm, which breaks at the first hard flip and hands off
to a separate deterministic `greedy_prune` pass.

## Our own hyperparameter sweep on a 40-node Cora dev subset (Adam)
| β=α_l1=α_l2 | Coverage |
|---|---|
| 0.5 (paper's β) | 1/40 |
| 0.05 | 5/40 |
| 0.01 | 10/40 |
| 0.0 (final algorithm) | 21/40 |

SGD (paper's optimizer) at β=0.5: 0/40 (lr=0.1) and 1/40 (lr=1.0) — worse
than Adam at every β we tried, on this architecture/dataset. The paper's own
winning recipe, run faithfully, does not transfer well here.

## Read-only isolation diagnostic (new; forward passes only, no search, no writes to production data)
For every node where the production run found no counterfactual, checked
whether removing the **entire** subgraph's edges (not just a minimal
subset) flips the prediction:

| | Not found (n) | Isolation flips (search ceiling missed) | Isolation still doesn't flip (no budget could help) |
|---|---|---|---|
| Cora | 344 | 43 (12.5%) | 301 (87.5%) |
| Products | 140 | 12 (8.6%) | 128 (91.4%) |

So the *true* achievable ceiling for our search (given unlimited budget) is
≈241/542 (44.5%) Cora and ≈72/200 (36%) Products — our actual found counts
(198, 60) already capture 82-83% of that ceiling. The large majority of
"not found" nodes (87-91%) are not attributable to search budget at all:
no edge subset within the 2-hop subgraph can change their prediction,
because the classification is driven by node content (bag-of-words) rather
than structure for most of these real-graph nodes — unlike the paper's
purpose-built, feature-free synthetic benchmarks.

## Weight-norm comparison (self- vs neighbor-transform), inconclusive on its own
`lin_r` (self) vs `lin_l` (neighbor) weight-matrix Frobenius norms are close
(within ~5-10%, self slightly larger) in both checkpoints — raw weight norm
does not, by itself, strongly support "the model ignores neighbors."
Superseded by the isolation diagnostic above as the real behavioral
evidence.
