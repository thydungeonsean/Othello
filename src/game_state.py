import pygame
from pygame.locals import *
from colors import *
from game_settings import *
# game components
from game_logic import GameLogic
from game_grid import GameGrid
from game_board import GameBoard
from player import Player
from ai_player import AIPlayer
from turn_manager import TurnManager
from highlighter import Highlighter
from logger import Logger
from button import Button

from layout import *


class Game(object):

    def __init__(self, manager, white_player='human', black_player='human'):

        # game state members
        self.game_manager = manager
        self.game_running = False
        self.needs_redraw = True
        self.screen = None
        self.clock = pygame.time.Clock()

        # game components
        self.game_logic = GameLogic(self)
        self.game_grid = GameGrid(self)
        self.game_board = None

        self.white_player = None
        self.black_player = None
        self.initialize_players(white_player, black_player)

        self.turn_manager = TurnManager(self)
        self.highlighter = Highlighter(self)
        self.logger = Logger(self)

        self.buttons = {}

    def init(self):

        self.screen = pygame.display.get_surface()
        self.game_running = True

        self.screen.fill(BLACK)

        # initialize game components
        self.game_board = GameBoard(self, self.game_grid)
        self.highlighter.init()
        self.initialize_buttons()

    def initialize_buttons(self):

        restart_button = Button(restart_coord, 'Restart', self.restart, restart_anchor, False)
        end_button = Button(end_coord, 'End Game', self.exit_game, end_anchor)
        self.buttons['restart'] = restart_button
        self.buttons['end'] = end_button

    def initialize_players(self, white, black):

        players = []
        sides = ['white', 'black']
        constructors = []
        for p_type in (white, black):
            if p_type == 'human':
                constructors.append(Player)
            else:
                constructors.append(AIPlayer)

        for i in (0, 1):
            players.append(
                constructors[i](self, sides[i])
            )

        self.white_player = players[0]
        self.black_player = players[1]

    # main game loop
    def main(self):

        while self.game_running:

            self.handle_input()
            self.run_logic()
            if self.needs_redraw:
                self.draw_all()
                self.update_display()
                self.reset_redraw()
            self.tick()

    def handle_input(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.exit_program()

            elif event.type == MOUSEBUTTONDOWN:

                if self.active_player.is_human() and self.mouse_over_grid():
                    self.active_player.try_to_place_piece(self.mouse_grid_position())
                else:
                    for button in self.buttons.itervalues():
                        if button.active and button.mouse_is_over():
                            button.on_click()

    @property
    def active_player(self):
        return self.turn_manager.active_player

    def mouse_over_grid(self):
        mx, my = pygame.mouse.get_pos()
        return my > BOARD_Y_OFFSET

    def mouse_grid_position(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.game_grid.translate_mouse_to_grid_coord(mouse_pos)

    def exit_game(self):
        self.game_running = False

    def exit_program(self):
        self.game_running = False
        self.game_manager.exit_game()
        print 'here'

    def run_logic(self):
        self.turn_manager.run()
        if not self.active_player.is_human() and self.turn_manager.game_running:
            self.active_player.run_logic()

    def draw_all(self):
        self.game_board.draw(self.screen)
        self.highlighter.draw(self.screen)
        self.logger.draw_scores(self.screen)
        self.logger.draw_log(self.screen)

        for button in self.buttons.itervalues():
            if button.active:
                button.draw(self.screen)

    def update_display(self):
        pygame.display.update()

    def request_redraw(self):
        self.needs_redraw = True

    def reset_redraw(self):
        self.needs_redraw = False

    def tick(self):
        self.clock.tick(FPS)

    def black_score(self):
        return self.game_grid.get_score(BLACK_PIECE)

    def white_score(self):
        return self.game_grid.get_score(WHITE_PIECE)

    def activate_button(self, key):
        self.buttons[key].set_active()

    def hide_button(self, key):
        self.buttons[key].hide()

    def restart(self):
        self.game_grid.reset_state()
        self.turn_manager.reset_state()
        self.request_redraw()
        self.hide_button('restart')
