from typing import List, Annotated

from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import UserOutput, UserInput, UserUpdatedOutput
from .service import UserService
from ...core.database import get_db

user_router = APIRouter(prefix='/user')
service = UserService()


@user_router.get('/',
                 response_model=List[UserOutput],
                 status_code=status.HTTP_200_OK,
                 description='List all users')
async def list_users(db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        return await service.find(db)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))


@user_router.get('/{user_id}',
                 response_model=UserOutput,
                 status_code=status.HTTP_200_OK,
                 description='Get user by id')
async def get_by_id(user_id: UUID4, db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        return await service.find_by(user_id, db)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))


@user_router.post('/',
                  response_model=None,
                  status_code=status.HTTP_201_CREATED,
                  description='Create a new user')
async def add_new_user(user: UserInput, db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        await service.create(user, db)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))


@user_router.put('/{user_id}',
                 response_model=UserUpdatedOutput,
                 status_code=status.HTTP_200_OK,
                 description='Update user')
async def update_user(user_id: UUID4, user: UserInput, db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        return await service.update(user_id, user, db)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))
