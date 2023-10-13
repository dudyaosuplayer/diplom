from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from fastapi import Depends
from typing import Annotated
import db.config as config

engine = create_engine(
    url=f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    echo=False,
)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()


db_dependencies = Annotated[Session, Depends(get_db)]
