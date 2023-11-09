from domain.exceptions import InvalidBallNumber


class BallNumber:
    MAX_VALUE = 9
    MIN_VALUE = 1

    def __init__(self, value: int):
        self._validate(value)
        self._value = value

    def __eq__(self, other):
        return self._value == other.value

    def __hash__(self):
        return hash(self._value)

    @property
    def value(self):
        return self._value

    def _validate(self, value):
        if value < BallNumber.MIN_VALUE or value > BallNumber.MAX_VALUE:
            raise InvalidBallNumber("1~9 숫자여야 합니다.")
