#!/bin/bash
#SBATCH --job-name=gxain_cora_paperaligned
#SBATCH --output=$WORKSPACE/graphxain_paperaligned_rerun_2026-08-03/cora/gxain_cora_paperaligned_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Cora
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Cora paper-aligned rerun ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_cora_paperaligned_with_persistence.py

echo "Finished: $(date)"
