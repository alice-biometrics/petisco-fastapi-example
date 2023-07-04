from petisco import Builder, CrudRepository, Dependency, InmemoryCrudRepository
from petisco.extra.rabbitmq import get_rabbitmq_message_dependencies

from app import APPLICATION_NAME, ORGANIZATION
from app.src.task.label.domain.task_labeler import TaskLabeler
from app.src.task.label.infrastructure.fake_task_labeler import FakeTaskLabeler
from app.src.task.label.infrastructure.size_task_labeler import SizeTaskLabeler
from app.src.task.shared.domain.task import Task
from app.src.task.shared.infrastructure.folder_task_repository import (
    FolderTaskRepository,
)
from app.src.task.shared.infrastructure.sql.sql_task_repository import SqlTaskRepository


def dependencies_provider() -> list[Dependency]:
    repositories = [
        Dependency(
            CrudRepository,
            alias="task_repository",
            envar_modifier="TASK_REPOSITORY_TYPE",
            builders={
                "default": Builder(InmemoryCrudRepository[Task]),
                "sql": Builder(SqlTaskRepository),
                "folder": Builder(FolderTaskRepository, folder="folder_task_database"),
            },
        )
    ]
    app_services = [
        Dependency(
            TaskLabeler,
            envar_modifier="TASK_LABELER_TYPE",
            builders={
                "default": Builder(SizeTaskLabeler),
                "fake": Builder(FakeTaskLabeler),
            },
        ),
    ]

    message_dependencies = get_rabbitmq_message_dependencies(
        ORGANIZATION, APPLICATION_NAME
    )

    dependencies = repositories + app_services + message_dependencies
    return dependencies
