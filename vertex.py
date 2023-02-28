import pygame

import colors


class Vertex:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw(self, win):
        pygame.draw.circle(win, colors.LIGHT_BLUE, (self.x, self.y), 20)

        font = pygame.font.SysFont('comicsans', 23)
        text = font.render(self.text, True, colors.BLACK)
        win.blit(text,
                 (self.x + (1 - text.get_width() / 2), self.y + (1 - text.get_height() / 2)))
