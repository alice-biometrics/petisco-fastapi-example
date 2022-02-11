from fastapi import APIRouter, Request

from app.src.checks.application.healthcheck_controller import HealthCheckController

router = APIRouter()


@router.get("/healthcheck", tags=["Checks"])
def healthcheck(request: Request):
    return HealthCheckController().execute()
