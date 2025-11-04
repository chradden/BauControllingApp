from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app import crud
from app.crud import project as project_crud

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
async def create_project(payload: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await project_crud.create(db, payload)


@router.get("", response_model=List[ProjectRead])
async def list_projects(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await project_crud.get_multi(db, skip=skip, limit=limit)


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(project_id: int, db: AsyncSession = Depends(get_db)):
    obj = await project_crud.get(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return obj


@router.put("/{project_id}", response_model=ProjectRead)
async def update_project(project_id: int, payload: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    obj = await project_crud.get(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return await project_crud.update(db, obj, payload)


@router.delete("/{project_id}", response_model=ProjectRead)
async def delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
    obj = await project_crud.remove(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return obj
