import pytest

from app.src.task.create.application.create_task_controller import CreateTaskController
from tests.mothers.task_mother import TaskMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.unit
class TestCreateTaskController:
    def setup(self):
        TaskRepositoryMother.empty()

    def should_construct_and_execute(self):
        task = TaskMother.any()
        CreateTaskController().execute(task)
