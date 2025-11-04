from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


async def create(db: AsyncSession, obj_in: UserCreate) -> User:
    # Note: caller should hash the password; for MVP we store a placeholder
    data = obj_in.model_dump()
    password = data.pop("password", None)
    obj = User(**data, hashed_password=password)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get(db: AsyncSession, id: int) -> User | None:
    return await db.get(User, id)


async def get_multi(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


async def update(db: AsyncSession, db_obj: User, obj_in: UserUpdate) -> User:
    data = obj_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(db_obj, field, value)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def remove(db: AsyncSession, id: int) -> User | None:
    obj = await get(db, id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj
