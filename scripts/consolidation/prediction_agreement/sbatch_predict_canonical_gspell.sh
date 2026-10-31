#!/bin/bash
#SBATCH --job-name=predagree_gspell
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/prediction_agreement/predagree_gspell_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=00:30:00
#SBATCH --mem=32G

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate
python $WORKSPACE/production_run_2026-07-27/prediction_agreement/predict_canonical_and_gspell.py
