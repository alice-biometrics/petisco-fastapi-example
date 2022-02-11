import pytest
from petisco import assert_http

from app.src.task.shared.domain.task import Task
from tests.mothers.task_mother import TaskMother
from tests.mothers.task_repository_mother import TaskRepositoryMother
from tests.mothers.uuid_mother import UuidMother


@pytest.mark.acceptance
class TestDeleteTask:
    task: Task
    id: str

    def setup(self):
        self.task = TaskMother.any()
        self.id = self.task.aggregate_id.value
        TaskRepositoryMother.with_task(self.task)

    def should_return_200_with_task_when_exist(self, client_app):
        response = client_app.delete(f"/task/{self.id}")
        assert_http(response, 200)

    def should_return_404_when_task_do_not_exist(self, client_app):
        response = client_app.delete(f"/task/{UuidMother.any_str()}")
        assert_http(response, 404)
