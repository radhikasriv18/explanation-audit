# GSPELL/Products embedding-projection pipeline — failure characterization

**Run:** job 50765167, seed=42, freshly-trained projector (400 epochs, same config as the two prior corrupted runs except the seed). Output: `LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt`. Raw output has been kept as-is, not discarded or silently substituted.

## Result: the corruption reproduces with seed=42

This is not a seed-specific artifact. Both prior runs (2026-05-12 seed=4978, 2026-06-17 seed=4978) and this run (seed=42) show the same qualitative failure: the LLM confabulates plausible-sounding but factually wrong descriptions of specific products.

**Concrete example (target node 1691, predicted class "Beauty"):**

| Node | Model's fabricated summary | Actual product (`products_canonical.pt.raw_text`) |
|---|---|---|
| 0 | "A skincare set for a radiant complexion." | Aimee Gowns Original Bra-less Nursing Gown (maternity/nursing wear) |
| 134 | "A makeup kit for a flawless look." | Tucks Medicated Cooling Pads — hemorrhoidal treatment pads |
| 1680 | "A perfume for a delightful aroma." | Pampers Swaddlers Diapers Size 1 (baby diapers) |

**Second example (target node 1191, predicted class involves dog products):** the model invents specific sub-types — "a bowl," "a brush," "a collar," "a toy," "treats" — for five neighbor nodes that are, per `raw_text`, all specifically **dog toys** (a talking plush toy, a KONG toy, a squeaker ball, etc.), none of which are actually a bowl, brush, collar, or treats.

Bulk scan of all 200 entries: 1/200 outright degenerate (near-empty, `<<END>>`-truncated collapse), 3/200 under 100 characters — the *overt* collapse rate is low; the more common and harder-to-catch failure is confident, fluent, wrong content like the examples above.

## Root cause (architectural, not incidental)

Traced in `main.py`/`eval_utils.py`: GSPELL's actual explanation-generation call (`-m gspell`) always passes `generate_by="embedding"`. Inside `generate_exp_by_llm`, the branch that gives the LLM literal keyword text (`build_inputs_cora_bow`) is gated on `dataset.name_ == "cora"`; for Products, `dataset.name_ == "amazon_products"` (`data_utils.py:261`), so generation falls through to `build_inputs_embeds_vanilla_eos` — the LLM receives only a handful of continuous soft-prompt embedding tokens (the GNN embedding, projected by `GNNToSoftPrompt`), **not any literal words describing the product or its neighbors**. The only literal text in the prompt is the category label (`Predicted Category: <canonical prediction>`) and the target/neighbor node IDs.

This means the LLM has no lexical grounding to describe specific product identities from — it can only pattern-match plausible content consistent with the category label and free-associate the rest. That is exactly the observed behavior: category-consistent, fluently-written, but specifically wrong. Cora does not show this failure because `build_inputs_cora_bow` gives the LLM the real (Porter-stemmed) BOW keywords per node as literal text.

**Implication:** changing the seed cannot fix this — the failure is a consequence of the embedding-projection architecture applied to a domain (product descriptions) where the LLM needs specific factual content it was never given. Retraining the projector (as done in this run) does not change which information reaches the LLM's context window.

## What this run does NOT tell us

This does not indicate the projector is "badly trained" in the conventional sense — `Fidelity (Sufficiency): 0.70` in this run's own evaluation output is comparable to the canonical model's own eval accuracy (71.0%), meaning the projected embeddings do carry classification-relevant signal. The failure is specific to open-ended natural-language generation grounded in those embeddings, not to the embeddings' predictive content.

## Disposition

- Raw output kept as-is: `LOGIC2/GSPELL/output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt`.
- Text-based fallback variant launched separately (job 50783204, `-m llm`, literal BOW-keyword-text prompts via `build_inputs_vanilla`) — does not use embedding projection, saved to its own timestamped output directory, clearly distinct from the real-pipeline attempt.
- Recommend the paper report both: the real embedding-projection pipeline's fidelity numbers (valid) alongside its generation failure (a finding), and the text-based fallback's explanations as the actually-usable Products/GSPELL narrative text.
