from typing import Sequence

from pydantic import UUID4
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .model import User
from .schema import UserInput


class UserService:

    @classmethod
    async def create(cls, user_input: UserInput, session: AsyncSession) -> None:
        user = User(**user_input.dict())

        if await cls.find_by_name(user.name, session):
            raise Exception(f"User with name {user.name} already exists")

        session.add(user)
        await session.commit()

    @classmethod
    async def find(cls, session: AsyncSession) -> Sequence[User]:
        users = await session.execute(select(User))
        return users.scalars().all()

    @classmethod
    async def find_by(cls, user_id: UUID4, session: AsyncSession) -> User:
        query = select(User).where(User.id == user_id)
        user = await session.execute(query)
        return user.scalar()

    @classmethod
    async def find_by_name(cls, name: str, session: AsyncSession) -> User:
        query = select(User).where(User.name == name)
        user = await session.execute(query)
        return user.scalar()

    @classmethod
    async def update(cls, user_id: UUID4, user_input: UserInput, session: AsyncSession) -> User:
        if not await cls.find_by(user_id, session):
            raise Exception(f"User with id {user_id} not found")

        query = update(User).where(User.id == user_id).values(**user_input.dict())
        await session.execute(query)
        await session.commit()
        return await cls.find_by(user_id, session)
