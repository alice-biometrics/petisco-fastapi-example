import pytest
from petisco import assert_http

from app.src.task.shared.domain.task import Task
from tests.mothers.task_json_mother import TaskJsonMother
from tests.mothers.task_mother import TaskMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.acceptance
class TestPatchTask:
    task: Task
    id: str

    def setup_method(self):
        self.task = TaskMother.any()
        self.id = self.task.aggregate_id.value
        TaskRepositoryMother.with_task(self.task)

    def should_success_with_any_valid_json(self, client_app):
        response = client_app.patch("/task", json=TaskJsonMother.with_id(self.id))
        assert_http(response, 200)

    def q(self, client_app):
        response = client_app.patch("/task", json=TaskJsonMother.any())
        assert_http(response, 404)
