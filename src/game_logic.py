from game_settings import *


class GameLogic(object):

    def __init__(self, state):
        self.state = state
        self.valid_moves = {}

    @property
    def game_grid(self):
        return self.state.game_grid

    def calculate_valid_moves(self, color_piece):
        self.valid_moves.clear()
        flanks = []
        for cell in filter(lambda x: self.is_possible_flank(x, color_piece), self.game_grid.all_cells):
            flanks = self.calculate_flanks(cell, color_piece)
            if flanks:
                self.valid_moves[cell] = flanks

    def is_possible_flank(self, cell, color_piece):
        return self.cell_is_empty(cell) and self.adjacent_to_enemy(cell, color_piece)

    # def placement_is_valid_for_color(self, cell, color_piece):
    #     if not self.cell_is_empty(cell):
    #         return False
    #
    #     if not self.adjacent_to_enemy(cell, color_piece):
    #         return False
    #
    #     return self.will_trigger_flank(cell, color_piece)

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

    # def will_trigger_flank(self, cell, color_piece):
    #     return True

    def calculate_flanks(self, cell, color_piece):

        flank_list = []

        dir_vectors = [(1, 0), (-1, 0), (0, 1), (0, -1),
               (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for vec in dir_vectors:
            flank_list.extend(self.get_flanks_on_vector(cell, color_piece, vec))

        return flank_list

    def get_flanks_on_vector(self, (cx, cy), color_piece, (vx, vy)):

        x, y = cx + vx, cy + vy  # first postion on vector
        possible_flank = True

        flanked_cells = []

        while possible_flank:

            # if vector ends in empty cell or off the map, there is no flank
            if not self.game_grid.on_grid((x, y)) or self.cell_is_empty((x, y)):
                possible_flank = False

            # if next piece on vector is opponenets pieces, it's possibly a flank
            elif self.is_opposing_piece((x, y), color_piece):
                flanked_cells.append((x, y))

            # if next piece of vector is ours, then all intermediate enemies are flanked
            else:
                break

            x += vx
            y += vy

        if not possible_flank:
            del flanked_cells[:]

        return flanked_cells
