import os

import pytest

if os.getenv("END2END_TEST"):
    from tests.end2end.fixtures import *
else:
    from fastapi.testclient import TestClient

    from app.application import application

    application.configure(testing=True)
    test_app = application.get_app()

    @pytest.fixture
    def client_app():
        return TestClient(test_app)
