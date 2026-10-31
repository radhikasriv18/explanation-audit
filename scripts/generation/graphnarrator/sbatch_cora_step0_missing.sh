#!/bin/bash
#SBATCH --job-name=gn_cora_step0_missing
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/graphnarrator_cora/step0_missing_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=06:00:00
#SBATCH --mem=64G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate

python run_cora_step0_missing_seeded.py
