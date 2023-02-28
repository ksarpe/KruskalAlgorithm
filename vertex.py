import pygame

import colors


class Vertex:
    def __init__(self, x, y, radius, text):
        self.x = x
        self.y = y
        self.radius = radius
        self.text = text

    def draw(self, win):
        pygame.draw.circle(win, colors.LIGHT_BLUE, (self.x, self.y), self.radius)

        font = pygame.font.SysFont('comicsans', 23)
        text = font.render(self.text, True, colors.BLACK)
        win.blit(text,
                 (self.x + (1 - text.get_width() / 2), self.y + (1 - text.get_height() / 2)))
