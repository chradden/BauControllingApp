from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate


async def create(db: AsyncSession, obj_in: InvoiceCreate) -> Invoice:
    obj = Invoice(**obj_in.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get(db: AsyncSession, id: int) -> Invoice | None:
    return await db.get(Invoice, id)


async def get_multi(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Invoice]:
    result = await db.execute(select(Invoice).offset(skip).limit(limit))
    return result.scalars().all()


async def update(db: AsyncSession, db_obj: Invoice, obj_in: InvoiceUpdate) -> Invoice:
    data = obj_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(db_obj, field, value)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def remove(db: AsyncSession, id: int) -> Invoice | None:
    obj = await get(db, id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj
