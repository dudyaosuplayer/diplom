from typing import Annotated

from fastapi import APIRouter, Path, HTTPException, status

from backend.auth.auth import auth_dependencies
from backend.db.database import db_dependencies
from backend.models.models import Project
from backend.utils.fastapi.schemas.project_schemas import ProjectCreate, ProjectResponse, ProjectUpdate
from backend.utils.fastapi.tags import Tags
from backend.utils.users import ProjectRole
from backend.utils.statuses import ProjectStatus
from backend.db.queries.projects import get_projects, get_project_by_name, get_project_by_id
from backend.db.queries.users import get_user_by_id, get_users_from_project

router = APIRouter(prefix='/projects', tags=[Tags.projects])


# TODO: Прописать документацию и валидацию для всех эндпоинтов связанных с Project

@router.get("/get_projects", description='This method returns all projects')
def get_projects(db: db_dependencies, user: auth_dependencies):
    try:
        if user.role == ProjectRole.ProductManager:
            projects = get_projects(db)
            return projects
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: You are not a Product Manager")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    


@router.post("/create_project", response_model=ProjectCreate, description='This method creates project')
def create_project(project_name: Annotated[str, Path(..., title="Project Name", description="Name of the project to retrieve", max_length=50)], 
                   project_status: ProjectStatus, db: db_dependencies, user: auth_dependencies):
    try:
        if not project_name or project_status:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Some field is empty")
        if user.role == ProjectRole.ProductManager:
            project = get_project_by_name(project_name, db)
            if project:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Project with this name already exists")
            new_project = Project(name=project_name, status=project_status)
            db.add(new_project)
            db.commit()
            return new_project
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: You are not a Product Manager")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/get_project/{project_id}", response_model=ProjectResponse,
            description='This method returns a project by ID')
def get_project(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project to retrieve", ge=0)],
                db: db_dependencies):
    try:
        project = get_project_by_id(project_id, db)
        if not project:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
        project = ProjectResponse(id=project.id,
                                  name=project.name,
                                  status=project.status)
        return project
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put("/update_project/{project_id}", description='This method updates the name and status of a project by ID')
def update_project(
        project_id: Annotated[int, Path(..., title="Project ID", description="The ID of project to retrieve", ge=0)],
        project_name: str, project_status: ProjectStatus, db: db_dependencies, user: auth_dependencies):
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
            return {"message": "Project updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: You are not a Product Manager")


@router.post("/add_user/{project_id}/{user_id}", description='Add user to project')
def add_user_to_project(db: db_dependencies,
                        current_user: auth_dependencies,
                        project_id: int = Path(..., description="The ID of the project"),
                        user_id: int = Path(..., description="The ID of the user")):
    if current_user.role != ProjectRole.ProductManager:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied. You must be a Product Manager to add users to a project.")
    project = get_project_by_id(project_id, db)
    user = get_user_by_id(user_id, db)
    if not project:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not found")
    project.users.append(user)
    db.commit()
    db.refresh(project)
    return {"message": "User added to project successfully"}


@router.get("/get_users/{project_id}", description='Get users attached to a project')
def get_users_attached_to_project(db: db_dependencies,
                                  project_id: int = Path(..., description="The ID of the project")):
    project = get_users_from_project(project_id, db)
    if not project:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project not found")
    users = project.users
    return users
