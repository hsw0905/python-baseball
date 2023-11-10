from domain.ball import Ball
from domain.ball_status import BallStatus
from domain.exceptions import InvalidBallSize


class Balls:
    SIZE = 3

    def __init__(self, balls: list[Ball]):
        self._validate(balls)
        self._balls = balls

    def get_list(self):
        return self._balls

    def _validate(self, balls: list[Ball]):
        if len(list(set(balls))) != Balls.SIZE:
            raise InvalidBallSize("서로 다른 3개 볼이어야 합니다.")

    def play(self, other: Ball):
        for ball in self._balls:
            result = ball.play(other)
            if result != BallStatus.NOTHING:
                return result
            else:
                continue
        return BallStatus.NOTHING

