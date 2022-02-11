import pytest
from petisco import assert_http


@pytest.mark.acceptance
class TestGetHealthcheck:
    def should_success(self, client_app):
        response = client_app.get(
            "/healthcheck",
        )
        assert_http(response, 200)
