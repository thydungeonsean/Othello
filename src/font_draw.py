import pygame
from colors import RED

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
