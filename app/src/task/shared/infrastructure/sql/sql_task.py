from datetime import datetime

from petisco import SqlBase, Uuid
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.src.task.shared.domain.task import Task


class SqlTask(SqlBase[Task]):

    __tablename__ = "Task"

    id: Mapped[int] = Column(Integer, primary_key=True)

    aggregate_id: Mapped[str] = Column(String(36))
    name: Mapped[str] = Column(String(50))
    description: Mapped[str] = Column(String(200))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.utcnow()
    )
    # labels: list[str] | None = list()

    def to_domain(self) -> Task:
        return Task(
            name=self.name,
            description=self.description,
            aggregate_id=Uuid(self.aggregate_id),
            created_at=self.created_at,
        )

    @staticmethod
    def from_domain(task: Task) -> "SqlTask":
        return SqlTask(
            name=task.name,
            description=task.description,
            aggregate_id=task.aggregate_id.value,
            created_at=task.created_at,
        )
