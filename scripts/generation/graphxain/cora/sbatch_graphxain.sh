#!/bin/bash
#SBATCH --job-name=graphxain_cora
#SBATCH --output=$WORKSPACE/GraphXAIN_Cora/output/graphxain_cora_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

# Usage:
#   export OPENAI_API_KEY=sk-...
#   sbatch sbatch_graphxain.sh
#
# Runs GraphXAIN on all 542 Cora test nodes (2-hop subgraph + GNNExplainer + GPT-4o).
# GPU recommended: ~3-5 min total on V100 vs ~3 hours on CPU.
# Outputs:
#   output/graphxain_cora_narratives.json   {node_id: narrative}
#   output/graphxain_cora_dims.json         {node_id: [top7_dims]} -> fed to unified_eval.py

if [ -z "$OPENAI_API_KEY" ]; then
    echo "ERROR: OPENAI_API_KEY is not set. Export it before submitting:"
    echo "  export OPENAI_API_KEY=sk-..."
    echo "  sbatch sbatch_graphxain.sh"
    exit 1
fi

cd $WORKSPACE/GraphXAIN_Cora

source $WORKSPACE/graphnarrCora/GraphNarrator/venv/bin/activate

mkdir -p output

python run_graphxain_cora.py \
    --cora_pt    $WORKSPACE/cora_canonical.pt \
    --gnn_ckpt   $WORKSPACE/llm-graph-cf/pretrained/sage_canonical.pt \
    --vocab      $WORKSPACE/llm-graph-cf/data/cora_vocab.json \
    --out_dir    $WORKSPACE/GraphXAIN_Cora/output \
    --gnnexpl_epochs 100 \
    --top_k_feat 7 \
    --top_k_nb   7 \
    --seed       42
