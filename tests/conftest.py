import pytest
import json
import yaml
from pathlib import Path

from api.booking_api import BookingAPI


@pytest.fixture(scope="session")
def config():
    config_path = Path(__file__).resolve().parent.parent / "config" / "config.yaml"

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


@pytest.fixture(scope="session")
def booking_api(config):
    return BookingAPI(
        base_url=config["base_url"],
        timeout=config["timeout"]
    )


@pytest.fixture(scope="session")
def auth_token(booking_api):
    response = booking_api.authenticate("admin", "password123")

    assert response.status_code == 200, (
        f"Authentication failed: {response.text}"
    )

    return response.json()["token"]

@pytest.fixture(scope="session")
def booking_data():
    data_path = Path(__file__).resolve().parent.parent / "test_data" / "booking_data.json"

    with open(data_path, "r") as file:
        return json.load(file)