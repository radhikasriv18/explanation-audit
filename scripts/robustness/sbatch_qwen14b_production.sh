#!/bin/bash
#SBATCH --job-name=qwen14b_prod
#SBATCH --output=$WORKSPACE/robustness_2026-10-30/logs/qwen14b_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=batch
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=06:00:00
#SBATCH --mem=32G

# Full run: all 60 nodes in robustness_subset.json (30 Cora + 30 Products).
set -euo pipefail
cd $WORKSPACE/robustness_2026-10-30
source $WORKSPACE/llm-graph-cf/venv/bin/activate
export HF_HUB_OFFLINE=1
# Run the vLLM engine in-process. GPTQ config validation initializes CUDA, which
# forces vLLM to spawn its engine process; the spawned child inherits Ray's
# thirdparty_files on sys.path and fails importing its broken bundled psutil
# (smoke job 56853757). In-process changes no model, prompt or sampling setting.
export VLLM_ENABLE_V1_MULTIPROCESSING=0
# Triton compiles its launcher with $CC; the site's default compiler module sets CC=icc, which
# failed in smoke job 56854414. Use system gcc (Triton's default when CC is unset).
export CC=/usr/bin/gcc

nvidia-smi
# GPU memory trace every 2 s for the memory report
nvidia-smi --query-gpu=timestamp,memory.used,memory.total,utilization.gpu \
    --format=csv -l 2 > logs/qwen14b_prod_gpumem_${SLURM_JOB_ID}.csv &
SMI_PID=$!

python run_qwen14b_regen.py --out_dir production

kill $SMI_PID
