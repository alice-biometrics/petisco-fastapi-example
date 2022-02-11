from unittest.mock import Mock

import pytest
from meiga import isFailure
from meiga.assertions import assert_failure, assert_success
from petisco import CrudRepository, DomainEventBus, Uuid

from app.src.task.delete.application.task_deleter import TaskDeleter
from tests.mothers.uuid_mother import UuidMother


@pytest.mark.unit
class TestTaskDeleter:
    aggregate_id: Uuid
    mock_repository: Mock
    mock_domain_event_bus: Mock

    def setup(self):
        self.aggregate_id = UuidMother.any()
        self.mock_repository = Mock(CrudRepository)
        self.mock_domain_event_bus = Mock(DomainEventBus)

    def should_success_when_happy_path(self):
        task_deleter = TaskDeleter(
            repository=self.mock_repository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_deleter.execute(self.aggregate_id)
        assert_success(result)

        self.mock_respository.remove.assert_called_once()
        self.mock_domain_event_bus.publish.assert_called_once()

    def should_failure_when_repository_fails(self):
        self.mock_respository.remove = Mock(return_value=isFailure)

        task_deleter = TaskDeleter(
            repository=self.mock_repository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_deleter.execute(self.aggregate_id)
        assert_failure(result)

        self.mock_respository.remove.assert_called_once()
        self.mock_domain_event_bus.publish.assert_not_called()
