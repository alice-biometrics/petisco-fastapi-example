from meiga import BoolResult
from petisco import Container, CrudRepository, DomainEventBus, Uuid
from petisco.extra.fastapi import FastAPIController

from app.src.task.delete.application.task_deleter import TaskDeleter


class DeleteTaskController(FastAPIController):
    def execute(self, aggregate_id: Uuid) -> BoolResult:
        deleter = TaskDeleter(
            repository=Container.get(CrudRepository, alias="task_repository"),
            domain_event_bus=Container.get(DomainEventBus),
        )
        return deleter.execute(aggregate_id)
