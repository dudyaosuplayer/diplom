from fastapi import FastAPI

from backend.endpoints import projects, tasks, users

def add_routers(app: FastAPI):
    app.include_router(projects.router)
    app.include_router(tasks.router)
    app.include_router(users.router)
