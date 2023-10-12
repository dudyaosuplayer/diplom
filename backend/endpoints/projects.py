from fastapi import APIRouter, Depends, Path, Query

from utils.fastapi.tags import Tags

router = APIRouter()


@router.get("/projects/get_projects",
         description='This method returns all projects',
         tags=[Tags.projects])
def get_projects():
    try:
        # TODO get projects
        projects = ''
        return projects
    except Exception as e:
        raise e


@router.post("/projects/{project_id}",
          description='This method creates project',
          tags=[Tags.projects])
def create_project(project_id: str = Path()):
    try:
        # TODO create project
        projects = ''
        return projects
    except Exception as e:
        raise e
