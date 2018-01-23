import pygame
from pygame.locals import *


class Game(object):

    FPS = 60

    def __init__(self):

        self.game_running = False
        self.screen = None
        self.clock = pygame.time.Clock()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 740))
        self.game_running = True

        self.screen.fill((100,200,100))

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
        pass

    def update_display(self):
        pygame.display.update()

    def tick(self):
        self.clock.tick(Game.FPS)
