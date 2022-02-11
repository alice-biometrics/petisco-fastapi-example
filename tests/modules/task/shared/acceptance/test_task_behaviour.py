import pytest
from petisco import assert_http

from tests.mothers.task_json_mother import TaskJsonMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.acceptance
class TestTaskBehaviour:
    def setup(self):
        TaskRepositoryMother.empty()

    def should_success_on_complete_task_execution(self, client_app):
        task_json = TaskJsonMother.any()
        task_id = task_json.get("id")

        response = client_app.post("/task", json=task_json)
        assert_http(response, 200)

        response = client_app.get(f"/task/{task_id}")
        assert_http(response, 200)
        payload = response.json()
        payload.pop("created_at")
        labels = payload.pop("labels")
        assert labels == ["small"]
        assert payload == task_json

        task_json["name"] = "New name"
        response = client_app.patch("/task", json=task_json)
        assert_http(response, 200)

        response = client_app.delete(f"/task/{task_id}")
        assert_http(response, 200)

        response = client_app.get(f"/task/{task_id}")
        assert_http(response, 404)

    # TODO
    # def should_success_when_creates_several_tasks_and_list_them(self, client_app):
    #     expected_tasks = 5
    #     for _ in range(expected_tasks):
    #         client_app.post("/task", json=TaskJsonMother.random())
    #
    #     response = client_app.get(f"/tasks")
    #     assert_http(response, 200)
    #     assert len(response.json()) == expected_tasks
