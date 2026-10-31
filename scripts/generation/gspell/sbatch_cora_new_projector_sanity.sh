#!/bin/bash
#SBATCH --job-name=gspell_cora_newproj_sanity
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/gspell_cora_newprojector_sanity20_2026-08-16/sanity_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

mkdir -p $WORKSPACE/production_run_2026-07-27/gspell_cora_newprojector_sanity20_2026-08-16

cd $WORKSPACE/LOGIC2/GSPELL
source narratives/bin/activate

export SPLIT_PATH="./cora_splits_sanity20.npz"
export OUT_SUBDIR="gspell_cora_newprojector_sanity20_2026-08-16"

python run_cora_new_projector.py
