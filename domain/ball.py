from domain.ball_number import BallNumber
from domain.ball_position import BallPosition
from domain.ball_status import BallStatus


class Ball:
    def __init__(self, number: BallNumber, position: BallPosition):
        self._number = number
        self._position = position

    def __eq__(self, other):
        return self._number == other.number and self._position == other.position

    def __hash__(self):
        return hash((self._number, self._position))

    @property
    def number(self):
        return self._number

    @property
    def position(self):
        return self._position

    def play(self, other) -> BallStatus:
        if (self._number == other.number
                and self._position == other.position):
            return BallStatus.STRIKE
        elif self._number == other.number:
            return BallStatus.BALL
        else:
            return BallStatus.NOTHING
