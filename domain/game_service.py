from domain.ball import Ball
from domain.ball_number import BallNumber
from domain.ball_position import BallPosition
from domain.ball_status import BallStatus
from domain.balls import Balls
from domain.number_dto import NumberDto


class GameService:
    MAX_STRIKE_COUNT = 3

    def __init__(self):
        self._strike = 0
        self._ball = 0

    def play(self, dto: NumberDto, random_numbers: list[int]):

        computer = self._to_balls(random_numbers)
        user = self._to_balls(dto.numbers)

        for ball in user.get_list():
            result = computer.play(ball)
            if result == BallStatus.STRIKE:
                self._strike += 1
            elif result == BallStatus.BALL:
                self._ball += 1

    def _to_balls(self, numbers: list[int]):
        result = []
        positions = [1, 2, 3]

        for number, position in zip(numbers, positions):
            result.append(Ball(BallNumber(number), BallPosition(position)))

        return Balls(result)

    def report(self):
        if self._strike != 0 and self._ball != 0:
            return f"{self._ball}볼 {self._strike}스트라이크"
        elif self._strike == 0 and self._ball != 0:
            return f"{self._ball}볼"
        elif self._strike != 0 and self._ball == 0:
            return f"{self._strike}스트라이크"
        else:
            return "낫싱"

    def reset(self):
        self._strike = 0
        self._ball = 0

    def is_finish(self):
        return self._strike == GameService.MAX_STRIKE_COUNT
