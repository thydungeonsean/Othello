from game_settings import *


class TurnManager(object):

    def __init__(self, state):

        self.state = state
        self.players = {WHITE_PIECE: self.state.white_player, BLACK_PIECE: self.state.black_player}
        self.active_player = self.players[BLACK_PIECE]
        self.pass_count = 0
        self.turn_active = False
        self.game_running = True

    def run(self):
        if not self.turn_active and self.game_running:
            self.turn_active = True
            self.begin_turn()

    def begin_turn(self):
        self.state.game_logic.calculate_valid_moves(self.active_player.game_piece)
        # check if player is forced to pass
        self.pass_if_no_moves()

        if self.game_running:
            self.set_log_message()
            # if player is ai, ...
        else:
            self.determine_winner()

    def end_turn(self):
        self.switch_active_player()
        self.turn_active = False

    def switch_active_player(self):
        self.active_player = self.players[self.active_player.opposed_piece]

    def pass_if_no_moves(self):

        if len(self.state.game_logic.valid_moves) == 0:
            self.pass_count += 1
            self.end_turn()
        else:
            self.pass_count = 0

        if self.pass_count > 1:
            self.game_running = False

    def set_log_message(self):

        message = []
        current = 'White'
        other = 'Black'
        if self.active_player.color == 'black':
            current = 'Black'
            other = 'White'

        message.append(current)
        message.append("'s turn")

        if self.pass_count > 0:
            message.append(' - ')
            message.append(other)
            message.append(' had to pass :(')

        message = ''.join(message)
        self.state.logger.update_log(message)

    def determine_winner(self):

        white = int(self.state.white_score())
        black = int(self.state.black_score())
        if white > black:
            message = 'Game Over - White player wins!'
        elif black > white:
            message = 'Game Over - Black player wins!'
        else:
            message = 'Game Over - It\'s a draw, you both lose.'

        self.state.logger.update_log(message)
        self.state.activate_button('restart')

    def reset_state(self):

        self.active_player = self.players[BLACK_PIECE]
        self.pass_count = 0
        self.turn_active = False
        self.game_running = True
