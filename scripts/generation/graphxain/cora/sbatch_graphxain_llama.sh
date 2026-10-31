#!/bin/bash
#SBATCH --job-name=graphxain_llama
#SBATCH --output=$WORKSPACE/GraphXAIN_Cora/output/graphxain_llama_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=08:00:00
#SBATCH --mem=64G

# Usage:
#   sbatch sbatch_graphxain_llama.sh
#
# Runs GraphXAIN on all 542 Cora test nodes using Meta-Llama-3.1-8B-Instruct via vllm.
# No API key needed. Requires ~16GB GPU memory for the model + GNNExplainer.
# Outputs:
#   output/graphxain_cora_llama_narratives.json   {node_id: narrative}
#   output/graphxain_cora_dims.json               {node_id: [top7_dims]} (shared with GPT-4o run)

cd $WORKSPACE/GraphXAIN_Cora

source $WORKSPACE/graphnarrCora/GraphNarrator/venv/bin/activate

mkdir -p output

python run_graphxain_cora.py \
    --cora_pt    $WORKSPACE/cora_canonical.pt \
    --gnn_ckpt   $WORKSPACE/llm-graph-cf/pretrained/sage_canonical.pt \
    --vocab      $WORKSPACE/llm-graph-cf/data/cora_vocab.json \
    --out_dir    $WORKSPACE/GraphXAIN_Cora/output \
    --llm_backend llama \
    --llama_model meta-llama/Meta-Llama-3.1-8B-Instruct \
    --gnnexpl_epochs 100 \
    --top_k_feat 7 \
    --top_k_nb   7 \
    --seed       42
