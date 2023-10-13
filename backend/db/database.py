from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from fastapi import Depends
from typing import Annotated
import backend.db.config as config

engine = create_engine(
    url=f"postgresql+psycopg://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    echo=False,
)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_db() -> Session:
    """
    Provides a database session as a context manager.

    This function is used to manage database sessions in FastAPI as a context manager.
    It yields a database session for use within a specific scope and ensures that the session
    is properly closed when the scope is exited.

    Yields:
        Session: A SQLAlchemy database session for database operations.

    Example:
        Usage of this function typically appears within FastAPI route functions as follows:
        ```python
        def some_route(db: Session = Depends(get_db)):
            # Use the database session 'db' for database operations.
            # The session will be automatically closed when the route function exits.
        ```
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()


db_dependencies = Annotated[Session, Depends(get_db)]
