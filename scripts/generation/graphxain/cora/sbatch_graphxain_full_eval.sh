#!/bin/bash
#SBATCH --job-name=gxain_cora_fulleval
#SBATCH --output=$WORKSPACE/GraphXAIN_Cora/output/gxain_cora_fulleval_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Cora

source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Cora Full Eval ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"
echo "Node: $SLURMD_NODENAME"
nvidia-smi

python run_graphxain_cora_full_eval.py \
    --splits $WORKSPACE/graphnarrCora/GraphNarrator/cora_splits_seed42.npz \
    --gnnexpl_epochs 100

echo "Finished: $(date)"
