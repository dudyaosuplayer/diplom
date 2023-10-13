from fastapi import FastAPI
import uvicorn

from utils.fastapi.router import add_routers
import backend.models.models as models
from backend.db.database import engine, get_db, Session, Base

# Проверка
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db: Session = next(get_db())

user1 = models.User(nickname="user1", email="user1@example.com", p_hash="hash1", password="password1", cookie="cookie1")
user2 = models.User(nickname="user2", email="user2@example.com", p_hash="hash2", password="password2", cookie="cookie2")

db.add(user1)
db.add(user2)

db.commit()

# Создаем и добавляем проекты
project1 = models.Project(name="Project 1", status="Active")
project2 = models.Project(name="Project 2", status="Inactive")

db.add(project1)
db.add(project2)

user1.projects.append(project1)
project1.users.append(user2)
project2.users.append(user2)

db.commit()
# print('user1.projects:', user1.projects, 'project1.users:', project1.users, 'project2.users:', project2.users)

# Создаем и добавляем задачи
task1 = models.Task(parent_id=0, body="Task 1", task_name="Task 1", user_id=user1.id, project_id=project1.id,
             status="Incomplete")
task2 = models.Task(parent_id=0, body="Task 2", task_name="Task 2", user_id=user2.id, project_id=project1.id,
             status="Complete")

db.add(task1)
db.add(task2)

db.commit()

print('user1.tasks', user1.tasks, 'user2.tasks', user2.tasks)
# Создаем и добавляем комментарии
comment1 = models.Comment(user_id=user1.id, task_id=task1.id, text="Comment 1 for Task 1")
comment2 = models.Comment(user_id=user2.id, task_id=task1.id, text="Comment 2 for Task 1")
comment3 = models.Comment(user_id=user1.id, task_id=task2.id, text="Comment 1 for Task 2")

db.add(comment1)
db.add(comment2)
db.add(comment3)

db.commit()

db.close()

app = FastAPI(
    title='Project Managing API',
    description='',
    version='1.0.0'
)
add_routers(app)


# Run the FastAPI application
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)
