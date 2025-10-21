from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, CheckConstraint, Index

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

    # resumes: Mapped[list["Resumes"]] = relationship(
    #     back_populates="raw_vacancy"
    # )

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class Resumes(Base):
    __tablename__ = "resumes"

    id               : Mapped[intpk]
    title            : Mapped[str_256]
    compensation_min : Mapped[int | None]
    compensation_max : Mapped[int | None]
    workload         : Mapped[Workload]
    raw_vacancy_id   : Mapped[int | None] = mapped_column(ForeignKey("raw_vacansies.id", ondelete='SET NULL'))  # CASCADE
    created_at       : Mapped[created_at]
    updated_at       : Mapped[updated_at]

    # raw_vacancy: Mapped["RawVacancys"] = relationship(
    #     back_populates="resumes"
    # )

    # user_send_resume: Mapped[list["Users"]] = relationship(
    #     back_populates="user_send_resume",
    #     secondary="users_resumes"
    # )


    repr_cols = ['id']

    __table_args__ = (
        Index("title_index", "title"),
        CheckConstraint("compensation_min > 0", name="check_compensation_min_positive")
    )

class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str_256]
    first_name: Mapped[str_256 | None]

    # user_send_resume: Mapped[list["Resumes"]] = relationship(
    #     back_populates="user_send_resume",
    #     secondary="users_resumes"
    # )

class UsersResumes(Base):
    __tablename__ = "users_resumes"

    user_id   : Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )
    resume_id : Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        primary_key=True
    )