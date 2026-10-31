"""Fix the judge subset before any judging: 12 of the 30 robustness nodes per dataset (24 total).

Same procedure as ../make_robustness_subset.py: the survey nodes are forced in (Cora 510, 2334, 1062;
Products 1852, 8438), and the rest are drawn with numpy.random.default_rng(42) without replacement
from the remaining subset nodes sorted by global node ID. Precision (and F1) are judged on these 24
nodes for every configuration; recall and the text metrics use all 30 per dataset.
Writes judge_subset.json and refuses to overwrite it.
"""
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "judge_subset.json"
SEED, N_PER_DATASET = 42, 12
SURVEY = {"cora": [510, 2334, 1062], "products": [1852, 8438]}


def main():
    assert not OUT.exists(), f"{OUT} exists; the judge subset is fixed"
    sub = json.load(open(HERE.parent / "robustness_subset.json"))
    out = {"seed": SEED, "n_per_dataset": N_PER_DATASET, "source": "../robustness_subset.json", "datasets": {}}
    for ds, survey in SURVEY.items():
        nodes = {n["global_node_id"]: n for n in sub["datasets"][ds]["nodes"]}
        assert all(s in nodes and nodes[s]["is_survey"] for s in survey)
        rest = sorted(g for g in nodes if g not in survey)
        rng = np.random.default_rng(SEED)
        drawn = [int(x) for x in rng.choice(rest, size=N_PER_DATASET - len(survey), replace=False)]
        out["datasets"][ds] = [{"global_node_id": g, "cf_key": nodes[g]["cf_key"], "is_survey": g in survey}
                               for g in sorted(survey + drawn)]
        print(ds, [g for g in sorted(survey + drawn)])
    json.dump(out, open(OUT, "w"), indent=1)


if __name__ == "__main__":
    main()
