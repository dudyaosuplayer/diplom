from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Path, HTTPException, status, Query

from backend.auth.auth import auth_dependencies
from backend.db.database import db_dependencies
from backend.models.models import User, Task
from backend.utils.fastapi.schemas.task_schemas import TaskResponse, TaskCreate
from backend.utils.fastapi.tags import Tags
from backend.db.queries.users import get_user_by_id
from backend.db.queries.tasks import get_tasks_by_project_id, get_task_by_from_project, get_task_by_task_id, \
    assign_task_to_user, get_tasks_by_user_in_project
from backend.db.queries.projects import get_project_by_id
from utils.statuses import TaskStatus
from utils.users import ProjectRole


router = APIRouter(prefix='/tasks', tags=[Tags.tasks])


@router.get("/get_tasks/{project_id}", description='This method returns all tasks from project')
def get_tasks(db: db_dependencies,
              project_id: int = Path(..., title="Project ID", description="The ID of the project to extract tasks from", ge=0)):
    try:
        tasks = get_tasks_by_project_id(project_id, db)
        if not tasks:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Tasks not found")
        response_tasks = [TaskResponse(id=task.id,
                                       parent_id=task.parent_id,
                                       body=task.body,
                                       task_name=task.task_name,
                                       timestamp=task.timestamp if task.timestamp else datetime.now(),
                                       user_id=task.user_id,
                                       project_id=task.project_id,
                                       status=task.status) for task in tasks]
        return response_tasks
    except Exception as e:
        raise e


@router.get("/get_task/{project_id}/{task_id}", description='This method returns task from project')
def get_task(db: db_dependencies, current_user: auth_dependencies,
             project_id: int = Path(..., title="Project ID", description="The ID of the project"),
             task_id: int = Path(..., title="Task ID", description="The ID of the task")):
    try:
        if User.role != ProjectRole.ProductManager:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Product Manager can create a task")
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
                                     status=task.status)
        return response_task
    except Exception as e:
        raise e


@router.post("/get_task/{project_id}/{task_id}/{task_name}", description='This method creates task in project')
def create_task(user_id: int,
                task_status: TaskStatus,
                db: db_dependencies,
                body: Optional[str] = Query(None),
                task_name: str = Path(..., title="Task Name", description="Name of the task to retrieve", max_length=150),
                project_id: int = Path(..., title="Project ID", description="The ID of the project"),
                parent_id: Optional[int] = Query(None, title="Parent ID", description="The ID of the parent task")):
    try:
        project_exists = get_project_by_id(project_id, db)
        parent_task_exists = get_task_by_task_id(parent_id, db)
        if not project_exists:
            raise HTTPException(status_code=404, detail="Project not found")
        if parent_id and not parent_task_exists:
            raise HTTPException(status_code=404, detail="Parent task not found")
        new_task = Task(body=body,
                        task_name=task_name,
                        timestamp=datetime.now(),
                        user_id=user_id,
                        project_id=project_id,
                        status=TaskStatus.Postponed)
        if task_status:
            new_task.status = task_status
        if parent_id:
            new_task.parent_id = parent_id
        db.add(new_task)
        db.commit()
        return {"message": "Task was created successfully"}
    except Exception as e:
        raise e


@router.post("/assign_task", description='This method allows a Product Manager to assign tasks to Developers and Testers.')
def assign_task(db: db_dependencies, current_user: auth_dependencies,
                task_id: int = Query(..., title="Task ID", description="The ID of the task"),
                assigned_user_id: int = Query(..., title="Task ID", description="The ID of the task")):
    try:
        if current_user.role != ProjectRole.ProductManager:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to assign tasks.")
        task = get_task_by_task_id(task_id, db)
        if task is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Task not found")
        user = get_user_by_id(db, assigned_user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with ID {assigned_user_id} not found")
        if user.role not in [ProjectRole.Developer, ProjectRole.Tester]:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"User with ID {assigned_user_id} cannot be assigned to a task.")
        if assign_task_to_user(task_id, assigned_user_id, db):
            return {"detail": f"Task with ID {task_id} assigned to user with ID {assigned_user_id} successfuly"}
    except Exception as e:
        raise e


@router.get("/{user_id}/{project_id}", description='This method returns all tasks in project assigned to user')
def get_tasks_for_user(project_id: int, user_id: int, db: db_dependencies):
    try:
        user = get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not found")
        project = get_project_by_id(project_id, db)
        if not project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Porject not found")
        tasks = get_tasks_by_user_in_project(project_id, user_id, db)
        if not tasks:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Tasks not found for this user")
        return tasks
    except Exception as e:
        raise e


@router.patch("/change_task_status")
def change_task_status(task_status: TaskStatus, db: db_dependencies,
                       task_id: int = Query(..., title="Task ID", description="The ID of the task")):
    try:
        task = get_task_by_task_id(task_id, db)
        if not task:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Task not found for this user")
        task.status = task_status
        db.commit()
        return {"message": "Task was updated succesfully"}
    except Exception as e:
        raise e
