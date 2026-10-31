#!/bin/bash
#SBATCH --job-name=gxain_products_corrected
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/production_corrected_2026-09-07/gxain_products_corrected_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

mkdir -p $WORKSPACE/GraphXAIN_Products/production_corrected_2026-09-07

cd $WORKSPACE/GraphXAIN_Products
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products Production Run, CORRECTED (leakage fix isolated) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_products_production_corrected_2026-09-07.py

echo "Finished: $(date)"
