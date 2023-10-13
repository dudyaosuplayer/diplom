from datetime import datetime
from pydantic import BaseModel, constr


class ProjectCreate(BaseModel):
    name: str
    status: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    status: str


class ProjectUpdate(BaseModel):
    name: str
    status: str


class CommentResponse(BaseModel):
    id: int
    user_id: int
    task_id: int
    timestamp: datetime
    text: str


class CommentCreate(BaseModel):
    user_id: int
    task_id: int
    timestamp: datetime
    text: str

class UserCreate(BaseModel):
    nickname: str
    role: str
    password: constr(min_length=6, max_length=8)

    class Config:
        from_attributes = True


class UserDelete(BaseModel):
    nickname: str
    password: str


class Task(BaseModel):
    id: int
    body: str
    task_name: str
    user_id: int
    project_id: int
    status: str

