from typing import Any

from litestar import Controller, get
from litestar.di import Provide

from app.dependencies import model_dependencie, tokenizer_dependencie
from app.services import AssistService
from app.schemas import Request, Responce


class Assist(Controller):
    """Class for routing and dependencies providing"""

    path = "/assist"
    @get()
    async def list_form_populations(
        self, model: Any, tokenizer: Any, query: Request 
    ) -> Responce:
        """Request processing"""
        return AssistService(model, tokenizer).assist(query)
