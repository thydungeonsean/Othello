import pygame
from game_settings import BOARD_Y_OFFSET, TILE_WIDTH
from colors import *


class GameBoard(object):

    width = 8
    height = 8

    def __init__(self, state):

        self.board_topleft = (0, BOARD_Y_OFFSET)
        self.tile_surface = self.initialize_tile_surface()
        self.board_surface = self.initialize_board_surface()

    def initialize_tile_surface(self):
        tile = pygame.Surface((TILE_WIDTH, TILE_WIDTH)).convert()
        tile.fill(BOARD_COLOR_DARK)
        return tile

    def initialize_board_surface(self):

        cls = GameBoard
        board = pygame.Surface((cls.width*TILE_WIDTH, cls.height*TILE_WIDTH)).convert()
        board.fill(BOARD_COLOR_LIGHT)

        for y in range(0, GameBoard.height, 2):
            for x in range(0, GameBoard.width):
                coord = (x * TILE_WIDTH, (y + x % 2)*TILE_WIDTH)
                board.blit(self.tile_surface, coord)

        return board

    def draw(self, surface):

        surface.blit(self.board_surface, self.board_topleft)
