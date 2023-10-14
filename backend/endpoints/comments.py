from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Path, HTTPException

from backend.db.database import db_dependencies
from backend.models.models import Comment, Task, User
from backend.utils.fastapi.schemas.comment_schemas import CommentResponse, CommentCreate
from backend.utils.fastapi.tags import Tags


router = APIRouter(prefix='/comment', tags=[Tags.authentication])


@router.get("/comments/get_comments_task/{task_id}",
            description='This method returns all comments from task',
            tags=[Tags.comments])
def get_comments_tasks(task_id: Annotated[int, Path(..., title="Task ID", description="The ID of the task to retrieve", ge=0)],
                       db: db_dependencies):
    try:
        comments = db.query(Comment).filter(Comment.task_id == task_id).all()
        if not comments:
            raise HTTPException(status_code=404, detail="Comments not found")
        response_comments = [CommentResponse(id=comment.id,
                                             user_id=comment.user_id,
                                             task_id=comment.task_id,
                                             timestamp=comment.timestamp if comment.timestamp else datetime.now(),
                                             text=comment.text) for comment in comments]
        return response_comments
    except Exception as e:
        raise e


@router.get("/comments/get_comments_user/{user_id}",
            description='This method returns all comments from user',
            tags=[Tags.comments])
def get_comments_user(
        user_id: Annotated[
            int, Path(..., title="User ID", description="The ID of the user to retrieve", ge=0)],
        db: db_dependencies
):
    try:
        comments = db.query(Comment).filter(Comment.user_id == user_id).all()
        if not comments:
            raise HTTPException(status_code=404, detail="Comments not found")
        response_comments = [CommentResponse(id=comment.id,
                                             user_id=comment.user_id,
                                             task_id=comment.task_id,
                                             timestamp=comment.timestamp if comment.timestamp else datetime.now(),
                                             text=comment.text) for comment in comments]
        return response_comments
    except Exception as e:
        raise e


@router.post("/comments/create_comment",
             description='This method creates a new comment for a user and task',
             tags=[Tags.comments])
def create_comment(comment_request: CommentCreate, db: db_dependencies) -> CommentCreate:
    try:
        # Проверка существования пользователя с указанным user_id и задачи с указанным task_id
        user_exists = db.query(User).filter(User.id == comment_request.user_id).first()
        task_exists = db.query(Task).filter(Task.id == comment_request.task_id).first()
        if not user_exists or not task_exists:
            raise HTTPException(status_code=404, detail="User or task not found")
        # Создание нового комментария и добавление его в базу данных
        new_comment = Comment(user_id=comment_request.user_id,
                              task_id=comment_request.task_id,
                              timestamp=comment_request.timestamp,
                              text=comment_request.text)
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        # Создание объекта CommentResponse из нового комментария и возвращение его в качестве ответа
        response_comment = CommentResponse(id=new_comment.id,
                                           user_id=new_comment.user_id,
                                           task_id=new_comment.task_id,
                                           timestamp=new_comment.timestamp,
                                           text=new_comment.text)
        return response_comment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
