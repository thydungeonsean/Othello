import pygame
from game_state import Game
from game_settings import *


class GameManager(object):

    def __init__(self):

        self.game = None
        self.players = {'white': 'human',
                         'black': 'ai'}

    def init(self):

        pygame.init()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.create_game()

    def create_game(self):
        self.game = Game(white_player=self.players['white'], black_player=self.players['black'])
        self.game.init()

    def main(self):

        self.game.main()

        pygame.quit()
