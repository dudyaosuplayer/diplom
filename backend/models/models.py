from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from backend.db.database import Base
from backend.utils.users import ProjectRole

ROLE_USER = 0
ROLE_ADMIN = 1


project_user_association = Table(
    'project_user_association',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id', ondelete='CASCADE')),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE')),
    extend_existing=True
)


class Project(Base):
    __tablename__ = 'project'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    status = Column(String(10))

    tasks = relationship('Task', lazy=True, cascade='all, delete')
    users = relationship('User', secondary=project_user_association, back_populates="projects", lazy=True, cascade='all, delete')

    def __repr__(self):
        return '<Project %r have users %r>' % (self.name, self.users)


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), index=True, unique=True)
    email = Column(String(64), index=True, unique=True)
    p_hash = Column(String(96))
    password = Column(String(24))
    cookie = Column(String(8))
    role = Column(String(24), default=ProjectRole.Developer)
    register_date = Column(DateTime)

    projects = relationship('Project', secondary=project_user_association, back_populates='users', lazy=True, cascade='all, delete')
    tasks = relationship('Task', lazy=True, cascade='all, delete')
    comment = relationship('Comment', lazy=True, cascade='all, delete')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Task(Base):
    __tablename__ = 'task'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, default=0, index=True)
    body = Column(String())
    task_name = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    project_id = Column(Integer, ForeignKey('project.id', ondelete='CASCADE'))
    status = Column(String(10))
    
    comment = relationship('Comment', lazy=True, cascade='all, delete')

    def __repr__(self):
        return '<Task %r>' % self.body


class Comment(Base):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'))
    task_id = Column(Integer, ForeignKey("task.id", ondelete='CASCADE'))
    timestamp = Column(DateTime)
    text = Column(String())

    def __repr__(self):
        return '<Comment %r>' % self.text
