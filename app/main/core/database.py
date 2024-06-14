from uuid import uuid4

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .env import DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME


class Connection:
    def __init__(self):
        self.db_user = DB_USER
        self.db_pwd = DB_PWD
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_name = DB_NAME

    def get_session(self):
        engine = create_async_engine(
            f'postgresql+asyncpg://{self.db_user}:{self.db_pwd}@{self.db_host}:{self.db_port}/{self.db_name}',
            connect_args={
                'prepared_statement_name_func': lambda: f'__asyncpg_{uuid4()}__',
            },
        )

        return sessionmaker(engine, class_=AsyncSession)
