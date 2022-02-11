import os
from uuid import uuid4

import pytest


@pytest.mark.end2end
@pytest.mark.skipif(
    not os.environ.get("END2END_TEST"),
    reason="To run end2end test, please define END2END_TEST envar",
)
def test_user(client):
    task_id = str(uuid4())
    user = dict(name="Task", description="Awesome Task", id=task_id)
    response = client.post(user)
    assert response.status_code == 200, f"Error {response.json()}"

    user["description"] = "Awesome Task and Application"
    response = client.update(user)
    assert response.status_code == 200, f"Error {response.json()}"

    response = client.get(task_id)
    assert response.status_code == 200, f"Error {response.json()}"

    response = client.delete(task_id)
    assert response.status_code == 200, f"Error {response.json()}"
