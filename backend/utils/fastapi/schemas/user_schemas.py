
from typing import Optional

from pydantic import BaseModel, EmailStr, constr

from backend.utils.users import ProjectRole


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    nickname: str
    role: ProjectRole
    email: EmailStr
    password: constr(min_length=6, max_length=8)

    class Config:
        from_attributes = True


class UserDelete(BaseModel):
    nickname: str
    password: str


class UserDTO(BaseModel):
    id: int
    register_date: Optional[str]
    nickname: str
    email: Optional[str]
    role: str
