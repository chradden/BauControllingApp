from __future__ import annotations
from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class InvoiceBase(BaseModel):
    amount: float = 0.0
    due_date: Optional[date] = None
    paid: bool = False


class InvoiceCreate(InvoiceBase):
    contract_id: int


class InvoiceUpdate(InvoiceBase):
    pass


class InvoiceRead(InvoiceBase):
    id: int
    contract_id: int

    model_config = ConfigDict(from_attributes=True)
