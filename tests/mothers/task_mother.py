from petisco import Uuid

from app.src.task.shared.domain.task import Task


class TaskMother:
    @staticmethod
    def any(name: str = "MyTaskName", description: str = "MyTaskDescription") -> Task:
        return Task.create(
            aggregate_id=Uuid("17b37cdc-027b-4fdb-bdbe-b72ced9744b9"),
            name=name,
            description=description,
        )

    @staticmethod
    def updated(
        name: str = "MyTaskName", description: str = "MyTaskDescription"
    ) -> Task:
        return Task.update(
            aggregate_id=Uuid("17b37cdc-027b-4fdb-bdbe-b72ced9744b9"),
            name=name,
            description=description,
        )

    @staticmethod
    def random(
        name: str = "MyTaskName", description: str = "MyTaskDescription"
    ) -> Task:
        return Task.create(
            aggregate_id=Uuid.v4(),
            name=name,
            description=description,
        )
