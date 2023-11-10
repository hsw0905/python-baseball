from domain.game_service import GameService
from domain.number_dto import NumberDto


def test_play_nothing():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [4, 5, 6])

    assert game_service.report() == "낫싱"


def test_play_1_ball():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [2, 5, 6])

    assert game_service.report() == "1볼"


def test_play_2_ball():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [2, 5, 1])

    assert game_service.report() == "2볼"


def test_play_1_strike():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [1, 5, 4])

    assert game_service.report() == "1스트라이크"


def test_play_2_strike():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [1, 2, 4])

    assert game_service.report() == "2스트라이크"


def test_play_1_strike_1_ball():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [1, 5, 2])

    assert game_service.report() == "1볼 1스트라이크"


def test_play_1_strike_2_ball():
    game_service = GameService()

    game_service.play(NumberDto([1, 2, 3]), [1, 3, 2])

    assert game_service.report() == "2볼 1스트라이크"