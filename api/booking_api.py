
from api.base_api import BaseAPI


class BookingAPI(BaseAPI):

    def authenticate(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        return self.post("/auth", payload)

    def create_booking(self, payload):
        return self.post("/booking", payload)

    def get_booking(self, booking_id):
        return self.get(f"/booking/{booking_id}")

    def update_booking(self, booking_id, payload, token):
        headers = {"Cookie": f"token={token}"}
        return self.put(
            f"/booking/{booking_id}",
            payload,
            headers
        )

    def partial_update_booking(self, booking_id, payload, token):
        headers = {"Cookie": f"token={token}"}
        return self.patch(
            f"/booking/{booking_id}",
            payload,
            headers
        )

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}
        return self.delete(
            f"/booking/{booking_id}",
            headers
        )
