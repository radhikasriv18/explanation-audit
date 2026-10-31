#!/bin/bash
#SBATCH --job-name=products_cf_data
#SBATCH --output=$WORKSPACE/llm-graph-cf/products_cf_data_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=04:00:00
#SBATCH --mem=64G

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

# Step 1: Build Products vocabulary (2000-dim BOW → word list)
python src/build_vocab.py \
    --cora_data_path $WORKSPACE/products_canonical.pt \
    --vocab_path data/products_vocab.json \
    --node_words_path data/products_node_words.json

# Step 2: Generate CF-GNNFeatures counterfactual data for 200 Products eval nodes
python src/cf_gnnfeatures.py \
    --cora_data_path $WORKSPACE/products_canonical.pt \
    --gnn_ckpt $WORKSPACE/sage_products_canonical.pt \
    --node_words_path data/products_vocab.json \
    --output_dir data/products/cf-gnnfeatures-canonical \
    --split_path $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --seed 42 \
    --num_hops 2
