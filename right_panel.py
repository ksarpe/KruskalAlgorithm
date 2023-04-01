import pygame
import colors


class RightPanel:
    def __init__(self, x):
        self.x = x
        self.text = ""
        self.text_color = colors.BLACK
        self.result = []
        self.graph = []
        self.rank = []
        self.parent = []

    def set_result(self, res):
        self.result = res

    def set_graph(self, g):
        self.graph = g

    def set_rank(self, r):
        self.rank = r

    def set_parent(self, par):
        self.parent = par

    def set_log(self, text, color):
        self.text = text
        self.text_color = color

    def draw(self, win):
        pygame.draw.line(win, colors.BLACK, (0, 520), (1080, 520), 3)
        font = pygame.font.SysFont('comicsans', 17)
        text = font.render("Graph: " + str(self.graph), True, self.text_color)
        win.blit(text, (15, 560))
        text = font.render("Result: " + str(self.result), True, self.text_color)
        win.blit(text, (15, 526))
        text = font.render("Parent: " + str(self.parent), True, self.text_color)
        win.blit(text, (15, 594))
        text = font.render("Rank: " + str(self.rank), True, self.text_color)
        win.blit(text, (15, 628))
