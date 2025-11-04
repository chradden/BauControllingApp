from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.invoice import InvoiceCreate, InvoiceRead, InvoiceUpdate
from app.crud import invoice as invoice_crud

router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.post("", response_model=InvoiceRead, status_code=status.HTTP_201_CREATED)
async def create_invoice(payload: InvoiceCreate, db: AsyncSession = Depends(get_db)):
    return await invoice_crud.create(db, payload)


@router.get("", response_model=List[InvoiceRead])
async def list_invoices(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await invoice_crud.get_multi(db, skip=skip, limit=limit)


@router.get("/{invoice_id}", response_model=InvoiceRead)
async def get_invoice(invoice_id: int, db: AsyncSession = Depends(get_db)):
    obj = await invoice_crud.get(db, invoice_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return obj


@router.put("/{invoice_id}", response_model=InvoiceRead)
async def update_invoice(invoice_id: int, payload: InvoiceUpdate, db: AsyncSession = Depends(get_db)):
    obj = await invoice_crud.get(db, invoice_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return await invoice_crud.update(db, obj, payload)


@router.delete("/{invoice_id}", response_model=InvoiceRead)
async def delete_invoice(invoice_id: int, db: AsyncSession = Depends(get_db)):
    obj = await invoice_crud.remove(db, invoice_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return obj
