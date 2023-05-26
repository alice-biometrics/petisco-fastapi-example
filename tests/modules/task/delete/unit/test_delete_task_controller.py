import pytest
from fastapi.exceptions import HTTPException
from petisco import AggregateNotFoundError, Uuid
from petisco.extra.fastapi import as_fastapi

from app.src.task.delete.application.delete_task_controller import DeleteTaskController
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.unit
class TestDeleteTaskController:
    def setup_method(self):
        TaskRepositoryMother.empty()

    def should_construct_and_execute_http_exception_not_found(self):
        with pytest.raises(HTTPException):
            result = DeleteTaskController().execute(Uuid.v4())
            as_fastapi(result)

    def should_construct_and_execute_fail_when_not_found(self):
        result = DeleteTaskController().execute(Uuid.v4())
        result.assert_failure(value_is_instance_of=AggregateNotFoundError)
