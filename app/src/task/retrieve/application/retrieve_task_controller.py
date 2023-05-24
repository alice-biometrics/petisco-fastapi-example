from meiga import Error, Result
from petisco import Container, CrudRepository, DomainEventBus, Uuid
from petisco.extra.fastapi import FastAPIController

from app.api.models import TaskOut
from app.src.task.retrieve.application.task_retriever import TaskRetriever
from app.src.task.shared.domain.task import Task


class RetrieveTaskController(FastAPIController):
    class Config:
        success_handler = lambda result: TaskOut.from_task(result.value)  # noqa

    def execute(self, aggregate_id: Uuid) -> Result[Task, Error]:
        retriever = TaskRetriever(
            repository=Container.get(CrudRepository, alias="task_repository"),
            domain_event_bus=Container.get(DomainEventBus),
        )
        return retriever.execute(aggregate_id)
