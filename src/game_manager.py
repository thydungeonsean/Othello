import pygame
from pygame.locals import *
from game_state import Game
from game_settings import *
from colors import *
from button import Button
from control_toggle import ControlToggle
from layout import *


class GameManager(object):

    player_type_flip = {'human': 'ai', 'ai': 'human'}

    def __init__(self):

        self.game = None
        self.screen = None
        self.players = {'white': 'human',
                         'black': 'ai'}
        self.game_running = True
        self.clock = pygame.time.Clock()
        self.buttons = []
        self.toggles = {}
        self.needs_redraw = True

    def init(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.initialize_buttons()

    def initialize_buttons(self):

        start_button = Button(start_coord, 'Start Game', self.start_new_game, start_anchor)

        def f():
            pass

        black_label = Button(black_label_coord, 'Black:', f, black_anchor)
        black_toggle = ControlToggle(black_coord, self.players['black'].capitalize(), self.toggle_black, black_anchor)
        white_label = Button(white_label_coord, 'White:', f, white_anchor)
        white_toggle = ControlToggle(white_coord, self.players['white'].capitalize(), self.toggle_white, white_anchor)

        exit_button = Button(exit_coord, 'Exit', self.exit_game, exit_anchor)

        self.buttons.extend((start_button, black_label, black_toggle, white_label, white_toggle, exit_button))
        self.toggles['black'] = black_toggle
        self.toggles['white'] = white_toggle

    def start_new_game(self):
        self.game = Game(self, white_player=self.players['white'], black_player=self.players['black'])
        self.game.init()
        self.game.main()
        self.needs_redraw = True

    def main(self):

        while self.game_running:
            self.handle_input()

            if self.needs_redraw:
                self.draw()
                pygame.display.update()

            self.clock.tick(FPS)

        pygame.quit()

    def handle_input(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.exit_game()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exit_game()

            elif event.type == MOUSEBUTTONDOWN:

                for button in self.buttons:
                    if button.mouse_is_over():
                        button.on_click()

    def draw(self):

        self.screen.fill(BLACK)

        for button in self.buttons:
            button.draw(self.screen)

        self.needs_redraw = False

    def exit_game(self):
        self.game_running = False

    def toggle_black(self):

        self.toggle_player('black')

    def toggle_white(self):

        self.toggle_player('white')

    def toggle_player(self, team):

        new_control = GameManager.player_type_flip[self.players[team]]
        self.players[team] = new_control

        self.toggles[team].flip_toggle(new_control.capitalize())
        self.needs_redraw = True
