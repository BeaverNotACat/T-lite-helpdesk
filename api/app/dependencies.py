from typing import Any

from litestar.datastructures import State
from transformers import AutoTokenizer, AutoModelForCausalLM

async def model_dependencie(state: State) -> Any:
    """Recieve model object from application state"""
    model = getattr(state, "model", None)
    if model is None:
        raise ValueError("Model is not in state")
    return model


async def tokenizer_dependencie(state: State) -> Any:
    """Recieve tokenizer object from application state"""
    tokenizer = getattr(state, "tokenizer", None)
    if tokenizer is None:
        raise ValueError("Tokenizer is not in state")
    return tokenizer
