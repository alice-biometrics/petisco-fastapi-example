import pytest
from petisco import assert_http

from app.src.task.shared.domain.task import Task
from tests.mothers.task_json_mother import TaskJsonMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.acceptance
class TestPostTask:
    task: Task
    id: str

    def setup_method(self):
        TaskRepositoryMother.empty()

    def should_success_with_any_valid_json(self, client_app):
        json = TaskJsonMother.any()
        response = client_app.post("/task", json=json)
        assert_http(response, 200)

    def should_success_with_valid_json_without_id(self, client_app):
        json = TaskJsonMother.without_id()
        response = client_app.post("/task", json=json)
        assert_http(response, 200)

    def should_failure_when_given_an_invalid_json(self, client_app):
        json = TaskJsonMother.invalid()
        response = client_app.post("/task", json=json)
        assert_http(response, 422)

    def should_failure_when_save_twice(self, client_app):
        json = TaskJsonMother.any()
        response = client_app.post("/task", json=json)
        assert_http(response, 200)
        response = client_app.post("/task", json=json)
        assert_http(response, 409)

    def should_failure_when_long_name_is_given(self, client_app):
        json = TaskJsonMother.any("long-name" * 10)
        response = client_app.post("/task", json=json)
        assert_http(response, 422)

    def should_failure_when_long_description_is_given(self, client_app):
        json = TaskJsonMother.any("long-description" * 100)
        response = client_app.post("/task", json=json)
        assert_http(response, 422)
