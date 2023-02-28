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
        self.assign_observer()
        self.window = pygame.display.set_mode((1080, 720))
        self.btn_start = Button(colors.GREEN, 40, 15, 230, 36, "START")
        self.btn_edge = Button(colors.RED, 290, 15, 150, 36, "Add Edge")
        self.btn_clear = Button(colors.RED, 465, 15, 120, 36, "Clear")
        self.vertices = []
        self.lines = []

    def assign_observer(self):
        if self.graph is not None:
            self.graph.add_observer(self.update_lines_colors)

    def update_lines_colors(self, result):
        source = result[0]
        dest = result[1]
        print(source, dest)
        line_start = ()
        line_end = ()
        for v in self.vertices:
            print("checking: ", v)
            if int(v.text) - 1 == source:
                line_start = (v.x, v.y)
            if int(v.text) - 1 == dest:
                line_end = (v.x, v.y)

        print(line_start, line_end)
        for line in self.lines:
            if line.x1 == line_start[0] \
                    and line.y1 == line_start[1] \
                    and line.x2 == line_end[0] \
                    and line.y2 == line_end[1]:
                line.color = colors.GREEN
                break

    def add_vertex(self, x, y):
        v = Vertex(x, y, str(self.INCREMENT))
        self.INCREMENT += 1
        self.vertices.append(v)
        self.graph.add_vertex()

    def clear(self):
        self.lines = []
        self.vertices = []
        self.graph.clear()

    def draw(self):
        self.window.fill(colors.GRAY)
        pygame.draw.line(self.window, colors.BLACK, (0, 66), (1080, 66), 3)
        self.btn_start.draw(self.window, True)
        self.btn_edge.draw(self.window, True)
        self.btn_clear.draw(self.window, True)
        for line in self.lines:
            line.draw(self.window)
        for vertex in self.vertices:
            vertex.draw(self.window)

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
        new_line = Line(self.vertices[source - 1].x, self.vertices[source - 1].y, self.vertices[dest - 1].x,
                        self.vertices[dest - 1].y, weight)
        self.lines.append(new_line)

    def check_clicks(self):
        mouse = pygame.mouse.get_pos()

        if self.btn_edge.click(mouse):
            tkinter_thread = threading.Thread(target=self.handle_input)
            tkinter_thread.start()
        if self.btn_clear.click(mouse):
            self.clear()
        if mouse[1] > 84:  # if click is under top menu
            self.add_vertex(*mouse)
        elif self.btn_start.click(mouse):
            kruskal_thread = threading.Thread(target=self.graph.kruskal_mst)
            kruskal_thread.start()

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
