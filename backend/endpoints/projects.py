from typing import Annotated

from fastapi import APIRouter, Path, HTTPException, status, Depends

from backend.auth.auth import auth_dependencies, verify_credentials
from backend.db.database import db_dependencies
from backend.models.models import Project
from backend.utils.fastapi.schemas.project_schemas import ProjectResponse
from backend.utils.fastapi.tags import Tags
from backend.utils.users import ProjectRole
from backend.utils.statuses import ProjectStatus
from backend.db.queries.projects import get_all_projects, get_project_by_name, get_project_by_id


router = APIRouter(prefix='/projects', tags=[Tags.projects])


# TODO: Прописать документацию и валидацию для всех эндпоинтов связанных с Project

@router.get("/get_projects", description='This method returns all projects')
def get_projects(db: db_dependencies, user: auth_dependencies):
    try:
        if user.role == ProjectRole.ProductManager:
            projects = get_all_projects(db)
            return projects
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Access denied: You are not a Product Manager")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/create_project/{project_name}", description='This method creates project')
def create_project(project_status: ProjectStatus, db: db_dependencies, user: auth_dependencies,
                   project_name: str = Path(..., title="Project Name", description="Name of the project to retrieve", 
                                            min_length=1, max_length=50)):
    try:
        if not project_name or not project_status:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Some field is empty")
        if user.role == ProjectRole.ProductManager:
            project = get_project_by_name(project_name, db)
            if project:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail="Project with this name already exists")
            new_project = Project(name=project_name, status=project_status)
            db.add(new_project)
            db.commit()
            return {"message": "Project was successfully created"}
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Access denied: You are not a Product Manager")
    except Exception as e:
        raise e


@router.get("/get_project/{project_id}", response_model=ProjectResponse,
            description='This method returns a project by ID')
def get_project(db: db_dependencies, user: auth_dependencies,
                project_id: int = Path(..., title="Project ID", description="The ID of the project to retrieve", ge=0)):
    try:
        if user.role != ProjectRole.ProductManager:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: Insufficient privileges")
        project = get_project_by_id(project_id, db)
        if not project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
        project = ProjectResponse(id=project.id,
                                  name=project.name,
                                  status=project.status)
        return project
    except Exception as e:
        raise e


@router.put("/update_project/{project_id}", description='This method updates the name and status of a project by ID')
def update_project(project_status: ProjectStatus, db: db_dependencies, user: auth_dependencies,
        project_id: Annotated[int, Path(..., title="Project ID", description="The ID of project to retrieve", ge=0)],
        project_name: str = Path(..., title="Project Name", description="Name of the project to retrieve", 
                                 min_length=1, max_length=50)):
    if user.role == ProjectRole.ProductManager:
        try:
            project = get_project_by_id(project_id, db)
            if not project:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
            if project_name:
                project.name = project_name
            if project_status:
                project.status = project_status
            db.commit()
            return {"message": "Project was updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Access denied: You are not a Product Manager")

