#!/bin/bash
#SBATCH --job-name=gxain_products_schemaaligned_prod
#SBATCH --output=$WORKSPACE/graphxain_schemaaligned_production_2026-08-16/products/gxain_products_schemaaligned_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=01:30:00
#SBATCH --mem=64G

cd $WORKSPACE/GraphXAIN_Products
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Products full eval, schema-aligned (200 nodes) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_graphxain_products_full_eval_schemaaligned.py \
    --out_dir $WORKSPACE/graphxain_schemaaligned_production_2026-08-16/products \
    --dump_prompts

echo "Finished: $(date)"
