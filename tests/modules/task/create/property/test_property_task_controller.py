import pytest
from fastapi.exceptions import HTTPException
from hypothesis import given
from hypothesis import strategies as st

from app.src.task.create.application.create_task_controller import CreateTaskController
from tests.mothers.task_mother import TaskMother
from tests.mothers.task_repository_mother import TaskRepositoryMother


@pytest.mark.property
class TestPropertyCreateTaskController:
    def setup_method(self):
        TaskRepositoryMother.empty()

    def teardown_method(self):
        TaskRepositoryMother.empty()

    @given(st.text(), st.text())
    def should_construct_and_execute(self, name, description):
        task = TaskMother.random(name, description)
        try:
            result = CreateTaskController().execute(task)
            assert isinstance(result, dict)
        except HTTPException as exc:
            assert exc.status_code == 422
