#!/bin/bash
#SBATCH --job-name=qwen14b_a100_prod
#SBATCH --output=$WORKSPACE/robustness_2026-10-30/logs/qwen14b_a100_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --cluster=<A100_CLUSTER>
#SBATCH --partition=debug-quad
#SBATCH --gpus-per-node=1
#SBATCH --time=00:50:00
#SBATCH --mem=32G

# A100 full run: all 60 nodes in robustness_subset.json (30 Cora + 30 Products).
# debug-quad partition: same node pool as the A100 smoke test (job 8208796, a0001), so the
# smoke-vs-production identity check for Cora 1782 / Products 1958 compares like hardware.
# Estimated 11 min typical, 18 min if every node hit max_tokens, + ~1.5 min startup.
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
# Triton compiles cuda_utils.c, which needs cuda.h; the venv's Triton does not bundle
# it (A100 smoke job 8208758 failed). Headers from the module matching torch cu128.
module load cuda/12.8.1
export CPATH=$CUDA_HOME/include${CPATH:+:$CPATH}

nvidia-smi
# GPU memory trace every 2 s for the memory report
nvidia-smi --query-gpu=timestamp,memory.used,memory.total,utilization.gpu \
    --format=csv -l 2 > logs/qwen14b_a100_prod_gpumem_${SLURM_JOB_ID}.csv &
SMI_PID=$!

python run_qwen14b_regen.py --out_dir production_a100

kill $SMI_PID
