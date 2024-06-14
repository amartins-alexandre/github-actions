import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, MetaData, UUID, text
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema='fastapi')
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = 'user'

    id: uuid = Column(UUID(), primary_key=True, server_default=text("gen_random_uuid()"))
    name: str = Column(String(50))
    email: str = Column(String(50), unique=True, index=True)
    created_at: datetime = Column(DateTime, default=datetime.now())
    updated_at: datetime = Column(DateTime, onupdate=datetime.now(), server_onupdate=text("now()"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
