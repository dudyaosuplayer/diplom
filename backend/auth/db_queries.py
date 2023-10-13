from sqlalchemy.orm import Session
from models import User
from auth.schemas import UserCreate, UserDelete


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password
    db_user = User(username=user.username, email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: UserDelete):
    db_user = get_user_by_username(db, username=user.username)
    db.delete(db_user)
    db.commit()
    return db_user


def update_user(db: Session, user: UserCreate, user_id: int):
    db_user = get_user_by_id(db, user_id=user_id)
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
