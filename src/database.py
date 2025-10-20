from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine, text, String

from typing import Annotated
from config import settings


engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo = False,
)


session_factory = sessionmaker(engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }