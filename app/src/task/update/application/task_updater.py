from meiga import BoolResult, isSuccess
from petisco import CrudRepository, DomainEventBus, UseCase

from app.src.task.shared.domain.task import Task


class TaskUpdater(UseCase):
    def __init__(
        self,
        repository: CrudRepository,
        domain_event_bus: DomainEventBus,
    ):
        self.repository = repository
        self.domain_event_bus = domain_event_bus

    def execute(
        self,
        task: Task,
    ) -> BoolResult:
        self.repository.update(task).unwrap_or_return()
        self.domain_event_bus.publish_list(task.pull_domain_events())
        return isSuccess
