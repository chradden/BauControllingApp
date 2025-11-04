from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.crud import user as user_crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_crud.create(db, payload)


@router.get("", response_model=List[UserRead])
async def list_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await user_crud.get_multi(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    obj = await user_crud.get(db, user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, payload: UserUpdate, db: AsyncSession = Depends(get_db)):
    obj = await user_crud.get(db, user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return await user_crud.update(db, obj, payload)


@router.delete("/{user_id}", response_model=UserRead)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    obj = await user_crud.remove(db, user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj
