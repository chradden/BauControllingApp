from __future__ import annotations
from datetime import date
from typing import Optional, List
from pydantic import BaseModel
from pydantic import ConfigDict


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
