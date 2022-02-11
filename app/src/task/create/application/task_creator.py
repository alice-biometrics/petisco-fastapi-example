from meiga import BoolResult, isSuccess
from petisco import CrudRepository, DomainEventBus, UseCase

from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.shared.domain.task import Task


class TaskCreator(UseCase):
    def __init__(
        self,
        labeler: TaskLabeler,
        repository: CrudRepository,
        domain_event_bus: DomainEventBus,
    ):
        self.labeler = labeler
        self.repository = repository
        self.domain_event_bus = domain_event_bus

    def execute(
        self,
        task: Task,
    ) -> BoolResult:
        task = self.labeler.execute(task).unwrap_or_return()
        self.repository.save(task).unwrap_or_return()
        self.domain_event_bus.publish_list(task.pull_domain_events())
        return isSuccess
