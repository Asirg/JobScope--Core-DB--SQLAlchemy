from sqlalchemy.orm import Mapped

from database import Base
from models.annotated import intpk, created_at, updated_at, str_256


class VacansiesSource(Base):
    __tablename__ = "vacancies_sources"

    id: Mapped[intpk]
    name: Mapped[str_256]
    link: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]




# class RawVacancys(Base):
#     __tablename__ = "raw_vacansies"

#     id: Mapped[intpk]
#     name: Mapped[str_256]

# class Workload(enum.Enum):
#     parttime = "parttime"
#     fulltime = "fulltime"

# class Resumes(Base):
#     __tablename__ = "resumes"

#     id               : Mapped[intpk]
#     title            : Mapped[str_256]
#     compensation_min : Mapped[int | None]
#     compensation_max : Mapped[int | None]
#     workload         : Mapped[Workload]
#     raw_vacancy_id   : Mapped[int | None] = mapped_column(ForeignKey("raw_vacansies.id", ondelete='SET NULL'))  # CASCADE
#     created_at       : Mapped[created_at]
#     updated_at       : Mapped[updated_at]


#     repr_cols = ['id']

#     __table_args__ = (
#         Index("title_index", "title"),
#         CheckConstraint("compensation_min > 0", name="check_compensation_min_positive")
#     )

# class Users(Base):
#     __tablename__ = "users"

#     id: Mapped[intpk]
#     username: Mapped[str_256]
#     first_name: Mapped[str_256 | None]

# class UsersResumes(Base):
#     __tablename__ = "users_resumes"

#     user_id   : Mapped[int] = mapped_column(
#         ForeignKey("users.id", ondelete="CASCADE"),
#         primary_key=True
#     )
#     resume_id : Mapped[int] = mapped_column(
#         ForeignKey("resumes.id", ondelete="CASCADE"),
#         primary_key=True
#     )