from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import Litestar
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "t-bank-ai/T-lite-instruct-0.1"


@asynccontextmanager
async def model_setup(app: Litestar) -> AsyncGenerator[None, None]:
    """Add model object to application state"""
    model = getattr(app.state, "model", None)
    if model is None:
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
        app.state.assess_model = model
    try:
        yield
    finally:
        ...


@asynccontextmanager
async def tokenizer_setup(app: Litestar) -> AsyncGenerator[None, None]:
    """Add tokenizer object to application state"""
    model = getattr(app.state, "tokenizer", None)
    if model is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        app.state.assess_model = tokenizer
    try:
        yield
    finally:
        ...
