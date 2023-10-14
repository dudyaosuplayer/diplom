from sqlalchemy.orm import Session

from backend.models.models import Project


def get_all_projects(db: Session) -> Project:
    return db.query(Project).all()


def get_project_by_name(name: str, db: Session) -> Project:
    return db.query(Project).where(Project.name == name).first()


def get_project_by_id(id: int, db: Session) -> Project:
    return db.query(Project).where(Project.id == id).first()
