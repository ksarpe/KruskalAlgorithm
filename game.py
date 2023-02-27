import pygame
from button import Button

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((1080, 720))
        self.btn_vertex = Button((0, 255, 0), 800, 600, 20, 20, "VertexON")

    def draw(self):
        self.btn_vertex.draw(self.window, True)
        pygame.display.flip()

    def check_clicks(self):
        mouse = pygame.mouse.get_pos()

        if self.btn_vertex.is_over(mouse):
            print("mouse over")


    def run(self):
        running = True
        while running:
            self.draw()
            self.clock.tick(30)
            self.window.fill((255, 255, 255))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.check_clicks()

            # end event handling

        # end main loop
        pygame.quit()
