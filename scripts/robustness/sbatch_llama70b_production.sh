#!/bin/bash
#SBATCH --job-name=llama70b_prod
#SBATCH --output=$WORKSPACE/robustness_2026-10-30/logs/llama70b_prod_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --cluster=<A100_CLUSTER>
#SBATCH --partition=debug-quad
#SBATCH --gpus-per-node=1
#SBATCH --time=01:00:00
#SBATCH --mem=64G

# Llama-3.1-70B GPTQ-INT4 production. debug-quad (1 h max) is the only partition up right
# now with A100-SXM4-80GB nodes. One job per method/dataset slice, each estimated under 1 h:
#   sbatch sbatch_llama70b_production.sh cf cora
#   sbatch sbatch_llama70b_production.sh cf products
#   sbatch sbatch_llama70b_production.sh graphxain "cora products"
#   sbatch sbatch_llama70b_production.sh graphnarrator cora
#   sbatch sbatch_llama70b_production.sh graphnarrator products
# Resumable: finished nodes are skipped, so resubmit the same command if a job times out.
METHODS=${1:?methods}
DATASETS=${2:?datasets}
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
    --format=csv -l 2 > logs/llama70b_prod_gpumem_${SLURM_JOB_ID}.csv &
SMI_PID=$!

python run_llama70b_regen.py --methods $METHODS --datasets $DATASETS --out_dir llama70b

kill $SMI_PID
