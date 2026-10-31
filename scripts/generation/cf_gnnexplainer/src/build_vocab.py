"""
build_vocab.py

Reconstruct the original Cora BOW vocabulary that matches data.x in cora_canonical.pt.
data.x uses the original McCallum Cora BOW (Porter-stemmed, 1433 dims). This script
reverse-engineers the vocab by matching Porter-stemmed tokens from raw_text to each
feature column via Jaccard similarity.

Saves:
  - data/cora_vocab.json       : list of 1433 words (index → word, matches data.x dims)
  - data/cora_node_words.json  : {str(node_id): [word, ...]} derived directly from data.x

Usage:
    python src/build_vocab.py --cora_data_path ./cora_canonical.pt
"""

import argparse
import json
import os
import re

import numpy as np
import torch
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from scipy.sparse import lil_matrix, csr_matrix


# Words in the "Title: ... Abstract: ..." format that aren't content vocabulary
_FORMAT_ARTIFACTS = {"titl", "abstract", "title", "section", "paper", "present"}


def build_and_save(cora_data_path: str, vocab_path: str, node_words_path: str) -> None:
    print(f"Loading {cora_data_path} ...")
    data = torch.load(cora_data_path, map_location="cpu", weights_only=False)
    raw_texts: list = data.raw_text
    num_nodes = len(raw_texts)
    x = data.x.numpy()  # (num_nodes, F)
    n_features = x.shape[1]
    print(f"  {num_nodes} nodes, {n_features} feature dims loaded.")

    stemmer = PorterStemmer()
    en_stops = set(stopwords.words("english"))

    # Porter-stem tokens, filtering out stopwords and format artifacts
    print("Porter-stemming raw texts (stopwords filtered) ...")
    stemmed_sets: list = []
    for text in raw_texts:
        tokens = re.findall(r"\b[a-z]+\b", text.lower())
        stems = set(
            stemmer.stem(t) for t in tokens
            if len(t) > 2 and t not in en_stops
            and stemmer.stem(t) not in _FORMAT_ARTIFACTS
        )
        stemmed_sets.append(stems)

    # Build sorted list of all unique stems
    all_stems_raw = sorted(set(s for ss in stemmed_sets for s in ss))
    stem_to_col_raw = {s: i for i, s in enumerate(all_stems_raw)}
    S_raw = len(all_stems_raw)
    print(f"  Unique Porter stems (before df filter): {S_raw}")

    # Build sparse binary stem-presence matrix to handle large vocabs (e.g. Products).
    # Dense would be num_nodes × S_raw × 4 bytes which OOMs for large datasets.
    print("Building sparse stem matrix ...")
    stem_matrix_raw = lil_matrix((num_nodes, S_raw), dtype=np.float32)
    for i, stems in enumerate(stemmed_sets):
        for s in stems:
            if s in stem_to_col_raw:
                stem_matrix_raw[i, stem_to_col_raw[s]] = 1.0
    stem_matrix_raw = csr_matrix(stem_matrix_raw)

    # Filter stems by document frequency: keep those appearing in [3, 40%] of docs.
    # This removes remaining format artifacts (very high df) and hapax legomena.
    stem_sums_raw = np.asarray(stem_matrix_raw.sum(axis=0)).flatten()
    keep_mask = (stem_sums_raw >= 3) & (stem_sums_raw <= 0.40 * num_nodes)
    filtered_indices = keep_mask.nonzero()[0]
    all_stems = [all_stems_raw[i] for i in filtered_indices]
    stem_matrix = csr_matrix(stem_matrix_raw[:, filtered_indices])
    stem_sums = np.asarray(stem_matrix.sum(axis=0)).flatten()
    print(f"  Unique Porter stems (after df filter): {len(all_stems)}")

    # For each feature dim j in data.x, find the stem with highest Jaccard similarity.
    # Use sparse matrix-vector multiply: stem_matrix.T @ feat_col gives intersection counts
    # efficiently without materialising a huge dense intermediate array.
    print("Matching feature dims to stems via Jaccard similarity ...")
    vocab: list = []
    for j in range(n_features):
        feat_col = x[:, j]
        feat_sum = feat_col.sum()
        if feat_sum == 0:
            vocab.append(f"unk_{j}")
            continue
        intersect = np.asarray(stem_matrix.T.dot(feat_col)).flatten()  # (S,)
        union = feat_sum + stem_sums - intersect
        jaccard = np.where(union > 0, intersect / union, 0.0)
        best_idx = int(jaccard.argmax())
        vocab.append(all_stems[best_idx])

    unique_words = len(set(vocab))
    print(f"  Unique vocab words: {unique_words} / {n_features}")

    # Build per-node word lists DIRECTLY from data.x + derived vocab
    node_words: dict = {}
    for i in range(num_nodes):
        active_dims = x[i].nonzero()[0].tolist()
        node_words[str(i)] = [vocab[j] for j in active_dims]

    os.makedirs(os.path.dirname(vocab_path) if os.path.dirname(vocab_path) else ".", exist_ok=True)

    with open(vocab_path, "w", encoding="utf-8") as f:
        json.dump(vocab, f)
    print(f"Saved vocabulary to {vocab_path}")

    with open(node_words_path, "w", encoding="utf-8") as f:
        json.dump(node_words, f)
    print(f"Saved node word lists to {node_words_path}")


def main():
    parser = argparse.ArgumentParser(description="Build Cora vocabulary from canonical.pt raw_text")
    parser.add_argument("--cora_data_path", type=str, required=True,
                        help="Path to cora_canonical.pt")
    parser.add_argument("--vocab_path", type=str, default="data/cora_vocab.json",
                        help="Output path for vocabulary JSON")
    parser.add_argument("--node_words_path", type=str, default="data/cora_node_words.json",
                        help="Output path for per-node word lists JSON")
    args = parser.parse_args()

    build_and_save(args.cora_data_path, args.vocab_path, args.node_words_path)


if __name__ == "__main__":
    main()
