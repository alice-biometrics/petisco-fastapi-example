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

        filtered_tasks = [
            task for task in response.json()["result"] if task.pop("created_at")
        ]
        expected_tasks = [task for task in [self.task.dict()] if task.pop("created_at")]
        assert filtered_tasks == expected_tasks
