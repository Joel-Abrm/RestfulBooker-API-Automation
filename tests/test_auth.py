
import pytest
import allure


@allure.feature("Authentication API")
@allure.story("Valid Authentication")
@allure.title("Verify successful authentication")
def test_valid_authentication(booking_api):
    response = booking_api.authenticate("admin", "password123")

    assert response.status_code == 200

    response_data = response.json()

    assert "token" in response_data
    assert response_data["token"] is not None


@allure.feature("Authentication API")
@allure.story("Invalid Authentication")
@allure.title("Verify authentication fails with invalid credentials")
def test_invalid_authentication(booking_api):
    response = booking_api.authenticate(
        username="wrong_user",
        password="wrong_password"
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["reason"] == "Bad credentials"
