from unittest.mock import Mock

import pytest
from meiga import Success, isFailure
from meiga.assertions import assert_failure, assert_success
from petisco import CrudRepository, DomainEventBus

from app.src.task.retrieve.application.task_retriever import TaskRetriever
from app.src.task.shared.domain.task import Task
from tests.mothers.task_mother import TaskMother
from tests.mothers.uuid_mother import UuidMother


@pytest.mark.unit
class TestTaskRetriever:
    def setup(self):
        self.aggregate_id = UuidMother.any()
        self.mock_respository = Mock(CrudRepository)
        self.mock_respository.retrieve = Mock(return_value=Success(TaskMother.any()))
        self.mock_domain_event_bus = Mock(DomainEventBus)

    def should_success_when_happy_path(self):
        task_retriever = TaskRetriever(
            repository=self.mock_respository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_retriever.execute(self.aggregate_id)
        assert_success(result, value_is_instance_of=Task)

        self.mock_respository.retrieve.assert_called_once()
        self.mock_domain_event_bus.publish.assert_called_once()

    def should_failure_when_repository_fails(self):
        self.mock_respository.retrieve = Mock(return_value=isFailure)

        task_retriever = TaskRetriever(
            repository=self.mock_respository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_retriever.execute(self.aggregate_id)
        assert_failure(result)

        self.mock_respository.retrieve.assert_called_once()
        self.mock_domain_event_bus.publish.assert_not_called()
