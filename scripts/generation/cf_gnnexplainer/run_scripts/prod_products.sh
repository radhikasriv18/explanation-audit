#!/bin/bash
#SBATCH --job-name=cfgnnexp_products_prod
#SBATCH --output=$WORKSPACE/cf_gnnexplainer_run_2026-08-10/logs/prod_products_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=16G
#SBATCH --cpus-per-task=4

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

python src/cf_gnnexplainer.py \
    --cora_data_path $WORKSPACE/products_canonical.pt \
    --gnn_ckpt $WORKSPACE/sage_products_canonical.pt \
    --node_words_path data/products_vocab.json \
    --output_dir data/products/cf-gnnexplainer-canonical \
    --split_path $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --seed 42 --max_epochs 500 --lr 0.3
