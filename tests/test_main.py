from http import HTTPStatus

from fastapi.testclient import TestClient
from src.main import app
from structlog.testing import capture_logs

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK
    assert response.text == ""


def test_read_main():
    # Example of testing logging using a context manager
    with capture_logs() as cap_logs:
        response = client.get("/")
        assert {"event": "In root path", "log_level": "info"} in cap_logs
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"msg": "Hello World"}
