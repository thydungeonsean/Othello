from random import randint
from game_settings import *


class GameGrid(object):

    def __init__(self, state):

        self.state = state
        self.grid = [[randint(0, 2) for y in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

    def get_cell(self, (x, y)):
        return self.grid[x][y]

    def update_cell(self, (x, y), cell_value):
        self.grid[x][y] = cell_value
        self.state.request_redraw()

    def translate_mouse_to_grid_coord(self, (mx, my)):
        my -= BOARD_Y_OFFSET
        return mx / TILE_WIDTH, my / TILE_WIDTH

    def on_grid(self, (x, y)):
        return 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT
