import pytest
from petisco.extra.fastapi import as_fastapi

from app.src.checks.application.healthcheck_controller import HealthCheckController


@pytest.mark.unit
class TestUnitHealthcheck:
    def should_success(self):
        result = HealthCheckController().execute()
        result = as_fastapi(result)
        assert isinstance(result, dict)
