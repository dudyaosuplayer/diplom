from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from backend.db.database import Base, engine, get_db, Session

ROLE_USER = 0
ROLE_ADMIN = 1

project_user_association = Table(
    'project_user_association',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
)


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    status = Column(String(10))
    owner = Column(Integer)  # user.id

    users = relationship('User', secondary=project_user_association, back_populates="projects")

    def __repr__(self):
        return '<Project %r have users %r>' % (self.name, self.users)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), index=True, unique=True)
    email = Column(String(64), index=True, unique=True)
    p_hash = Column(String(96))
    password = Column(String(24))
    cookie = Column(String(8))
    role = Column(SmallInteger, default=ROLE_USER)
    register_date = Column(DateTime)

    projects = relationship('Project', secondary=project_user_association, back_populates='users')
    task = relationship('Task')
    comment = relationship('Comment')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, default=0, index=True)
    body = Column(String())
    task_name = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    project_id = Column(Integer, index=True)
    status = Column(String(10))
    depth = Column(Integer, default=0)

    comment = relationship('Comment')

    def __repr__(self):
        return '<Task %r>' % self.body


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    task_id = Column(Integer, ForeignKey("task.id"))
    timestamp = Column(DateTime)
    text = Column(String())

    def __repr__(self):
        return '<Comment %r>' % self.text


# Проверка
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db: Session = next(get_db())

user1 = User(nickname="user1", email="user1@example.com", p_hash="hash1", password="password1", cookie="cookie1")
user2 = User(nickname="user2", email="user2@example.com", p_hash="hash2", password="password2", cookie="cookie2")

db.add(user1)
db.add(user2)

db.commit()

db.close()
