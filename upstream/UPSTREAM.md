# Upstream repositories

The four explanation methods are not copied into this package. Clone each at the commit below, then apply our
patch (where there is one). The patches were checked with `git apply --check` against a clean export of each commit.

| Method | Repository | Commit | Our patch | Workspace path the scripts expect |
|---|---|---|---|---|
| GraphNarrator | https://github.com/pb0316/GraphNarrator | `38c08d2f7e136f98ff2f470bef6a2f41b75bc467` | `patches/graphnarrator.patch` | `graphnarrCora/GraphNarrator/` |
| GSPELL | https://github.com/pbaghershahi/GSPELL | `5412e674af8a44707f88b42aad933b356c079473` | `patches/gspell.patch` | `LOGIC2/GSPELL/` |
| llm-graph-cf (CF-GNNExplainer narrations) | https://github.com/flaat/llm-graph-cf | `16cc238bb32cdc19a96e6f57347a9344e95cee5d` | `patches/llm-graph-cf.patch` | `llm-graph-cf/` |
| GraphXAIN | https://github.com/ADMAntwerp/GraphXAIN | `82c158cc71df695f9888b1728044ccdfcc43150c` | none (unmodified; our GraphXAIN pipeline is standalone, see `scripts/generation/graphxain/`) | `GraphXAIN/` |

```bash
WS=/path/to/workspace
git clone https://github.com/pb0316/GraphNarrator "$WS/graphnarrCora/GraphNarrator"
git -C "$WS/graphnarrCora/GraphNarrator" checkout 38c08d2f7e136f98ff2f470bef6a2f41b75bc467
git -C "$WS/graphnarrCora/GraphNarrator" apply "$PKG/upstream/patches/graphnarrator.patch"
# same pattern for GSPELL (-> $WS/LOGIC2/GSPELL) and llm-graph-cf (-> $WS/llm-graph-cf)
```

Then copy the new files we added inside each checkout from `scripts/generation/<method>/` into the checkout root
(`graphnarrator/` → GraphNarrator root, `gspell/` → GSPELL root, `cf_gnnexplainer/` → llm-graph-cf root; `src/` keeps its
sub-path). `tools/setup_workspace.sh` links them there for you.

## What each patch changes

**graphnarrator.patch** (8 files, +557 / −108): `dataset.py` / `preprocess.py` load the shared canonical Cora graph
(`--cora_data_path`) and add Products; `tag.py` keeps local→global node-id metadata on each subgraph;
`free_text_explanation.py` adds the local Hugging Face generation path (with the 6000-character prompt truncation the
paper's GraphNarrator texts were generated under) and the Products prompt template (`v_products`); `main.py` adds
`--dataset`, `--pkl_dir`, `--use_local_hf` and a single-process path for local generation; `clm.py` / `filter.py`
point the filter LM at `google/gemma-2-2b-it`; `models/joint_model.py` fixes a hard-coded sequence-length tensor.

**gspell.patch** (6 files, +373 / −56): `data_utils.py` / `main.py` / `config/*.yaml` load the canonical graphs,
splits and GNN settings (`processed_data_path`, `split_path`); `train_utils.py` can train on a node subset
(avoids an O(N²) OOM on Products); `eval_utils.py` holds the prompt builders used for our runs (including the
upstream vanilla builder) and the `eval_llm_explanations` fixes described in
`docs/run_notes/production_run_standardization_notes.md` §20. The Hugging Face token is read from `$HUGGINGFACE_TOKEN`.

**llm-graph-cf.patch** (4 files, +96 / −36): `main.py` adds `--llm` and `--explainer` (explainer output folder,
e.g. `cf-gnnexplainer-canonical`); `src/llms_m.py` adds the vLLM path, seeding, Products, and picks "adjacency matrix"
wording for edge-removal explainers; `src/prompts.py` adds `CANONICAL_PROMPT`; `data/kb.py` adds the Products
knowledge-base text.
The explainer itself (`src/cf_gnnexplainer.py`, an adaptation of CF-GNNExplainer to GraphSAGE) is a new file and
lives in `scripts/generation/cf_gnnexplainer/src/`.

## Local differences deliberately left out of the patches

- GraphNarrator: deletions of upstream notebooks and `models/LMs/BERT_LRP/{code/requirements.txt, models/BERT-Google/vocab.txt}`
  in our working copy (space clean-up, not a code change).
- GSPELL: deletion of `TAGLAS/.gitattributes` (not a code change).
- llm-graph-cf: a regenerated output file, `data/results/gnnexplainer_Llama-3.2-3B-Instruct_aids_Response.json` (data, not code; unrelated to the paper).
