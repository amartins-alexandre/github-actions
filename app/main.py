from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import sessionmanager
from .core import config
from .domain.routers import api_router


def init_api(init_db=True) -> FastAPI:
    lifespan = None

    if init_db:
        sessionmanager.init(config.DB_HOST_STRING)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if sessionmanager.engine is not None:
                await sessionmanager.close()

    api = FastAPI(
        version=f"v{config.SEM_VER}",
        openapi_url=f"{config.API_V1_STR}/openapi.json",
        lifespan=lifespan
    )

    api.include_router(api_router, prefix=config.API_V1_STR, tags=["user"])

    return api


api = init_api()
