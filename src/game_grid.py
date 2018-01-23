from random import randint
from game_settings import *


class GameGrid(object):

    def __init__(self, state):

        self.state = state
        self.grid = [[EMPTY for y in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]
        self.start_game_state()

    def start_game_state(self):
        self.update_cell((3, 3), BLACK_PIECE)
        self.update_cell((4, 4), BLACK_PIECE)
        self.update_cell((4, 3), WHITE_PIECE)
        self.update_cell((3, 4), WHITE_PIECE)

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

    def get_adjacent_cells(self, (x, y)):

        adj = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
               (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
        return filter(lambda cell: self.on_grid(cell), adj)
