from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


async def create(db: AsyncSession, obj_in: ProjectCreate) -> Project:
    obj = Project(**obj_in.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get(db: AsyncSession, id: int) -> Project | None:
    return await db.get(Project, id)


async def get_multi(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Project]:
    result = await db.execute(select(Project).offset(skip).limit(limit))
    return result.scalars().all()


async def update(db: AsyncSession, db_obj: Project, obj_in: ProjectUpdate) -> Project:
    data = obj_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(db_obj, field, value)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def remove(db: AsyncSession, id: int) -> Project | None:
    obj = await get(db, id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj
