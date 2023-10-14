from pydantic import BaseModel


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
