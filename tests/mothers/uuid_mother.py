from petisco import Uuid


class UuidMother:
    @staticmethod
    def any() -> Uuid:
        return Uuid.v4()

    @staticmethod
    def any_str() -> str:
        return Uuid.v4().value
