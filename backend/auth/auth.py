from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from backend.db.queries.users import get_user_by_username
from backend.db.database import get_db


security = HTTPBasic()


def verify_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=str(credentials.username))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'User {credentials.username} not found',
            headers={'WWW-Authenticate': 'Basic'}
        )
    if credentials.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Incorrect password',
            headers={'WWW-Authenticate': 'Basic'}
        )

    return user


auth_dependencies = Annotated[HTTPBasicCredentials, Depends(verify_credentials)]
