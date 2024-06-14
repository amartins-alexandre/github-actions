from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.main import api_router
from src.main.core import config
from src.main.core.config import API_V1_STR, APP_PROFILE, SEM_VER
from src.main.core.database import sessionmanager


def init_app(init_db=True):
    lifespan = None

    if init_db:
        sessionmanager.init(config.DB_URL_CONFIG)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if sessionmanager.engine is not None:
                await sessionmanager.close()

    api = FastAPI(
        version=f"v{SEM_VER}",
        openapi_url=f"{API_V1_STR}/openapi.json",
        lifespan=lifespan
    )

    api.include_router(api_router, prefix=API_V1_STR, tags=["user"])

    return api


if __name__ == "__main__":
    uvicorn.run('src.main.server:init_app', reload=(APP_PROFILE == "dev"))
