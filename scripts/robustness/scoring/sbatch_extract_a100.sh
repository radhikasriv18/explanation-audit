#!/bin/bash
#SBATCH --job-name=rb_extract
#SBATCH --output=$WORKSPACE/robustness_2026-10-30/scoring/logs/extract_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --cluster=<A100_CLUSTER>
#SBATCH --partition=nextgen
#SBATCH --gpus-per-node=1
#SBATCH --time=03:00:00
#SBATCH --mem=48G
#SBATCH --cpus-per-task=4

# A100 (V100 queue was 5-9 h out). Same venv, model, prompt, greedy decoding and
# offline settings as the pilot extraction
# (grounding_judge_pilot/run_extract.sbatch). Args: SHARD NSHARDS
set -euo pipefail
cd $WORKSPACE/robustness_2026-10-30/scoring
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
nvidia-smi -L
$WORKSPACE/graphnarrCora/GraphNarrator/venv/bin/python extract_robustness.py --shard "$1" --nshards "$2"
