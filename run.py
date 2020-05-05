

from src.game import Game
from time import sleep


if __name__ == "__main__":
    game = Game()

    print("Starting New game")
    sleep(3)

    game.run()