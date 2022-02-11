from typing import Dict

from meiga import Error, Result, Success
from petisco.extra.fastapi import FastAPIController

from app import APPLICATION_NAME, APPLICATION_VERSION


class HealthCheckController(FastAPIController):
    def execute(self) -> Result[Dict, Error]:
        healthcheck = {
            "app_name": APPLICATION_NAME,
            "app_version": APPLICATION_VERSION,
        }
        return Success(healthcheck)
