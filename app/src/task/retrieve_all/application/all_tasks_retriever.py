from typing import List

from meiga import Error, Result, Success
from petisco import CrudRepository, UseCase

from app.src.task.shared.domain.task import Task


class AllTasksRetriever(UseCase):
    def __init__(
        self,
        repository: CrudRepository,
    ):
        self.repository = repository

    def execute(self) -> Result[List[Task], Error]:
        tasks = self.repository.retrieve_all().unwrap_or_return()
        return Success(tasks)
