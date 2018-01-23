from game_board import GameBoard
from game_settings import *


class Player(object):

    piece_code_dict = {'white': WHITE_PIECE, 'black': BLACK_PIECE}

    def __init__(self, state, color):

        self.state = state
        self.color = color
        self.human = True

    def is_human(self):
        return self.human

    @property
    def game_piece(self):
        return Player.piece_code_dict[self.color]

    def play_piece(self, cell):
        self.state.game_grid.update_cell(cell, self.game_piece)
        # trigger flank

    def try_to_place_piece(self, cell):
        if self.placement_is_valid(cell):
            self.play_piece(cell)

    def placement_is_valid(self, cell):
        return self.state.game_logic.placement_is_valid_for_color(cell, self.game_piece)
