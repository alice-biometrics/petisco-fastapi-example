import pytest
from petisco import assert_http

from app.src.task.shared.domain.task import Task
from tests.mothers.task_mother import TaskMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.acceptance
class TestGetTasks:
    task: Task
    id: str

    def setup_method(self):
        self.task = TaskMother.any()
        self.id = self.task.aggregate_id.value
        TaskRepositoryMother.with_task(self.task)

    def should_return_200(self, client_app):
        response = client_app.get("/tasks")
        assert_http(response, 200)
        assert response.json()["result"] == [self.task.dict()]
