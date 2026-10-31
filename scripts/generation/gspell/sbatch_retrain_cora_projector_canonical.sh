#!/bin/bash
#SBATCH --job-name=gspell_cora_proj_retrain
#SBATCH --output=$WORKSPACE/LOGIC2/GSPELL/pretrained/cora-meta-llama/meta-llama/Llama-3.1-8B-Instruct-canonical-projector-retrain-2026-08-16/retrain_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=03:00:00
#SBATCH --mem=32G

mkdir -p "$WORKSPACE/LOGIC2/GSPELL/pretrained/cora-meta-llama/meta-llama/Llama-3.1-8B-Instruct-canonical-projector-retrain-2026-08-16"

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

python retrain_cora_projector_canonical.py
