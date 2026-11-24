
import requests
from utils.logger import logger


class BaseAPI:

    def __init__(self, base_url, timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint):
        logger.info(f"GET Request: {endpoint}")

        response = self.session.get(
            self.base_url + endpoint,
            timeout=self.timeout
        )

        logger.info(f"GET Response Status: {response.status_code}")
        return response

    def post(self, endpoint, payload):
        logger.info(f"POST Request: {endpoint}")

        response = self.session.post(
            self.base_url + endpoint,
            json=payload,
            timeout=self.timeout
        )

        logger.info(f"POST Response Status: {response.status_code}")
        return response

    def put(self, endpoint, payload, headers=None):
        logger.info(f"PUT Request: {endpoint}")

        response = self.session.put(
            self.base_url + endpoint,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

        logger.info(f"PUT Response Status: {response.status_code}")
        return response

    def patch(self, endpoint, payload, headers=None):
        logger.info(f"PATCH Request: {endpoint}")

        response = self.session.patch(
            self.base_url + endpoint,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

        logger.info(f"PATCH Response Status: {response.status_code}")
        return response

    def delete(self, endpoint, headers=None):
        logger.info(f"DELETE Request: {endpoint}")

        response = self.session.delete(
            self.base_url + endpoint,
            headers=headers,
            timeout=self.timeout
        )

        logger.info(f"DELETE Response Status: {response.status_code}")
        return response
