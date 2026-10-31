"""
Paper-aligned retrain of GraphNarrator's TAG classifier (Pan et al., ACL 2025,
Appendix F: lr=1e-3, batch_size=500, "train until converged"). Reimplements
preprocess.py's train() loop with:
  - lr=1e-3, batch_size=500 (vs. the original checkpoint's lr=1e-5, batch=16)
  - patience-based early stopping + a hard epoch cap, since "until converged"
    isn't itself an algorithm
  - torch/numpy seeded per-epoch (seed = 42 + epoch) so a resumed job chain
    reproduces exactly the same NeighborLoader batches as an uninterrupted run
  - resumable via a JSON state file + a "latest" checkpoint, so a SLURM
    wall-clock kill loses at most one epoch of work
  - architecture, optimizer (AdamW, weight_decay=0.0), dropout (0.0), and
    num_neighbors ([10, 10]) all UNCHANGED from the original -- the paper
    doesn't specify these, so there is nothing to align them to
  - the frozen-BERT / detached-embeddings design is UNCHANGED (this is what
    makes batch_size=500 memory-cheap; see calibration notes)
  - encoder.encode() is called ONE STRING AT A TIME, matching the original
    code exactly -- batching was tested and rejected (see
    standardization_notes.md: batched vs unbatched MyBertModel outputs differ
    by ~2.0 max abs diff, not floating-point noise -- a real bug in the
    repo's custom BERT_LRP reimplementation, not something to route around
    silently here)

Saves to NEW filenames -- never touches GNN_cora_seed_42.pt / GNN_products_seed_42.pt.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch
from torch.optim import AdamW
from torch_geometric.loader import NeighborLoader

import sys
sys.path.insert(0, "./graphnarrCora/GraphNarrator")
from dataset import CORA, Products, Encoder  # noqa: E402
from models.joint_model import LM_GNN_Joint_Model  # noqa: E402
from log import logger  # noqa: E402


def seed_everything(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)


@torch.no_grad()
def eval_loader(loader, model, encoder, texts, cap_steps=None):
    predictions, ground_truths = [], []
    for step, batch in enumerate(loader):
        if cap_steps is not None and step >= cap_steps:
            break
        embs = torch.cat([encoder.encode(texts[i]).detach() for i in batch.n_id.tolist()], dim=0)
        edge_index = batch.edge_index
        logits = model.forward_gnn(embs, edge_index)
        predictions.append(logits.argmax(dim=1))
        ground_truths.append(batch.y)
    predictions = torch.cat(predictions, dim=0)
    ground_truths = torch.cat(ground_truths, dim=0)
    correct = (predictions == ground_truths).float()
    return (correct.sum() / len(correct)).item(), len(correct)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["cora", "products"], required=True)
    ap.add_argument("--cora_data_path", default="./cora_canonical.pt")
    ap.add_argument("--products_data_path", default="./products_canonical.pt")
    ap.add_argument("--split_path", default="./LOGIC2/GSPELL/products_splits_seed42.npz")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--batch_size", type=int, default=500)
    ap.add_argument("--patience", type=int, default=5)
    ap.add_argument("--max_epochs", type=int, default=30)
    ap.add_argument("--final_eval", choices=["full_test_mask", "eval_idx"], default="full_test_mask")
    ap.add_argument("--ckpt_prefix", required=True)
    args = ap.parse_args()

    seed_everything(args.seed)

    if args.dataset == "cora":
        data, text, num_classes = CORA.load(seed=args.seed, data_path=args.cora_data_path)
    else:
        data, text, num_classes = Products.load(data_path=args.products_data_path, split_path=args.split_path)

    for attr in ("raw_text", "text"):
        if hasattr(data, attr):
            delattr(data, attr)
    data = data.to("cuda")

    encoder = Encoder()
    model = LM_GNN_Joint_Model(lm_model_name="bert-base-uncased", gnn_model_name="SAGE", out_dim=num_classes).to("cuda")

    optimizer = AdamW(model.parameters(), lr=args.lr, weight_decay=0.00)

    state_path = Path(f"{args.ckpt_prefix}_train_state.json")
    latest_ckpt = Path(f"{args.ckpt_prefix}_latest.pt")

    if state_path.exists():
        state = json.loads(state_path.read_text())
        extendable = (
            state.get("done")
            and state.get("stop_reason") == "epoch_cap"
            and args.max_epochs > state["epoch"] + 1
        )
        if state.get("done") and not extendable:
            logger.info(
                "Training already marked done (stop_reason=%s, epoch=%s) and not extendable with max_epochs=%d. Nothing to do.",
                state.get("stop_reason"), state.get("epoch"), args.max_epochs,
            )
            return
        model.gnn.load_state_dict(torch.load(latest_ckpt))
        start_epoch = state["epoch"] + 1
        best_val_accuracy = state["best_val_accuracy"]
        best_epoch = state["best_epoch"]
        epochs_without_improvement = state["epochs_without_improvement"]
        val_curve = state["val_curve"]
        if extendable:
            logger.info(
                "Extending a previously epoch_cap-stopped run: resuming from epoch %d with new max_epochs=%d "
                "(best_val_acc=%.4f at epoch %d, epochs_without_improvement=%d)",
                start_epoch, args.max_epochs, best_val_accuracy, best_epoch, epochs_without_improvement,
            )
        else:
            logger.info("Resuming from epoch %d (best_val_acc=%.4f at epoch %d)", start_epoch, best_val_accuracy, best_epoch)
    else:
        start_epoch = 0
        best_val_accuracy = 0.0
        best_epoch = -1
        epochs_without_improvement = 0
        val_curve = []

    best_ckpt_path = Path(f"{args.ckpt_prefix}_best.pt")
    stop_reason = "already_at_cap_on_resume"

    for epoch in range(start_epoch, args.max_epochs):
        epoch_t0 = time.time()

        seed_everything(args.seed + epoch)
        train_loader = NeighborLoader(data, num_neighbors=[10, 10], batch_size=args.batch_size, input_nodes=data.train_mask)

        model.train()
        total_loss, n_steps = 0.0, 0
        for step, batch in enumerate(train_loader):
            n_steps += 1
            model.train()
            optimizer.zero_grad()
            embs = torch.cat([encoder.encode(text[i]).detach() for i in batch.n_id.tolist()], dim=0)
            edge_index = batch.edge_index
            logits = model.forward_gnn(embs, edge_index)
            loss = torch.nn.CrossEntropyLoss()(logits, batch.y)
            total_loss += loss.item()
            loss.backward()
            optimizer.step()
            logger.info("Epoch %d Step %d: sampled=%d loss=%.4f", epoch, step, batch.n_id.shape[0], loss.item())

        seed_everything(args.seed + 100000 + epoch)
        val_loader = NeighborLoader(data, num_neighbors=[10, 10], batch_size=args.batch_size, input_nodes=data.val_mask)
        model.eval()
        val_acc, n_val = eval_loader(val_loader, model, encoder, text)

        val_curve.append([epoch, val_acc])
        logger.info("Epoch %d: train_loss=%.4f val_acc=%.4f (n=%d) time=%.1fs", epoch, total_loss / n_steps, val_acc, n_val, time.time() - epoch_t0)

        improved = val_acc > best_val_accuracy
        if improved:
            best_val_accuracy = val_acc
            best_epoch = epoch
            epochs_without_improvement = 0
            torch.save(model.gnn.state_dict(), best_ckpt_path)
        else:
            epochs_without_improvement += 1

        torch.save(model.gnn.state_dict(), latest_ckpt)

        done = False
        stop_reason = None
        if epochs_without_improvement >= args.patience:
            done = True
            stop_reason = "patience"
        elif epoch + 1 >= args.max_epochs:
            done = True
            stop_reason = "epoch_cap"

        state = {
            "epoch": epoch,
            "best_val_accuracy": best_val_accuracy,
            "best_epoch": best_epoch,
            "epochs_without_improvement": epochs_without_improvement,
            "val_curve": val_curve,
            "done": done,
            "stop_reason": stop_reason,
        }
        state_path.write_text(json.dumps(state, indent=2))

        if done:
            logger.info("Stopping: %s (best_val_acc=%.4f at epoch %d)", stop_reason, best_val_accuracy, best_epoch)
            break

    # final evaluation using the BEST checkpoint
    model.gnn.load_state_dict(torch.load(best_ckpt_path))
    model.eval()

    if args.final_eval == "full_test_mask":
        test_loader = NeighborLoader(data, num_neighbors=[10, 10], batch_size=args.batch_size, input_nodes=data.test_mask)
        test_acc, n_test = eval_loader(test_loader, model, encoder, text)
        test_desc = f"full test_mask (n={n_test})"
    else:
        splits = np.load(args.split_path)
        eval_idx = splits["eval_idx"]
        eval_mask = torch.zeros(data.num_nodes, dtype=torch.bool, device=data.x.device)
        eval_mask[torch.as_tensor(eval_idx, dtype=torch.long, device=data.x.device)] = True
        test_loader = NeighborLoader(data, num_neighbors=[10, 10], batch_size=args.batch_size, input_nodes=eval_mask)
        test_acc, n_test = eval_loader(test_loader, model, encoder, text)
        test_desc = f"eval_idx only (n={n_test}) -- restricted per user instruction, deviation from original full test_mask evaluation"

    logger.info("Final test accuracy (%s): %.4f", test_desc, test_acc)

    final_ckpt = Path(f"{args.ckpt_prefix}.pt")
    torch.save(model.gnn.state_dict(), final_ckpt)

    summary = {
        "dataset": args.dataset,
        "lr": args.lr,
        "batch_size": args.batch_size,
        "patience": args.patience,
        "max_epochs": args.max_epochs,
        "seed": args.seed,
        "val_curve": val_curve,
        "best_val_accuracy": best_val_accuracy,
        "best_epoch": best_epoch,
        "stop_reason": stop_reason,
        "final_test_accuracy": test_acc,
        "final_test_description": test_desc,
        "final_checkpoint": str(final_ckpt),
    }
    Path(f"{args.ckpt_prefix}_summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
