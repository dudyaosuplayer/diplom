from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Path, HTTPException

from backend.db.database import db_dependencies
from backend.models.models import Task, Project
from backend.utils.fastapi.schemas.task_schemas import TaskResponse, TaskCreate
from backend.utils.fastapi.tags import Tags

router = APIRouter(prefix='/tasks', tags=[Tags.tasks])


@router.get("/tasks/get_tasks/{project_id}",
            description='This method returns all tasks from project',
            tags=[Tags.tasks])
def get_tasks(project_id: Annotated[
    int, Path(..., title="Project ID", description="The ID of the project to extract tasks from", ge=0)],
              db: db_dependencies):
    try:
        tasks = db.query(Task).filter(Task.project_id == project_id).all()
        if not tasks:
            raise HTTPException(status_code=404, detail="Comments not found")
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
        raise e


@router.get("/tasks/get_task/{project_id}/{task_id}",
            description='This method returns task from project',
            tags=[Tags.tasks])
def get_task(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project")],
             task_id: Annotated[int, Path(..., title="Task ID", description="The ID of the task")],
             db: db_dependencies):
    try:
        task = db.query(Task).filter(Task.project_id == project_id, Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
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
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tasks/create_task/{project_id}/{task_id}",
             description='This method creates task in project',
             tags=[Tags.tasks])
def create_task(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project")],
                task_id: Annotated[int, Path(..., title="Task ID", description="The ID of the parent task")],
                task_request: TaskCreate,
                db: db_dependencies):
    try:
        # Проверка существования проекта и задачи
        project_exists = db.query(Project).filter(Project.id == project_id).first()
        parent_task_exists = db.query(Task).filter(Task.id == task_id).first()
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
        raise HTTPException(status_code=500, detail=str(e))
