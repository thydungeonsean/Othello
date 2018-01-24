from font_draw import FontDraw
import pygame
from colors  import RED


class Button(object):

    def __init__(self, coord, text, func, anchor='tl', active=True):

        self.function = func
        self.image = self.create_button_image(text)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.anchor = anchor
        self.coord = self.adjust_position(coord)
        self.active = active

    def create_button_image(self, text):

        image = FontDraw.get_instance().write_button_text(text)
        rect = image.get_rect()

        pygame.draw.rect(image, RED, rect, 1)

        return image.convert()

    def adjust_position(self, coord):

        rect = self.image.get_rect()
        if self.anchor == 'tl':
            rect.topleft = coord
        elif self.anchor == 'tr':
            rect.topright = coord
        elif self.anchor == 'cen':
            rect.center = coord

        coord = rect.topleft
        return coord

    def on_click(self):
        self.function()

    def draw(self, surface):
        surface.blit(self.image, self.coord)

    def mouse_is_over(self):

        mx, my = pygame.mouse.get_pos()
        x, y = self.coord

        return x <= mx < x + self.w, y <= my < y + self.h

    def set_active(self):
        self.active = True

    def hide(self):
        self.active = False
