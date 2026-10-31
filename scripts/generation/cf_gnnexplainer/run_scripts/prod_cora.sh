#!/bin/bash
#SBATCH --job-name=cfgnnexp_cora_prod
#SBATCH --output=$WORKSPACE/cf_gnnexplainer_run_2026-08-10/logs/prod_cora_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=16G
#SBATCH --cpus-per-task=4

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

python src/cf_gnnexplainer.py \
    --cora_data_path $WORKSPACE/cora_canonical.pt \
    --gnn_ckpt pretrained/sage_canonical.pt \
    --node_words_path data/cora_vocab.json \
    --output_dir data/cora/cf-gnnexplainer-canonical \
    --split_path $WORKSPACE/LOGIC2/GSPELL/cora_splits_seed42.npz \
    --seed 42 --max_epochs 500 --lr 0.3
