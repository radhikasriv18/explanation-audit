#!/bin/bash
#SBATCH --job-name=llama70b_smoke
#SBATCH --output=$WORKSPACE/robustness_2026-10-30/logs/llama70b_smoke_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --cluster=<A100_CLUSTER>
#SBATCH --partition=debug-quad
#SBATCH --gpus-per-node=1
#SBATCH --time=00:40:00
#SBATCH --mem=64G

# Smoke test: Llama-3.1-70B GPTQ-INT4, all three methods on the same two nodes as the
# Qwen smoke test (Cora 1782, Products 1958) = 6 generations. Checks model load, GPU memory,
# and measures tok/s to firm up the production time estimates.
# Estimated ~5 min load + ~5-8 min generation.
set -euo pipefail
cd $WORKSPACE/robustness_2026-10-30
source $WORKSPACE/llm-graph-cf/venv/bin/activate
export HF_HUB_OFFLINE=1
# Same cluster/vLLM fixes as the Qwen A100 run (see sbatch_qwen14b_a100_production.sh):
# in-process engine (Ray psutil), system gcc for Triton, cuda.h from the cuda module.
export VLLM_ENABLE_V1_MULTIPROCESSING=0
export CC=/usr/bin/gcc
module load cuda/12.8.1
export CPATH=$CUDA_HOME/include${CPATH:+:$CPATH}

nvidia-smi
# Fail fast unless this is an 80 GB A100 (weights alone are ~37 GiB).
MEM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | head -1)
[ "$MEM" -ge 79000 ] || { echo "GPU has ${MEM} MiB, need 80 GB"; exit 1; }

nvidia-smi --query-gpu=timestamp,memory.used,memory.total,utilization.gpu \
    --format=csv -l 2 > logs/llama70b_smoke_gpumem_${SLURM_JOB_ID}.csv &
SMI_PID=$!

python run_llama70b_regen.py --methods cf graphxain graphnarrator --datasets cora products \
    --out_dir llama70b_smoke --nodes cora:1782 products:1958

kill $SMI_PID
