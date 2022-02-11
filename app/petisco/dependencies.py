from typing import List

from petisco import Builder, Dependency, InmemoryCrudRepository
from petisco.extra.rabbitmq import get_rabbitmq_message_dependencies

from app import APPLICATION_NAME, ORGANIZATION
from app.src.task.shared.domain.task import Task
from app.src.task.shared.infrastructure.folder_crud_repository import (
    FolderTaskCrudRepository,
)


def dependencies_provider() -> List[Dependency]:
    repositories = []
    app_services = [
        Dependency(
            name="task_repository",
            default_builder=Builder(InmemoryCrudRepository[Task]),
            envar_modifier="TASK_REPOSITORY_TYPE",
            builders={
                "folder": Builder(
                    FolderTaskCrudRepository, folder="folder_task_database"
                )
            },
        ),
    ]
    message_dependencies = get_rabbitmq_message_dependencies(
        ORGANIZATION, APPLICATION_NAME
    )

    dependencies = repositories + app_services + message_dependencies
    return dependencies
