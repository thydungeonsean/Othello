from player import Player
from random import choice

class AIPlayer(Player):

    DELAY = 3

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

        moves = self.state.game_logic.valid_moves.keys()

        move = choice(moves)
        self.play_piece(move)
        self.trigger_flank(move)

        self.state.turn_manager.end_turn()
