#!/bin/bash
#SBATCH --job-name=gxain_products_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/graphxain_products/gxain_products_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

cd $WORKSPACE/GraphXAIN_Products
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products Production Run (with persistence) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_products_production_with_persistence.py

echo "Finished: $(date)"
