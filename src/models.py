from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, text

from database import Base, str_256

import datetime
import enum


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.timezone.utc)
)]


class RawVacancys(Base):
    __tablename__ = "raw_vacansies"

    id: Mapped[intpk]
    name: Mapped[str_256]

class Workload(enum.Enum):
    parttime = "parttme"
    fullname = "fulltime"

class Resumes(Base):
    __tablename__ = "resumes"

    id               : Mapped[intpk]
    title            : Mapped[str_256]
    compensation_min : Mapped[int | None]
    compensation_max : Mapped[int | None]
    # workload         : Mapped[Workload]
    raw_vacancy_id   : Mapped[int | None] = mapped_column(ForeignKey("raw_vacansies.id", ondelete='SET NULL'))  # CASCADE
    created_at       : Mapped[created_at]
    # created_at       : Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    # created_at       : Mapped[datetime.datetime] = mapped_column(default=)
    updated_at       : Mapped[updated_at]