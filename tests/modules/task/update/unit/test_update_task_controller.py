import pytest
from fastapi.exceptions import HTTPException

from app.src.task.update.application.update_task_controller import UpdateTaskController
from tests.mothers.task_mother import TaskMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.unit
class TestUpdateTaskController:
    def setup_method(self):
        TaskRepositoryMother.empty()

    def should_construct_and_execute_with_http_exception_not_found(self):
        with pytest.raises(HTTPException):
            task = TaskMother.any()
            UpdateTaskController().execute(task)
