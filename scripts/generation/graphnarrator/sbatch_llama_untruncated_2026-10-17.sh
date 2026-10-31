#!/bin/bash
#SBATCH --job-name=gn_llama_untrunc
#SBATCH --output=$WORKSPACE/graphnarrCora/GraphNarrator/outputs/logs/gn_llama_untrunc_%x_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=24:00:00
#SBATCH --mem=64G

# Usage: sbatch --job-name=gn_llama_cora sbatch_llama_untruncated_2026-10-17.sh cora
#        sbatch --job-name=gn_llama_products sbatch_llama_untruncated_2026-10-17.sh products
# Resumable: rerunning skips nodes whose output json already exists.

DATASET=${1:?dataset (cora|products) required}

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate

echo "=== GraphNarrator $DATASET, base Llama-3.1-8B-Instruct, untruncated, full eval set ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"
nvidia-smi --query-gpu=name,memory.total --format=csv

python run_llama_untruncated_2026-10-17.py --dataset "$DATASET"

echo "Finished: $(date)"
