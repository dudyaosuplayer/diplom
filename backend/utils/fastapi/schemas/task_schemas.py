from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    body: str
    task_name: str
    user_id: int
    project_id: int
    status: str