import pytest

from domain.ball_number import BallNumber
from domain.exceptions import InvalidBallNumber


def test_should_have_range_in_1_to_9():
    edge_values = [0, -1, 10]
    for value in edge_values:
        with pytest.raises(InvalidBallNumber):
            BallNumber(value)

