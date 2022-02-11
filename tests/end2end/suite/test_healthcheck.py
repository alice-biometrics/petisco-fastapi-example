import os

import pytest


@pytest.mark.end2end
@pytest.mark.skipif(
    not os.environ.get("END2END_TEST"),
    reason="To run end2end test, please define END2END_TEST envar",
)
def test_healthcheck_deployment_test(client):
    response = client.healthcheck()
    assert response.status_code == 200, f"Error {response.json()}"
