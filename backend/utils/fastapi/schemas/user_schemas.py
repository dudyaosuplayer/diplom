from pydantic import BaseModel, constr

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    nickname: str
    role: str
    email: str
    password: constr(min_length=6, max_length=8)

    class Config:
        from_attributes = True


class UserDelete(BaseModel):
    nickname: str
    password: str