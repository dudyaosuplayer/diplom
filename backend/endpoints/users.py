from typing import Annotated

from fastapi import APIRouter, Path, Query, HTTPException

from backend.auth_dep import auth_dependencies
from backend.db.database import db_dependencies
from backend.db.queries.user_queries import get_users, get_user_by_username, get_user_by_id, \
    get_task, assign_task_to_user
from backend.models.models import Project, Task
from backend.utils.fastapi.tags import Tags
from backend.utils.fastapi.schemas.user_schemas import User, UserCreate, UserDelete
from backend.utils.fastapi.schemas.task_schemas import TaskSchema


router = APIRouter(prefix='/users', tags=[Tags.users])


@router.get("/get_users", description='This method returns all users')
def get_users(db: db_dependencies,
              skip: Annotated[int | None, Query(title="Number of values to skip",
                                                description="Number of values to skip (from the beginning)")] = 0,
              limit: Annotated[int | None, Query(title="Limit number of entries",
                                                 description="Limit number of entries (100 is optimal)")] = 100):
    try:
        users = get_users(db, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise e


@router.get("/users/get_users/{project_id}", description='This method returns all users from project')
def get_project_users(db: db_dependencies,
                      project_id: int = Path(..., description="The ID of the project")):
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return {"message": "Project not found"}
        users = project.users
        return users
    except Exception as e:
        raise e
    finally:
        db.close()


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
    db_user_username = get_user_by_username(db, username=user.nickname)
    if db_user_username:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)


@router.post("/assign_task", description='This method allows a Product Manager to assign tasks to Developers and Testers.')
def assign_task(task_id: int,
                assigned_user_id: int,  # Список идентификаторов пользователей, которым назначается задача
                db: db_dependencies,
                current_user: auth_dependencies):
    if current_user.role != "Product Manager":
        raise HTTPException(status_code=403, detail="You don't have permission to assign tasks.")
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    user = get_user_by_id(db, assigned_user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with ID {assigned_user_id} not found")
    if user.role not in ["Developer", "Tester"]:
        raise HTTPException(status_code=400, detail=f"User with ID {assigned_user_id} cannot be assigned to a task.")
    # Назначение задачи пользователю
    assign_task_to_user(db, task_id, assigned_user_id)
    # Вернуть обновленную задачу
    return {"detail": f"Task with ID {task_id} assigned to user width ID {assigned_user_id} successful!"}


@router.get("/{user_id}/task", response_model=TaskSchema)
def get_task_for_user(user_id: int, db: db_dependencies):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    task = db.query(Task).filter(Task.user_id == user_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found for this user")
    return task
