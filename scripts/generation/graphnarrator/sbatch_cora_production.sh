#!/bin/bash
#SBATCH --job-name=gn_cora_prod
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/graphnarrator_cora/gn_cora_prod_%j.txt
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpu-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=12:00:00
#SBATCH --mem=64G

cd $WORKSPACE/graphnarrCora/GraphNarrator
source venv/bin/activate

# exp_id=100: fresh ID, not reused from any prior run. pkl_dir now has full
# (or as-full-as-achievable) coverage of the 542-node Cora eval split after
# the step-0-missing recovery run. Prompt + raw response are already
# persisted per-node by FreeTextExpGenerator.save() into
# outputs/generated_expls-100/{index}.json -- no wrapper needed.
python main.py \
    --mode manual \
    --step 1 \
    --seed 42 \
    --dataset cora \
    --cora_data_path $WORKSPACE/cora_canonical.pt \
    --pkl_dir outputs/pkls_cora_eval \
    --exp_id 100 \
    --model_id meta-llama/Meta-Llama-3.1-8B-Instruct \
    --use_local_hf \
    --num_processes 1 \
    --device cuda
