from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

import db.config as config


metadata = MetaData()


engine = create_engine(
    url=f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    echo=True,
)

table_name = 'project_user_association'  # Убедитесь, что имя таблицы корректное
table = metadata.tables.get(table_name)

# Удалите таблицу из метаданных
if table is not None:
    metadata.remove(table)

Session = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()


db_dependencies = Annotated[Session, Depends(get_db)]
