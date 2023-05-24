from meiga import BoolResult
from petisco import Container, CrudRepository, DomainEventBus
from petisco.extra.fastapi import FastAPIController

from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.shared.domain.task import Task
from app.src.task.update.application.task_updater import TaskUpdater


class UpdateTaskController(FastAPIController):
    def execute(self, task: Task) -> BoolResult:
        updater = TaskUpdater(
            labeler=Container.get(TaskLabeler),
            repository=Container.get(CrudRepository, alias="task_repository"),
            domain_event_bus=Container.get(DomainEventBus),
        )
        return updater.execute(task=task)
