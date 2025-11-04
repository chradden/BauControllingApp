from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.contract import Contract
from app.schemas.contract import ContractCreate, ContractUpdate


async def create(db: AsyncSession, obj_in: ContractCreate) -> Contract:
    obj = Contract(**obj_in.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get(db: AsyncSession, id: int) -> Contract | None:
    return await db.get(Contract, id)


async def get_multi(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Contract]:
    result = await db.execute(select(Contract).offset(skip).limit(limit))
    return result.scalars().all()


async def update(db: AsyncSession, db_obj: Contract, obj_in: ContractUpdate) -> Contract:
    data = obj_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(db_obj, field, value)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def remove(db: AsyncSession, id: int) -> Contract | None:
    obj = await get(db, id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj
