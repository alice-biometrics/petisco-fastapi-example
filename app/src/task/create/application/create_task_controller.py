from meiga import BoolResult
from petisco import Container, CrudRepository, DomainEventBus
from petisco.extra.fastapi import FastAPIController

from app.src.task.create.application.task_creator import TaskCreator
from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.shared.domain.task import Task


class CreateTaskController(FastAPIController):
    def execute(self, task: Task) -> BoolResult:
        task_creator = TaskCreator(
            labeler=Container.get(TaskLabeler),
            repository=Container.get(CrudRepository, alias="task_repository"),
            domain_event_bus=Container.get(DomainEventBus),
        )
        return task_creator.execute(task=task)
