from fastapi import APIRouter

from app.main.domain.user.routes import user_router

api_router = APIRouter()

api_router.include_router(user_router)
