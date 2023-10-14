from sqlalchemy.orm import Session

from backend.models.models import User, Task


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def assign_task_to_user(db: Session, task_id: int, assigned_user_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    user = db.query(User).filter(User.id == assigned_user_id).first()
    if task and user:
        task.user_id = assigned_user_id
        db.commit()
        return True
    return False
