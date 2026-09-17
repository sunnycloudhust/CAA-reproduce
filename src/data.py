"""Load and prepare HH-RLHF examples."""

from __future__ import annotations

from typing import Any

def prompt_from_conversation(conversation: str) -> str:
    marker = "\n\nAssistant:"
    if marker not in conversation:
        return conversation
    return conversation.rsplit(marker, 1)[0] + marker


def load_hh_rlhf_data(
    dataset_name: str,
    split: str,
    max_contrast: int,
    max_eval: int,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    from datasets import load_dataset

    dataset = load_dataset(dataset_name, split=split)
    contrast_rows = dataset.select(range(min(max_contrast, len(dataset))))
    eval_rows = dataset.select(range(min(max_eval, len(dataset))))
    contrast = [
        {"positive": row["chosen"], "negative": row["rejected"]}
        for row in contrast_rows
    ]
    evaluation = [{"prompt": prompt_from_conversation(row["chosen"])} for row in eval_rows]
    return contrast, evaluation
