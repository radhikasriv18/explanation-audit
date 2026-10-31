#!/bin/bash
#SBATCH --job-name=gj_pilot_extract
#SBATCH --output=$WORKSPACE/grounding_judge_pilot/logs/extract_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=48G
#SBATCH --cpus-per-task=4

set -euo pipefail
cd $WORKSPACE/grounding_judge_pilot
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
nvidia-smi -L
$WORKSPACE/graphnarrCora/GraphNarrator/venv/bin/python -c "import torch,transformers;print('torch',torch.__version__,'transformers',transformers.__version__)"
$WORKSPACE/graphnarrCora/GraphNarrator/venv/bin/python extract_claims.py "$@"
