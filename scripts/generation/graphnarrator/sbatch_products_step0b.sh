#!/bin/bash
#SBATCH --job-name=gn_products_pkl
#SBATCH --output=$WORKSPACE/graphnarrCora/GraphNarrator/outputs/logs/products_pkl_%j.txt
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=64G

cd $WORKSPACE/graphnarrCora/GraphNarrator

source $WORKSPACE/miniforge3/envs/gn310_gpu/bin/activate 2>/dev/null || true
source venv/bin/activate 2>/dev/null || true

mkdir -p outputs/logs outputs/pkls_products

# Generate saliency pkl files for 200 eval nodes (GNN already trained)
python main.py \
    --mode manual \
    --step 0 \
    --seed 42 \
    --dataset products \
    --products_data_path $WORKSPACE/products_canonical.pt \
    --split_path $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --num_eval_nodes 200 \
    --pkl_dir outputs/pkls_products \
    --lm_model bert-base-uncased \
    --gnn_model SAGE \
    --exp_id 0 \
    --model_id gpt-4o-mini-2024-07-18 \
    --device cuda
