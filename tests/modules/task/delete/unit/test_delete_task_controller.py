import pytest
from fastapi.exceptions import HTTPException
from petisco import Uuid

from app.src.task.delete.application.delete_task_controller import DeleteTaskController
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.unit
class TestDeleteTaskController:
    def setup_method(self):
        TaskRepositoryMother.empty()

    def should_construct_and_execute_http_exception_not_found(self):
        with pytest.raises(HTTPException):
            DeleteTaskController().execute(Uuid.v4())
