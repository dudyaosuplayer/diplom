from datetime import datetime

from pydantic import BaseModel


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
