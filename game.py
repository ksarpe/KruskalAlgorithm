import pygame
from button import Button
import colors
from vertex import Vertex
import tkinter as tk
from input_box import InputBox


class Game:
    INCREMENT = 1

    def __init__(self, graph):
        pygame.init()
        pygame.font.init()
        self.graph = graph
        self.window = pygame.display.set_mode((1080, 720))
        self.btn_vertex = Button(colors.RED, 15, 15, 150, 36, "VertexON")
        self.btn_edge = Button(colors.RED, 180, 15, 150, 36, "Add Edge")
        self.vertices = []

    def add_vertex(self, x, y):
        v = Vertex(colors.BLUE, x, y, 20, str(self.INCREMENT))
        self.INCREMENT += 1
        self.vertices.append(v)
        self.graph.add_vertex()
        print(f"Current vertex amount:{self.graph.V}")

    def draw(self):
        self.window.fill((255, 255, 255))
        self.btn_vertex.draw(self.window, True)
        self.btn_edge.draw(self.window, True)
        for vertex in self.vertices:
            vertex.draw(self.window)
        pygame.display.flip()

    def open_tkinter_window(self):
        root = tk.Tk()
        root.title("Tkinter Window")
        root.geometry("300x200")
        root.mainloop()

    def check_clicks(self, pos):
        mouse = pygame.mouse.get_pos()

        if self.btn_edge.button_rect.collidepoint(pos):
            self.open_tkinter_window()
        if mouse[1] > 80:  # if click is under top menu
            self.add_vertex(*mouse)
        elif self.btn_vertex.button_rect.collidepoint(pos):
            print("mouse over")

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            #clock.tick(15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and self.btn_edge.button_rect.collidepoint(event.pos):
                    self.open_tkinter_window()

            self.draw()
        pygame.quit()
