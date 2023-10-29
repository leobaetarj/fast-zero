from fastapi import FastAPI

from src.application import endpoints
from src.application.containers import Container


def create_app() -> FastAPI:
    container = Container()
    # container.config.giphy.api_key.from_env("GIPHY_API_KEY") # example config

    fast_api = FastAPI()
    fast_api.container = container
    fast_api.include_router(endpoints.router)

    return fast_api


app = create_app()
