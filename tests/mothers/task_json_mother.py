from petisco import Uuid


class TaskJsonMother:
    @staticmethod
    def any(name: str = "string", description: str = "string") -> dict:
        return {
            "name": name,
            "description": description,
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        }

    @staticmethod
    def with_id(id: str) -> dict:
        return {
            "name": "string",
            "description": "string",
            "id": id,
        }

    @staticmethod
    def random() -> dict:
        return {
            "name": "string",
            "description": "string",
            "id": Uuid.v4().value,
        }

    @staticmethod
    def without_id(name: str = "string", description: str = "string") -> dict:
        return {
            "name": name,
            "description": description,
        }

    @staticmethod
    def invalid() -> dict:
        return {}
