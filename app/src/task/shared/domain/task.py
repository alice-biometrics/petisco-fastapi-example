from datetime import datetime

from petisco import AggregateRoot, Uuid
from pydantic import constr, validator

from app.src.task.shared.domain.events import TaskCreated


class Task(AggregateRoot):
    name: constr(max_length=50)
    description: constr(max_length=200)
    created_at: datetime | None = None
    labels: list[str] | None = list()

    @validator("aggregate_id", pre=True, always=True)
    def set_aggregate_id(cls, v):
        return v or Uuid.v4()

    @validator("created_at", pre=True, always=True)
    def set_created_at(cls, v):
        return v or datetime.utcnow()

    @staticmethod
    def create(name: str, description: str, aggregate_id: Uuid | None = None):
        task = Task(name=name, description=description, aggregate_id=aggregate_id)
        task.record(TaskCreated())
        return task
