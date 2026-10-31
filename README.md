# Code and data release

Code and data for comparing four LLM-based GNN explanation methods (GraphNarrator, GSPELL, GraphXAIN and
CF-GNNExplainer with LLM narration) on Cora (542 evaluation nodes) and Amazon Products (200 evaluation nodes):
the full standardized runs of all four methods, text metrics, rule-based grounding metrics,
an LLM grounding judge, and a robustness study that regenerates explanations with other LLMs.

Upstream method code is **not** included. `upstream/UPSTREAM.md` gives each repository's URL and commit, and
`upstream/patches/` holds our changes as `git apply`-able patches.

## Layout

```
README.md
upstream/
  UPSTREAM.md                 repo URLs, commits, what each patch changes
  patches/                    graphnarrator.patch, gspell.patch, llm-graph-cf.patch (GraphXAIN is unmodified)
scripts/
  generation/
    graphnarrator/            run/sbatch scripts added to the GraphNarrator checkout (exp 100 Cora, exp 101 Products;
                              paper-aligned retrain + prediction agreement; untruncated full-eval rerun)
    graphxain/{cora,products} standalone GraphXAIN pipeline (GNNExplainer + Llama-3.1-8B narrative) on the full eval
                              sets: original, paper-aligned and schema-aligned variants
    cf_gnnexplainer/          src/cf_gnnexplainer.py (CF-GNNExplainer adapted to GraphSAGE), CF-GNNFeatures,
                              canonical GNN training, vocab, narration sbatch scripts; run_scripts/ = production jobs
    gspell/                   canonical data, projector retraining, persistence wrappers, corrected eval
  consolidation/              per-method outputs -> one {global_node_id: {explanation_text, prompt, ...}} JSON;
                              prediction_agreement/ (canonical GNN vs. each method's own predictions)
  metrics/
    text_metrics/             compute_text_metrics_production.py: readability, Halstead lexical complexity,
                              entity-graph complexity on the full eval sets
    readability/              Flesch-Kincaid components on the sources behind the readability table
    grounding/                rule-based grounding precision (one script per method) and recall / F1
    entity_graph/             entity-graph complexity v5 and per-method entity counts
    gspell/                   GSPELL rows for the readability / lexical / entity tables, Kruskal-Wallis tests
    gspell_style/             GSPELL-paper metrics (fidelity, comprehensiveness) for GraphNarrator and CF
  judge/                      LLM grounding judge; FROZEN_JUDGE_PROMPT.md is the exact prompt and settings
  robustness/                 subset selection, regeneration (Qwen2.5-14B, Llama-3.1-70B, GPT-4o, GPT-4o-mini)
                              and scoring/ (judge and metrics for the regenerated texts)
data/
  inputs/                     cora_canonical.pt (canonical Cora graph) and seed-42 splits for Cora and Products
  explanations/
    full_eval_consolidated/   all four methods, Cora 542 + Products 200, keyed by global node id
    graphnarrator_raw/        GraphNarrator exp 100 (Cora) / 101 (Products) per-node JSON (prompt + response)
                              and index -> global node id maps
    graphxain_schemaaligned/  GraphXAIN full run used for grounding and the judge (no true-class leakage)
    graphxain_paperaligned/   GraphXAIN full run used for the readability table
    cf_gnnexplainer/          explainer_output/ (factual + counterfactual graphs, removed edges) and
                              llm_narrations/ (Llama-3.1-8B narrations)
    gspell_final/             final GSPELL run (Cora and Products, embedding path)
  metrics/                    full-eval outputs: text metrics, readability, GSPELL metrics, GSPELL corrected eval,
                              CF-GNNExplainer edge-accuracy audit, prediction agreement
  robustness/                 regeneration subset, regenerated texts per model, scoring outputs
                              (all metrics computed on a fixed subset of 12 Cora + 12 Products nodes)
tools/
  workspace_layout.tsv        package path -> workspace path the scripts expect
  setup_workspace.sh          recreates that layout as symlinks
```

## Which script produces which result

| Result | Script(s) |
|---|---|
| Generated explanations, all methods, full eval sets | `scripts/generation/*`, then `scripts/consolidation/consolidate_*.py` |
| Prediction agreement (canonical GNN vs. method predictions) | `scripts/consolidation/prediction_agreement/predict_canonical_and_gspell.py`, `predict_graphnarrator.py`, `merge_report.py` |
| Readability (Flesch-Kincaid) table | `scripts/metrics/readability/fk_components_pooled_table_sources.py`, `cf_nonempty_recompute.py` |
| Text metrics on the full eval sets (FK, lexical, entity graph) | `scripts/metrics/text_metrics/compute_text_metrics_production.py` |
| GSPELL rows of the readability / lexical / entity tables; four-method Kruskal-Wallis | `scripts/metrics/gspell/stage_a_extract.py` → `stage_b_metrics.py` → `stage_c_fk30_all_methods.py` |
| Entity-graph complexity | `scripts/metrics/entity_graph/compute_entity_graph_v5.py` |
| CF-GNNExplainer coverage and edge-accuracy audit | `scripts/generation/cf_gnnexplainer/src/cf_gnnexplainer.py` |
| Grounding precision / recall / F1 | `scripts/metrics/grounding/{graphnarrator,graphxain,cf_gnnexplainer}/grounding_precision_rulebased*.py`, `grounding_recall_f1.py` |
| LLM grounding judge | `scripts/judge/judge_gemini.py`, `judge_gemini_3methods.py`; agreement with hand labels: `report_gemini_full.py` |
| Robustness to the narrating LLM | `scripts/robustness/make_robustness_subset.py`; `run_qwen14b_regen.py`, `run_llama70b_regen.py`, `run_gpt4o_graphxain.py`, `run_gpt4omini_graphnarrator.py`; `scoring/{prepare_judge_inputs,judge_robustness,compute_metrics}.py` |

## How to reproduce

1. **Workspace.** Clone and patch the upstream repositories as in `upstream/UPSTREAM.md`, then run
   `bash tools/setup_workspace.sh /path/to/workspace` and `export WORKSPACE=/path/to/workspace`.
   Python scripts use paths relative to the workspace root, so run them from `$WORKSPACE`; the shell scripts use
   `$WORKSPACE` directly. `#SBATCH` headers are from our Slurm cluster: set `--account`, partition and
   `--cluster` (`<ACCOUNT>`, `<A100_CLUSTER>`) for yours.
2. **Inputs.** `data/inputs/` holds the canonical Cora graph (`cora_canonical.pt`: PyG `Data` with features,
   labels, edges and node text) and the seed-42 splits for both datasets. Not included:
   `products_canonical.pt` (454 MB; rebuild with `scripts/generation/gspell/gen_products_canonical.py`) and the
   canonical GraphSAGE checkpoints `llm-graph-cf/pretrained/sage_canonical.pt` (train with
   `scripts/generation/cf_gnnexplainer/src/train_gnn.py`) and `sage_products_canonical.pt` (train with
   `scripts/generation/gspell/train_products_canonical_gnn.py`). GSPELL's internal `data_canonical.pth` is made by
   `gen_canonical_data.py` / `gen_products_canonical_data.py`. Model weights come from Hugging Face:
   `meta-llama/Meta-Llama-3.1-8B-Instruct`, `Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4`
   (revision `08fdbde5eea15cd2aae884125fbfd604dec19818`), `hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4`
   (revision `1b0ae7f9d6da8b79f36fdc24912f950ecb2b6e91`).
3. **Environments.** Each upstream repository's own requirements, plus: `transformers` 4.44.2 for GraphNarrator; `vllm` for the Qwen / Llama-70B regeneration; `textstat` 0.7.13 and `scipy` 1.13.1 for every
   readability / lexical metric (other textstat versions give different FK values); `google-genai` for the judge;
   `openai` for the GPT-4o / GPT-4o-mini runs.
4. **API keys** are read from the environment only: `OPENAI_API_KEY`, `GEMINI_API_KEY`, `HUGGINGFACE_TOKEN`.
   None are included.
5. **Order.** Generation → consolidation → metrics → robustness (regeneration → judge →
   `compute_metrics.py`). Every stage's outputs are in `data/`, so any stage can be rerun on its own.
6. **Determinism.** Generation used seed 42. LLM outputs still differ across GPU types: compare regenerated text
   only against runs on the same hardware (A100 for the robustness runs, V100 for the rest).
