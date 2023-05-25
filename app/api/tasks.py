from uuid import UUID

from fastapi import APIRouter
from petisco import Uuid

from app.api.models import TaskIn, TaskOut
from app.src.task.create.application.create_task_controller import CreateTaskController
from app.src.task.delete.application.delete_task_controller import DeleteTaskController
from app.src.task.retrieve.application.retrieve_task_controller import (
    RetrieveTaskController,
)
from app.src.task.retrieve_all.application.retrieve_all_tasks_controller import (
    RetrieveAllTasksController,
)
from app.src.task.update.application.update_task_controller import UpdateTaskController

router = APIRouter(tags=["Tasks"])


@router.post("/task")
async def create_task(task: TaskIn):
    return CreateTaskController().execute(task.to_task())


@router.get("/task/{id}", response_model=TaskOut)
async def retrieve_task(id: UUID):
    aggregate_id = Uuid(str(id))
    return RetrieveTaskController().execute(aggregate_id)


@router.get("/tasks")
async def retrieve_all_tasks():
    return RetrieveAllTasksController().execute()


@router.patch("/task")
async def update_task(task: TaskIn):
    return UpdateTaskController().execute(task.to_task())


@router.delete("/task/{id}")
async def delete_task(id: UUID):
    aggregate_id = Uuid(str(id))
    return DeleteTaskController().execute(aggregate_id)
