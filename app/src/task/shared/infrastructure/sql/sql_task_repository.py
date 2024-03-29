# from collections.abc import Callable
# from typing import ContextManager

from meiga import BoolResult, Error, Failure, Result, Success, isSuccess
from meiga.decorators import meiga
from petisco import (
    AggregateAlreadyExistError,
    AggregateNotFoundError,
    CrudRepository,
    Uuid,
    databases,
)
from petisco.extra.sqlalchemy import SqlDatabase, SqlSessionScope

# from petisco.base.application.patterns.crud_repository import CrudRepository
# from petisco.base.domain.errors.defaults.already_exists import (
#     AggregateAlreadyExistError,
# )
# from petisco.base.domain.errors.defaults.not_found import AggregateNotFoundError
# from petisco.base.domain.model.uuid import Uuid
from sqlalchemy import select

from app.src.task.shared.domain.task import Task
from app.src.task.shared.infrastructure.sql.sql_task import SqlTask


class SqlTaskRepository(CrudRepository[Task]):
    session_scope: SqlSessionScope

    def __init__(self):
        self.session_scope = databases.get(
            SqlDatabase, alias="sql-tasks"
        ).get_session_scope()

    @meiga
    def save(self, task: Task) -> BoolResult:

        with self.session_scope() as session:
            query = select(SqlTask).where(
                SqlTask.aggregate_id == task.aggregate_id.value
            )
            sql_task = session.execute(query).one_or_none()

            if sql_task:
                return Failure(AggregateAlreadyExistError(task.aggregate_id))

            sql_task = SqlTask.from_domain(task)
            session.add(sql_task)

        return isSuccess

    @meiga
    def retrieve(self, aggregate_id: Uuid) -> Result[Task, Error]:
        with self.session_scope() as session:
            query = select(SqlTask).where(SqlTask.aggregate_id == aggregate_id.value)
            sql_task = session.execute(query).one_or_none()

            if sql_task is None:
                return Failure(AggregateNotFoundError(aggregate_id))

            task = sql_task[0].to_domain()

            return Success(task)

    def update(self, task: Task) -> BoolResult:
        with self.session_scope() as session:
            query = select(SqlTask).where(
                SqlTask.aggregate_id == task.aggregate_id.value
            )
            sql_task = session.execute(query).one_or_none()

            if sql_task is None:
                return Failure(AggregateNotFoundError(task.aggregate_id))

            sql_task = SqlTask.from_domain(task)
            session.add(sql_task)

        return isSuccess

    def remove(self, aggregate_id: Uuid) -> BoolResult:
        with self.session_scope() as session:
            query = select(SqlTask).where(SqlTask.aggregate_id == aggregate_id.value)
            sql_task = session.execute(query).one_or_none()

            if sql_task is None:
                return Failure(AggregateNotFoundError(aggregate_id))

            session.delete(sql_task[0])

        return isSuccess

    def retrieve_all(self) -> Result[list[Task], Error]:
        with self.session_scope() as session:
            query = select(SqlTask)
            sql_tasks = session.execute(query).all()
            tasks = [sql_task[0].to_domain() for sql_task in sql_tasks]

        return Success(tasks)

    def clear(self):
        databases.clear_database(SqlDatabase, alias="sql-tasks")
