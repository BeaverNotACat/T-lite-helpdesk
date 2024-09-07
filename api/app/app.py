from litestar import Litestar, MediaType, Request, Response
from litestar.exceptions import HTTPException, ValidationException
from litestar.di import Provide
from litestar.config.cors import CORSConfig

from app.state import model_setup, tokenizer_setup
from app.dependencies import model_dependencie, tokenizer_dependencie
from app.routes import Assist


def validation_exception_handler(
    request: Request, exc: ValidationException
) -> Response:
    """Make validation error as it was decribed in contract"""
    return Response(
        media_type=MediaType.TEXT,
        content=f"""
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "{exc.detail}",
      "type": "{exc}"
    }
  ]
}
        """,
        status_code=422,
    )


cors_config = CORSConfig(allow_origins=["*"])

app = Litestar(
    lifespan=[model_setup, tokenizer_setup],
    dependencies={
        "model": Provide(model_dependencie),
        "tokenizer": Provide(tokenizer_dependencie),
    },
    route_handlers=[Assist],
    cors_config=cors_config,
)
