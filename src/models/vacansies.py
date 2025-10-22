from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Enum
from geoalchemy2 import Geometry

from datetime import datetime
import enum

from database import Base
from models.annotated import intpk, created_at, updated_at, str_256



class VacansiesSource(Base):
    __tablename__ = "vacancies_sources"

    id  : Mapped[intpk]
    name: Mapped[str_256]
    link: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class RawVacancys(Base):
    __tablename__ = "raw_vacansies"

    id     : Mapped[intpk]
    title  : Mapped[str]
    link   : Mapped[str]
    content: Mapped[str]
    
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[datetime]

class Company(Base):
    __tablename__ = "companies"

    id           : Mapped[intpk]
    name         : Mapped[str]
    official_link: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class Speciality(Base):
    __tablename__ = "specialities"

    id  : Mapped[intpk]
    name: Mapped[str_256]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class Technology(Base):
    __tablename__ = "technologies"

    id  : Mapped[intpk]
    name: Mapped[str_256]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class Language(Base):
    __tablename__ = "languages"

    id  : Mapped[intpk]
    name: Mapped[str_256]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class LanguageLevel(Base):
    __tablename__ = "languages_levels"

    id  : Mapped[intpk]
    name: Mapped[str_256]

    language_id: Mapped[int] = mapped_column(
        ForeignKey("languages.id", ondelete="CASCADE")
    )

class WorkMode(Base):
    __tablename__ = "workmodes"

    id: Mapped[intpk]
    value: Mapped[str_256]

class WorkLoad(Base):
    __tablename__ = "workloads"

    id: Mapped[intpk]
    value: Mapped[str_256]
    
class Vacansy(Base):
    __tablename__ = "vacansies"

    id: Mapped[intpk]

    title: Mapped[str_256]

    raw_vacansy_id: Mapped[int | None] = mapped_column(
        ForeignKey("raw_vacansies.id", ondelete="SET NULL")
    )
    company_id: Mapped[int | None] = mapped_column(
        ForeignKey("companies.id", ondelete="SET NULL")
    )
    speciality_id: Mapped[int | None] = mapped_column(
        ForeignKey("specialities.id", ondelete="SET NULL")
    )

    workmode: Mapped[int | None] = mapped_column(
        ForeignKey("workmodes.id", ondelete="SET NULL")
    )
    workload: Mapped[int | None]  = mapped_column(
        ForeignKey("workloads.id", ondelete="SET NULL")
    )

    compensation_min: Mapped[int | None]
    compensation_max: Mapped[int | None]

    location: Mapped[str] = mapped_column(Geometry(geometry_type="POINT", srid=4326))

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class VacansySpecialityExperience(Base):
    __tablename__ = "vacancy_speciality_experiences"

    speciality_id: Mapped[int] = mapped_column(
        ForeignKey("specialities.id", ondelete="CASCADE"),
        primary_key=True
    )

    vacansy_id: Mapped[int] = mapped_column(
        ForeignKey("vacansies.id", ondelete="CASCADE"),
        primary_key=True
    )

    experience: Mapped[float]

    type_of_obligation_id: Mapped[int | None] = mapped_column(
        ForeignKey('type_of_obligation.id', ondelete="SET NULL")
    )

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class TypeOfObligation(Base):
    __tablename__ = "type_of_obligation"

    id: Mapped[intpk]
    value: Mapped[str_256]

class TechnologyLevel(Base):
    __tablename__ = "technology_levels"

    id: Mapped[intpk]
    value: Mapped[str_256]

class LanguageLevel(Base):
    __tablename__ = "language_levels"

    id: Mapped[intpk]
    value: Mapped[str_256]

class VacansyTechnology(Base):
    __tablename__ = "vacansies_technologies"

    technology_id: Mapped[int] = mapped_column(
        ForeignKey("technologies.id", ondelete="CASCADE"),
        primary_key=True
    )

    vacansy_id: Mapped[int] = mapped_column(
        ForeignKey("vacansies.id", ondelete="CASCADE"),
        primary_key=True
    )

    type_of_obligation_id: Mapped[int | None] = mapped_column(
        ForeignKey("type_of_obligation.id", ondelete="SET NULL")
    )

    technology_level_id: Mapped[int | None] = mapped_column(
        ForeignKey("technology_levels.id", ondelete="SET NULL")
    )

class VacansyLanguage(Base):
    __tablename__ = "vacansies_languages"

    language_id: Mapped[int] = mapped_column(
        ForeignKey("languages.id", ondelete="CASCADE"),
        primary_key=True
    )

    vacansy_id: Mapped[int] = mapped_column(
        ForeignKey("vacansies.id", ondelete="CASCADE"),
        primary_key=True
    )

    type_of_obligation_id: Mapped[int | None] = mapped_column(
        ForeignKey("type_of_obligation.id", ondelete="SET NULL")
    )

    language_level_id: Mapped[int | None] = mapped_column(
        ForeignKey("language_levels.id", ondelete="SET NULL")
    )