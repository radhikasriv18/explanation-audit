#!/bin/bash
#SBATCH --job-name=gx_products_eval
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/graphxain_products_eval_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=64G

# Runs GraphXAIN on the same 200 eval nodes as llm-graph-cf/GraphNarrator/GSPELL
# (from products_splits_seed42.npz), enabling 4-way method comparison.
# Outputs to output/eval_split/ to avoid overwriting the original 0-237 run.

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/GSPELL/narratives/bin/activate

mkdir -p output/eval_split

python run_graphxain_products.py \
    --data_pt    $WORKSPACE/products_canonical.pt \
    --gnn_ckpt   $WORKSPACE/sage_products_canonical.pt \
    --vocab      $WORKSPACE/llm-graph-cf/data/products_vocab.json \
    --out_dir    $WORKSPACE/GraphXAIN_Products/output/eval_split \
    --split_path $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --llm_backend llama \
    --llama_model meta-llama/Meta-Llama-3.1-8B-Instruct \
    --gnnexpl_epochs 100 \
    --top_k_feat 7 \
    --top_k_nb   7 \
    --seed       42
