from meiga import BoolResult
from petisco import Container
from petisco.extra.fastapi import FastAPIController

from app.src.task.create.application.task_creator import TaskCreator
from app.src.task.shared.domain.task import Task


class CreateTaskController(FastAPIController):
    def execute(self, task: Task) -> BoolResult:
        task_creator = TaskCreator(
            repository=Container.get("task_repository"),
            domain_event_bus=Container.get("domain_event_bus"),
        )
        return task_creator.execute(task=task)
