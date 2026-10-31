#!/bin/bash
#SBATCH --job-name=gxain_cora_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/graphxain_cora/gxain_cora_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Cora
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Cora Production Run (with persistence) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_cora_production_with_persistence.py

echo "Finished: $(date)"
