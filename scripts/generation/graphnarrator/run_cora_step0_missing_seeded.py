"""
Runs GraphNarrator's own unmodified step-0 pkl generation (preprocess.generate_dataset,
invoked via main.py's existing --mode manual --step 0 path) to fill in the 144
Cora pkls missing from outputs/pkls_cora_eval/ (398/542 existed; this run does not
touch the existing 398 -- generate_dataset already skips any index whose pkl file
exists, before the expensive BERT+GNN explain() call, so reruns are naturally
additive-only).

The only change from a bare `python main.py --mode manual --step 0 ...` invocation
is seeding torch/numpy/random for reproducibility -- main.py's manual-mode path
does not seed the NeighborLoader's stochastic neighbor sampling at all, so without
this the newly-generated pkls (for the 144 missing nodes) would not be reproducible
across reruns. No sampling logic, retry/OOM-skip behavior, or memory limits are
changed.
"""
import random
import sys

import numpy as np
import torch

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed(SEED)
    torch.cuda.manual_seed_all(SEED)

sys.argv = [
    "main.py",
    "--mode", "manual",
    "--step", "0",
    "--seed", "42",
    "--dataset", "cora",
    "--cora_data_path", "./cora_canonical.pt",
    "--pkl_dir", "outputs/pkls_cora_eval",
    "--device", "cuda",
]

import runpy  # noqa: E402

runpy.run_path("main.py", run_name="__main__")
