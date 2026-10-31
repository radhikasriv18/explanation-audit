"""
Scope Span metric -- VALIDATION ONLY, node 510 (GraphNarrator, exp_id=3).

Reuses ENTITY_REF_RE from compute_text_metrics.py unmodified (same
numeric Node/Article/Product + number, or ROOT, pattern already used for
Entity Graph Complexity -- numeric-only here since this is Cora, no title
fallback, consistent with how Entity Graph Complexity was computed for
this dataset).

Sentence splitter: the ORIGINAL re.split(r"(?<=[.!?])\s+", text) fails to
split when sentence-ending punctuation is immediately followed by a
closing quote before whitespace (e.g. `Theory."\n\nHere...`) -- the same
bug found and fixed for CF-GNNExplainer's edge-recall sentence splitting
earlier. Fixed here the same way: an optional quote char
between the punctuation and the whitespace run.

Scope applied to the WHOLE explanation_text (the full assistant response),
matching exactly what Entity Graph Complexity was already computed over --
not scoped down to just the "Free-Text Explanation" subsection.

Definition:
  1. Split into sentences, numbered 1..n.
  2. For each distinct entity (ENTITY_REF_RE match), record every sentence
     index it appears in.
  3. span(entity) = last_sentence_index - first_sentence_index (0 if
     mentioned only once).
  4. Per text: mean_span, max_span, normalized_mean_span = mean_span / n.
"""
import json
import re
import sys

sys.path.insert(0, "./graphnarrCora/GraphNarrator")

ENTITY_REF_RE = re.compile(
    r"\b(?:Node|Article|Product)[\s\-]?(\d+(?:\.\d+)*)\b|\b(ROOT)\b", re.IGNORECASE
)

SENTENCE_SPLIT_FIXED = re.compile(r"(?<=[.!?])[\"']?\s+")


def split_sentences(text):
    return [s.strip() for s in SENTENCE_SPLIT_FIXED.split(text) if s.strip()]


def scope_span(text):
    sentences = split_sentences(text)
    entity_sentence_indices = {}  # entity_id -> [sentence indices (1-based)]
    for i, sent in enumerate(sentences, start=1):
        for m in ENTITY_REF_RE.finditer(sent):
            entity_id = "ROOT" if m.group(2) else m.group(1)
            entity_sentence_indices.setdefault(entity_id, []).append(i)

    spans = {}
    for entity_id, indices in entity_sentence_indices.items():
        spans[entity_id] = max(indices) - min(indices)

    n_sentences = len(sentences)
    span_values = list(spans.values())
    mean_span = sum(span_values) / len(span_values) if span_values else 0.0
    max_span = max(span_values) if span_values else 0
    normalized_mean_span = mean_span / n_sentences if n_sentences else 0.0

    return {
        "sentences": sentences,
        "entity_sentence_indices": entity_sentence_indices,
        "spans": spans,
        "n_sentences": n_sentences,
        "mean_span": mean_span,
        "max_span": max_span,
        "normalized_mean_span": normalized_mean_span,
    }


if __name__ == "__main__":
    d = json.load(open("./graphnarrCora/GraphNarrator/outputs/generated_expls-3/85.json"))
    text = d["messages"][2]["content"]

    result = scope_span(text)

    print("=" * 100)
    print("SENTENCE-BY-SENTENCE BREAKDOWN (node 510, exp_id=3)")
    print("=" * 100)
    for i, s in enumerate(result["sentences"], start=1):
        print(f"[{i}] {s}")

    print()
    print("=" * 100)
    print("ENTITY -> SENTENCE INDICES")
    print("=" * 100)
    for entity_id, indices in sorted(result["entity_sentence_indices"].items(), key=lambda kv: (kv[0] != "ROOT", kv[0])):
        print(f"  {entity_id!r}: sentences {indices}  -> span = {result['spans'][entity_id]}")

    print()
    print("=" * 100)
    print("AGGREGATES")
    print("=" * 100)
    print(f"  n_sentences = {result['n_sentences']}")
    print(f"  n_entities  = {len(result['spans'])}")
    print(f"  mean_span   = {result['mean_span']:.4f}")
    print(f"  max_span    = {result['max_span']}")
    print(f"  normalized_mean_span = {result['normalized_mean_span']:.4f}")
