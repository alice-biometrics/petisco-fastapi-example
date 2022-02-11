from meiga import BoolResult
from petisco import Container
from petisco.extra.fastapi import FastAPIController

from app.src.task.shared.domain.task import Task
from app.src.task.update.application.task_updater import TaskUpdater


class UpdateTaskController(FastAPIController):
    def execute(self, task: Task) -> BoolResult:
        updater = TaskUpdater(
            labeler=Container.get("task_labeler"),
            repository=Container.get("task_repository"),
            domain_event_bus=Container.get("domain_event_bus"),
        )
        return updater.execute(task=task)
