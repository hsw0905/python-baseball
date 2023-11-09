import pytest

from domain.ball_position import BallPosition
from domain.exceptions import InvalidBallPosition


def test_should_have_range_in_1_to_3():
    edge_values = [0, -1, 4]
    for value in edge_values:
        with pytest.raises(InvalidBallPosition):
            BallPosition(value)
