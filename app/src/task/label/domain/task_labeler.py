from meiga import Error, NotImplementedMethodError, Result
from petisco import AppService

from app.src.task.shared.domain.task import Task


class TaskLabeler(AppService):
    def execute(self, task: Task) -> Result[Task, Error]:
        return NotImplementedMethodError
