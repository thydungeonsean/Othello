import pygame
from game_settings import BOARD_Y_OFFSET, TILE_WIDTH
from colors import *
from random import randint


class GameBoard(object):

    width = 8
    height = 8

    EMPTY = 0
    WHITE_PIECE = 1
    BLACK_PIECE = 2

    def __init__(self, state):

        self.board_topleft = (0, BOARD_Y_OFFSET)
        self.tile_surface = self.initialize_tile_surface()
        self.board_surface = self.initialize_board_surface()

        cls = GameBoard
        self.grid = [[randint(0, 2) for y in range(cls.height)] for x in range(cls.width)]

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

        cls = GameBoard
        for cell in ((x, y) for y in range(cls.height) for x in range(cls.width)):
            self.draw_cell(surface, cell)

    def draw_cell(self, surface, (x, y)):

        if self.grid[x][y] == GameBoard.WHITE_PIECE:
            self.draw_white_piece(surface, (x, y))
        elif self.grid[x][y] == GameBoard.BLACK_PIECE:
            self.draw_black_piece(surface, (x, y))

    def draw_piece(self, surface, (x, y), fore_color, back_color):
        grid_coord = (x * TILE_WIDTH, y * TILE_WIDTH + BOARD_Y_OFFSET)
        self.draw_piece_back(surface, grid_coord, back_color)
        self.draw_piece_front(surface, grid_coord, fore_color)

    def draw_white_piece(self, surface, (x, y)):
        self.draw_piece(surface, (x, y), WHITE_MAIN, WHITE_HIGHLIGHT)

    def draw_black_piece(self, surface, (x, y)):
        self.draw_piece(surface, (x, y), BLACK_MAIN, BLACK_HIGHLIGHT)

    def draw_piece_back(self, surface, (x, y), color):
        x += TILE_WIDTH/2
        y += TILE_WIDTH/2
        pygame.draw.circle(surface, color, (x, y), TILE_WIDTH/2 - 5)

    def draw_piece_front(self, surface, (x, y), color):
        x += TILE_WIDTH/2 - 3
        y += TILE_WIDTH/2 - 5
        pygame.draw.circle(surface, color, (x, y), TILE_WIDTH/2 - 6)
