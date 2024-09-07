from litestar import Litestar
from litestar.di import Provide
from litestar.config.cors import CORSConfig

from app.state import model_setup, tokenizer_setup
from app.dependencies import model_dependencie, tokenizer_dependencie
from app.routes import Assist


cors_config = CORSConfig(allow_origins=["*"])

app = Litestar(
    lifespan=[model_setup, tokenizer_setup],
    dependencies = {
        "model": Provide(model_dependencie),
        "tokenizer": Provide(tokenizer_dependencie)
    },
    route_handlers=[Assist],
    cors_config=cors_config,
)
