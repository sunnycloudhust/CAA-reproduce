"""Build activation steering vectors from preference pairs."""

from __future__ import annotations

from typing import Any

import torch
from tqdm import tqdm

from .model_utils import find_transformer_layers


def hidden_state_from_output(output: Any) -> torch.Tensor:
    return output[0] if isinstance(output, tuple) else output


def last_token_hidden(
    model: torch.nn.Module,
    tokenizer: Any,
    text: str,
    layer: int,
) -> torch.Tensor:
    encoded = tokenizer(text, return_tensors="pt").to(model.device)
    captured: list[torch.Tensor] = []

    def capture(module: torch.nn.Module, inputs: tuple[Any, ...], output: Any) -> Any:
        del module, inputs
        captured.append(hidden_state_from_output(output)[:, -1, :].detach())
        return output

    handle = find_transformer_layers(model)[layer].register_forward_hook(capture)
    try:
        with torch.no_grad():
            model(**encoded, use_cache=False)
    finally:
        handle.remove()
    return captured[0].squeeze(0)


def build_steering_vector(
    model: torch.nn.Module,
    tokenizer: Any,
    pairs: list[dict[str, str]],
    layer: int,
) -> torch.Tensor:
    differences = []
    for pair in tqdm(pairs, desc="Building steering vector"):
        positive = last_token_hidden(model, tokenizer, pair["positive"], layer)
        negative = last_token_hidden(model, tokenizer, pair["negative"], layer)
        differences.append(positive - negative)
    vector = torch.stack(differences).mean(dim=0)
    return vector / vector.norm().clamp_min(1e-8)
