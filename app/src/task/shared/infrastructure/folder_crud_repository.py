import json
import os
import shutil
from os import listdir
from os.path import isfile, join
from pathlib import Path

from meiga import BoolResult, Error, Failure, Result, Success, isSuccess
from meiga.decorators import meiga
from petisco.base.application.patterns.crud_repository import (
    AggregateRootType,
    CrudRepository,
)
from petisco.base.domain.errors.defaults.already_exists import (
    AggregateAlreadyExistError,
)
from petisco.base.domain.errors.defaults.not_found import AggregateNotFoundError
from petisco.base.domain.model.uuid import Uuid

from app.src.task.shared.domain.task import Task


class FolderTaskCrudRepository(CrudRepository[Task]):
    def __init__(self, folder: str):
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)

    def _get_data(self) -> dict[Uuid, Task]:
        filenames = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
        data = {}
        for filename in filenames:
            with open(f"{self.folder}/{filename}") as file:
                json_object = json.load(file)
                # TODO: review (New Petisco)
                aggregate_id = Uuid(json_object["aggregate_id"])
                json_object["aggregate_id"] = aggregate_id
                data[aggregate_id] = Task(**json_object)
        return data

    def _write(self, aggregate_root: Task):
        path = Path(f"{self.folder}/{aggregate_root.aggregate_id.value}.json")
        path.write_text(aggregate_root.json())

    def _remove(self, aggregate_id: Uuid):
        path = Path(f"{self.folder}/{aggregate_id.value}.json")
        path.unlink()

    @meiga
    def save(self, aggregate_root: Task) -> BoolResult:
        data = self._get_data()
        if aggregate_root.aggregate_id in data:
            return Failure(AggregateAlreadyExistError(aggregate_root.aggregate_id))
        self._write(aggregate_root)
        return isSuccess

    @meiga
    def retrieve(self, aggregate_id: Uuid) -> Result[Task, Error]:
        data = self._get_data()
        aggregate_root = data.get(aggregate_id)
        if aggregate_root is None:
            return Failure(AggregateNotFoundError(aggregate_id))
        return Success(aggregate_root)

    def update(self, aggregate_root: Task) -> BoolResult:
        data = self._get_data()
        if aggregate_root.aggregate_id not in data:
            return Failure(AggregateNotFoundError(aggregate_root.aggregate_id))
        self._write(aggregate_root)
        return isSuccess

    def remove(self, aggregate_id: Uuid) -> BoolResult:
        data = self._get_data()
        if aggregate_id not in data:
            return Failure(AggregateNotFoundError(aggregate_id))
        self._remove(aggregate_id)
        return isSuccess

    def retrieve_all(self) -> Result[list[AggregateRootType], Error]:
        data = self._get_data()
        return Success(list(data.values()))

    def clear(self):
        shutil.rmtree(self.folder)
        os.makedirs(self.folder, exist_ok=True)
