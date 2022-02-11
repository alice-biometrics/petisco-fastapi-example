import pytest

from tests.end2end.client import Client


@pytest.fixture
def client(variables):
    return Client(variables["host"])
