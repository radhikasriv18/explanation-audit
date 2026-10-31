"""
Generate products_canonical.pt and products_splits_seed42.npz.

products_canonical.pt  — PyG Data object matching cora_canonical.pt schema:
    x            : float [54025, 2000]  BOW features (top-2000 words, binary)
    y            : long  [54025]        class label indices
    edge_index   : long  [2, 144638]    co-purchase edges
    raw_text     : list  [54025]        product title+content strings
    label_names  : list  [47]           Amazon category names
    train_mask   : bool  [54025]
    val_mask     : bool  [54025]
    test_mask    : bool  [54025]

products_splits_seed42.npz — fixed index arrays:
    train_idx    : official ogbn-products train split (14708 nodes)
    val_idx      : official ogbn-products val split   (1572 nodes)
    test_idx     : official ogbn-products test split  (37745 nodes)
    eval_idx     : 200-node fixed eval subset from test_idx, seed 42
                   (used by all 3 repos for LLM explanation generation)

Usage:
    cd ./LOGIC2/GSPELL
    source narratives/bin/activate
    python gen_products_canonical.py
"""

import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import torch
from torch_geometric.data import Data
from sklearn.feature_extraction.text import CountVectorizer

TAGLAS_ROOT   = "./TAGDataset"
OUT_DATA      = "./products_canonical.pt"
OUT_SPLITS    = "./products_splits_seed42.npz"
N_BOW_WORDS   = 2000
EVAL_SIZE     = 200
SEED          = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)


# ── 1. Load TAGLAS Products ───────────────────────────────────────────────────
print("Loading TAGLAS Products dataset ...")
from TAGLAS.datasets.products import Products
taglas_ds = Products(root=TAGLAS_ROOT)
data_tag  = taglas_ds[0]

raw_text    = list(data_tag.x)          # 54025 product description strings
x_original  = data_tag.x_original      # [54025, 100] float
label_map   = data_tag.label_map        # [54025] long  (class indices)
label_names = list(data_tag.label)      # 47 category strings
edge_index  = data_tag.edge_index       # [2, 144638]

print(f"  nodes={len(raw_text)}, edges={edge_index.shape[1]}, classes={len(label_names)}")


# ── 2. BOW features (matches GSPELL AmazonProductDataset with use_bow=True) ──
print(f"Computing BOW features (top {N_BOW_WORDS} words, binary) ...")
vectorizer = CountVectorizer(max_features=N_BOW_WORDS, binary=True)
bow_matrix = vectorizer.fit_transform(raw_text).toarray()   # [54025, 2000]
x_bow      = torch.as_tensor(bow_matrix, dtype=torch.float)
print(f"  BOW shape: {x_bow.shape}")


# ── 3. Official ogbn-products splits (fixed, from TAGLAS side_data) ───────────
print("Reading official ogbn-products splits ...")
split      = taglas_ds.side_data.node_split
train_idx  = split.train.numpy()   # 14708
val_idx    = split.val.numpy()     # 1572
test_idx   = split.test.numpy()    # 37745

print(f"  train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)}")

# 200-node eval subset from test, fixed seed 42
rng = np.random.default_rng(SEED)
eval_idx = rng.choice(test_idx, size=EVAL_SIZE, replace=False)
eval_idx.sort()
print(f"  eval subset: {len(eval_idx)} nodes (seed {SEED})")

# Build boolean masks for canonical .pt
n = len(raw_text)
train_mask = torch.zeros(n, dtype=torch.bool)
val_mask   = torch.zeros(n, dtype=torch.bool)
test_mask  = torch.zeros(n, dtype=torch.bool)
train_mask[train_idx] = True
val_mask[val_idx]     = True
test_mask[test_idx]   = True


# ── 4. Build canonical Data object ───────────────────────────────────────────
print("Building products_canonical.pt ...")
canonical = Data(
    x          = x_bow,
    y          = label_map.long(),
    edge_index = edge_index,
    raw_text   = raw_text,
    label_names= label_names,
    train_mask = train_mask,
    val_mask   = val_mask,
    test_mask  = test_mask,
)

torch.save(canonical, OUT_DATA)
print(f"  Saved: {OUT_DATA}")


# ── 5. Save splits ────────────────────────────────────────────────────────────
np.savez(
    OUT_SPLITS,
    train_idx = train_idx,
    val_idx   = val_idx,
    test_idx  = test_idx,
    eval_idx  = eval_idx,
)
print(f"  Saved: {OUT_SPLITS}")


# ── 6. Sanity check ───────────────────────────────────────────────────────────
print("\n=== Sanity check ===")
loaded = torch.load(OUT_DATA, map_location="cpu", weights_only=False)
print(f"  x:           {loaded.x.shape}  dtype={loaded.x.dtype}")
print(f"  y:           {loaded.y.shape}  dtype={loaded.y.dtype}")
print(f"  edge_index:  {loaded.edge_index.shape}")
print(f"  raw_text:    {len(loaded.raw_text)} strings")
print(f"  label_names: {len(loaded.label_names)} classes")
print(f"  train_mask:  {loaded.train_mask.sum().item()} nodes")
print(f"  val_mask:    {loaded.val_mask.sum().item()} nodes")
print(f"  test_mask:   {loaded.test_mask.sum().item()} nodes")
print(f"\n  Sample label_names: {loaded.label_names[:5]}")
print(f"  Sample raw_text[0]: {loaded.raw_text[0][:120]} ...")
print(f"  y unique classes: {loaded.y.unique().shape[0]}")
splits_loaded = np.load(OUT_SPLITS)
print(f"\n  splits train={len(splits_loaded['train_idx'])} "
      f"val={len(splits_loaded['val_idx'])} "
      f"test={len(splits_loaded['test_idx'])} "
      f"eval={len(splits_loaded['eval_idx'])}")
print("\nDone.")
