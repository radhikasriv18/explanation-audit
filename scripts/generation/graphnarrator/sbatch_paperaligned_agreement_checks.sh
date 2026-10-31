#!/bin/bash
#SBATCH --job-name=gn_paperaligned_agreement
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/prediction_agreement/gn_paperaligned_agreement_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=01:00:00
#SBATCH --mem=32G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate
echo "=== full-batch ==="
python predict_graphnarrator_paperaligned.py
echo "=== stochastic ==="
python native_stochastic_agreement_paperaligned.py
