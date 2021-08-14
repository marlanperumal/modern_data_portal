from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from .. import schemas, methods
from ..dependencies import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("", response_model=List[schemas.Item])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    items = methods.items.get_items(db, skip=skip, limit=limit)
    return items
