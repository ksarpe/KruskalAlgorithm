from Graph import Graph

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 9)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()
