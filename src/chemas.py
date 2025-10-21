from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

from models import Workload

class RawVacansiesAddDTO(BaseModel):
    name:str

class RawVacansiesDTO(BaseModel):
    id:int


class ResumesAddDTO(BaseModel):
    title:str
    compensation_min: Optional[int]
    compensation_max: Optional[int]
    Workload: Workload
    raw_vacancy_id: Optional[int]

class ResumesDTO(BaseModel):
    title:str
    created_at: datetime
    updated_at: datetime


class ResumeRelDTO(ResumesDTO):
    raw_vacansy: "RawVacansiesDTO"

class RawVacansiesRelDTO(RawVacansiesDTO):
    resumes: list["ResumesDTO"]
