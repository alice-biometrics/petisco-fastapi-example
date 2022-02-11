from meiga import BoolResult, isSuccess
from petisco import CrudRepository, DomainEventBus, UseCase, Uuid

from app.src.task.shared.domain.events import TaskDeleted


class TaskDeleter(UseCase):
    def __init__(
        self,
        repository: CrudRepository,
        domain_event_bus: DomainEventBus,
    ):
        self.repository = repository
        self.domain_event_bus = domain_event_bus

    def execute(self, aggregate_id: Uuid) -> BoolResult:
        self.repository.remove(aggregate_id).unwrap_or_return()
        self.domain_event_bus.publish(TaskDeleted())
        return isSuccess
