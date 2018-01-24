import sys
from game_manager import GameManager


def main():

    game = GameManager()
    game.init()
    game.main()

    sys.exit()
