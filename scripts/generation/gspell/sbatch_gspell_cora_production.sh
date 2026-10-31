#!/bin/bash
#SBATCH --job-name=gspell_cora_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/gspell_cora/gspell_cora_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=48:00:00
#SBATCH --mem=32G

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

python run_cora_production_with_persistence.py
