from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Path, HTTPException, status

from backend.auth.auth import auth_dependencies
from backend.db.database import db_dependencies
from backend.models.models import User, Task
from backend.utils.fastapi.schemas.task_schemas import TaskResponse, TaskCreate
from backend.utils.fastapi.tags import Tags
from backend.db.queries.users import get_user_by_id
from backend.db.queries.tasks import get_task_by_project_id, get_task_by_from_project, get_task_by_task_id, \
    assign_task_to_user
from backend.db.queries.projects import get_project_by_id
from utils.statuses import TaskStatus
from utils.users import ProjectRole


router = APIRouter(prefix='/tasks', tags=[Tags.tasks])


@router.get("/get_tasks/{project_id}", description='This method returns all tasks from project')
def get_tasks(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project to extract tasks from", ge=0)],
              db: db_dependencies):
    try:
        tasks = get_task_by_project_id(project_id, db)
        if not tasks:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Comments not found")
        response_tasks = [TaskResponse(id=task.id,
                                       parent_id=task.parent_id,
                                       body=task.body,
                                       task_name=task.task_name,
                                       timestamp=task.timestamp if task.timestamp else datetime.now(),
                                       user_id=task.user_id,
                                       project_id=task.project_id,
                                       status=task.status,
                                       depth=task.depth) for task in tasks]
        return response_tasks
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/get_task/{project_id}/{task_id}", description='This method returns task from project')
def get_task(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project")],
             task_id: Annotated[int, Path(..., title="Task ID", description="The ID of the task")],
             db: db_dependencies):
    try:
        task = get_task_by_from_project(project_id, task_id, db)
        if not task:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Task not found")
        response_task = TaskResponse(id=task.id,
                                     parent_id=task.parent_id,
                                     body=task.body,
                                     task_name=task.task_name,
                                     timestamp=task.timestamp if task.timestamp else datetime.now(),
                                     user_id=task.user_id,
                                     project_id=task.project_id,
                                     status=task.status,
                                     depth=task.depth)
        return response_task
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/get_task/{project_id}/{task_id}", description='This method creates task in project')
def create_task(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project")],
                task_id: Annotated[int, Path(..., title="Task ID", description="The ID of the parent task")],
                task_request: TaskCreate,
                db: db_dependencies):
    try:
        # Проверка существования проекта и задачи
        project_exists = get_project_by_id(project_id, db)
        parent_task_exists = get_task_by_task_id(task_id, db)
        if not project_exists or not parent_task_exists:
            raise HTTPException(status_code=404, detail="Project or parent task not found")
        # Создание новой задачи и добавление ее в базу данных
        new_task = Task(project_id=project_id,
                        parent_id=task_id,
                        body=task_request.body,
                        task_name=task_request.task_name)
                        # Другие поля задачи, которые необходимо заполнить
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        # Создание объекта TaskResponse из новой задачи и возвращение его в качестве ответа
        response_task = TaskResponse(id=new_task.id,
                                     parent_id=new_task.parent_id,
                                     body=new_task.body,
                                     task_name=new_task.task_name,
                                     timestamp=new_task.timestamp,
                                     user_id=new_task.user_id,
                                     project_id=new_task.project_id,
                                     status=new_task.status,
                                     depth=new_task.depth)
        return response_task
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/assign_task", description='This method allows a Product Manager to assign tasks to Developers and Testers.')
def assign_task(task_id: int,
                assigned_user_id: int,
                db: db_dependencies,
                current_user: auth_dependencies):
    if current_user.role != ProjectRole.ProductManager:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to assign tasks.")
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Task not found")
    user = get_user_by_id(db, assigned_user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with ID {assigned_user_id} not found")
    if user.role not in [ProjectRole.Developer, ProjectRole.Tester]:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"User with ID {assigned_user_id} cannot be assigned to a task.")
    assign_task_to_user(db, task_id, assigned_user_id)
    return {"detail": f"Task with ID {task_id} assigned to user width ID {assigned_user_id} successful!"}


@router.get("/{user_id}/task", response_model=TaskResponse)
def get_task_for_user(user_id: int, db: db_dependencies):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    task = get_task_for_user(user_id, db)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found for this user")
    return task
