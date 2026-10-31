#!/bin/bash
#SBATCH --job-name=gn_products_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/graphnarrator_products/gn_products_prod_%j.txt
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate

# exp_id=101: fresh ID. pkls_products already covers the full 200-node
# Products eval split (no coverage gap for Products).
python main.py \
    --mode manual \
    --step 1 \
    --seed 42 \
    --dataset products \
    --num_eval_nodes 200 \
    --pkl_dir outputs/pkls_products \
    --exp_id 101 \
    --model_id meta-llama/Meta-Llama-3.1-8B-Instruct \
    --use_local_hf \
    --num_processes 1 \
    --device cuda
