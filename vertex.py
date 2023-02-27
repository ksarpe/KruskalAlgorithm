import pygame


class Vertex:
    def __init__(self, color, x, y, radius, text):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.text = text

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

        font = pygame.font.SysFont('comicsans', 23)
        text = font.render(self.text, True, (255, 255, 255))
        win.blit(text,
                 (self.x + (1 - text.get_width() / 2), self.y + (1 - text.get_height() / 2)))
