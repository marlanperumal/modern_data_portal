from celery.result import AsyncResult
from celery.exceptions import TimeoutError
from fastapi import APIRouter, Request, Response, status

from ..tasks import add
from ..schemas.tasks import Task, TaskResponse, TaskError

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


def serialize_task(task: AsyncResult):
    return {
        "task_id": task.task_id,
        "status": task.status,
        "ready": task.ready(),
        "successful": task.successful()
    }


@router.get("/results/{task_id}")
async def get_task_result(task_id: str):
    task = AsyncResult(task_id)
    if task.ready():
        result = serialize_task(task)
        result["result"] = task.get()
        return result


@router.get(
    "/add",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Task,
)
async def add_items(x: int, y: int, request: Request, response: Response):
    task: AsyncResult = add.delay(x, y)
    response.headers["location"] = request.url_for(
        "get_task_result", task_id=task.id
    )
    response.status_code = 202
    return serialize_task(task)
