from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from datetime import datetime

from database import Base
from models.annotated import intpk, created_at, updated_at, str_256



class Users(Base):
    __tablename__ = "users"

    id        : Mapped[intpk]
    username  : Mapped[str_256]
    last_name : Mapped[str_256]
    first_name: Mapped[str_256]
    email     : Mapped[str_256]
    password  : Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class Resumes(Base):
    __tablename__ = "resumes"

    id               : Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    title            : Mapped[str_256]
    active           : Mapped[bool]
    compensation_min : Mapped[int | None]
    compensation_max : Mapped[int | None]
    workload         : Mapped[int] = mapped_column(
        ForeignKey("workloads.id", ondelete="CASCADE")
    )

    created_at       : Mapped[created_at]
    updated_at       : Mapped[updated_at]

class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    speciality_id: Mapped[int | None] = mapped_column(
        ForeignKey('specialities.id', ondelete="SET NULL")
    )

class WorkerSkill(Base):
    __tablename__ = 'worker_skills'

    worker_id: Mapped[intpk] = mapped_column(
        ForeignKey('workers.id', ondelete="CASCADE"),
        primary_key=True
    )

    technology_id: Mapped[intpk] = mapped_column(
        ForeignKey('technologies.id', ondelete="CASCADE"),
        primary_key=True
    )

    technology_level_id: Mapped[int | None] = mapped_column(
        ForeignKey('technology_levels.id', ondelete="SET NULL")
    )

class ExperienceWorker(Base):
    __tablename__ = "experience_workers"

    id: Mapped[intpk]
    worker_id: Mapped[int] = mapped_column(
        ForeignKey('workers.id', ondelete="CASCADE")
    )

    speciality_id: Mapped[int | None] = mapped_column(
        ForeignKey("specialities.id", ondelete="SET NULL")
    )

    vacansy_id: Mapped[int | None] = mapped_column(
        ForeignKey("vacansies.id", ondelete="SET NULL")
    )

    title: Mapped[str_256]
    content: Mapped[str]

    employment_at: Mapped[datetime]
    dismissal_at:  Mapped[datetime]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]