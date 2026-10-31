#!/bin/bash
#SBATCH --job-name=cfgnnexp_llm_cora
#SBATCH --output=$WORKSPACE/cf_gnnexplainer_run_2026-08-10/logs/llm_gen_cora_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=04:00:00
#SBATCH --mem=32G

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

python main.py \
    --model_name llama_8B \
    --explainer cf-gnnexplainer-canonical \
    --dataset cora \
    --prompt_type standard \
    --seed 42 \
    --max_tokens 2048 \
    --max_model_len 16000
