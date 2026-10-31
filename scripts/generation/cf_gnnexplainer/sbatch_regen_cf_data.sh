#!/bin/bash
#SBATCH --job-name=regen_cf_data
#SBATCH --output=$WORKSPACE/llm-graph-cf/regen_cf_data_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

cd $WORKSPACE/llm-graph-cf

source venv/bin/activate

# Step 1: Rebuild vocabulary using Porter-stemmed Jaccard matching to data.x
echo "=== Step 1: Rebuilding vocabulary ==="
python src/build_vocab.py \
    --cora_data_path $WORKSPACE/cora_canonical.pt \
    --vocab_path data/cora_vocab.json \
    --node_words_path data/cora_node_words.json

# Step 2: Back up old CF data
echo "=== Step 2: Backing up old CF data ==="
OLD_DIR=data/cora/cf-gnnfeatures-canonical
BACKUP_DIR=data/cora/cf-gnnfeatures-canonical-backup-wrong-vocab
if [ -d "$OLD_DIR" ] && [ ! -d "$BACKUP_DIR" ]; then
    cp -r "$OLD_DIR" "$BACKUP_DIR"
    echo "Backed up old CF data to $BACKUP_DIR"
fi

# Step 3: Regenerate CF descriptions with correct vocabulary
echo "=== Step 3: Regenerating CF descriptions ==="
python src/cf_gnnfeatures.py \
    --cora_data_path $WORKSPACE/cora_canonical.pt \
    --gnn_ckpt pretrained/sage_canonical.pt \
    --node_words_path data/cora_vocab.json \
    --output_dir data/cora/cf-gnnfeatures-canonical \
    --seed 42

echo "=== Done ==="
