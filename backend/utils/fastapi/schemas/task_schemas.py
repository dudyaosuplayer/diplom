from datetime import datetime

from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    parent_id: int
    body: str
    task_name: str
    timestamp: datetime
    user_id: int
    project_id: int
    status: str
    depth: int


class TaskCreate(BaseModel):
    parent_id: int
    body: str
    task_name: str
    timestamp: datetime
    user_id: int
    project_id: int
    status: str
    depth: int

