from __future__ import annotations
from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ContractBase(BaseModel):
    contractor: Optional[str] = None
    value: float = 0.0
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class ContractCreate(ContractBase):
    project_id: int


class ContractUpdate(ContractBase):
    pass


class ContractRead(ContractBase):
    id: int
    project_id: int

    model_config = ConfigDict(from_attributes=True)
