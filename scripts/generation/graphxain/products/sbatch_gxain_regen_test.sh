#!/bin/bash
#SBATCH --job-name=gxain_regen_test
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/gxain_regen_test_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=00:30:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products Regen Test (3 nodes) ==="
echo "Started: $(date)"

python run_graphxain_products_full_eval.py \
    --splits $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --max_nodes 3 \
    --regen_narratives \
    --out_dir $WORKSPACE/GraphXAIN_Products/output/regen_test \
    --gnnexpl_epochs 100

echo "Finished: $(date)"
