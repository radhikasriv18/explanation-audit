#!/bin/bash
#SBATCH --job-name=gspell_products_textfallback
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/gspell_products_textfallback/gspell_products_textfallback_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=32G

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

# Text-based fallback variant (-m llm): uses build_inputs_vanilla (literal BOW
# keyword text per neighbor via a plain HF transformers.pipeline), NOT the
# embedding-projection soft-prompt path (-m gspell) that reproduced the known
# fabrication/generation-collapse failure with seed=42 (see
# gspell_products/FAILURE_CHARACTERIZATION.md). Same canonical GNN checkpoint
# and predictions (gnn_preds sourced from data_canonical.pth), same seed=42,
# same 200-node eval split. Saved separately, clearly labeled -- this does
# NOT replace or silently substitute for the real embedding-projection
# attempt's raw output.
GNN_GSPELL="./pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct/sage_canonical.pth"
DATA_CANONICAL="./output/products-meta-llama/Meta-Llama-3.1-8B-Instruct/data_canonical.pth"

python main.py \
    -cff "./config/amazon_products.yaml" \
    -m llm \
    --split_path ./products_splits_seed42.npz \
    -pgp "$GNN_GSPELL" \
    -pdp "$DATA_CANONICAL" \
    -gt sage \
    -ghd 768 \
    -gnh 2 \
    --seed 42
