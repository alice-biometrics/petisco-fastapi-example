import requests
from requests import Response


class Client:
    def __init__(self, host):
        self.host = host

    def healthcheck(self) -> Response:
        response = requests.get(url=f"{self.host}/healthcheck")
        return response

    def post(self, json: dict) -> Response:
        response = requests.post(url=f"{self.host}/task", json=json)
        return response

    def get(self, task_id: str) -> Response:
        response = requests.get(url=f"{self.host}/task/{task_id}")
        return response

    def update(self, json: dict) -> Response:
        response = requests.patch(url=f"{self.host}/task", json=json)
        return response

    def delete(self, task_id: str) -> Response:
        response = requests.delete(url=f"{self.host}/task/{task_id}")
        return response
