from game_settings import *

class TurnManager(object):

    def __init__(self, state):

        self.state = state
        self.players = {WHITE_PIECE: self.state.white_player, BLACK_PIECE: self.state.black_player}
        self.active_player = self.players[WHITE_PIECE]
        self.pass_count = 0
        self.turn_active = False

    def run(self):
        if not self.turn_active:
            self.turn_active = True
            self.begin_turn()

    def begin_turn(self):
        self.state.game_logic.calculate_valid_moves(self.active_player.game_piece)
        # check if player is forced to pass
        self.pass_if_no_moves()
        # if player is ai, ...

    def end_turn(self):
        self.switch_active_player()
        self.turn_active = False

    def switch_active_player(self):
        self.active_player = self.players[self.active_player.opposed_piece]

    def pass_if_no_moves(self):

        if len(self.state.game_logic.valid_moves) == 0:
            print 'no valid_moves, %s has to pass' % self.active_player.color
            self.pass_count += 1
            self.end_turn()
        else:
            self.pass_count = 0

        if self.pass_count > 1:
            print 'game over'
