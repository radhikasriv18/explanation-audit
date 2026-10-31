#!/bin/bash
#SBATCH --job-name=llm_cf_cora_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/llmgraphcf_cora/llm_cf_cora_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=32G

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

# explainer dir is a copy of the real cf-gnnfeatures-canonical data (409/542
# nodes -- max_steps=500 recovery found 0/133 additional CFs, see
# standardization_notes.md). Distinct explainer name -> distinct output
# filename, so this does not touch the pre-existing
# data/results/cf-gnnfeatures-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json
python main.py \
    --model_name llama_8B \
    --explainer cf-gnnfeatures-canonical-production-2026-07-27 \
    --dataset cora \
    --prompt_type standard \
    --seed 42 \
    --max_tokens 2048 \
    --max_model_len 16000
