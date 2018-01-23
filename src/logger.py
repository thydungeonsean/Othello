from font_draw import FontDraw
from game_settings import *
import pygame
from colors import BLACK


class Logger(object):

    log_coord = (SCREEN_WIDTH / 2, 50)

    def __init__(self, state):
        self.state = state
        self.log_text = 'Hi fucker'
        self.top_bar = pygame.Surface((SCREEN_WIDTH, BOARD_Y_OFFSET))
        self.top_bar.fill(BLACK)

    def draw_scores(self, surface):

        self.draw_black_score(surface)
        self.draw_white_score(surface)

    def draw_black_score(self, surface):

        text_surf = FontDraw.get_instance().write_score('Black: ' + self.state.black_score())
        rect = text_surf.get_rect()
        rect.bottomleft = (0, SCREEN_HEIGHT)

        surface.blit(text_surf, rect)

    def draw_white_score(self, surface):

        text_surf = FontDraw.get_instance().write_score('White: ' + self.state.white_score())
        rect = text_surf.get_rect()
        rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

        surface.blit(text_surf, rect)


    def draw_log(self, surface):

        surface.blit(self.top_bar, (0, 0))

        text_surf = FontDraw.get_instance().write_log(self.log_text)
        rect = text_surf.get_rect()
        rect.center = Logger.log_coord

        surface.blit(text_surf, rect)

    def update_log(self, text):
        self.log_text = text
        self.state.request_redraw()
