from typing import Annotated

from fastapi import APIRouter, Path, HTTPException

from backend.auth.auth import auth_dependencies
from backend.db.database import db_dependencies
from backend.models.models import Project, User
from backend.utils.fastapi.schemas.project_schemas import ProjectCreate, ProjectResponse, ProjectUpdate
from backend.utils.fastapi.tags import Tags

router = APIRouter(prefix='/projects', tags=[Tags.projects])

# TODO: Прописать документацию и валидацию для всех эндпоинтов связанных с Project

@router.get("/get_projects", description='This method returns all projects')
def get_projects(db: db_dependencies, user: auth_dependencies):
    if user.role == 'Product Manager':
        try:
            projects = db.query(Project).all()
            return projects
        except Exception as e:
            raise e
    else:
        raise HTTPException(status_code=403, detail="Access denied: You are not a Product Manager")


@router.post("/create_project", response_model=ProjectCreate, description='This method creates project')
def create_project(project_data: ProjectCreate, db: db_dependencies, user: auth_dependencies):
    if user.role == 'Product Manager':
        try:
            new_project = Project(name=project_data.name, status=project_data.status)
            db.add(new_project)
            db.commit()
            return new_project
        except Exception as e:
            raise e
    else:
        raise HTTPException(status_code=403, detail="Access denied: You are not a Product Manager")


@router.get("/get_project/{project_id}", response_model=ProjectResponse, description='This method returns a project by ID')
def get_project(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of the project to retrieve", ge=0)],
                db: db_dependencies):
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        response_project = ProjectResponse(
            id=project.id,
            name=project.name,
            status=project.status,
        )
        return response_project
    except Exception as e:
        raise e


@router.put("/update_project/{project_id}", description='This method updates the name and status of a project by ID')
def update_project(project_id: Annotated[int, Path(..., title="Project ID", description="The ID of project to retrieve", ge=0)],
                   project_data: ProjectUpdate,
                   db: db_dependencies,
                   user: auth_dependencies):
    if user.role == 'Product Manager':
        try:
            project = db.query(Project).filter(Project.id == project_id).first()
            if not project:
                raise HTTPException(status_code=404, detail="Project not found")
            project.name = project_data.name
            project.status = project_data.status
            db.commit()
            return {"message": "Project updated successfully"}
        except Exception as e:
            raise e
    else:
        raise HTTPException(status_code=403, detail="Access denied: You are not a Product Manager")


@router.post("/add_user/{project_id}/{user_id}", description='Add user to project')
def add_user_to_project(db: db_dependencies,
                        current_user: auth_dependencies,
                        project_id: int = Path(..., description="The ID of the project"),
                        user_id: int = Path(..., description="The ID of the user")):
    if current_user.role != "Product Manager":
        raise HTTPException(status_code=403,
                            detail="Permission denied. You must be a Product Manager to add users to a project.")
    project = db.query(Project).filter(Project.id == project_id).first()
    user = db.query(User).filter(User.id == user_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    project.users.append(user)
    db.commit()
    db.refresh(project)
    return {"message": "User added to project successfully"}


@router.get("/get_users/{project_id}", description='Get users attached to a project')
def get_users_attached_to_project(db: db_dependencies,
                                  project_id: int = Path(..., description="The ID of the project")):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    users = project.users
    return users
