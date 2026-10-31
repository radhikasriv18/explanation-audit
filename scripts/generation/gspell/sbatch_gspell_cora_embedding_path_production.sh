#!/bin/bash
#SBATCH --job-name=gspell_cora_embpath
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/gspell_cora_embedding_path_2026-08-10/gspell_cora_embpath_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=48:00:00
#SBATCH --mem=32G

mkdir -p $WORKSPACE/production_run_2026-07-27/gspell_cora_embedding_path_2026-08-10

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

python run_cora_embedding_path_production.py
