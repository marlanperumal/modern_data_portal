from typing import Optional, Any
from pydantic import BaseModel


class Task(BaseModel):
    task_id: str
    status: str
    ready: bool
    successful: bool
    result: Optional[Any] = None
    error: Optional[str] = None


class TaskResponse(BaseModel):
    result: Any


class TaskError(BaseModel):
    error: str
