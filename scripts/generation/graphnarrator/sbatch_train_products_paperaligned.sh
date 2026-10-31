#!/bin/bash
#SBATCH --job-name=gn_train_products_paperaligned
#SBATCH --output=$WORKSPACE/graphnarrCora/GraphNarrator/checkpoints_paperaligned_2026-08-04/train_products_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=32G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate

python train_paperaligned.py \
    --dataset products \
    --seed 42 \
    --lr 1e-3 \
    --batch_size 500 \
    --patience 5 \
    --max_epochs 40 \
    --final_eval eval_idx \
    --ckpt_prefix checkpoints_paperaligned_2026-08-04/GNN_products_seed_42_paperaligned
