from unittest.mock import Mock

import pytest
from meiga import isFailure
from meiga.assertions import assert_failure, assert_success
from petisco import CrudRepository, DomainEventBus

from app.src.task.create.application.task_creator import TaskCreator
from tests.mothers.task_mother import TaskMother


@pytest.mark.unit
class TestTaskCreator:
    def setup(self):
        self.mock_respository = Mock(CrudRepository)
        self.mock_domain_event_bus = Mock(DomainEventBus)

    def should_success_when_happy_path(self):
        task_creator = TaskCreator(
            repository=self.mock_respository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_creator.execute(TaskMother.any())
        assert_success(result)

        self.mock_respository.save.assert_called_once()
        self.mock_domain_event_bus.publish_list.assert_called_once()

    def should_failure_when_repository_fails(self):
        self.mock_respository.save = Mock(return_value=isFailure)

        task_creator = TaskCreator(
            repository=self.mock_respository,
            domain_event_bus=self.mock_domain_event_bus,
        )

        result = task_creator.execute(TaskMother.any())
        assert_failure(result)

        self.mock_respository.save.assert_called_once()
        self.mock_domain_event_bus.publish_list.assert_not_called()
