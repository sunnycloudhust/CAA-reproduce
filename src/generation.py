"""Generate baseline and activation-steered responses."""

from __future__ import annotations

from typing import Any

import torch

from .model_utils import find_transformer_layers
from .steering import hidden_state_from_output


def generate(
    model: torch.nn.Module,
    tokenizer: Any,
    prompt: str,
    max_new_tokens: int,
    steering_vector: torch.Tensor | None = None,
    layer: int = 0,
    alpha: float = 0.0,
) -> str:
    encoded = tokenizer(prompt, return_tensors="pt").to(model.device)
    handle = None
    if steering_vector is not None and alpha != 0:
        layers = find_transformer_layers(model)

        def steer(module: torch.nn.Module, inputs: tuple[Any, ...], output: Any) -> Any:
            del module, inputs
            hidden = hidden_state_from_output(output).clone()
            hidden[:, -1, :] += alpha * steering_vector.to(hidden.device, hidden.dtype)
            if isinstance(output, tuple):
                return (hidden, *output[1:])
            return hidden

        handle = layers[layer].register_forward_hook(steer)
    try:
        with torch.no_grad():
            generated = model.generate(
                **encoded,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )
    finally:
        if handle is not None:
            handle.remove()
    return tokenizer.decode(generated[0], skip_special_tokens=True)
