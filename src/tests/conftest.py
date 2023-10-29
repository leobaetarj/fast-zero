import pytest
from fastapi.testclient import TestClient

from src.application.app import app


@pytest.fixture
def client():
    return TestClient(app)
