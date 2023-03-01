# system imports
import threading
import pygame

# local imports
from button import Button
import colors
from vertex import Vertex
from input_box import InputBox
from line import Line
from bottom_panel import BottomPanel
from example import  ExampleCreator


class Game:
    # constants
    INCREMENT = 1  # for vertex numeration
    VERSION = "v2.0"

    def __init__(self, graph):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('KruskalVisApp ' + self.VERSION)
        self.graph = graph
        self.assign_observers()  # assign function as observer to listen to graph object color change
        self.window = pygame.display.set_mode((1080, 720))

        # buttons
        self.btn_start = Button(colors.GREEN, 40, 15, 230, 36, "START")
        self.btn_edge = Button(colors.RED, 290, 15, 150, 36, "Add Edge")
        self.btn_clear = Button(colors.RED, 465, 15, 120, 36, "Clear")
        self.btn_example1 = Button(colors.LIGHT_BLUE, 970, 15, 36, 36, "1")
        self.btn_example2 = Button(colors.LIGHT_BLUE, 1020, 15, 36, 36, "2")

        self.bottom_panel = BottomPanel(680)
        self.example_creator = ExampleCreator(self)

        self.kruskal_thread = threading.Thread()
        self.started = False  # ongoing algorithm
        self.can_modify = True  # while example is on the board
        self.vertices = []
        self.lines = []

    # for assigning observer for other classes functions
    def assign_observers(self):
        # listen to graph edge added to actual results list
        if self.graph is not None:
            self.graph.add_green_observer(self.update_lines_colors)
            self.graph.add_finish_observer(self.algorithm_finish_callback)

    def algorithm_finish_callback(self):
        self.bottom_panel.set_log("Algorithm has been finished successfully", colors.BLACK)

    # this is a listener, it is triggered only by graph class
    # it changes last changed color of edge
    def update_lines_colors(self, last_result):
        source = last_result[0]
        dest = last_result[1]
        line_start = ()
        line_end = ()

        # find where is the start and end of an edge
        for v in self.vertices:
            if int(v.text) - 1 == source:
                line_start = (v.x, v.y)
            if int(v.text) - 1 == dest:
                line_end = (v.x, v.y)

        # search for correct line which has the same start/end coordinates
        for line in self.lines:
            if line.x1 == line_start[0] \
                    and line.y1 == line_start[1] \
                    and line.x2 == line_end[0] \
                    and line.y2 == line_end[1]:
                line.color = colors.GREEN
                break

    # add vertex to game and to graph class
    def add_vertex(self, x, y):
        v = Vertex(x, y, str(self.INCREMENT))
        self.INCREMENT += 1
        self.vertices.append(v)
        self.graph.add_vertex()

    # add edge to game(as line) and to graph class
    def add_edge(self, source, dest, weight):
        self.graph.add_edge(source, dest, weight)

        new_line = Line(self.vertices[source - 1].x, self.vertices[source - 1].y, self.vertices[dest - 1].x,
                        self.vertices[dest - 1].y, weight)
        self.lines.append(new_line)

    # prepare board and graph class for new usage
    def clear(self):
        if self.started:
            self.bottom_panel.set_log("Cannot clear after start!", colors.ERROR_LOG)
            return

        self.lines = []
        self.vertices = []
        self.graph.clear()
        self.INCREMENT = 1
        self.bottom_panel.set_log("Board has been cleared.", colors.BLACK)
        self.can_modify = True

    def draw(self):
        self.window.fill(colors.BG_COLOR)
        pygame.draw.line(self.window, colors.BLACK, (0, 66), (1080, 66), 3)
        self.bottom_panel.draw(self.window)
        self.btn_start.draw(self.window, True)
        self.btn_edge.draw(self.window, True)
        self.btn_clear.draw(self.window, True)
        self.btn_example1.draw(self.window, True)
        self.btn_example2.draw(self.window, True)
        for line in self.lines:
            line.draw(self.window)
        for vertex in self.vertices:
            vertex.draw(self.window)

        pygame.display.flip()

    # get input from InputBox and add edge from user
    def handle_input(self):
        entry_list = []
        input_box = InputBox(entry_list)
        input_box.run()

        if not entry_list:
            return
        # check if user inputs are digits
        if entry_list[0].isdigit() and entry_list[1].isdigit() and entry_list[0].isdigit():
            source = int(entry_list[0])
            dest = int(entry_list[1])
            weight = int(entry_list[2])

            # check if we have such vertices on the board
            if len(self.vertices) > source - 1 and len(self.vertices) > dest - 1:
                self.add_edge(source, dest, weight)
            else:
                self.bottom_panel.set_log("There is no such vertex on the board!", colors.ERROR_LOG)
        else:
            self.bottom_panel.set_log("You put wrong values!", colors.ERROR_LOG)

    def check_clicks(self):
        mouse = pygame.mouse.get_pos()

        if self.btn_edge.click(mouse):
            if self.can_modify:
                tkinter_thread = threading.Thread(target=self.handle_input)
                tkinter_thread.start()
            else:
                self.bottom_panel.set_log("You cannot add edge when example is on the board", colors.ERROR_LOG)
        if self.btn_clear.click(mouse):
            self.clear()
        if 84 < mouse[1] < 660:  # if click is under top menu
            if self.can_modify:
                self.add_vertex(*mouse)
            else:
                self.bottom_panel.set_log("You cannot add vertex when example is on the board!", colors.ERROR_LOG)

        if self.btn_example1.click(mouse):
            if self.can_modify:
                self.example_creator.make_example_one()
                self.can_modify = False
            else:
                self.bottom_panel.set_log("Firstly clear the board!", colors.ERROR_LOG)

        if self.btn_example2.click(mouse):
            if self.can_modify:
                self.example_creator.make_example_two()
                self.can_modify = False
            else:
                self.bottom_panel.set_log("Firstly clear the board!", colors.ERROR_LOG)

        if self.btn_start.click(mouse):
            if self.graph.V < 2 or (len(self.lines) + 1) < self.graph.V:
                self.bottom_panel.set_log("Board is wrong!", colors.ERROR_LOG)
                return

            if not self.started:
                self.bottom_panel.set_log("Algorithm has been started!", colors.BLACK)
                for line in self.lines:
                    line.color = colors.BG_COLOR
                self.kruskal_thread = threading.Thread(target=self.graph.kruskal_mst)
                self.kruskal_thread.start()
                self.started = True
            else:
                self.bottom_panel.set_log("You need to wait until algorithm has been finished in order to start over again!", colors.ERROR_LOG)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(5)

            if not self.kruskal_thread.is_alive():
                self.started = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_clicks()

            self.draw()
        pygame.quit()
