from fastapi import FastAPI

from endpoints import projects, tasks, users, comments


def add_routers(app: FastAPI):
    app.include_router(projects.router)
    app.include_router(tasks.router)
    app.include_router(users.router)
    app.include_router(comments.router)