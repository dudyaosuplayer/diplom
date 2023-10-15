from typing import List

from sqlalchemy.orm import Session

from backend.models.models import User, Task


def get_task_by_task_id(task_id: int, db: Session) -> List[Task]:
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks_by_project_id(project_id: int, db: Session) -> Task:
    return db.query(Task).filter(Task.project_id == project_id).all()


def get_task_by_from_project(project_id: int, task_id, db: Session) -> Task:
    return db.query(Task).filter(Task.project_id == project_id, Task.id == task_id).first()


def assign_task_to_user(task_id: int, assigned_user_id: int, db: Session) -> bool:
    task = db.query(Task).filter(Task.id == task_id).first()
    user = db.query(User).filter(User.id == assigned_user_id).first()
    if task and user:
        task.user_id = assigned_user_id
        db.commit()
        return True
    return False
