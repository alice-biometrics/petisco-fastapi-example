from petisco import Container, CrudRepository

from app.src.task.shared.domain.task import Task
from tests.mothers.task_mother import TaskMother


class TaskRepositoryMother:
    @staticmethod
    def empty():
        repository = Container.get(CrudRepository, alias="task_repository")
        repository.clear()
        return repository

    @staticmethod
    def with_task(task: Task = TaskMother.any()):
        repository = TaskRepositoryMother.empty()
        repository.save(task)
        return repository
