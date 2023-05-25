from typing import List

from meiga import Error, Result
from petisco import Container, CrudRepository
from petisco.extra.fastapi import FastAPIController

from app.src.task.retrieve_all.application.all_tasks_retriever import AllTasksRetriever
from app.src.task.shared.domain.task import Task


class RetrieveAllTasksController(FastAPIController):
    def execute(self) -> Result[List[Task], Error]:
        return AllTasksRetriever(
            repository=Container.get(CrudRepository, alias="task_repository")
        ).execute()
