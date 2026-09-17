"""Compare baseline generation with activation steering."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tqdm import tqdm
from transformers import set_seed

from .data import load_hh_rlhf_data
from .generation import generate
from .model_utils import find_transformer_layers, load_causal_lm
from .steering import build_steering_vector


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="sshleifer/tiny-gpt2")
    parser.add_argument("--layer", type=int, default=0)
    parser.add_argument("--alpha", type=float, default=2.0)
    parser.add_argument("--max-new-tokens", type=int, default=80)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--dataset", default="Anthropic/hh-rlhf")
    parser.add_argument("--dataset-split", default="train")
    parser.add_argument("--max-contrast", type=int, default=64)
    parser.add_argument("--max-eval", type=int, default=16)
    parser.add_argument("--output-file", type=Path, default=Path("results/comparison.jsonl"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    set_seed(args.seed)
    tokenizer, model = load_causal_lm(args.model)

    layers = find_transformer_layers(model)
    if not 0 <= args.layer < len(layers):
        raise ValueError(f"layer must be between 0 and {len(layers) - 1}")
    contrast_pairs, eval_items = load_hh_rlhf_data(
        args.dataset,
        args.dataset_split,
        args.max_contrast,
        args.max_eval,
    )
    vector = build_steering_vector(model, tokenizer, contrast_pairs, args.layer)

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    with args.output_file.open("w") as output:
        for item in tqdm(eval_items, desc="Running evaluation"):
            prompt = item["prompt"]
            row = {
                "prompt": prompt,
                "model": args.model,
                "layer": args.layer,
                "alpha": args.alpha,
                "base": generate(model, tokenizer, prompt, args.max_new_tokens),
                "steered": generate(
                    model,
                    tokenizer,
                    prompt,
                    args.max_new_tokens,
                    vector,
                    args.layer,
                    args.alpha,
                ),
            }
            output.write(json.dumps(row) + "\n")
    print(f"Saved {args.output_file}")


if __name__ == "__main__":
    main()
