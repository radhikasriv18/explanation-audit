#!/bin/bash
#SBATCH --job-name=gn_train_cora_paperaligned
#SBATCH --output=$WORKSPACE/graphnarrCora/GraphNarrator/checkpoints_paperaligned_2026-08-04/train_cora_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=04:00:00
#SBATCH --mem=32G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate

python train_paperaligned.py \
    --dataset cora \
    --seed 42 \
    --lr 1e-3 \
    --batch_size 500 \
    --patience 5 \
    --max_epochs 45 \
    --final_eval full_test_mask \
    --ckpt_prefix checkpoints_paperaligned_2026-08-04/GNN_cora_seed_42_paperaligned
