from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from backend.db.database import Base

ROLE_USER = 0
ROLE_ADMIN = 1

project_user_association = Table(
    'project_user_association',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    status = Column(String(10))
    tasks = relationship('Task', lazy=True)
    users = relationship('User', secondary=project_user_association, back_populates="projects", lazy=True)

    def __repr__(self):
        return f'Project(id={self.id}, name={self.name}, status={self.status})'


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
    projects = relationship('Project', secondary=project_user_association, back_populates='users', lazy=True)
    tasks = relationship('Task', lazy=True)
    comment = relationship('Comment', lazy=True)

    def __repr__(self):
        return f'User(id={self.id}, nickname={self.nickname}, email={self.email}, p_hash={self.p_hash}, ' \
               f'password={self.password}, cookie={self.cookie}, role={self.role}, register_date={self.register_date})'


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, default=0, index=True)
    body = Column(String())
    task_name = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    project_id = Column(Integer, ForeignKey('project.id'))
    status = Column(String(10))
    depth = Column(Integer, default=0)

    comment = relationship('Comment', lazy=True)

    def __repr__(self):
        return f'Task(id={self.id}, parent_id={self.parent_id}, body={self.body}, task_name={self.task_name}, ' \
               f'timestamp={self.timestamp}, user_id={self.user_id}, project_id={self.project_id}, register_date={self.status}, ' \
               f'status={self.status})'


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    task_id = Column(Integer, ForeignKey("task.id"))
    timestamp = Column(DateTime)
    text = Column(String())

    def __repr__(self):
        return f'Comment(id={self.id}, user_id={self.user_id}, task_id={self.task_id}, timestamp={self.timestamp}, text={self.text})'
