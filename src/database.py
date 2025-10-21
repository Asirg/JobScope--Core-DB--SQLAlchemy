from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine, text, String

from typing import Annotated
from config import settings


engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo = False,
)


session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass