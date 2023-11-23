import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models.dependencies import get_test_sign_detector


@pytest.fixture
def client() -> TestClient:
    """
    Gets test client with test sign detector
    """
    app.state.sign_detector = get_test_sign_detector()
    with TestClient(app) as current_client:
        yield current_client
