# Grounding LLM-as-judge — Phase 1 pilot (claim extraction)

Date: 2026-10-06. Extraction only: no judging, no scoring, no OpenAI calls, no full-set runs.
No existing file outside this folder was modified (source mtimes checked after the run).

## Files
| File | What |
|---|---|
| `build_answer_key.py` → `answer_key_texts.json` | The 21 adjudicated survey texts, copied verbatim, with source file, locator, sha256 prefix and persisted manual counts |
| `extract_claims.py` | Extraction prompt + Llama-3.1-8B-Instruct run + parser |
| `run_extract.sbatch` | Slurm job (gpu-exp, 1× V100-32GB). Ran as job **55450698**, 18 min, log in `logs/` |
| `reparse.py` | Re-parses the saved raw outputs with the current parser (no model call) |
| `extractions/<id>.json` | Per explanation: input text, prompt messages, rendered chat template, raw output, parsed claims, parse diagnostics, manual counts |
| `claim_counts.csv` | Extracted claim count next to the manual count |
| `logs/claim_counts_initial_parse_55450698.csv` | Counts from the first (buggy) parse, kept for the record |

Model and environment: `meta-llama/Meta-Llama-3.1-8B-Instruct` (local HF cache), fp16, SDPA attention, greedy decoding (`do_sample=False`, i.e. temperature 0), max_new_tokens 4096. Python from `graphnarrCora/GraphNarrator/venv` (torch 2.4.1+cu121, transformers 4.44.2). Runs offline.

## Answer-key texts and where each came from
| Method | Nodes | Source file | Text scored |
|---|---|---|---|
| GraphNarrator Cora | 510, 2334, 1062, 884 | `graphnarrCora/GraphNarrator/outputs/generated_expls-3/{85,463,203,168}.json` | `### Free-Text Explanation` section of the assistant message |
| GraphNarrator Products | 6813, 1852, 8766, 8438 | `graphnarrCora/GraphNarrator/outputs/generated_expls-products_untruncated_2026-09-07/{23,3,33,29}.json` (byte copies of `generated_expls-20`, gpt-4o-mini, untruncated) | same section |
| GraphXAIN | all 8 | `graphxain_survey_corrected_2026-08-07/{cora,products_6813_1852,products_8766_8438}/explainer_and_prompts.jsonl`, field `raw_llm_output` | whole output (asserted identical to the `narrative` field in rulebased_v2 JSON) |
| CF-GNNExplainer | Cora 510, 2334, 1062; Products 1852, 8438 | `cf_gnnexplainer_run_2026-08-10/survey_nodes/{cora,products}_survey_nodes.json`, field `llm_raw_output` | whole output |

Evidence for the GraphNarrator choice:
- Cora: the recall values in `grounding_per_node_from_chat.csv` (1.000 / 0.833 / 1.000 / 1.000) equal `grounding_recall_f1_results.json["graphnarrator_corrected"]`, which scored exp_id=3.
- Products: the chat precisions equal `precision_manual` in `graphnarrator_products_recall_f1_untruncated.json`, whose `source_dir` is the untruncated survey folder.
- All answer-key texts differ from the locked full-set sources (exp100/101, GraphXAIN 08-16, CF 177/60), as expected.

GraphNarrator was also run on the full assistant message (`*__full`, secondary). The adjudication was scoped to the Free-Text section, so the Free-Text run is the one to compare.

## Manual counts: what exists on disk
- No file holds a supported / contradicted / unverifiable split. The persisted adjudications are binary (supported True/False), so "unsupported" below combines contradicted and unverifiable.
- **GraphXAIN** (`grounding_precision_rulebased_v2/...RULEBASED_v2.json`) and **CF** (`cf_gnnexplainer_grounding_precision_RULEBASED.json`): `n_facts` / `n_supported` exist, and their precision equals the chat CSV exactly.
- **GraphNarrator Cora:** the chat precisions (0.750 / 0.778 / 0.900 / 0.909) have no per-claim file behind them, so their denominators are unknown. The only persisted count is the rule-based `n_facts` on exp_id=3 (13 / 8 / 8 / 11). All of those passed through the weak word-overlap fallback with precision 1.0, so they don't match the chat numbers.
- **GraphNarrator Products:** only a manual precision is stored (1852 = 1.000, 6813 = 0.800, 8766 = 0.857, 8438 = 0.750). There are no counts.

## Results (primary scope)
| id | extracted | manual n (sup/unsup) | chat precision |
|---|---|---|---|
| GraphNarrator_cora_510 | 14 | 13 (13/0) rule-based | 0.750 |
| GraphNarrator_cora_2334 | 10 | 8 (8/0) rule-based | 0.778 |
| GraphNarrator_cora_1062 | 11 | 8 (8/0) rule-based | 0.900 |
| GraphNarrator_cora_884 | 15 | 11 (11/0) rule-based | 0.909 |
| GraphNarrator_products_6813 | 13 | — | 0.800 |
| GraphNarrator_products_1852 | 10 | — | 1.000 |
| GraphNarrator_products_8766 | 8 | — | 0.857 |
| GraphNarrator_products_8438 | 11 | — | 0.750 |
| GraphXAIN_cora_510 | 22 | 10 (10/0) | 1.000 |
| GraphXAIN_cora_2334 | 7 | 2 (2/0) | 1.000 |
| GraphXAIN_cora_1062 | 13 | 4 (2/2) | 0.500 |
| GraphXAIN_cora_884 | 15 | 6 (5/1) | 0.833 |
| GraphXAIN_products_6813 | 13 | 4 (4/0) | 1.000 |
| GraphXAIN_products_1852 | 11 | 3 (3/0) | 1.000 |
| GraphXAIN_products_8766 | 13 | 7 (6/1) | 0.857 |
| GraphXAIN_products_8438 | 13 | 6 (4/2) | 0.667 |
| CF-GNNExplainer_cora_510 | 14 | 9 (5/4) | 0.556 |
| CF-GNNExplainer_cora_2334 | 16 | 9 (1/8) | 0.111 |
| CF-GNNExplainer_cora_1062 | 16 | 8 (7/1) | 0.875 |
| CF-GNNExplainer_products_1852 | 27 | 6 (4/2) | 0.667 |
| CF-GNNExplainer_products_8438 | 28 | 9 (4/5) | 0.444 |

Totals, extracted / manual: GraphNarrator Cora 50/40 (1.25×), GraphXAIN 107/42 (2.55×), CF 101/41 (2.46×).

## Parsing
- 25/29 outputs parsed as strict JSON.
- 4 had malformed closing braces and were recovered object by object. Repairs are logged in `parse_diagnostics.repairs`, and no claim object was lost:
  - GraphNarrator_cora_884, GraphNarrator_cora_510__full and GraphNarrator_cora_2334__full each dropped the final claim's closing brace.
  - CF products_8438 omitted the outer `]}`.
- The first parse reported these 4 as 0 claims: the fallback grabbed an inner `entities` object and still marked the run valid. That was a parser bug, fixed and re-parsed from the saved raw outputs without rerunning the model. Old values are kept in each file's `parse_history`.

## Observed extraction issues (to address before Phase 2)
1. **Scope mismatch with the manual counts.** The rule-based checkers counted only specific claim kinds:
   - GraphXAIN: cited BOW features plus neighbor citations.
   - CF: infos fields plus a few prose patterns.
   - GraphNarrator: per-node claims in the Free-Text section.

   The extractor also returns class_state, mechanism, importance and content claims, so higher counts are expected and don't by themselves mean over-extraction. Comparing like with like needs either a type filter or a re-adjudication with the new claim types.
2. **Prose that repeats an infos field is not merged in CF.** For example, "connected with 192, 356, 519" and "Factual_Target_Node_Neighbors ... [192, 356, 519]" are both kept, and "lost all its connections" appears alongside "Counterfactual neighbors empty". The merge step only drops exact (normalized-text) duplicates. CF Products 1852 and 8438 (27–28 claims) are inflated mainly by this and by repeated mechanism sentences.
3. **Hedges and evaluations are not always skipped.** Examples: "indicates a focus on...", "lacks strong relevance", "is well-supported by the following factors", "highlights the importance of...".
4. **claim_type drift.**
   - GraphNarrator_cora_1062 types every "Node-X discusses..." claim as content instead of neighbor, while the other three Cora nodes use neighbor correctly.
   - "The target node is 8438 / 510" (the Target_Node_ID field) is typed content.
5. **Atomicity is uneven.** Compound claims stay unsplit, e.g. "Node-1 discusses backpropagation and local minima" and "Node-3.1 to Node-3.4 elaborate on ...".
6. **The model repeats itself.** GraphNarrator_cora_1062 emitted 20 raw claims and 9 were exact repeats (merged).

---

## v2 rerun (2026-10-06): three approved prompt fixes

`USER_TEMPLATE_V2` in `extract_claims.py` (v1 kept unchanged for reproducibility):
1. Prose that restates an infos field is merged into that field's claim. The prompt also says which claim type each field gets.
2. Stricter skip rule for opinion and evaluative phrasing. It keeps only the checkable part of a mixed sentence, keeps importance claims only with a score, rank or ordering, and keeps mechanism claims only when they name specific items and a specific effect.
3. Target vs neighbor typed by the claim's subject: ROOT / node N / "the target" is the target, and every Node-X / Node-X.Y / other node ID is a neighbor.

Run: Slurm job **55451350** (`--prompt-version v2 --no-full`), 11m45s, same model, settings and 21 texts (primary scope only). Outputs:
- `extractions_v2/`
- `claim_counts_v2.csv`
- `count_comparison_v1_v2.csv`
- **`claim_answer_key_v2.csv`**: 280 claim rows with columns method, dataset, node, claim_id, claim_text, claim_type, entities (JSON), source_text_file, verdict (empty), note (empty). Built by `build_claim_answer_key_csv.py`.

Parsing: 20/21 strict. GraphNarrator_cora_884 was recovered with one logged brace repair; nothing was lost.

### Did the fixes work? (regex heuristics over all 21 texts, v1 → v2)
| Check | v1 | v2 |
|---|---|---|
| Total claims | 300 | 280 |
| Claims containing evaluative/hedge words | 59 | 41 |
| GraphNarrator claims whose subject is Node-X, typed neighbor | 32/52 (62%) | 39/65 (60%) |
| CF claims that are not infos-field claims (prose) | 78 | 57 |
| CF infos-field claims with the prescribed type | 20/23 | 19/22 |
| Invalid claim_type | 0 | 1 (`natural_language_explanation`, CF cora 510) |

Mixed results:
- **Evaluative skip (partial).** Inline evaluations are now trimmed ("Node-1 discusses backpropagation."), but Llama often moves the evaluation into its own claim instead of dropping it. For example, GraphNarrator cora 2334 has "Node-2 reinforces the classification", "Node-5 adds weight to the classification" and "...is well-supported". That is why 2334 went from 10 to 21.
- **Neighbor typing (no net gain).** cora 2334 is now fully correct (17 neighbor), but cora 1062 still types every Node-X claim as content.
- **CF merge (partial).** Prose drops in 4 of 5 texts (CF products 8438: 28 → 19), but CF cora 510 still keeps "connected with 192, 356, 519" next to the Neighbors field and three variants of "lost all connections". It also mistypes the Neighbors fields as feature.
- **New regression.** GraphXAIN products 6813 (13 → 18) now has fragmentary confidence variants ("prediction confidence of high / considerable / significant") and an invented negation ("does not have keywords like 'year'..."), which is not in the source.

Conclusion: prompt wording alone doesn't reliably enforce these three rules with Llama-3.1-8B. Options for the next step (not done):
- deterministic post-processing (subject-regex type override, CF prose-vs-field merge by entity-set match, evaluative-phrase filter);
- a two-pass extract-then-filter design;
- or rely on the manual verdict pass to label leftover non-claims (the `note` column can mark them).

---

## v3 (2026-10-06): source_span + span check + rule-based clean-up

Extraction: `USER_TEMPLATE_V3` (v2 rules plus a required verbatim `source_span` per claim). Slurm job **55451604** (`--prompt-version v3 --no-full`), same model, settings and 21 texts. Output in `extractions_v3/`.
- 18/21 parsed strictly.
- GraphNarrator_cora_1062 and CF-GNNExplainer_products_8438 hit the 4096-token output cap. Each lost its last, partial claim, and both were recovered per object.
- GraphXAIN_products_6813 also lost its final partial object.

Post-processing: `cleanup_v3.py` (no model call) → `cleaned_v3/<id>.json` (claims_final, each with `merged_from` where merged, plus cleanup_log), `cleanup_log_v3.csv` (every span_check_fail, relabel, drop and merge) and `span_check_failures_v3.csv` (every failure with a diagnostic cause and whether the claim reached the sheet).
- **Span check:** `source_span` must appear in the input text after collapsing whitespace only. Failures get `span_check=fail`, `unsupported_extraction=true`, and stay in the sheet.
- **Relabel by subject:**
  - A neighbor subject (Node-X, Node-X.Y, "Nodes 8 to 10", a numeric id other than the target, "the neighbor nodes") with type content, feature or class_state → neighbor.
  - A target subject (ROOT, "the target…", node <target>, and for GraphNarrator "Node 0", its local root id) with type neighbor → content.
  - structural, importance and mechanism are kept, since those types describe what is claimed.
- **Drop evaluation-only:** the claim matches an evaluative or hedge pattern and contains nothing checkable (no feature words, titles, classes, edges, other node ids, numbers, rank words or a factual predicate such as discusses/contains/mentions/is linked to). Mixed fact+evaluation claims are kept.
- **CF merge:** prose → infos-field claim when both name the same entity set (field value parsed from the field claim's span), plus explicit empty-set rules. Guards:
  - Natural_Language_Explanation is never a target.
  - The prose type must fit the field.
  - Prose with causal or explanatory wording, or naming Edge_Differences / Node_Differences, is never merged.

Rules changed after reviewing the first clean-up log (all before the final sheet was written):
1. "Node 0" added as a GraphNarrator target alias. Without it, 7 GraphNarrator Products target claims were wrongly relabeled as neighbor.
2. The merge guards above. Without them, CF products_1852 had 5 wrong merges (e.g. "the neighbor nodes also do not influence…" and the Edge_Differences line).
3. Causal verbs (affect, influence, contribute) were removed from the evaluative pattern, and the factual-predicate exemption was added. Without these, 5 GraphNarrator cora 2334 claims like "Node-3 discusses co-evolutionary learning, relevant to…" were dropped.

Sheet: **`claim_answer_key_v3.csv`** (262 rows; built by `build_claim_answer_key_v3.py`).
- Columns: method, dataset, node, claim_id, claim_text, claim_type (after clean-up), entities, source_text_file, source_span, span_check, corrected_type (empty), verdict (empty), note (empty).
- verdict values: supported, contradicted, unverifiable, not_a_claim. See `claim_answer_key_v3_codebook.md`.
- Counts per text: `count_comparison_v2_v3.csv`.

Totals: v2 280 → v3 extracted 286 → after clean-up 262 (11 relabels, 11 drops, 13 merges).

Span check: 74/286 extracted claims fail; 71 of them are in the sheet (2 were dropped, 1 merged).
- 33 are markdown only: the text has `**Node-1:**` and the span has `Node-1:`. 29 of these are in GraphNarrator cora 1062.
- 28 differ only in punctuation, case or quotes, mostly a dropped space before a quote (`like'smoothing,'`) or changed quote style.
- 13 contain words not in the text: paraphrase, a span stitched from two places, or a span that doesn't support the claim.

Known limitation: a passing span only proves the words exist in the text, not that they support the claim. GraphNarrator cora 1062 looped into 23 invented "Node-X is connected to Node-Y" claims, each pointing at a real (markdown-stripped) span. They are in the sheet for the annotator to mark not_a_claim.

---

## v4 (2026-10-06): looser span check + reference packets

No model call and no reruns. The two texts that hit the output cap (GraphNarrator_cora_1062, CF products_8438) were not rerun, as instructed.

**Span check v4** (`span_check_v4.py`). Both span and text are lowercased; markdown markers `*` and `#` are removed; quote characters (`' " ‘ ’ “ ”` and backtick) are replaced by spaces; spacing around punctuation is removed; whitespace is collapsed. The span must then be a substring of the text.
- Quote characters themselves are ignored, not only the spacing around them. 18 spans failed only because Llama swapped `"x"` for `'x'` or dropped the quotes.
- Result: all 33 markdown-only and 28 punctuation/quote-only v3 failures pass, all 13 paraphrased or stitched spans still fail, and all 191 v3 passes still pass.

**Sheet: `claim_answer_key_v4.csv`.** The same 262 rows as v3 (from `cleaned_v3/`), with span_check recomputed and a new `reference_file` column. 12 rows fail (the 13 paraphrased/stitched spans minus CF cora 510 c08, which was merged). These are listed in `span_check_failures_v4.csv`. Codebook: `claim_answer_key_v4_codebook.md`.

**Reference packets: `reference_packets/<id>.md`** (21 files), built by `build_reference_packets.py`. Each has:
1. The full explanation.
2. The exact persisted prompt:
   - GraphNarrator: system + user messages.
   - GraphXAIN: the `prompt` field.
   - CF: `llm_prompt` (the full rendered chat template).
3. The target node: ID, title, canonical raw_text, true class, canonical-SAGE predicted class, and the prediction the method's pipeline recorded.
4. 1-hop and 2-hop neighbors from canonical `edge_index` (ID, true class, title).
5. The method's own evidence:
   - GraphNarrator: per-token saliency for every subgraph node, from the pkl that produced the prompt. Cora `outputs/pkls` and Products `outputs/pkls_products` were verified: `TAG.text()` appears verbatim in each prompt, and the 2026-08-17 standardized pkls do not match. Node-X labels were rebuilt with tag.py's BFS labelling and checked: all 185 labels map to the right node text in the prompt.
   - GraphXAIN: top-7 features with importance, plus GNNExplainer 1-hop/2-hop neighbors with edge importance.
   - CF: factual and counterfactual class, removed edges, and the factual and counterfactual target dicts.
