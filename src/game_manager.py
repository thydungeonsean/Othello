import pygame
from pygame.locals import *
from game_state import Game
from game_settings import *
from colors import *
from button import Button
from layout import *


class GameManager(object):

    def __init__(self):

        self.game = None
        self.screen = None
        self.players = {'white': 'human',
                         'black': 'ai'}
        self.game_running = True
        self.clock = pygame.time.Clock()
        self.buttons = []
        self.needs_redraw = True

    def init(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.initialize_buttons()

    def initialize_buttons(self):

        start_button = Button(start_coord, 'Start Game', self.start_new_game, start_anchor)

        exit_button = Button(exit_coord, 'Exit', self.exit_game, exit_anchor)

        self.buttons.extend((start_button, exit_button))

    def start_new_game(self):
        print 'new game'
        self.game = Game(white_player=self.players['white'], black_player=self.players['black'])
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
                        print button
                        print pygame.mouse.get_pos()
                        button.on_click()

    def draw(self):

        self.screen.fill(BLACK)

        for button in self.buttons:
            button.draw(self.screen)

        self.needs_redraw = False

    def exit_game(self):
        self.game_running = False
