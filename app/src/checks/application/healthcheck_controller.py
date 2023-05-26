from meiga import Error, Result, Success
from petisco import unwrap_result_handler
from petisco.extra.fastapi import FastAPIController

from app import APPLICATION_NAME, APPLICATION_VERSION


class HealthCheckController(FastAPIController):
    class Config:
        success_handler: unwrap_result_handler

    def execute(self) -> Result[dict, Error]:
        healthcheck = {
            "app_name": APPLICATION_NAME,
            "app_version": APPLICATION_VERSION,
        }
        return Success(healthcheck)
