from litestar import Controller, get
from litestar.di import Provide
from transformers import AutoTokenizer, AutoModelForCausalLM

from app.dependencies import model_dependencie, tokenizer_dependencie
from app.services import AssistService
from app.schemas import Request, Responce


class Assist(Controller):
    """Class for routing and dependencies providing"""

    path = "/assist"
    dependencies = {
        "model": Provide(model_dependencie),
        "tokenizer": Provide(tokenizer_dependencie),
    }

    @get()
    async def list_form_populations(
        self, model: AutoModelForCausalLM, tokenizer: AutoTokenizer, query: Request 
    ) -> Responce:
        """Request processing"""
        return AssistService(model, tokenizer).assist(query)
