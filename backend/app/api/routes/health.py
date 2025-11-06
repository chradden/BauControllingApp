

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db
from app.models.din276 import DIN276CostGroup

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}


def build_tree(groups, parent_id=None):
    tree = []
    for g in [grp for grp in groups if grp.parent_id == parent_id]:
        node = {
            "id": g.id,
            "code": g.code,
            "name": g.name,
            "description": g.description,
            "level": g.level,
            "children": build_tree(groups, g.id)
        }
        tree.append(node)
    return tree


@router.get("/din276", response_model=None)
async def din276_hierarchy(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DIN276CostGroup))
    groups = result.scalars().all()
    tree = build_tree(groups)
    return {"din276": tree}
