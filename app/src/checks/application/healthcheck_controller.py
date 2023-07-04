from meiga import Error, Result, Success
from petisco.extra.fastapi import FastAPIController
from pydantic import ConfigDict

from app import APPLICATION_NAME, APPLICATION_VERSION


class HealthCheckController(FastAPIController):
    model_config = ConfigDict()

    def execute(self) -> Result[dict, Error]:
        healthcheck = {
            "app_name": APPLICATION_NAME,
            "app_version": APPLICATION_VERSION,
        }
        return Success(healthcheck)
