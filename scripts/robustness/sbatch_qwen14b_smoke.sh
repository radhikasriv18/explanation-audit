#!/bin/bash
#SBATCH --job-name=qwen14b_smoke
#SBATCH --output=$WORKSPACE/robustness_2026-10-30/logs/qwen14b_smoke_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --partition=gpudebug-exp
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=00:50:00
#SBATCH --mem=32G

# Smoke test: longest-prompt Cora node (1782; 25,048 Llama / 27,294 Qwen tokens) and
# longest-prompt Products node under Qwen (1958; 14,194 Llama / 15,289 Qwen tokens).
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
    --format=csv -l 2 > logs/qwen14b_smoke_gpumem_${SLURM_JOB_ID}.csv &
SMI_PID=$!

python run_qwen14b_regen.py --out_dir smoke_test --nodes cora:1782 products:1958

kill $SMI_PID
