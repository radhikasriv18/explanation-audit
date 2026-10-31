#!/bin/bash
#SBATCH --job-name=gxain_products_paperaligned
#SBATCH --output=$WORKSPACE/graphxain_paperaligned_rerun_2026-08-03/products/gxain_products_paperaligned_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

cd $WORKSPACE/GraphXAIN_Products
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products paper-aligned rerun ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_products_paperaligned_with_persistence.py

echo "Finished: $(date)"
