from domain.exceptions import InvalidBallPosition


class BallPosition:

    MAX_VALUE = 3
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
        if value < BallPosition.MIN_VALUE or value > BallPosition.MAX_VALUE:
            raise InvalidBallPosition("1~3 숫자여야 합니다.")
