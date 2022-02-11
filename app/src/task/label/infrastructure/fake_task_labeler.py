from meiga import Error, Result, Success

from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.shared.domain.task import Task


class FakeTaskLabeler(TaskLabeler):
    def execute(self, task: Task) -> Result[Task, Error]:
        return Success(task)
