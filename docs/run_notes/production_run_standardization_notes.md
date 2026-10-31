# Production Run — Standardization Notes

Run directory: `./production_run_2026-07-27/`
Purpose: paper-metrics production run across 4 explanation methods x 2 datasets (Cora, ogbn-Products), with full intermediate-output persistence and reproducibility.

_This file is being written incrementally as the run progresses. Sections marked TODO will be filled in as jobs complete._

---

## 1. Eval splits

| Dataset | Split file | Full eval set |
|---|---|---|
| Cora | `cora_splits_seed42.npz` (`test_idx`) | 542 nodes |
| Products | `products_splits_seed42.npz` (`eval_idx`, carved from the 37,745-node `test_idx`) | 200 nodes |

## 2. Checkpoints used, with md5

| Checkpoint | Path | md5 |
|---|---|---|
| Canonical SAGE, Cora | `llm-graph-cf/pretrained/sage_canonical.pt` | `858c5440fcfb3586309ccd2218713437` |
| Canonical SAGE, Products | `sage_products_canonical.pt` | `ccaf2c1d59dbecfc33dc45bd8f056d18` |
| GraphNarrator own GNN, Cora | `graphnarrCora/GraphNarrator/GNN_cora_seed_42.pt` | `c0bc5669b763594a1584bdaf0d779887` |
| GraphNarrator own GNN, Products | `graphnarrCora/GraphNarrator/GNN_products_seed_42.pt` | `5d4acde1ba20319da852d09537955987` |
| GSPELL own GNN, Cora (genuinely separate, ~30% acc) | `LOGIC2/GSPELL/pretrained/cora-meta-llama/.../2026-03-09-20-33-28/sage.pth` | `d590ad5ef63cfef9263be59c97fa4763` |
| GSPELL projector, Cora (reused, pre-existing) | `.../2026-03-09-23-12-28/projector.pth` | `521ead5ff784b58e81dacb2518c0a208` |
| GSPELL "own" GNN, Products (re-keyed canonical weights, NOT independently trained — see §4) | `.../products-meta-llama/Meta-Llama-3.1-8B-Instruct/sage_canonical.pth` | `400f674b7d118e2a5b04ff500dfa6833` |
| GSPELL projector, Products (seed=42, this run) | `LOGIC2/GSPELL/pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/projector.pth` | `63873653f485c5d1561cd038db323603` |
| `cora_canonical.pt` | top-level | `4feefd9db585538377534b360156673e` |
| `products_canonical.pt` | top-level | `c698b2d36e4a8b6370c5c4e5f2df14cd` |

## 3. Seeds and generation configs

All runs targeted seed=42 (torch/numpy/python random) unless noted.

| Method | Sampling config | Notes |
|---|---|---|
| GraphXAIN | `temperature=1.0, top_p=0.95, do_sample=True, repetition_penalty=1.1`, single global `torch.manual_seed(42)` at process start | Matches original survey-text generation config (per user instruction: preserve survey-text character while making reproducible via fixed seed) |
| GraphNarrator | local HF generation, `temperature`/sampling per `free_text_explanation.py`'s existing config (unchanged) | seed=42 passed via `--seed 42` |
| llm-graph-cf | `temperature=0.1, top_p=0.8, repetition_penalty=1.05` (script defaults, unchanged — these ARE the original survey-text settings) | **Deviation (fix, approved):** `--seed` was previously not actually reaching `set_full_reproducibility()` or vLLM's `SamplingParams` — both silently hardcoded to 42 regardless of the CLI flag. Fixed by threading `seed` through in both places (`src/llms_m.py`). Harmless for this run since 42 was already the de facto value, but now genuinely controlled by the flag. |
| GSPELL | Llama generation via `model.generate(..., pad_token_id=...)`, no explicit temperature override (uses HF defaults inside GSPELL's own `generate_exp_by_llm`) | seed=42 (Cora: pre-existing config; Products: this run's config override, see §5) |

## 4. GSPELL prediction-path finding

Traced empirically and via code (`eval_utils.py:238` `build_inputs_cora_bow`, `main.py:261-306`): when both `-pgp` (own checkpoint) and `-pdp` (`data_canonical.pth`) are passed to GSPELL's `main.py` — true for every existing GSPELL sbatch invocation, Cora and Products alike — the own-checkpoint forward pass (`sage.pth` for Cora, the re-keyed canonical weights for Products) is computed **only** to print a diagnostic test accuracy line; it is never used again. The `gnn_preds` tensor that actually feeds every prompt's `Predicted Category:` field is loaded from `data_canonical.pth`, which is itself built from the canonical checkpoint. Confirmed live from this production run's captured prompts (`gspell_cora/prompts_raw.jsonl`): node 1's prompt reads `Predicted Category: Rule_Learning` (= canonical prediction), while GSPELL's own Cora checkpoint predicts `Neural_Networks` for that node.

**Implication:** GSPELL's own checkpoint (30.4% agreement with canonical on Cora, see §6) is loaded but not in the causal path of any generated explanation — all GSPELL explanations for both datasets are anchored to the canonical model's predictions, not GSPELL's own (weaker, Cora) or tautologically-identical (Products) classifier.

## 5. GSPELL Products — seed / projector history

Both prior Products runs (2026-05-12, 2026-06-17 — the runs referenced in the original corruption reports) used the `amazon_products.yaml` config's default `seed: [4978]` and trained the projector from scratch each time (`pretrained_projector_path=[]`, 400 epochs) — **neither ever used seed 42**, unlike Cora, which reuses a pre-existing seed-42-trained `projector.pth`. This run (job 50765167) retrains the Products projector from scratch with `--seed 42` explicitly, same config otherwise (400 epochs, lr=0.001, gamma=0.7).

**Result: the corruption is seed-robust, not seed-specific.** This run reproduced the same fabrication failure as both seed-4978 runs (confident, fluent, but factually wrong product descriptions — e.g. a real "Bra-less Nursing Gown" described as "a skincare set for a radiant complexion"). Traced to an architectural cause, not an unlucky initialization: GSPELL's Products path uses `generate_by="embedding"` -> `build_inputs_embeds_vanilla_eos` (soft-prompt-only, no literal product text), whereas Cora uses `build_inputs_cora_bow` (literal BOW keyword text) — the LLM has no lexical grounding for Products and confabulates content consistent with the category label alone. See `gspell_products/FAILURE_CHARACTERIZATION.md` for full detail and evidence. A text-based fallback variant (`-m llm`, literal keyword text, no embedding projection) was run separately (job 50783204) per spec, saved distinctly, not silently substituted for the real pipeline's output.

## 6. Prediction agreement (full eval splits, computed before generation)

| | Cora (542) | Products (200) |
|---|---|---|
| Canonical accuracy | 89.7% | 71.0% |
| GraphNarrator vs canonical agreement | 51.1% | 31.5% |
| GraphNarrator own accuracy | 51.7% | 26.5% |
| GSPELL vs canonical agreement | 30.4% (genuine separate checkpoint) | 100% (tautological, re-keyed canonical weights — see §4) |
| GSPELL own accuracy | 30.3% | 71.0% |
| GraphXAIN, llm-graph-cf | 100% by construction (load canonical checkpoints directly) | same |

**Methodological deviation:** GraphNarrator's own eval procedure uses stochastic 10-neighbor x 2-hop `NeighborLoader` sampling; this check instead ran a full-batch forward pass (all node text BERT-encoded at once, full graph adjacency) for exact reproducibility. This is why the full-split numbers (51%/32%) differ from the original 2026-07-17 audit's 42% (which used a 352-node 3-way intersection, not the full split).

8-node survey check (Cora 510/2334/1062/884, Products 6813/1852/8766/8438): **8/8 agree** between GraphNarrator's own checkpoint and canonical — confirms the original audit's finding that this hand-picked set is not representative of the ~51%/32% population agreement rate.

## 7. llm-graph-cf CF-data coverage

Original CF-search (`max_steps=200`, gradient-based greedy feature removal) found valid counterfactuals for 409/542 Cora nodes and 177/200 Products nodes. The missing nodes are not a scoping gap — the search already attempted all eval nodes and failed to find a flip within budget for the rest.

**Recovery attempt (approved):** reran the identical search restricted to the missing 133 Cora / 23 Products nodes with `max_steps=500` (2.5x budget). Result: **0/133 Cora, 0/23 Products additional counterfactuals found.** No changes were made to `find_counterfactual`'s greedy logic itself (only a `--target_node_ids` filter was added to scope which nodes the outer loop visits).

**Final coverage:** 409/542 (75.5%) Cora, 177/200 (88.5%) Products. These nodes appear structurally resistant to this method's feature-removal-only counterfactual search, not merely budget-limited. Per-method metrics are computed on this covered subset; the coverage rate itself is reported as a result.

Missing node IDs:
- Cora (133): see `prediction_agreement/llmgraphcf_missing_nodes.json`
- Products (23): see `prediction_agreement/llmgraphcf_missing_nodes.json`

## 8. GraphNarrator Cora pkl coverage

`outputs/pkls_cora_eval/` originally had 398/542 required nodes (built once for a 398-node 3-way-intersection set in an earlier standardization pass, not the full split). Products had no such gap (200/200 already matched `eval_idx`).

**Recovery (approved):** reran GraphNarrator's own unmodified step-0 pkl generation (`preprocess.generate_dataset`, invoked via `main.py --mode manual --step 0`), scoped implicitly to the missing 144 index positions (the script already skips any index whose pkl file exists, before the expensive BERT+GNN `explain()` call — no `--target_node_ids`-style filter was needed). Added only: explicit `torch`/`numpy`/`random` seeding to 42 before the run, since `main.py`'s manual-mode path does not seed the `NeighborLoader`'s stochastic neighbor sampling at all (a latent gap, not something introduced by this run). No changes to sampling logic, retry/OOM-skip behavior, or memory limits.

**Result: 542/542 (100%) coverage.** All 144 missing nodes were recovered on this attempt — no OOM skips occurred (unlike llm-graph-cf's CF search, GraphNarrator's own fallback-length retry loop, `preprocess.py`'s `fallback_lengths` mechanism, successfully handled every node this time). Unlike llm-graph-cf, GraphNarrator's Cora eval set is now complete; no subset-reporting caveat needed for this method. See `graphnarrator_cora/index_to_global_node_id_mapping.json` for the full local-index -> global-node-ID table (`root_global_id` field per pkl, self-contained, not filename-order-dependent).

## 9. Environment fix — llm-graph-cf venv

`llm-graph-cf/venv` had a broken torch install (`torch==2.9.0` reported by pip, but `torch/bin/torch_shm_manager` was missing from the installed package — `import torch` itself failed at module init). This blocked the CF-search recovery jobs entirely.

**Fix (approved):** captured `pip freeze > llm-graph-cf/venv_freeze_before_fix_2026-07-27.txt` first, then `pip install --force-reinstall --no-deps --ignore-installed torch==2.9.0` (plain `--force-reinstall` failed with `uninstall-no-record-file` — the existing install had no RECORD file, consistent with a corrupted/incomplete original install; `--ignore-installed` bypassed the uninstall step and overwrote files directly). Verified post-fix: `torch.__version__ == '2.9.0+cu128'`, `torch_shm_manager` present, `torch_geometric` + the project's `gnn_model.GraphSAGE` import cleanly. Same exact version reinstalled, `--no-deps` so no other pinned packages were touched — dependent scripts should be unaffected.

## 10. Truncation logging (GraphNarrator)

Added one line to `free_text_explanation.py`'s existing 6000-char truncation check (`generate_explanations`): logs `node=<id> original_len=<n> truncated_to=6000` via the module's existing `logger` whenever the cutoff is hit. Truncation behavior itself (still cuts at 6000 chars) is unchanged — this only makes previously-silent truncation visible. TODO: pull affected node list from generation-job logs once GraphNarrator's LLM step runs.

## 11. Persistence wrappers (additive, no core-logic changes)

- **GSPELL/Cora, GSPELL/Products:** `run_cora_production_with_persistence.py` (and Products equivalent) monkeypatch `eval_utils.build_inputs_cora_bow`/`build_inputs_vanilla` to log the exact decoded prompt tokens per node; `main.py`'s own logic runs unmodified via `runpy`. Neighbor lists + YES/NO votes + raw LLM output were already persisted by GSPELL's own `generate_exp_by_llm` (the `explanation` field is undecoded raw model output).
- **GraphXAIN (Cora, Products):** `run_{cora,products}_production_with_persistence.py` load the original scripts as modules and monkeypatch `extract_top_features`, `extract_neighbors_by_hop`, `build_prompt`, `generate_llama` to log GNNExplainer's actual importance scores (not just top-k indices — the original gap), the edge-mask-derived neighbor tables, the exact prompt, and the raw narrative — all previously discarded except the final narrative and a bare list of feature indices.
- **GraphNarrator:** prompt + raw response were already persisted per-node by `FreeTextExpGenerator.save()` (`messages` list with user=prompt, assistant=response) — no wrapper needed for that. Added: pkl-snapshot recording + index-mapping table (`build_index_mapping_table.py`), truncation logging (§10).
- **llm-graph-cf:** prompt + raw output already persisted per-node by `llms_m.py` (`responses[key] = (prompt, generated_text)`) — no wrapper needed.

## 12. Job manifest

Generated 2026-07-27. All jobs on partition `gpu-exp`, `gres=gpu:v100-32g:1`, account `<ACCOUNT>`.

| Job ID | Method / dataset | Purpose | Output |
|---|---|---|---|
| 50765133 | prediction-agreement | canonical + GSPELL-own predictions, full splits | `prediction_agreement/{cora,products}_canonical_vs_gspell_full.json` |
| 50765134 | prediction-agreement | GraphNarrator-own predictions, full splits + 8-node survey | `prediction_agreement/{cora,products}_graphnarrator_own_predictions.json` |
| 50765163, 50765164 | llm-graph-cf CF recovery (FAILED — broken venv) | max_steps=500 attempt, superseded by 50768003/50768005 | — |
| 50765167 | GSPELL/Products | projector retrain, seed=42, real embedding-projection pipeline | `LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-<timestamp>/` |
| 50766335 | GSPELL/Cora | production generation (persistence wrapper) | `gspell_cora/prompts_raw.jsonl` + `LOGIC2/GSPELL/output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-14-17-08/GSPELL_explanations.pt` |
| 50766436 | GraphXAIN/Cora | production generation (persistence wrapper) | `graphxain_cora/explainer_and_prompts.jsonl` + dims/narratives JSONs |
| 50766437 | GraphXAIN/Products | production generation (persistence wrapper) — **COMPLETE, 200/200** | `graphxain_products/explainer_and_prompts.jsonl` + dims/narratives JSONs |
| 50768003, 50768005 | llm-graph-cf CF recovery, Cora (133 nodes) / Products (23 nodes) | max_steps=500 retry after venv fix — **0/133, 0/23 recovered** (confirmed unrecoverable, not a torch bug) | `llm-graph-cf/data/{cora,products}/cf-gnnfeatures-canonical-recovered-max500/` |
| 50770392 | GraphNarrator/Cora step-0 | missing-pkl generation (144 nodes) — **COMPLETE, 542/542** | `graphnarrCora/GraphNarrator/outputs/pkls_cora_eval/` |
| 50770401 | GraphNarrator/Products | production generation, exp_id=101 | `graphnarrCora/GraphNarrator/outputs/generated_expls-101/` |
| 50770409 | GraphNarrator/Cora | production generation, exp_id=100, full 542 nodes | `graphnarrCora/GraphNarrator/outputs/generated_expls-100/` |
| 50770411 | llm-graph-cf/Cora | LLM generation, 409-node covered subset | `llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json` |
| 50770412 | llm-graph-cf/Products | LLM generation, 177-node covered subset | `llm-graph-cf/data/results/cf-gnnfeatures-canonical-production-2026-07-27_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` |

| 50783204 | GSPELL/Products text-based fallback | `-m llm`, literal BOW-keyword text, no embedding projection | `LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-<timestamp>/LLM_explanations.pkl` |

**Final status (all jobs complete as of 2026-07-28):**

| Method | Dataset | Coverage | Notes |
|---|---|---|---|
| GraphXAIN | Cora | 542/542 | |
| GraphXAIN | Products | 200/200 | |
| GraphNarrator | Cora | 542/542 | pkl gap fully recovered |
| GraphNarrator | Products | 200/200 | |
| llm-graph-cf | Cora | 407/409 covered nodes | 2 skipped: prompt exceeded `max_model_len=32000` (37,600 / 36,653 tokens) — llm-graph-cf's own existing guard, clean skip not a crash |
| llm-graph-cf | Products | 177/177 covered nodes | |
| GSPELL | Cora | 542/542 | 21h26m, own eval: Fidelity 0.334, Explanation Size 2.42 |
| GSPELL | Products (real embedding-projection pipeline) | 200/200 generated | reproduced known fabrication failure — see §5 / `FAILURE_CHARACTERIZATION.md`; not silently accepted |
| GSPELL | Products (text-based fallback, `-m llm`) | 200/200 generated | genuinely lexically-grounded output (model reasons from literal keyword lists, e.g. "cutting," "blade," "handles" actually present in the neighbor's keywords) — no fabrication observed, in contrast to the embedding-projection run. A downstream automatic-evaluation call in `main.py` (`eval_llm_explanations`, indexing `generated_exp_paths[i]` which is never populated for the `-m llm` path without an explicit `-gep` flag) crashed with `IndexError` *after* the generation output was already saved successfully — this is a pre-existing bug in GSPELL's own code, unrelated to any change made in this run, and does not affect the persisted `LLM_explanations.pkl` (verified: 200/200 unique target nodes, md5 `e54e15ff486dcf54cd3627cc2ed47cf7`). |

## 13. Consolidation into keyed JSON format

`consolidated/` holds one JSON per method per dataset (9 files: `graphxain_{cora,products}.json`, `gspell_cora.json`, `gspell_products_{embedding,textfallback}.json`, `graphnarrator_{cora,products}.json`, `llmgraphcf_{cora,products}.json`), each `{"<global_node_id>": {"explanation_text", "prompt", "generation_config"}}`.

GraphNarrator and llm-graph-cf natively index by local/sequential position, not global node ID — mapped via `index_to_global_node_id_mapping.json` (root_global_id read directly from each pkl, not assumed from file order) and `factual_target_dict_repr.json`'s `Target_Node_ID` field (same entry_idx used to write both files in the same loop iteration) respectively.

**Verification (`consolidated/verify_consolidation.py`):** all 9 files — every key is a valid, unique global node ID within the respective eval split; node counts match the coverage table exactly (542/542/542/200/200/542/200/407/177); 3-node-per-file spot-check against native output is byte-identical on both `explanation_text` and `prompt` for every file (27/27 checks passed); zero nodes present in native output but absent from consolidated, for all 9 files.

GSPELL/Products-embedding has `"prompt": null` with a documented reason (`prompt_unavailable_reason`) — no persistence wrapper was built for that job, and the prompt is only partially textual to begin with (continuous GNN-embedding soft-prompt tokens, no discrete text form — see §5/FAILURE_CHARACTERIZATION.md). This is the one file where the prompt field is not literal.

## 14. Text metrics over full eval sets

`consolidated/extract_neighbor_titles_full.py` generalizes the original 4-node `neighbor_titles.json` to all 200 Products eval nodes (identical extraction logic — 1-hop/2-hop membership from each node's own GraphNarrator pkl subgraph, same title regex — cross-checked to match the original file exactly on the 4 overlapping nodes).

`consolidated/compute_text_metrics_production.py` adapts `compute_text_metrics.py`: only the extraction step changed (reads the 9 consolidated JSONs instead of the 3 survey `.txt` files, iterates the full eval sets instead of the 8 survey nodes); every metric function (`readability`, `halstead`, `entity_counts`, `entity_measures`) is copied verbatim, unchanged. No human-rating correlation section — no survey covers the full eval sets. Cora entity matching uses only the numeric "Node N" pattern (no neighbor-titles file passed, same as the original script's fallback for any untitled node); Products uses `neighbor_titles_full.json`.

Results: `consolidated/metrics_per_text_{cora,products}.csv` (row count matches method coverage exactly: Cora 2033 = 542×4 − 135 llm-graph-cf gap; Products 977 = 200×5 − 23 llm-graph-cf gap). Per-method averages printed by the script; GSPELL/Products is reported as two rows (`GSPELL_embedding`, `GSPELL_textfallback`) since both variants are retained and characterized separately, not collapsed into one.

**Still outstanding:** none — all originally-specified deliverables for this production run are complete.

## 15. GraphXAIN vs. paper verification (2026-08-03)

Verified against Cedro & Martens, *GraphXAIN: Narratives to Explain Graph Neural Networks* (arXiv:2411.02540v3), Section 4.4 and Appendix A, and the untouched upstream repo (`GraphXAIN/notebooks/GraphXAIN_NBA_tutorial.ipynb`).

**Ground-truth-label leakage investigation** (before any code changes):

| Nodes | Script | True label in prompt? |
|---|---|---|
| Cora 510, 2334, 1062, 884 (survey) | `GraphXAIN_Cora/run_graphxain_2hop.py` | No |
| Products 6813, 1852 (survey) | `GraphXAIN_Products/run_graphxain_products_2hop.py` | Yes, unconditional |
| Products 8766, 8438 (survey) | `GraphXAIN_Products/regen_comparison_text_8766_8438.py` (`GXAIN_PROMPT`) | Yes, unconditional |
| Full eval sets (production run, pre-2026-08-03) | `run_graphxain_{cora,products}_full_eval.py` | Yes, unconditional (`"True Class"`, `"Correct"` in `pred_info`) |

None of the three survey-generation scripts contain the "Do NOT reference specific node IDs" rule — it is unique to the full-eval production scripts.

**Ground-truth leakage in the other three methods:** none found. GraphNarrator's template only receives `label=graph.prediction` (the model's own predicted class, `tag.py:151`/`free_text_explanation.py:341-344`) — `ground_truth` is stored on the `TAG` object but never read into a prompt. llm-graph-cf's `Factual_Target_Node_Class`/`Counterfactual_Target_Node_class` (`cf_gnnfeatures.py:425,437`) are the model's own predictions (`orig_pred`/`cf_pred` argmax), not `data.y`. GSPELL's three prompt-builders all source `Predicted Category` from `gnn_preds[target_node]`; `data.y` appears once in `eval_utils.py` (line 532), inside an unrelated post-hoc evaluation helper never used for prompt construction.

**Full list of differences between our GraphXAIN implementation and the paper:**

| Aspect | Paper | Our implementation | Status |
|---|---|---|---|
| LLM | GPT-4o | Llama-3.1-8B-Instruct | Kept (different model, resource constraint) |
| Sampling | `temperature=1.0` (OpenAI API) | `temperature=1.0, top_p=0.95, do_sample=True, repetition_penalty=1.1` (HF `generate`) | Kept — temperature matches, extra HF-specific sampling params have no OpenAI equivalent |
| Prompt: dataset/task description | Included | Included | Match |
| Prompt: target node feature values | All continuous + categorical features, with importance/value/percentile/description, split by type | No categorical/continuous split (BOW features are uniformly binary); no percentile block for the target node | Kept as a known simplification — deliberately not changed in this rerun |
| Prompt: target node's full feature-importance list | All features, sorted | Top-7 only | Kept — matches paper's separate "top-7 in narrative" *rule*, but paper's schema wants the *full sorted list* passed in and only the narrative is restricted to mentioning 7; we never pass more than 7 to begin with |
| Prompt: number of edges / neighbor label ratio | Included | Not included | Kept, not addressed in this rerun |
| Prompt: subgraph nodes' feature values + percentiles | Included | Not included — neighbor rows give `edge_importance`, `class`, and a raw text/title snippet instead | Kept, not addressed in this rerun |
| Subgraph size | Flat top-7 nodes by GNNExplainer edge importance, no hop-tiering | Split: top-7 1-hop + top-10 (Cora) / top-12 (Products) 2-hop = up to 17-19 nodes | **Kept as-is per explicit instruction** — documented here as a known deviation rather than changed |
| Ground truth in prompt | Not part of the schema (`Model's Prediction` = predicted class + probability only) | Was present (`"True Class"`, `"Correct"`) in the full-eval scripts | **Fixed in the 2026-08-03 rerun** — removed, `pred_info` now `{Target Node, Predicted Class, Confidence}` only |
| "Do NOT reference specific node IDs" rule | No equivalent; paper's content-rules 2/3 explicitly say to establish node/edge references clearly, and its own published example narratives name nodes by ID (e.g. Fig. 1: "the connection with node 62... nodes 302, 233, and 26") | Was present in the full-eval scripts' format rules | **Fixed in the 2026-08-03 rerun** — removed |
| Number of most-important features in narrative | 7 (`num_feat=7`) | 7 (`TOP_K_FEAT=7`) | Match |
| Sentence limit | 8 | 8 | Match |

## 16. GraphXAIN paper-aligned rerun (2026-08-03)

Two changes applied to new copies of the full-eval scripts (`run_graphxain_{cora,products}_full_eval_paperaligned.py`, in `GraphXAIN_Cora/` and `GraphXAIN_Products/` respectively — originals untouched):
1. Removed the "Do NOT reference specific node IDs" format rule.
2. Removed `"True Class"` and `"Correct"` from `pred_info`, keeping `Target Node`, `Predicted Class`, `Confidence`.

Subgraph caps (`TOP_K_1HOP=7`, `TOP_K_2HOP=10` Cora / `12` Products) deliberately left unchanged — see §15 table.

Same seed (42), same model (Llama-3.1-8B-Instruct), same sampling config (`temperature=1.0, top_p=0.95, do_sample=True, repetition_penalty=1.1`), same persistence-wrapper mechanism as the original production run. Output: `./graphxain_paperaligned_rerun_2026-08-03/{cora,products}/` — new directory, original `production_run_2026-07-27/graphxain_{cora,products}/` outputs untouched.

Jobs: 51002174 (Cora, complete, 542/542, 1h19m40s), 51002175 (Products, complete, 200/200, 29m03s). Text-metrics comparison (old vs. new) pending — consolidation of the paper-aligned outputs into the keyed JSON format not yet done as of this writing.

## 17. GraphNarrator checkpoint investigation (2026-08-04)

Summary for the record:

- **Checkpoints**: `GNN_cora_seed_42.pt` (md5 `c0bc5669b763594a1584bdaf0d779887`), `GNN_products_seed_42.pt` (md5 `5d4acde1ba20319da852d09537955987`), loaded at `preprocess.py:214-223`.
- **Training recipe used**: `preprocess.py:17-180` `train()` — `AdamW(lr=1e-5, weight_decay=0.0)`, `EPOCHS=5`, `BATCH_SIZE=16`, best-val-accuracy checkpoint selection, frozen BERT (embeddings `.detach()`-ed before the GNN, only `model.gnn.state_dict()` saved). Products training log (`outputs/logs/products_step0_47527451.txt`) confirms this recipe was actually used and shows validation accuracy still climbing at epoch 5 (0.230→0.282→0.302→0.315→0.332) — not converged. No surviving log for Cora's training invocation, but the checkpoint naming convention matches this same function.
- **Paper's recipe** (Pan et al., ACL 2025, arXiv:2410.15268, Appendix F): `lr=1e-3, batch_size=500`, "train until converged" — no optimizer, weight decay, dropout, or neighbor-sampling depth specified anywhere in the paper for the base TAG classifier (the paper's own metrics are entirely about explanation quality — PMI, Simulatability, Brevity, human ratings — it never reports the base classifier's own accuracy on any dataset, so there is no published number to compare our measured accuracy against).
- **Split verification**: empirically confirmed (not assumed) that both `cora_canonical.pt` and `products_canonical.pt`'s baked-in `train_mask`/`val_mask`/`test_mask` are identical to `cora_splits_seed42.npz` / `products_splits_seed42.npz`'s `train_idx`/`val_idx`/`test_idx` (ran `CORA.get_cora_casestudy(SEED=42)` directly and compared node-ID sets; loaded `products_canonical.pt` masks directly and compared). Zero overlap between Products' 200-node `eval_idx` and its `train_mask`/`val_mask`. No leakage, no split mismatch — the low accuracy is real, not an artifact of training on eval data.
- **Full-batch vs. GraphNarrator's own stochastic 10-neighbor/2-hop inference** (`native_stochastic_agreement.py`, seeded torch/numpy=42, `NeighborLoader(num_neighbors=[10,10])`, seed node predictions extracted via `batch.input_id[:batch.batch_size]`): Cora agreement-vs-canonical 51.1%→46.9%, own accuracy 51.7%→48.2%; Products agreement 31.5%→31.0%, own accuracy 26.5%→26.5% (unchanged). Confirms the low numbers are not a full-batch measurement artifact.

**Bug found**: batching `Encoder.encode()` calls (multiple texts in one BERT forward pass, vs. the original one-string-at-a-time loop) was tested as a possible speedup for the batch_size=500 retrain. Speedup was only 1.35x (BERT-base at `max_length=512` is compute-bound per token, not overhead-bound — batching mostly saves Python/kernel-launch overhead, not the real cost). More importantly, **batched and unbatched outputs from the repo's custom `MyBertModel` (BERT_LRP reimplementation) do not match** — max absolute difference ~2.0 on the pooled output (nowhere near floating-point noise), indicating `MyBertModel` mishandles padding/attention-masking when multiple differently-padded sequences are batched together. This is a real bug in the repo's custom BERT class, not something introduced by this investigation. **Not routed around** — the retrain (§18) keeps the original one-string-at-a-time encoding to avoid it, accepting the resulting slower wall-clock time.

**Reproducibility gap in the original checkpoints**: `preprocess.py`'s `train()` never seeds the `NeighborLoader`'s stochastic 2-hop neighbor sampling (no `torch.manual_seed`/`np.random.seed` call anywhere in the function). This means `GNN_cora_seed_42.pt` and `GNN_products_seed_42.pt` — despite the "seed_42" filename — were **not trained via a reproducible procedure**; the "seed 42" in the name refers only to the (correctly reproducible) train/val/test split generation, not to the stochastic neighbor sampling used during actual gradient updates. Re-running the original recipe would not reproduce the same weights. The paper-aligned retrain (§18) fixes this by seeding `torch.manual_seed(42 + epoch)` / `np.random.seed(42 + epoch)` before building each epoch's loader.

## 18. GraphNarrator paper-aligned retrain (2026-08-04)

New script `train_paperaligned.py` (GraphNarrator repo root) — reimplements `preprocess.py`'s `train()` with:
- `lr=1e-3`, `batch_size=500` (paper's Appendix F recipe)
- Patience-based early stopping (stop if validation accuracy doesn't improve for `patience` consecutive epochs) + a hard epoch cap, as a concrete operationalization of "train until converged" — Cora: patience=5, cap=30; Products: patience=5, cap=20 (lower cap, given the per-epoch cost)
- `torch.manual_seed(42 + epoch)` / `np.random.seed(42 + epoch)` before building each epoch's train/val `NeighborLoader` — makes a resumed job chain reproduce exactly the same batches as an uninterrupted run (fixes the reproducibility gap above)
- Resumable: JSON state file (`epoch`, `best_val_accuracy`, `best_epoch`, `epochs_without_improvement`, `val_curve`, `done`, `stop_reason`) + a `_latest.pt` checkpoint saved every epoch, so a SLURM wall-clock kill loses at most one epoch; a job that finds `done: true` in the state file exits immediately
- Architecture, optimizer (`AdamW`, `weight_decay=0.0`), dropout (`0.0`), `num_neighbors=[10, 10]` all **unchanged** — the paper doesn't specify these
- `Encoder.encode()` still called one string at a time — the batching bug above is not routed around
- Products' final test evaluation restricted to the 200-node `eval_idx` rather than the full 37,745-node `test_mask` (`--final_eval eval_idx`) — **deliberate deviation from the original code**, done because the full test_mask pass would cost a separate 1.5-4 hours and we only need eval_idx for the agreement comparison that follows

Saved to new files, originals untouched: `checkpoints_paperaligned_2026-08-04/GNN_{cora,products}_seed_42_paperaligned{_latest,_best,}.pt` (final = `_best` copied at stop time).

Jobs: Cora — 51102340 (single job, `--time=4:00:00`, expected sufficient given ~2.4 min/epoch). Products — chained 51102354→51102355→51102356→51102357→51102358 (5× `--dependency=afterany`, 8h each, up to 40h total) given the ~40-80 min/epoch cost measured in calibration.

**First pass results — both hit the epoch cap, not patience (not converged):**

| | Cora (cap=30) | Products (cap=20) |
|---|---|---|
| Best epoch | 27 | 19 (the very last epoch) |
| Best val accuracy | 0.7025 | 0.7016 |
| Stop reason | `epoch_cap` | `epoch_cap` |
| epochs_without_improvement at stop | 2 (of patience=5) | 0 — still improving |

Products was unambiguously not converged (best epoch = last epoch, curve still climbing). Cora's last 2 epochs had dropped below the peak but hadn't gone 5 epochs without improvement, so `epoch_cap`, not `patience`, was still the actual stop trigger — plausible near-peak but not confirmed.

Full-batch / stochastic agreement-vs-canonical on these first-pass checkpoints (via `predict_graphnarrator_paperaligned.py` / `native_stochastic_agreement_paperaligned.py`, same methodology as §6/the original checkpoint check):

| | Cora old → new | Products old → new |
|---|---|---|
| Full-batch own accuracy | 51.7% → 75.8% | 26.5% → 63.5% |
| Full-batch agreement vs. canonical | 51.1% → 73.2% | 31.5% → 70.5% |
| Stochastic own accuracy | 48.2% → 71.6% | 26.5% → 65.0% |
| Stochastic agreement vs. canonical | 46.9% → 70.5% | 31.0% → 71.5% |

**Extension (user-approved, same day):** `train_paperaligned.py` updated to support resuming a run that stopped via `epoch_cap` (not `patience`) when resubmitted with a higher `--max_epochs` — the state file's `done: true` no longer short-circuits the run if `stop_reason == "epoch_cap"` and the new cap leaves room. Cora resubmitted with `--max_epochs 45` (job 51136150, resumed cleanly from epoch 30) — **stopped on `patience` this time**, best epoch still 27 (val acc 0.7025, unchanged — never beaten in epochs 28-32), confirming the plateau is real. Checkpoint is therefore byte-identical to the first pass; agreement/accuracy numbers above stand unchanged for Cora.

Products resubmitted with `--max_epochs 40` (chain 51136151→...→51136156) — finished within the first chain job (51136151, 3h21m); jobs 2-6 found `done: true` and exited in <30s each, as designed. **Stopped on `patience`** this time: best epoch 21 (val acc 0.7242, up from the first pass's 0.7016 at epoch 19), epochs 22-26 all below peak.

**Final numbers, both datasets now patience-confirmed (not cap-limited):**

| | Cora (unchanged, best_epoch=27) | Products (best_epoch=21, up from 19) |
|---|---|---|
| Full-batch own accuracy | 75.8% | **66.5%** (was 63.5%) |
| Full-batch agreement vs. canonical | 73.2% | **74.5%** (was 70.5%) |
| Stochastic own accuracy | 71.6% | **66.0%** (was 65.0%) |
| Stochastic agreement vs. canonical | 70.5% | **74.5%** (was 71.5%) |

Cora's checkpoint never changed across the extension (best epoch never moved past 27), so its agreement numbers are identical to the first pass, now on firmer footing (patience-confirmed rather than cap-limited). Both datasets' paper-aligned checkpoints are now genuinely converged by the patience criterion, not epoch-cap artifacts.

## 19. GraphXAIN re-verification and 8-survey-node corrected regeneration (2026-08-07)

Re-verified §15's findings against the live paper text (arXiv:2411.02540v3 §4.4/Appendix A) — all four deviations still hold as described. Two additional findings not previously documented:

1. **§16's "TOP_K_1HOP=7 ... Cora ... deliberately left unchanged" is wrong for the original survey stimuli.** It's true of the full-eval scripts, but the actual generator of the 4 Cora survey nodes' text (`GraphXAIN_Cora/run_graphxain_2hop.py`) used `TOP_K_1HOP=5`, not 7. §16 conflated the two. This means the full-eval-paperaligned rerun (§16) is NOT a faithful stand-in for a corrected version of the original Cora survey stimuli — it would silently show 2 more 1-hop neighbors than participants saw.
2. **Products 8766/8438 use a third, structurally different pipeline** (`GraphXAIN_Products/regen_comparison_text_8766_8438.py`, `GXAIN_PROMPT` section): reuses a precomputed indices-only `graphxain_products_dims.json` (no importance values ever computed) and pulls neighbors from a GraphNarrator pkl's full unranked adjacency, rather than a fresh GNNExplainer edge-mask ranking like the other two survey scripts.

None of the 3 original survey-generation scripts (`run_graphxain_2hop.py`, `run_graphxain_products_2hop.py`, `regen_comparison_text_8766_8438.py`) had a "Do NOT reference specific node IDs" rule to begin with — confirmed still true, consistent with §15's original finding.

**Corrected, persisted regeneration** (user-approved plan: faithful per-script fix, not reuse of the full-eval-paperaligned pipeline): wrote 3 new scripts, one per original generator, each a minimal-diff copy with only the leakage fields removed + `torch.manual_seed(42)` + JSONL persistence added — originals untouched:
- `GraphXAIN_Cora/run_cora_survey_corrected_2026-08-07.py` — no leakage existed to remove; `TOP_K_1HOP=5`/`TOP_K_2HOP=10` preserved exactly as original.
- `GraphXAIN_Products/run_products_6813_1852_corrected_2026-08-07.py` — removed `"True Class"`/`"Correct"` from `pred_info`; `TOP_K_1HOP=7`/`TOP_K_2HOP=12` preserved.
- `GraphXAIN_Products/run_products_8766_8438_corrected_2026-08-07.py` — removed the unconditional `"**True Category:**"` line from `GXAIN_PROMPT`. **Documented deviation (user-approved):** since the original mechanism never computed real importance values for this pair (precomputed indices-only dims + unranked pkl adjacency — neither has an importance signal to persist), this script runs a genuine fresh GNNExplainer pass instead, adopting the sibling script's `TOP_K_1HOP=7`/`TOP_K_2HOP=12` edge-mask-ranked selection. The GXAIN_PROMPT wording, example block, and this script's own sampling config (`temperature=0.7, top_p=0.9, max_new_tokens=700` — distinct from the other two survey scripts' `1.0/0.95`) are preserved exactly. Feature/neighbor *content* for this pair may differ somewhat from the original stimuli as a result — unlike the other two corrections, which reproduce the original selection mechanism exactly.

Run via `sbatch_{cora_survey,products_6813_1852,products_8766_8438}_corrected.sh`, jobs 51102376/51102377/51102378, all complete same-day. Output: `./graphxain_survey_corrected_2026-08-07/{cora,products_6813_1852,products_8766_8438}/explainer_and_prompts.jsonl` — 8/8 nodes covered, every record carries real `node_mask`/`edge_mask`-derived importance values (not just indices), full prompt, raw LLM output. Verified zero ground-truth-leakage strings and zero "Do NOT reference" text in any of the 8 prompts.

**Confirmed untouched (md5 match, pre/post):** `cora_explanation_comparison_llama.txt` (`080b928e...`), `products_explanation_comparison_llama.txt` (`a7d79a2a...`), `products_explanation_comparison_llama_8766_8438.txt` (`67a0d6b2...`) — the actual 20-participant survey stimuli. Original generator scripts' mtimes also confirmed to predate this regeneration.

## 20. GSPELL `eval_llm_explanations` index bug + post-hoc filter provenance (2026-08-10)

**Bug: `eval_llm_explanations` indexes by list position, not real node ID, and generation runs over scattered splits.** `eval_utils.eval_llm_explanations`'s metric loop does `for i in range(num_eval_samples): ego_graph = nx.ego_graph(G, i, ...); gnn_preds[i]`, treating loop position `i` as the literal graph node ID. This is correct only when generation ran over `range(N)` in order — which is what upstream's own `generate_exp_by_llm` always does (confirmed against `github.com/pbaghershahi/GSPELL.git`: no scattered-split support exists upstream at all, `for node_idx in range(max_num_eval_nodes)` unconditionally). Our repo separately added scattered-split support (`--split_path`/`node_ids`, uncommitted local diff, not upstream) so generation can run over a real held-out split (`test_idx`/`eval_idx`) instead of literal node IDs `0..N-1` — but `eval_llm_explanations` was never updated to match. Verified empirically, not just by reading: for the Cora text-path run's saved `GSPELL_explanations.pt`, `target_node` at list position `i` equals `test_idx[i]` for 542/542 entries and equals `i` itself for 0/542.

**Every previously reported GSPELL Fidelity/Size number is affected, both datasets.** Cora's and Products' eval splits (`test_idx`/`eval_idx` in `cora_splits_seed42.npz`/`products_splits_seed42.npz`) are both scattered, sorted-but-non-contiguous node ID lists, not `range(N)` — so the bug is live in every GSPELL run done so far. Corrected re-evaluation (additive wrapper, `corrected_eval.py`/`apply_corrected_eval.py` — does not modify `eval_utils.py`; reuses `eval_llm_explanations`'s own logic with `i` replaced by each entry's real `target_node`), applied to already-generated output with no new LLM generation:

| Arm | Fidelity (previously logged / corrected) | Size (previously logged / corrected) |
|---|---|---|
| Cora, text path (`build_inputs_cora_bow`, run 2026-05-22-20-50-49) | 0.334 / **0.306** | 2.42 / **23.5** |
| Products, embedding path (job 50765167, the fabricating run) | 0.700 / **0.915** | 1.00 / **7.68** |
| Cora, embedding path (job 51180082, resubmit of 51137037 — see below) | 0.332 / **0.310** | 1.69 / **12.50** |

Job 51137037 (first submission) queued ~24h on `gpu-exp` behind a maintenance reservation, then started and crashed on the very first node — cause was a bug in *our own* persistence wrapper (`run_cora_embedding_path_production.py`'s `_sha256_tensor` called `.numpy()` on a bfloat16 tensor, which numpy doesn't support; the real embeddings tensor handed to `model.generate` was never touched, only the checksum helper). Fixed by upcasting to float32 before hashing; resubmitted as job 51180082, ran cleanly end-to-end (542/542 nodes, ~10h wall time), completed 2026-08-14.

Direction of the error isn't consistent (Cora's corrected fidelity is lower than logged; Products' is higher) — it's not a simple bias, it's evaluating against the wrong node's ego-graph and GNN prediction entirely, so no consistent correction factor applies. Full detail incl. comprehensiveness/random-baseline/alignment: `production_run_2026-07-27/corrected_eval_{cora_textpath,products_embpath,cora_embpath}_2026-08-10/corrected_metrics.json`.

**The post-hoc filter ("Po" in the paper's Table 10 ablation) was already present and already active in every run, including the fabricating Products one.** Not partially implemented — `extract_neighbor_support`'s regex parse plus the `if s in neighbors` membership check inside `eval_llm_explanations` is byte-for-byte identical to upstream (diffed directly against a fresh clone of `github.com/pbaghershahi/GSPELL.git`), and `eval_llm_explanations` runs automatically after every `-m gspell` generation call, unconditionally. It was never absent; what was absent was persistence of what it discards. Added (same wrapper): `prefilter_postfilter_removed.jsonl` per arm, logging raw parse / filtered result / removed set per node per batch.

Measured hallucination rate (fraction of parsed node-ID citations that were not in the batch of real neighbors offered, hence discarded by the filter): **Cora text path 0/19370 (0.0%)** — `build_inputs_cora_bow` explicitly hands the LLM the exact real IDs and instructs it to analyze only those, and it does. **Products embedding path 989/3039 (32.5%)** — confirms the filter is catching real hallucinated node-ID citations at scale on the fabricating run, not just passing everything through. Two distinct patterns in what gets removed: (a) ~10% of removed citations (102/989) are the model restating the target node itself inside a neighbor-batch response (real, valid node, just not a member of that specific batch — arguably not "hallucination" in the paper's sense, an artifact of per-batch scoping); (b) the remaining ~90% (887/989) are genuinely invented IDs, e.g. target node 3305's neighbor batch was exactly `[3249, 343]` (2 real neighbors) but the model additionally invented and labeled 11 more IDs (`1201, 908, 472, 281, 901, 123, 456, 789, 234, 567, 890`) that don't exist in that batch — round-number pattern-completion with no lexical grounding, consistent with `FAILURE_CHARACTERIZATION.md`'s finding that Products generation has no literal product text to ground on. **The filter did catch and remove these** — they do not appear in the corrected Size/Fidelity computation above. What the filter cannot catch: fabricated *content* about a correctly-cited real neighbor (e.g. the "Bra-less Nursing Gown" described as "a skincare set" — real ID, wrong description) — the paper's χ/S_v formalism only filters on node-ID membership in `T_v^Φ`, not factual correctness of what's said about a real, correctly-cited node.

**Cora's embedding path (job 51180082) shows the identical fabrication signature as Products, and more cleanly demonstrable — anachronism.** Hallucination rate 1439/15484 (9.3%) — lower than Products' 32.5% but far above the text path's 0%, same architectural cause (`build_inputs_embeds_vanilla_eos`, soft-prompt-only, no literal text). Content check on survey node 510 (real BOW keywords, independently recomputed from `cora_canonical.pt`: `adaptation, algorithms, ... combinatorial, ... heuristic, heuristics, ... optimization, ... pruning, search, ...` — a Genetic_Algorithms paper about combinatorial optimization): the embedding-path output instead invents `Neural Networks, Deep Learning, Computer Vision, Object Detection, YOLO, YOLOv2` as this node's "keywords." Cora (Sen et al. 2008, papers predate ~2007) cannot contain a paper about YOLO (2016) or use "Deep Learning" as a category term — this is unambiguous confabulation, not a paraphrase of real content, and more clearly diagnosable than the Products case since there's no ambiguity about whether the content could plausibly be real. Survey node 1062 degenerated further: the model's output abandoned the explanation format entirely and described the prompt template itself ("You can input the target paper and its keywords... The options are to calculate the similarity...") rather than producing any analysis — consistent with the "generation collapse" pattern `FAILURE_CHARACTERIZATION.md` documented at low frequency on Products (1/200 nodes).
