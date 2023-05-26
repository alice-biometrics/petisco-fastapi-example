from petisco import SqlBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.src.task.shared.domain.task import Task


class SqlTask(SqlBase[Task]):

    __tablename__ = "Task"

    id: Mapped[int] = Column(Integer, primary_key=True)

    aggregate_id: Mapped[str] = Column(String(36))
    name: Mapped[str] = Column(String(50))
    description: Mapped[str] = Column(String(200))
    # created_at: Mapped[datetime] = Column(String(200)))
    # labels: list[str] | None = list()

    def to_domain(self) -> Task:
        return Task(
            name=self.name, description=self.description, aggregate_id=self.aggregate_id
        )

    @staticmethod
    def from_domain(task: Task) -> "SqlTask":
        return SqlTask(
            name=task.name, description=task.description, aggregate_id=task.aggregate_id
        )
