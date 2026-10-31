#!/bin/bash
#SBATCH --job-name=gspell_products_seed42
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/gspell_products/gspell_products_seed42_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=48:00:00
#SBATCH --mem=32G

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

# Fresh projector training with seed=42 (prior two Products runs, 2026-05-12 and
# 2026-06-17, both used the config file's default seed=4978 and never trained a
# seed-42 projector -- this is the compliance-mandated production run, real
# embedding-projection pipeline. Same config as those runs (400 projector epochs,
# lr=0.001) except the seed override below. data_canonical.pth is reused (it is
# canonical-model output, not something seed-dependent to retrain).
GNN_GSPELL="./pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct/sage_canonical.pth"
DATA_CANONICAL="./output/products-meta-llama/Meta-Llama-3.1-8B-Instruct/data_canonical.pth"

python main.py \
    -cff "./config/amazon_products.yaml" \
    -m gspell \
    --split_path ./products_splits_seed42.npz \
    -pgp "$GNN_GSPELL" \
    -pdp "$DATA_CANONICAL" \
    -gt sage \
    -ghd 768 \
    -gnh 2 \
    --seed 42
