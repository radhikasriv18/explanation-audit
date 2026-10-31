#!/bin/bash
#SBATCH --job-name=gxain_prod_fulleval
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/gxain_prod_fulleval_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products Full Eval ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"
echo "Node: $SLURMD_NODENAME"
nvidia-smi

python run_graphxain_products_full_eval.py \
    --splits $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --gnnexpl_epochs 100

echo "Finished: $(date)"
