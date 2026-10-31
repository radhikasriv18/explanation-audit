#!/bin/bash
#SBATCH --job-name=gn_products_step0
#SBATCH --output=$WORKSPACE/graphnarrCora/GraphNarrator/outputs/logs/products_step0_%j.txt
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=06:00:00
#SBATCH --mem=64G

cd $WORKSPACE/graphnarrCora/GraphNarrator

source $WORKSPACE/miniforge3/envs/gn310_gpu/bin/activate 2>/dev/null || true
source venv/bin/activate 2>/dev/null || true

mkdir -p outputs/logs outputs/pkls_products

# Train BERT+SAGE GNN on Products (saves GNN_products_seed_42.pt)
python preprocess.py \
    --mode train \
    --dataset products \
    --products_data_path $WORKSPACE/products_canonical.pt \
    --split_path $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --seed 42 \
    --gnn_model SAGE \
    --device cuda

# Generate saliency pkl files for 200 eval nodes
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
