
import pytest
import allure


@allure.feature("Booking API")
@allure.story("Create Booking")
@allure.title("Verify successful booking creation")
def test_create_booking(booking_api, booking_data):
    payload = booking_data["valid_booking"]

    response = booking_api.create_booking(payload)

    assert response.status_code == 200

    response_data = response.json()

    assert "bookingid" in response_data
    assert response_data["booking"]["firstname"] == payload["firstname"]
    assert response_data["booking"]["lastname"] == payload["lastname"]


@allure.feature("Booking API")
@allure.story("Get Booking")
@allure.title("Verify retrieving an existing booking")
def test_get_booking(booking_api):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    response = booking_api.get_booking(booking_id)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Joel"
    assert response.json()["lastname"] == "Tester"


@allure.feature("Booking API")
@allure.story("Update Booking")
@allure.title("Verify full booking update")
def test_update_booking(booking_api, auth_token):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    updated_payload = {
        "firstname": "Joel Updated",
        "lastname": "Tester",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-15"
        },
        "additionalneeds": "Lunch"
    }

    response = booking_api.update_booking(
        booking_id,
        updated_payload,
        auth_token
    )

    assert response.status_code == 200
    assert response.json()["firstname"] == "Joel Updated"
    assert response.json()["totalprice"] == 200


@allure.feature("Booking API")
@allure.story("Partial Update Booking")
@allure.title("Verify partial booking update")
def test_partial_update_booking(booking_api, auth_token):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    updated_payload = {
        "firstname": "Joel Updated"
    }

    response = booking_api.partial_update_booking(
        booking_id,
        updated_payload,
        auth_token
    )

    assert response.status_code == 200
    assert response.json()["firstname"] == "Joel Updated"
    assert response.json()["lastname"] == "Tester"
    assert response.json()["totalprice"] == 150


@allure.feature("Booking API")
@allure.story("Delete Booking")
@allure.title("Verify booking deletion")
def test_delete_booking(booking_api, auth_token):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    response = booking_api.delete_booking(booking_id, auth_token)

    assert response.status_code == 201

    get_response = booking_api.get_booking(booking_id)

    assert get_response.status_code == 404


@allure.feature("Booking API")
@allure.story("Negative Testing")
@allure.title("Verify error for nonexistent booking")
def test_get_nonexistent_booking(booking_api):
    response = booking_api.get_booking(-1)

    assert response.status_code == 404


@allure.feature("Booking API")
@allure.story("Negative Testing")
@allure.title("Verify update fails with invalid token")
def test_update_booking_with_invalid_token(booking_api):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    response = booking_api.update_booking(
        booking_id,
        payload,
        "invalid-token"
    )

    assert response.status_code == 403


@allure.feature("Booking API")
@allure.story("Negative Testing")
@allure.title("Verify partial update fails with invalid token")
def test_partial_update_with_invalid_token(booking_api):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    response = booking_api.partial_update_booking(
        booking_id,
        {"firstname": "Updated"},
        "invalid-token"
    )

    assert response.status_code == 403


@allure.feature("Booking API")
@allure.story("Negative Testing")
@allure.title("Verify deletion fails with invalid token")
def test_delete_booking_with_invalid_token(booking_api):
    payload = {
        "firstname": "Joel",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = booking_api.create_booking(payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    response = booking_api.delete_booking(
        booking_id,
        "invalid-token"
    )

    assert response.status_code == 403


@allure.feature("Booking API")
@allure.story("Parameterized Testing")
@allure.title("Verify booking creation for multiple users")
@pytest.mark.parametrize(
    "firstname, lastname",
    [
        ("Joel", "Tester"),
        ("John", "Smith"),
        ("David", "Brown")
    ]
)
def test_create_booking_multiple_users(
    booking_api, firstname, lastname
):
    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = booking_api.create_booking(payload)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["booking"]["firstname"] == firstname
    assert response_data["booking"]["lastname"] == lastname
