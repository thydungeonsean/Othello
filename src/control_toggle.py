from button import Button
from font_draw import FontDraw
import pygame
from colors import RED


class ControlToggle(Button):

    def __init__(self, coord, text, func, anchor):

        self.width = 100
        self.base_coord = coord
        Button.__init__(self, coord, text, func, anchor, True)

    def flip_toggle(self, new_text):

        self.image = self.create_button_image(new_text)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.coord = self.adjust_position(self.base_coord)

    def create_button_image(self, text):

        image = FontDraw.get_instance().write_button_text(text, self.width)
        rect = image.get_rect()

        pygame.draw.rect(image, RED, rect, 1)

        return image.convert()
