import pytest

from app.src.checks.application.healthcheck_controller import HealthCheckController


@pytest.mark.unit
class TestUnitHealthcheck:
    def should_success(self):
        result = HealthCheckController().execute()
        assert isinstance(result, dict)
