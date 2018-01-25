from player import Player
from random import choice

class AIPlayer(Player):

    DELAY = 25

    def __init__(self, state, color):

        Player.__init__(self, state, color)

        self.human = False
        self.counter = 1

    def run_logic(self):
        self.tick()
        if self.counter == 0:
            self.take_turn()

    def tick(self):
        self.counter += 1
        if self.counter >= AIPlayer.DELAY:
            self.counter = 0

    def take_turn(self):

        move = self.choose_available_move()
        self.play_piece(move)
        self.trigger_flank(move)

        self.state.turn_manager.end_turn()

    def choose_available_move(self):

        weighted_moves = {}

        self.weigh_moves(self.state.game_logic.valid_moves, weighted_moves)

        best_value = max(weighted_moves.values())
        best_moves = filter(lambda x: weighted_moves[x] == best_value, weighted_moves)

        return choice(best_moves)

    def weigh_moves(self, valid_moves, weighted_moves):

        for move in valid_moves:
            weighted_moves[move] = len(valid_moves[move])
