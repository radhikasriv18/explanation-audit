#!/bin/bash
#SBATCH --job-name=gxain_cora_schemaaligned_prod
#SBATCH --output=$WORKSPACE/graphxain_schemaaligned_production_2026-08-16/cora/gxain_cora_schemaaligned_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=03:00:00
#SBATCH --mem=48G

cd $WORKSPACE/GraphXAIN_Cora
source $WORKSPACE/LOGIC2/GSPELL/narratives/bin/activate

echo "=== GraphXAIN Cora full eval, schema-aligned (542 nodes) ==="
echo "Started: $(date)"
echo "Job ID: $SLURM_JOB_ID"

python run_graphxain_cora_full_eval_schemaaligned.py \
    --out_dir $WORKSPACE/graphxain_schemaaligned_production_2026-08-16/cora \
    --dump_prompts

echo "Finished: $(date)"
