from domain.game_controller import GameController
from domain.game_service import GameService

if __name__ == "__main__":
    controller = GameController(GameService())
    controller.run()
