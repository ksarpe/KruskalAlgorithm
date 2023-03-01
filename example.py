import time

import pygame


class ExampleCreator:
    def __init__(self, game):
        self.game = game  # game object for adding values

    def make_example_one(self):
        self.game.add_vertex(100, 360)  # 215 difference / 240 difference
        self.game.add_vertex(315, 120)
        self.game.add_vertex(315, 600)
        self.game.add_vertex(530, 120)
        self.game.add_vertex(530, 360)
        self.game.add_vertex(530, 600)
        self.game.add_vertex(745, 120)
        self.game.add_vertex(745, 600)
        self.game.add_vertex(960, 360)
        self.game.add_edge(1, 2, 4)
        self.game.add_edge(2, 3, 11)
        self.game.add_edge(1, 3, 8)
        self.game.add_edge(2, 4, 8)
        self.game.add_edge(5, 6, 6)
        self.game.add_edge(3, 5, 7)
        self.game.add_edge(4, 5, 2)
        self.game.add_edge(3, 6, 1)
        self.game.add_edge(4, 7, 7)
        self.game.add_edge(4, 8, 4)
        self.game.add_edge(6, 8, 2)
        self.game.add_edge(7, 8, 14)
        self.game.add_edge(7, 9, 9)
        self.game.add_edge(8, 9, 10)

    def make_example_two(self):
        self.game.add_vertex(150, 360)  # 110 difference / 110 difference
        self.game.add_vertex(260, 250)
        self.game.add_vertex(260, 470)
        self.game.add_vertex(370, 360)
        self.game.add_vertex(480, 250)
        self.game.add_vertex(590, 360)
        self.game.add_vertex(800, 470)
        self.game.add_vertex(900, 360)
        self.game.add_vertex(950, 470)
        self.game.add_edge(1, 2, 2)
        self.game.add_edge(1, 4, 2)
        self.game.add_edge(1, 3, 1)
        self.game.add_edge(2, 4, 1)
        self.game.add_edge(2, 5, 2)
        self.game.add_edge(3, 4, 1)
        self.game.add_edge(3, 7, 2)
        self.game.add_edge(4, 5, 2)
        self.game.add_edge(4, 6, 2)
        self.game.add_edge(5, 6, 1)
        self.game.add_edge(7, 8, 2)
        self.game.add_edge(7, 9, 2)
        self.game.add_edge(8, 9, 1)
