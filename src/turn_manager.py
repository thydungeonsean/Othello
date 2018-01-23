from game_settings import *

class TurnManager(object):

    def __init__(self, state):

        self.state = state
        self.players = {WHITE_PIECE: self.state.white_player, BLACK_PIECE: self.state.black_player}
        self.active_player = self.players[WHITE_PIECE]

    def begin_turn(self):
        self.state.game_logic.calculate_valid_moves(self.active_player.game_piece)
        # if player is ai, ...

    def end_turn(self):
        self.switch_active_player()
        self.begin_turn()

    def switch_active_player(self):
        self.active_player = self.players[self.active_player.opposed_piece]
