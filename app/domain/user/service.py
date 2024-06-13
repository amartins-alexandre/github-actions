from pydantic import UUID4
from sqlalchemy.future import select

from sqlalchemy import update
from typing import List

from app.core.database import PGConnection
from .model import User
from .schema import UserInput


class UserService:
    def __init__(self):
        self.async_session = PGConnection().get_session()

    async def create(self, user_input: UserInput) -> None:
        async with self.async_session() as session:
            user = User(**user_input.dict())

            if await self.find_by_name(user.name):
                raise Exception(f"User with name {user.name} already exists")

            session.add(user)
            await session.commit()

    async def find(self) -> List[User]:
        async with self.async_session() as session:
            users = await session.execute(select(User))
            return users.scalars().all()

    async def find_by(self, user_id: UUID4) -> User:
        async with self.async_session() as session:
            query = select(User).where(User.id == user_id)
            user = await session.execute(query)
            return user.scalar()

    async def find_by_name(self, name: str) -> User:
        async with self.async_session() as session:
            query = select(User).where(User.name == name)
            user = await session.execute(query)
            return user.scalar()

    async def update(self, user_id: UUID4, user: UserInput) -> User:
        async with self.async_session() as session:
            user_found = await self.find_by(user_id)

            if not user_found:
                raise Exception(f"User with id {user_id} not found")

            user_found = User(**user.dict())

            query = update(User).where(User.id == user_id).values(name=user.name, email=user.email)
            await session.execute(query)
            await session.commit()
            return user_found
