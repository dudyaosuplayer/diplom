from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from backend.db.database import Base, engine, get_db, Session

ROLE_USER = 0
ROLE_ADMIN = 1

project_user_association = Table(
    'project_user_association',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)


# class Association(Base):
#     __tablename__ = "project_user_association"
#     project_id = Column(ForeignKey("project.id"), primary_key=True)
#     user_id = Column(ForeignKey("user.id"), primary_key=True)
#     project = relationship("Project", back_populates="user")
#     user = relationship("User", back_populates="project")


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    status = Column(String(10))
    # owner = Column(Integer)  # user.id

    tasks = relationship('Task', lazy=True)
    users = relationship('User', secondary=project_user_association, back_populates="projects", lazy=True)

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

    projects = relationship('Project', secondary=project_user_association, back_populates='users', lazy=True)
    # projects = relationship('Association', back_populates='user')
    tasks = relationship('Task', lazy=True)
    comment = relationship('Comment', lazy=True)

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
    project_id = Column(Integer, ForeignKey('project.id'))
    status = Column(String(10))
    depth = Column(Integer, default=0)

    comment = relationship('Comment', lazy=True)

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

# Создаем и добавляем проекты
project1 = Project(name="Project 1", status="Active")
project2 = Project(name="Project 2", status="Inactive")

db.add(project1)
db.add(project2)

user1.projects.append(project1)
project1.users.append(user2)
project2.users.append(user2)

db.commit()
# print('user1.projects:', user1.projects, 'project1.users:', project1.users, 'project2.users:', project2.users)

# Создаем и добавляем задачи
task1 = Task(parent_id=0, body="Task 1", task_name="Task 1", user_id=user1.id, project_id=project1.id,
             status="Incomplete")
task2 = Task(parent_id=0, body="Task 2", task_name="Task 2", user_id=user2.id, project_id=project1.id,
             status="Complete")

db.add(task1)
db.add(task2)

db.commit()

print('user1.tasks', user1.tasks, 'user2.tasks', user2.tasks)
# Создаем и добавляем комментарии
comment1 = Comment(user_id=user1.id, task_id=task1.id, text="Comment 1 for Task 1")
comment2 = Comment(user_id=user2.id, task_id=task1.id, text="Comment 2 for Task 1")
comment3 = Comment(user_id=user1.id, task_id=task2.id, text="Comment 1 for Task 2")

db.add(comment1)
db.add(comment2)
db.add(comment3)

db.commit()

db.close()
