#!/bin/bash
#SBATCH --job-name=cf_products_recover500
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/llmgraphcf_products/cf_recover_max500_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=04:00:00
#SBATCH --mem=64G

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

python src/cf_gnnfeatures.py \
    --cora_data_path $WORKSPACE/products_canonical.pt \
    --gnn_ckpt $WORKSPACE/sage_products_canonical.pt \
    --node_words_path data/products_vocab.json \
    --output_dir data/products/cf-gnnfeatures-canonical-recovered-max500 \
    --split_path $WORKSPACE/LOGIC2/GSPELL/products_splits_seed42.npz \
    --seed 42 \
    --num_hops 2 \
    --max_steps 500 \
    --target_node_ids 3503,4157,4548,4886,5001,5661,6236,8056,9545,10483,12726,12744,13079,20262,23324,29164,29706,40923,40975,41275,45324,53644,53931
