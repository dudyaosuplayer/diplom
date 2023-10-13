from fastapi import APIRouter, Depends, Path, Query

from backend.utils.fastapi.tags import Tags


router = APIRouter()


@router.get("/tasks/get_tasks/{project_id}",
         description='This method returns all tasks from project',
         tags=[Tags.tasks])
def get_tasks(project_id: str = Path()):
    try:
        # TODO get tasks from project
        tasks = ''
        return tasks
    except Exception as e:
        raise e


@router.get("/tasks/get_task/{project_id}/{task_id}",
         description='This method returns task from project',
         tags=[Tags.tasks])
def get_task(project_id: str = Path(),
             task_id: str = Path()):
    try:
        # TODO get task from project
        tasks = ''
        return tasks
    except Exception as e:
        raise e


@router.post("/tasks/get_task/{project_id}/{task_id}",
         description='This method creates task in project',
         tags=[Tags.tasks])
def create_tasks(project_id: str = Path(),
                 task_id: str = Path()):
    try:
        # TODO create task in project
        tasks = ''
        return tasks
    except Exception as e:
        raise e
