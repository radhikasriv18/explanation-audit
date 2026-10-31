#!/bin/bash
#SBATCH --job-name=gxain_cora_corrected
#SBATCH --output=$WORKSPACE/GraphXAIN_Cora/production_corrected_2026-09-07/gxain_cora_corrected_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=48G

mkdir -p $WORKSPACE/GraphXAIN_Cora/production_corrected_2026-09-07

cd $WORKSPACE/GraphXAIN_Cora
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Cora Production Run, CORRECTED (leakage fix isolated) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_cora_production_corrected_2026-09-07.py

echo "Finished: $(date)"
