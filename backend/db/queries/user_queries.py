from sqlalchemy.orm import Session

from backend.models.models import User, Task
from backend.utils.fastapi.schemas.user_schemas import UserCreate, UserDelete
from backend.utils.fastapi.schemas.task_schemas import TaskSchema


def get_user_by_username(db: Session, username: str):
    """
    Get a user from the database by username.

    Args:
        db (Session): The database session.
        username (str): The username to search for.

    Returns:
        User: The user object.
    """
    return db.query(User).filter(User.nickname == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Get a list of users from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): Number of records to skip (default is 0).
        limit (int, optional): Maximum number of records to return (default is 100).

    Returns:
        list: A list of users.
    """
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    """
    Get a user from the database by ID.

    Args:
        db (Session): The database session.
        user_id (int): The user's ID.

    Returns:
        User: The user object.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    """
    Get a user from the database by email address.

    Args:
        db (Session): The database session.
        user_email (str): The user's email address to search for.

    Returns:
        User: The user object.
    """
    return db.query(User).filter(User.email == user_email).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user and add it to the database.

    Args:
        db (Session): The database session.
        user (UserCreate): The user data to create.

    Returns:
        User: The created user object.
    """
    fake_hashed_password = user.password
    db_user = User(nickname=user.nickname, role=user.role, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: UserDelete):
    """
    Delete a user from the database.

    Args:
        db (Session): The database session.
        user (UserDelete): The user data to delete.

    Returns:
        User: The deleted user object.
    """
    db_user = get_user_by_username(db, username=user.username)
    db.delete(db_user)
    db.commit()
    return db_user


def update_user(db: Session, user: UserCreate, user_id: int):
    """
    Update a user's information in the database.

    Args:
        db (Session): The database session.
        user (UserCreate): The updated user data.
        user_id (int): The user's ID to update.

    Returns:
        User: The updated user object.
    """
    db_user = get_user_by_id(db, user_id=user_id)
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_task(db: Session, task_id: int):
    """
    Get task by ID.

    Parameters:
    - **db** (Session): The database session.
    - **task_id** (int): The task's ID to update.

    Returns:
    - **Task**: The updated task object.
    """
    return db.query(Task).filter(Task.id == task_id).first()


def assign_task_to_user(db: Session, task_id: int, assigned_user_id: int):
    """
    Assign task to user by IDs.

    Parameters:
    - **db** (Session): The database session.
    - **task_id** (int): The task's ID to update.
    - **assigned_user_id** (int): The user's ID with assigned task.

    Returns:
    - **bool**: True, if successfully, else False.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    user = db.query(User).filter(User.id == assigned_user_id).first()

    if task and user:
        task.user_id = assigned_user_id
        db.commit()
        return True

    return False
