from typing import List

from fastapi import APIRouter, status, HTTPException
from pydantic import UUID4

from .schema import UserOutput, UserInput, UserUpdatedOutput
from .service import UserService

user_router = APIRouter(prefix='/user')
service = UserService()


@user_router.get('/',
                 response_model=List[UserOutput],
                 status_code=status.HTTP_200_OK,
                 description='List all users')
async def list_users():
    try:
        return await service.find()
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))


@user_router.get('/{user_id}',
                 response_model=UserOutput,
                 status_code=status.HTTP_200_OK,
                 description='Get user by id')
async def get_by_id(user_id: UUID4):
    try:
        return await service.find_by(user_id)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))


@user_router.post('/',
                  response_model=None,
                  status_code=status.HTTP_201_CREATED,
                  description='Create a new user')
async def add_new_user(user: UserInput):
    try:
        await service.create(user)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))


@user_router.put('/{user_id}',
                 response_model=UserUpdatedOutput,
                 status_code=status.HTTP_200_OK,
                 description='Update user')
async def update_user(user_id: UUID4, user: UserInput):
    try:
        return await service.update(user_id, user)
    except Exception as ex:
        raise HTTPException(400, detail=str(ex))
