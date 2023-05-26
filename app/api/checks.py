from fastapi import APIRouter, Request
from petisco.extra.fastapi import as_fastapi

from app.src.checks.application.healthcheck_controller import HealthCheckController

router = APIRouter()


@router.get("/healthcheck", tags=["Checks"])
def healthcheck(request: Request):
    result = HealthCheckController().execute()
    return as_fastapi(result)
