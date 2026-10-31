#!/bin/bash
#SBATCH --job-name=gxain_cora_regen
#SBATCH --output=$WORKSPACE/GraphXAIN_Cora/output/gxain_cora_regen_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Cora

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Cora Regen Narratives (de-stemmed) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"
nvidia-smi

python run_graphxain_cora_full_eval.py \
    --splits $WORKSPACE/graphnarrCora/GraphNarrator/cora_splits_seed42.npz \
    --regen_narratives \
    --gnnexpl_epochs 100

echo "Finished: $(date)"
