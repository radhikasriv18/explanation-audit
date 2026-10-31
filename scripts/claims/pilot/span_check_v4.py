"""
v4 span check (2026-10-06, approved loosening of the v3 whitespace-only rule).

A claim passes when its source_span, after normalization, is a substring of the equally
normalized explanation text. Normalization (applied to both sides):
  1. lowercase
  2. remove markdown markers * and #
  3. replace quote characters with a space: ' " and curly quotes (Llama swaps "x" -> 'x' or drops them;
     treated like spacing around quotes; this goes slightly beyond "spacing around quotes")
  4. remove whitespace around punctuation, collapse remaining whitespace
Paraphrased, stitched or otherwise reworded spans still fail.
"""
import re

QUOTES = "'\"‘’“”`"


def loose(s):
    s = (s or "").lower()
    s = re.sub(r"[*#]", "", s)
    s = re.sub("[" + re.escape(QUOTES) + "]", " ", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*([^\w\s])\s*", r"\1", s)
    return s.strip()


def span_check(span, text):
    ls = loose(span)
    return "pass" if ls and ls in loose(text) else "fail"
