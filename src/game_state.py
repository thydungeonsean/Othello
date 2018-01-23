import pygame
from pygame.locals import *
from colors import *
from game_settings import *
from game_board import GameBoard


class Game(object):

    def __init__(self):

        # game state members
        self.game_running = False
        self.screen = None
        self.clock = pygame.time.Clock()

        # game components
        self.game_board = None

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_running = True

        self.screen.fill(BLACK)

        # initialize game components
        self.game_board = GameBoard(self)

    # main game loop
    def main(self):

        while self.game_running:

            self.handle_input()
            self.run_logic()
            self.draw_all()
            self.update_display()
            self.tick()

        pygame.quit()

    def handle_input(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.exit_game()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exit_game()

    def exit_game(self):
        self.game_running = False

    def run_logic(self):
        pass

    def draw_all(self):
        self.game_board.draw(self.screen)

    def update_display(self):
        pygame.display.update()

    def tick(self):
        self.clock.tick(FPS)
