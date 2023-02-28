# system imports
import threading
import pygame

# local imports
from button import Button
import colors
from vertex import Vertex
from input_box import InputBox
from line import Line


class Game:
    INCREMENT = 1  # vertex number

    def __init__(self, graph):
        pygame.init()
        pygame.font.init()
        self.graph = graph
        self.window = pygame.display.set_mode((1080, 720))
        self.btn_vertex = Button(colors.RED, 40, 15, 230, 36, "Vertex ON/OFF")
        self.btn_edge = Button(colors.RED, 290, 15, 150, 36, "Add Edge")
        self.vertices = []
        self.lines = []

    def add_vertex(self, x, y):
        v = Vertex(colors.BLUE, x, y, 20, str(self.INCREMENT))
        self.INCREMENT += 1
        self.vertices.append(v)
        print("New game vertex:", self.vertices)
        self.graph.add_vertex()

    def draw(self):
        self.window.fill(colors.WHITE)
        self.btn_vertex.draw(self.window, True)
        self.btn_edge.draw(self.window, True)
        for vertex in self.vertices:
            vertex.draw(self.window)
        for line in self.lines:
            pygame.draw.line(self.window, colors.BLACK, (line.x1, line.y1), (line.x2, line.y2), 4)
        pygame.display.flip()

    def handle_input(self):
        entry_list = []
        input_box = InputBox(entry_list)
        input_box.run()

        # fetch return values:
        source = int(entry_list[0])
        dest = int(entry_list[1])
        weight = int(entry_list[2])
        # Add edge to graph instance, from returned list
        self.graph.add_edge(source, dest, weight)
        # draw line between point marked as entry_list[0] and entry_list[1]
        new_line = Line(self.vertices[source - 1].x, self.vertices[source - 1].y, self.vertices[dest - 1].x, self.vertices[dest - 1].y)
        self.lines.append(new_line)

    def check_clicks(self):
        mouse = pygame.mouse.get_pos()

        if self.btn_edge.click(mouse):
            tkinter_thread = threading.Thread(target=self.handle_input)
            tkinter_thread.start()
        if mouse[1] > 80:  # if click is under top menu
            self.add_vertex(*mouse)
        elif self.btn_vertex.click(mouse):
            print("mouse over")

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_clicks()

            self.draw()
        pygame.quit()
