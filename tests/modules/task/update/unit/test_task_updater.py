from unittest.mock import Mock

import pytest
from meiga import isFailure
from meiga.assertions import assert_failure, assert_success
from petisco import CrudRepository, DomainEventBus

from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.update.application.task_updater import TaskUpdater
from tests.mothers.task_mother import TaskMother


@pytest.mark.unit
class TestTaskUpdater:
    mock_labeler: Mock
    mock_repository: Mock
    mock_domain_event_bus: Mock

    def setup_method(self):
        self.mock_labeler = Mock(TaskLabeler)
        self.mock_repository = Mock(CrudRepository)
        self.mock_domain_event_bus = Mock(DomainEventBus)

    def should_success_when_happy_path(self):
        task_updater = TaskUpdater(
            labeler=self.mock_labeler,
            repository=self.mock_repository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_updater.execute(TaskMother.any())
        assert_success(result)

        self.mock_labeler.execute.assert_called_once()
        self.mock_repository.update.assert_called_once()
        self.mock_domain_event_bus.publish.assert_called_once()

    def should_failure_when_labeler_fails(self):
        self.mock_labeler.execute = Mock(return_value=isFailure)

        task_updater = TaskUpdater(
            labeler=self.mock_labeler,
            repository=self.mock_repository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_updater.execute(TaskMother.any())
        assert_failure(result)

        self.mock_labeler.execute.assert_called_once()
        self.mock_repository.update.assert_not_called()
        self.mock_domain_event_bus.publish.assert_not_called()

    def should_failure_when_repository_fails(self):
        self.mock_repository.update = Mock(return_value=isFailure)

        task_updater = TaskUpdater(
            labeler=self.mock_labeler,
            repository=self.mock_repository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_updater.execute(TaskMother.any())
        assert_failure(result)

        self.mock_labeler.execute.assert_called_once()
        self.mock_repository.update.assert_called_once()
        self.mock_domain_event_bus.publish.assert_not_called()
