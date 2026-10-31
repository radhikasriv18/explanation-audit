#!/bin/bash
#SBATCH --job-name=gxain_prod_regen
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/gxain_prod_regen_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products Regen Narratives (de-stemmed) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"
nvidia-smi

python run_graphxain_products_full_eval.py \
    --splits $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --regen_narratives \
    --gnnexpl_epochs 100

echo "Finished: $(date)"
