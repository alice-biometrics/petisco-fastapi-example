import requests
from requests import Response


class Client:
    def __init__(self, host):
        self.host = host

    def healthcheck(self) -> Response:
        response = requests.get(url=self.host + "/healthcheck")
        return response
