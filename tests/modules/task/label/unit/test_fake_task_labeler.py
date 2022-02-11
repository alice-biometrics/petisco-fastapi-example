import pytest
from meiga.assertions import assert_success

from app.src.task.label.infrastructure.fake_task_labeler import FakeTaskLabeler
from tests.mothers.task_mother import TaskMother


@pytest.mark.integration
class TestSizeTaskLabeler:
    def should_construct_and_execute(self):
        labeler = FakeTaskLabeler()
        task = TaskMother.any()
        result = labeler.execute(task)
        assert_success(result)
