import pygame
import colors


class RightPanel:
    def __init__(self, x):
        self.x = x
        self.text = ""
        self.text_color = colors.BLACK

    def set_log(self, text, color):
        self.text = text
        self.text_color = color

    def draw(self, win):
        pygame.draw.line(win, colors.BLACK, (850, 68), (850, 680), 3)
        font = pygame.font.SysFont('comicsans', 20)
        # text = font.render("Log: " + self.text, True, self.text_color)
        # win.blit(text, (15, self.y + 6))
