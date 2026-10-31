#!/bin/bash
#SBATCH --job-name=graphxain_products_gpt4o
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/graphxain_products_gpt4o_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

# Usage:
#   export OPENAI_API_KEY=sk-...
#   sbatch sbatch_graphxain_products_gpt4o.sh
#
# Runs GraphXAIN on the first 200 Amazon Products test nodes using GPT-4o.
# Outputs:
#   output/graphxain_products_gpt4o_narratives.json  {node_id: narrative}
#   output/graphxain_products_dims.json              {node_id: [top7_dims]}

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/graphnarrCora/GraphNarrator/venv/bin/activate

mkdir -p output

python run_graphxain_products.py \
    --data_pt    $WORKSPACE/products_canonical.pt \
    --gnn_ckpt   $WORKSPACE/sage_products_canonical.pt \
    --vocab      $WORKSPACE/llm-graph-cf/data/products_vocab.json \
    --out_dir    $WORKSPACE/GraphXAIN_Products/output \
    --llm_backend openai \
    --gpt_model  gpt-4o \
    --gnnexpl_epochs 100 \
    --top_k_feat 7 \
    --top_k_nb   7 \
    --max_nodes  200 \
    --seed       42
