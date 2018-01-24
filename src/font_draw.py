import pygame
from colors import RED, BLACK, WHITE

class FontDraw(object):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):

        self.score_font = pygame.font.Font(None, 48)
        self.log_font = pygame.font.Font(None, 32)

    def write_score(self, text):
        return self.score_font.render(text, True, RED)

    def write_log(self, text):
        return self.log_font.render(text, True, RED)

    def write_button_text(self, text):

        text_image = self.log_font.render(text, True, RED, BLACK)
        tr = text_image.get_rect()

        padded_x = text_image.get_width() + 30
        padded_y = 50

        padded_image = pygame.Surface((padded_x, padded_y)).convert()
        padded_image.fill(BLACK)

        w = padded_image.get_width()
        h = padded_image.get_height()

        tr.center = w/2, h/2

        padded_image.blit(text_image, tr)

        return padded_image
