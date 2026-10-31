#!/bin/bash
#SBATCH --job-name=predagree_gn
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/prediction_agreement/predagree_gn_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=01:00:00
#SBATCH --mem=64G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate
python $WORKSPACE/production_run_2026-07-27/prediction_agreement/predict_graphnarrator.py
