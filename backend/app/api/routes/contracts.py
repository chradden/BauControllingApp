from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.contract import ContractCreate, ContractRead, ContractUpdate
from app.crud import contract as contract_crud

router = APIRouter(prefix="/contracts", tags=["contracts"])


@router.post("", response_model=ContractRead, status_code=status.HTTP_201_CREATED)
async def create_contract(payload: ContractCreate, db: AsyncSession = Depends(get_db)):
    return await contract_crud.create(db, payload)


@router.get("", response_model=List[ContractRead])
async def list_contracts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await contract_crud.get_multi(db, skip=skip, limit=limit)


@router.get("/{contract_id}", response_model=ContractRead)
async def get_contract(contract_id: int, db: AsyncSession = Depends(get_db)):
    obj = await contract_crud.get(db, contract_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contract not found")
    return obj


@router.put("/{contract_id}", response_model=ContractRead)
async def update_contract(contract_id: int, payload: ContractUpdate, db: AsyncSession = Depends(get_db)):
    obj = await contract_crud.get(db, contract_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contract not found")
    return await contract_crud.update(db, obj, payload)


@router.delete("/{contract_id}", response_model=ContractRead)
async def delete_contract(contract_id: int, db: AsyncSession = Depends(get_db)):
    obj = await contract_crud.remove(db, contract_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contract not found")
    return obj
