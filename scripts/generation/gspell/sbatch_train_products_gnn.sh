#!/bin/bash
#SBATCH --job-name=products_gnn
#SBATCH --output=$WORKSPACE/LOGIC2/GSPELL/log/products_gnn_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

python train_products_canonical_gnn.py
