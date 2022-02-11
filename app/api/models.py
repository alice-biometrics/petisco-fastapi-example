from datetime import datetime
from typing import Optional
from uuid import UUID

from petisco import Uuid
from pydantic.main import BaseModel
from pydantic.types import constr

from app.src.task.shared.domain.task import Task


class TaskIn(BaseModel):
    name: constr(max_length=50)
    description: constr(max_length=200)
    id: Optional[UUID] = None

    def to_task(self) -> Task:
        return Task(
            aggregate_id=Uuid(str(self.id)) if self.id else None,
            name=self.name,
            description=self.description,
        )


class TaskOut(BaseModel):
    name: constr(max_length=50)
    description: constr(max_length=200)
    id: UUID
    created_at: datetime
    labels: list[str]

    @staticmethod
    def from_task(task: Task):
        return TaskOut(
            name=task.name,
            description=task.description,
            id=UUID(task.aggregate_id.value),
            created_at=task.created_at,
            labels=task.labels,
        )
