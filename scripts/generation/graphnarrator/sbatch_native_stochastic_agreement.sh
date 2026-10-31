#!/bin/bash
#SBATCH --job-name=gn_stochastic_agreement
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/prediction_agreement/gn_stochastic_agreement_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate
python native_stochastic_agreement.py
