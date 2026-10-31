#!/bin/bash
#SBATCH --job-name=gspell_products_fix
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/gspell_products_fix_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

python regen_gspell_products.py
