import pygame
import colors


class Line:
    def __init__(self, x1, y1, x2, y2, weight):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.weight = weight
        self.color = colors.LIGHT_BLUE2

    def draw(self, win):
        pygame.draw.line(win, self.color, (self.x1, self.y1), (self.x2, self.y2), 4)

        font = pygame.font.SysFont('comicsans', 23)
        text = font.render(str(self.weight), True, colors.BLACK)
        win.blit(text,
                 ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2))
