"""
Driver for corrected_eval.corrected_eval_llm_explanations. Reloads a
dataset+GNN checkpoint pair and an already-generated GSPELL_explanations.pt,
then runs the corrected (real-node-ID-indexed) evaluation with
pre/post-filter persistence. Does not regenerate any LLM output.

Usage: python apply_corrected_eval.py <arm_name>
  arm_name in {cora_textpath, products_embpath, cora_embpath}
"""
import sys

import torch

_orig_load = torch.load
def _default_cpu_map(*a, **k):
    k.setdefault("map_location", "cpu")
    return _orig_load(*a, **k)
torch.load = _default_cpu_map

from model import PretrainedModel
from utils import load_model
from corrected_eval import corrected_eval_llm_explanations

ARMS = {
    "cora_textpath": dict(
        data_canonical="./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth",
        gnn_ckpt="./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/sage.pth",
        generated_exps_path="./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-05-22-20-50-49/GSPELL_explanations.pt",
        out_dir="./production_run_2026-07-27/corrected_eval_cora_textpath_2026-08-10",
        prev_logged={"fidelity": 0.3339, "size": 2.4225, "comprehensiveness": 0.0007,
                     "random_baseline": 0.0001, "alignment": 0.0003,
                     "source_log": "log/evaluation/eval_gspell_cora_2026-05-22-20-50-49.log"},
    ),
    "products_embpath": dict(
        data_canonical="./output/products-meta-llama/Meta-Llama-3.1-8B-Instruct/data_canonical.pth",
        gnn_ckpt="./pretrained/products-meta-llama/Meta-Llama-3.1-8B-Instruct/sage_canonical.pth",
        generated_exps_path="./output/products-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-07-27-12-21-05/GSPELL_explanations.pt",
        out_dir="./production_run_2026-07-27/corrected_eval_products_embpath_2026-08-10",
        prev_logged={"fidelity": 0.7000, "size": 1.0000, "comprehensiveness": 0.0000,
                     "random_baseline": -0.0000, "alignment": 0.0000,
                     "source_log": "log/evaluation/eval_gspell_products_2026-07-27-12-21-05.log"},
    ),
    "cora_embpath": dict(
        data_canonical="./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/data_canonical.pth",
        gnn_ckpt="./pretrained/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-03-09-20-33-28/sage.pth",
        generated_exps_path="./output/cora-meta-llama/Meta-Llama-3.1-8B-Instruct-2026-08-12-17-13-34/GSPELL_explanations.pt",
        out_dir="./production_run_2026-07-27/corrected_eval_cora_embpath_2026-08-10",
        prev_logged={"fidelity": 0.3321, "size": 1.6882, "comprehensiveness": 0.0005,
                     "random_baseline": 0.0002, "alignment": 0.0004,
                     "source_log": "job 51180082 sbatch log, 2026-08-14 completion"},
    ),
}


def main():
    arm = sys.argv[1]
    generated_exps_path = sys.argv[2] if len(sys.argv) > 2 else None
    cfg = ARMS[arm]
    if generated_exps_path:
        cfg["generated_exps_path"] = generated_exps_path

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    outdict = torch.load(cfg["data_canonical"])
    dataset = outdict["dataset"]
    gnn_preds = outdict["gnn_preds"].to(device)

    model = PretrainedModel(
        gnn_type="sage",
        in_channels=dataset.n_feats,
        hidden_channels=768,
        out_channels=dataset.num_classes,
        gnn_num_hid_layers=2,
        decoder_type="linear",
        mode="node",
        device=device,
        with_last_dropout=False,
    ).to(device)
    load_model(model, read_checkpoint=True, pretrained_path=cfg["gnn_ckpt"])
    model.eval()

    generated_exps = torch.load(cfg["generated_exps_path"])
    print(f"Loaded {len(generated_exps)} entries from {cfg['generated_exps_path']}")

    summary = corrected_eval_llm_explanations(dataset, model, gnn_preds, generated_exps, device, cfg["out_dir"])

    print("\n=== Comparison: corrected vs previously logged (buggy) ===")
    print(f"Arm: {arm}")
    print(f"Corrected -- fidelity={summary['fidelity']:.4f} size={summary['size']:.4f} "
          f"comp={summary['comprehensiveness']:.4f} rand={summary['random_baseline']:.4f} "
          f"align={summary['alignment']:.4f}")
    if cfg["prev_logged"]:
        p = cfg["prev_logged"]
        print(f"Previous  -- fidelity={p['fidelity']:.4f} size={p['size']:.4f} "
              f"comp={p['comprehensiveness']:.4f} rand={p['random_baseline']:.4f} "
              f"align={p['alignment']:.4f}  (from {p['source_log']})")


if __name__ == "__main__":
    main()
