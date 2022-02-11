from meiga import Error, Result, Success
from petisco import CrudRepository, DomainEventBus, UseCase, Uuid

from app.src.task.shared.domain.events import TaskRetrieved
from app.src.task.shared.domain.task import Task


class TaskRetriever(UseCase):
    def __init__(
        self,
        repository: CrudRepository,
        domain_event_bus: DomainEventBus,
    ):
        self.repository = repository
        self.domain_event_bus = domain_event_bus

    def execute(self, aggregate_id: Uuid) -> Result[Task, Error]:
        task = self.repository.retrieve(aggregate_id).unwrap_or_return()
        self.domain_event_bus.publish(TaskRetrieved())
        return Success(task)
