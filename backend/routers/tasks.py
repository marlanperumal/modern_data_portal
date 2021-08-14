from fastapi import APIRouter
from celery.exceptions import TimeoutError

from ..tasks import add

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get("/add")
async def add_items(x: int, y: int):
    result = add.delay(x, y)
    try:
        return {"result": result.get(timeout=1)}
    except TimeoutError:
        return {"error": "timeout"}
