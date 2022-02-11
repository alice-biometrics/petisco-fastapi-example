import pytest
from meiga.assertions import assert_success

from app.src.task.label.infrastructure.size_task_labeler import SizeTaskLabeler
from app.src.task.shared.domain.task import Task
from tests.mothers.task_mother import TaskMother


@pytest.mark.integration
class TestSizeTaskLabeler:
    def _assert_label(self, task: Task, expected_label: str):
        label = task.labels.pop()
        assert label == expected_label

    @pytest.mark.parametrize(
        "description,expected_label",
        [
            ("o", "small"),
            ("o" * 11, "medium"),
            ("o" * 51, "large"),
            ("o" * 101, "extra-large"),
        ],
    )
    def should_construct_and_execute(self, description, expected_label):
        labeler = SizeTaskLabeler()
        task = TaskMother.any(description=description)
        result = labeler.execute(task)
        assert_success(result)
        task = result.unwrap()
        self._assert_label(task, expected_label)
