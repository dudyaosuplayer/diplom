from fastapi import APIRouter, Depends, Path, Query

from utils.fastapi.tags import Tags

router = APIRouter()


@router.get("/users/get_users/",
         description='This method returns all users',
         tags=[Tags.users])
def get_users():
    try:
        # TODO get users
        users = ''
        return users
    except Exception as e:
        raise e


@router.get("/users/get_users/{project_id}",
         description='This method returns all users from project',
         tags=[Tags.users])
def get_project_users(project_id: str = Path()):
    try:
        # TODO get users from project
        users = ''
        return users
    except Exception as e:
        raise e


@router.post("/users/create_user/",
         description='This method creates user',
         tags=[Tags.users])
def create_user():
    try:
        # TODO create task in project
        users = ''
        return users
    except Exception as e:
        raise e


@router.post("/users/change_user_project/",
         description='This method creates user',
         tags=[Tags.users])
def change_user_project():
    try:
        # TODO move some user to some project
        users = ''
        return users
    except Exception as e:
        raise e
