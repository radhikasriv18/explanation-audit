#!/bin/bash
#SBATCH --job-name=llm_cf_products_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/llmgraphcf_products/llm_cf_products_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=32G

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

# explainer dir is a copy of the real cf-gnnfeatures-canonical data (177/200
# nodes -- max_steps=500 recovery found 0/23 additional CFs, see
# standardization_notes.md).
python main.py \
    --model_name llama_8B \
    --explainer cf-gnnfeatures-canonical-production-2026-07-27 \
    --dataset products \
    --prompt_type standard \
    --seed 42 \
    --max_tokens 2048 \
    --max_model_len 16000
