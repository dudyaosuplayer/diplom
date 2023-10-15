from typing import List

from fastapi import APIRouter, Path, Query, HTTPException, status

from backend.auth.auth import auth_dependencies
from backend.db.database import db_dependencies
from backend.db.queries.projects import get_project_by_id
from backend.db.queries.users import get_all_users, get_user_by_id, get_user_by_username, create_new_user
from backend.utils.fastapi.tags import Tags
from backend.utils.fastapi.schemas.user_schemas import UserCreate, UserDTO
from backend.utils.users import ProjectRole


router = APIRouter(prefix='/users', tags=[Tags.users])


@router.get("/get_users", response_model=List[UserDTO], description='This method returns all users')
def get_users(db: db_dependencies,
              skip: int | None = Query(0, title="Number of values to skip", description="Number of values to skip (from the beginning)"),
              limit: int | None = Query(100, title="Limit number of entries", description="Limit number of entries (100 is optimal)")):
    try:
        users = get_all_users(db, skip=skip, limit=limit)
        user_dtos = [UserDTO(id=user.id,
                             register_date=user.register_date,
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
        project = get_project_by_id(project_id, db)
        if not project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
        users = project.users
        user_dtos = [UserDTO(id=user.id,
                             register_date=user.register_date,
                             nickname=user.nickname,
                             email=user.email,
                             role=user.role) for user in users]
        return user_dtos
    except Exception as e:
        raise e


@router.post("/create_user", description='This method creates user')
def create_user(user: UserCreate, db: db_dependencies):
    try:
        db_user_username = get_user_by_username(db, username=user.nickname)
        if db_user_username:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Username already registered")
        create_new_user(db=db, user=user)
        return {"message": "User was created successfully"}
    except Exception as e:
        raise e


@router.post("/add_user_to_project", description='Add user to project')
def add_user_to_project(db: db_dependencies,
                        current_user: auth_dependencies,
                        project_id: int = Query(..., description="The ID of the project"),
                        user_id: int = Query(..., description="The ID of the user")):
    try:
        if current_user.role != ProjectRole.ProductManager:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Permission denied. You must be a Product Manager to add users to a project.")
        project = get_project_by_id(project_id, db)
        user = get_user_by_id(db, user_id)
        if not project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not found")
        existing_users_in_project = [user.id for user in project.users]
        if user_id in existing_users_in_project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already attached to this project")
        project.users.append(user)
        db.commit()
        return {"message": "User added to project successfully"}
    except Exception as e:
        raise e


@router.get("/get_users/{project_id}", description='Get users attached to a project')
def get_users_attached_to_project(db: db_dependencies,
                                  project_id: int = Path(..., description="The ID of the project")):
    try:
        project = get_project_by_id(project_id, db)
        if not project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
        users = project.users
        return users
    except Exception as e:
        raise e
