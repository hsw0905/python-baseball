from domain.ball import Ball
from domain.ball_number import BallNumber
from domain.ball_position import BallPosition
from domain.ball_status import BallStatus


def test_equal():
    ball1 = Ball(BallNumber(1), BallPosition(1))
    ball2 = Ball(BallNumber(1), BallPosition(1))

    assert ball1 == ball2


def test_play_nothing():
    computer = Ball(BallNumber(1), BallPosition(1))
    user = Ball(BallNumber(2), BallPosition(1))

    assert computer.play(user) == BallStatus.NOTHING


def test_play_ball():
    computer = Ball(BallNumber(1), BallPosition(1))
    user = Ball(BallNumber(1), BallPosition(2))

    assert computer.play(user) == BallStatus.BALL


def test_play_strike():
    computer = Ball(BallNumber(1), BallPosition(1))
    user = Ball(BallNumber(1), BallPosition(1))

    assert computer.play(user) == BallStatus.STRIKE
