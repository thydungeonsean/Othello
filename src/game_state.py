import pygame
from pygame.locals import *
from colors import *
from game_settings import *
# game components
from game_grid import GameGrid
from game_board import GameBoard
from player import Player


class Game(object):

    def __init__(self):

        # game state members
        self.game_running = False
        self.needs_redraw = True
        self.screen = None
        self.clock = pygame.time.Clock()

        # game components
        self.game_grid = GameGrid(self)
        self.game_board = None
        self.turn_manager = None
        self.white_player = Player(self, 'white')
        self.black_player = Player(self, 'black')
        self.active_player = self.white_player

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_running = True

        self.screen.fill(BLACK)

        # initialize game components
        self.game_board = GameBoard(self, self.game_grid)

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

        pygame.quit()

    def handle_input(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.exit_game()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exit_game()

            elif event.type == MOUSEBUTTONDOWN:
                if self.active_player.is_human() and self.mouse_over_grid():
                    self.active_player.try_to_place_piece(self.mouse_grid_position())

    def mouse_over_grid(self):
        mx, my = pygame.mouse.get_pos()
        return my > BOARD_Y_OFFSET

    def mouse_grid_position(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.game_grid.translate_mouse_to_grid_coord(mouse_pos)

    def exit_game(self):
        self.game_running = False

    def run_logic(self):
        pass

    def draw_all(self):
        self.game_board.draw(self.screen)

    def update_display(self):
        pygame.display.update()

    def request_redraw(self):
        self.needs_redraw = True

    def reset_redraw(self):
        self.needs_redraw = False

    def tick(self):
        self.clock.tick(FPS)
