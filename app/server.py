import uvicorn
from fastapi import FastAPI

from app import api_router
from core.env import API_V1_STR, APP_PROFILE, SEM_VER

api = FastAPI(
    version=f"v{SEM_VER}",
    openapi_url=f"{API_V1_STR}/openapi.json"
)

api.include_router(api_router, prefix=API_V1_STR)

if __name__ == "__main__":
    uvicorn.run('app.server:api', reload=(APP_PROFILE == "dev"))
