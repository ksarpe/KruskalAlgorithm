from graph import Graph
from game import Game

if __name__ == '__main__':
    g = Graph()  # make clean graph
    game = Game(g)  # make window and pass graph to it
    game.run()  # start main loop
