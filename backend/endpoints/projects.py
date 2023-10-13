from fastapi import APIRouter, Depends, Path, Query, HTTPException
from typing import Annotated

from db.database import db_dependencies
from models.models import Project
from schemas import ProjectCreate, ProjectResponse, ProjectUpdate

from utils.fastapi.tags import Tags

router = APIRouter(
    prefix='/projects',
    tags=[[Tags.projects]]
)


# TODO: Прописать документацию и валидацию для всех эндпоинтов связанных с Project

@router.get(
    "/get_projects",
    description='This method returns all projects',
)
def get_projects(db: db_dependencies):
    try:
        projects = db.query(Project).all()
        return projects
    except Exception as e:
        raise e


@router.post(
    "/create_project",
    description='This method creates project',
)
def create_project(project_data: ProjectCreate, db: db_dependencies):
    try:
        new_project = Project(name=project_data.name, status=project_data.status)

        db.add(new_project)
        db.commit()

        return new_project
    except Exception as e:
        raise e


@router.get(
    "/get_project/{project_id}",
    response_model=ProjectResponse,
    description='This method returns a project by ID',
)
def get_project(
        project_id: Annotated[
            int, Path(..., title="Project ID", description="The ID of the project to retrieve", ge=0)],
        db: db_dependencies
):
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


@router.put(
    "/update_project/{project_id}",
    description='This method updates the name and status of a project by ID',
)
def update_project(
        project_id: Annotated[
            int, Path(..., title="Project ID", description="The ID of project to retrieve", ge=0)],
        project_data: ProjectUpdate,
        db: db_dependencies
):
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
