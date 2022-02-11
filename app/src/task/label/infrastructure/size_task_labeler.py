from meiga import Error, Result, Success

from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.shared.domain.task import Task


class SizeTaskLabeler(TaskLabeler):
    def execute(self, task: Task) -> Result[Task, Error]:
        size_description = len(task.description)
        if size_description < 10:
            label = "small"
        elif size_description < 50:
            label = "medium"
        elif size_description < 100:
            label = "large"
        else:
            label = "extra-large"
        task.labels.append(label)
        return Success(task)
