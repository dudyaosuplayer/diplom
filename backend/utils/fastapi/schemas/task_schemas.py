from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    parent_id: int
    body: str
    task_name: str
    timestamp: Optional[datetime] = None
    user_id: Optional[int] = None
    project_id: int
    status: Optional[str] = None
    depth: Optional[int] = None


class TaskCreate(BaseModel):
    body: str
    task_name: str
    timestamp: Optional[datetime] = None
    user_id: Optional[int] = None
    project_id: int
    status: Optional[str] = None
    depth: Optional[int] = None

