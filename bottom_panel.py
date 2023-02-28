import pygame
import colors


class BottomPanel:
    def __init__(self, y):
        self.y = y
        self.text = ""
        self.text_color = colors.BLACK

    def set_log(self, text, color):
        self.text = text
        self.text_color = color

    def draw(self, win):
        pygame.draw.line(win, colors.BLACK, (0, 680), (1080, 680), 3)
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render("Log: " + self.text, True, self.text_color)
        win.blit(text, (15, self.y + 6))
