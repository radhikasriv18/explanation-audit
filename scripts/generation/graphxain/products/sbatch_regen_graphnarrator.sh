#!/bin/bash
#SBATCH --job-name=gn_products_regen
#SBATCH --output=$WORKSPACE/GraphXAIN_Products/output/gn_products_regen_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Products

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

python regen_graphnarrator_products.py
