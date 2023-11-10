import random

from domain.game_service import GameService
from domain.number_dto import NumberDto


class GameController:
    def __init__(self, game_service: GameService):
        self._game_service = game_service

    def run(self):
        random_numbers = random.sample(range(1, 10), 3)

        while not self._game_service.is_finish():
            self._game_service.reset()
            print("숫자를 입력해주세요 : ", end="")
            input_number = [int(digit) for digit in input()]

            self._game_service.play(NumberDto(input_number), random_numbers)
            print(self._game_service.report())

        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")

        continue_or_quit = input()

        if continue_or_quit == "1":
            self._game_service.reset()
            self.run()
        elif continue_or_quit == "2":
            return
        else:
            print("[ERROR] - 잘못된 입력")
