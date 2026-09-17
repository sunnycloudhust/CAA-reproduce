"""Utilities for loading models and locating transformer layers."""

from __future__ import annotations

from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def find_transformer_layers(model: torch.nn.Module) -> torch.nn.ModuleList:
    candidates = [
        getattr(getattr(model, "transformer", None), "h", None),
        getattr(getattr(model, "model", None), "layers", None),
        getattr(getattr(model, "transformer", None), "layers", None),
    ]
    for layers in candidates:
        if isinstance(layers, torch.nn.ModuleList):
            return layers
    raise ValueError("Could not find transformer layers for this model architecture")


def load_causal_lm(model_name: str) -> tuple[Any, torch.nn.Module]:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=dtype).to(device)
    model.eval()
    return tokenizer, model
