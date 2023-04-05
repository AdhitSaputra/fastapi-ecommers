from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Column, DateTime, SQLModel, Field, String, Relationship
from sqlalchemy_utils import ChoiceType

from models.base import BaseUUIDModel
from schemas.common_schema import IGenderEnum


class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: EmailStr = Field(
        nullable=True, index=True, sa_column_kwargs={"unique": True}
    )
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=True)
    birthdate: datetime | None = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    role_id: UUID | None = Field(default=None, foreign_key="Role.id")
    phone: str | None
    gender: IGenderEnum | None = Field(
        default=IGenderEnum.other,
        sa_column=Column(ChoiceType(IGenderEnum, impl=String()))
    )
    state: str | None
    country: str | None
    address: str | None

class User(BaseUUIDModel, UserBase, table=True):
    hashed_password: str | None = Field(nullable=False, index=True)
    role: Optional["Role"] = Relationship(
        back_populates="users",
        sa_relationship_kwargs={"lazy": "joined"}
    )