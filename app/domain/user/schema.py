from datetime import datetime

from pydantic import BaseModel, UUID4, field_validator


def normalize_datetime_usa(dt: datetime | None) -> str | None:
    return dt.strftime('%Y-%d-%m %H:%M:%S') if isinstance(dt, datetime) else None


def normalize(name: str) -> str:
    return ' '.join((word.capitalize()) for word in name.split(' '))


class UserBase(BaseModel):
    id: UUID4


class UserUpdatedOutput(UserBase):
    name: str
    email: str

    _normalize_name = field_validator('name')(normalize)


class UserOutput(UserUpdatedOutput):
    created_at: datetime
    updated_at: datetime | None

    _normalize_created_at = field_validator('created_at')(normalize_datetime_usa)
    _normalize_updated_at = field_validator('updated_at')(normalize_datetime_usa)

    class Config:
        from_attributes = True


class UserInput(BaseModel):
    name: str
    email: str

    _normalize_name = field_validator('name')(normalize)
