import pytest

from domain.ball import Ball
from domain.ball_number import BallNumber
from domain.ball_position import BallPosition
from domain.ball_status import BallStatus
from domain.balls import Balls
from domain.exceptions import InvalidBallSize


def test_should_have_3_different_ball():
    ball1 = Ball(BallNumber(1), BallPosition(1))
    ball2 = Ball(BallNumber(1), BallPosition(1))
    ball3 = Ball(BallNumber(2), BallPosition(1))

    with pytest.raises(InvalidBallSize):
        Balls([ball1, ball2, ball3])


def test_play_nothing(computer_balls):
    ball = Ball(BallNumber(4), BallPosition(1))

    assert computer_balls.play(ball) == BallStatus.NOTHING


def test_play_ball(computer_balls):
    ball = Ball(BallNumber(2), BallPosition(1))

    assert computer_balls.play(ball) == BallStatus.BALL


def test_play_strike(computer_balls):
    ball = Ball(BallNumber(2), BallPosition(2))

    assert computer_balls.play(ball) == BallStatus.STRIKE
