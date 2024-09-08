from typing import Any

from litestar import Controller, post
from litestar.di import Provide

from app.dependencies import model_dependencie, tokenizer_dependencie
from app.services import AssistService
from app.schemas import Request, Responce


class Assist(Controller):
    """Class for routing and dependencies providing"""

    path = "/assist"
    @post()
    async def generate_tlite_answer(
        self, model: Any, tokenizer: Any, data: Request 
    ) -> Responce:
        """Request processing"""
        return Responce(AssistService(model, tokenizer).assist(data))
