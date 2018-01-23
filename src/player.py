from game_board import GameBoard
from game_settings import *


class Player(object):

    piece_code_dict = {'white': WHITE_PIECE, 'black': BLACK_PIECE}
    opposite_side = {WHITE_PIECE: BLACK_PIECE, BLACK_PIECE: WHITE_PIECE}

    def __init__(self, state, color):

        self.state = state
        self.game_grid = self.state.game_grid
        self.color = color
        self.human = True

    def is_human(self):
        return self.human

    @property
    def game_piece(self):
        return Player.piece_code_dict[self.color]

    @property
    def opposed_piece(self):
        return Player.opposite_side[self.game_piece]

    def play_piece(self, cell):
        self.game_grid.update_cell(cell, self.game_piece)

    def try_to_place_piece(self, cell):
        if self.placement_is_valid(cell):
            self.play_piece(cell)
            self.trigger_flank(cell)
            # end turn
            self.state.turn_manager.end_turn()

    def placement_is_valid(self, cell):
        # return self.state.game_logic.placement_is_valid_for_color(cell, self.game_piece)
        return cell in self.state.game_logic.valid_moves

    def trigger_flank(self, cell):

        flanked_pieces = self.state.game_logic.valid_moves[cell]
        for piece in flanked_pieces:
            self.game_grid.flip_piece(piece)
