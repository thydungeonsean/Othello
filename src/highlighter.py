import pygame
from game_settings import *
from colors import YELLOW


class Highlighter(object):

    def __init__(self, state):
        self.state = state
        self.highlight = None
        self.rect = pygame.Rect((0, 0), (TILE_WIDTH, TILE_WIDTH))

    def init(self):
        self.highlight = pygame.Surface((TILE_WIDTH, TILE_WIDTH)).convert()
        self.highlight.fill(YELLOW)
        self.highlight.set_alpha(75)

    def draw(self, surface):

        for cell in self.state.game_logic.valid_moves:
            self.highlight_cell(surface, cell)

    def highlight_cell(self, surface, (x, y)):

        self.rect.topleft = x * TILE_WIDTH, y * TILE_WIDTH + BOARD_Y_OFFSET
        #pygame.draw.rect(surface, YELLOW, self.rect, 2)
        surface.blit(self.highlight, self.rect)
