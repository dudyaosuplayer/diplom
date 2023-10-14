from typing import Annotated, List

from fastapi import APIRouter, Path, Query, HTTPException

from backend.auth.auth import auth_dependencies
from backend.db.database import db_dependencies
from backend.db.queries import users as users_q

from backend.models.models import Project
from backend.utils.fastapi.tags import Tags
from backend.utils.fastapi.schemas.user_schemas import User, UserCreate, UserDelete, UserDTO

router = APIRouter(prefix='/users', tags=[Tags.users])


# @router.get("/get_users", description='This method returns all users')
# def get_users(db: db_dependencies,
#               skip: Annotated[int | None, Query(title="Number of values to skip",
#                                                 description="Number of values to skip (from the beginning)")] = 0,
#               limit: Annotated[int | None, Query(title="Limit number of entries",
#                                                  description="Limit number of entries (100 is optimal)")] = 100):
#     try:
#         users = users_q.get_users(db, skip=skip, limit=limit)
#         return users
#     except Exception as e:
#         raise e


@router.get("/get_users", response_model=List[UserDTO], description='This method returns all users')
def get_users(
              db: db_dependencies,
              skip: int = 0,
              limit: int = 100):
    try:
        users = users_q.get_users(db, skip=skip, limit=limit)
        # Преобразуйте результат из ORM модели в DTO
        user_dtos = [UserDTO
                     (id=user.id,
                      register_date=str(user.register_date),  # или любой другой формат для даты
                      nickname=user.nickname,
                      email=user.email,
                      role=user.role) for user in users]
        return user_dtos
    except Exception as e:
        raise e


@router.get("/get_users/{project_id}", response_model=List[UserDTO], description='This method returns all users from project')
def get_project_users(db: db_dependencies,
                      credentials: auth_dependencies,
                      project_id: int = Path(..., description="The ID of the project")):
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return {"message": "Project not found"}
        users = project.users
        user_dtos = [UserDTO
                     (id=user.id,
                      register_date=str(user.register_date),  # или любой другой формат для даты
                      nickname=user.nickname,
                      email=user.email,
                      role=user.role) for user in users]
        return user_dtos
    except Exception as e:
        raise e
    finally:
        db.close()


# @router.get("/get_users/{project_id}", description='This method returns all users from project')
# def get_project_users(db: db_dependencies,
#                       credentials: auth_dependencies,
#                       project_id: int = Path(..., description="The ID of the project")):
#     try:
#         project = db.query(Project).filter(Project.id == project_id).first()
#         if not project:
#             return {"message": "Project not found"}
#         users = project.users
#         return users
#     except Exception as e:
#         raise e
#     finally:
#         db.close()


@router.post("/create_user", description='This method creates user')
def create_user(user: UserCreate, db: db_dependencies):
    """
    Create a new user.

    Parameters:
    - **user** (UserCreate): User data to create.
    - **db** (db_dependencies): Dependency to obtain a database session.

    Returns:
        User: The created user object.

    Possible Errors:
        HTTP 400: Email already registered.
        HTTP 400: Username already registered.
    """
    db_user_username = users_q.get_user_by_username(db, username=user.nickname)
    if db_user_username:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)
