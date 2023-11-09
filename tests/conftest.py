import pytest

from domain.ball import Ball
from domain.ball_number import BallNumber
from domain.ball_position import BallPosition
from domain.balls import Balls


@pytest.fixture
def computer_balls():
    ball1 = Ball(BallNumber(1), BallPosition(1))
    ball2 = Ball(BallNumber(2), BallPosition(2))
    ball3 = Ball(BallNumber(3), BallPosition(3))

    return Balls([ball1, ball2, ball3])
