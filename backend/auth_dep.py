from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from backend.db.database import get_db
from backend.db.queries.user_queries import get_user_by_username


security = HTTPBasic()


def verify_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=str(credentials.username))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'User {credentials.username} not found',
            headers={'WWW-Authenticate': 'Basic'}
        )
    return user


auth_dependencies = Annotated[HTTPBasicCredentials, Depends(verify_credentials)]
