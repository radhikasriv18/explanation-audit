#!/bin/bash
#SBATCH --job-name=judge_llama_hybrid
#SBATCH --output=$WORKSPACE/grounding_judge_2026-10-13/logs/judge_llama_hybrid_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=06:00:00
#SBATCH --mem=48G
# Usage: sbatch sbatch_judge_llama_hybrid.sh <nodes: all | cora:884,...> <run-dir>   (hybrid mode)
cd $WORKSPACE/grounding_judge_2026-10-13
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate
export HF_HUB_OFFLINE=1
nvidia-smi --query-gpu=name,memory.total --format=csv
python judge.py --backend llama --nodes "$1" --run-dir "$2" --hybrid
