from game_settings import *


class GameLogic(object):

    def __init__(self, state):
        self.state = state

    @property
    def game_grid(self):
        return self.state.game_grid

    def placement_is_valid_for_color(self, cell, color_piece):

        if not self.cell_is_empty(cell):
            return False

        if not self.adjacent_to_enemy(cell, color_piece):
            return False

        return self.will_trigger_flank(cell, color_piece)

    def cell_is_empty(self, cell):
        return self.game_grid.get_cell(cell) == EMPTY

    def adjacent_to_enemy(self, cell, color_piece):

        adj = self.game_grid.get_adjacent_cells(cell)
        for adj_cell in adj:
            if self.is_opposing_piece(adj_cell, color_piece):
                return True
        return False

    def is_opposing_piece(self, cell, color_piece):
        return self.game_grid.get_cell(cell) not in (EMPTY, color_piece)

    def will_trigger_flank(self, cell, color_piece):
        return True
