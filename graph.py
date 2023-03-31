import time

import colors


class Graph:

    def __init__(self):
        self.V = 0  # No. of vertices (initially 0)
        self.graph = []
        self.result = []
        self.line_color_observers = []
        self.finish_observers = []

    def add_line_color_observer(self, callback):
        self.line_color_observers.append(callback)

    def add_finish_observer(self, callback):
        self.finish_observers.append(callback)

    def clear(self):
        self.graph = []
        self.result = []
        self.V = 0

    def clear_result(self):
        self.result = []

    def add_vertex(self):
        self.V += 1
        print("Vertices amount updated:", self.V)

    def add_edge(self, u, v, w):  # source, dest, weight
        self.graph.append([u - 1, v - 1, w])
        print("Graph updated:", self.graph)

    def get_last_result(self):
        return self.result[len(self.result) - 1]

    # path compression technique, to have parent-child relationship
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # Union by rank
    def union(self, parent, rank, x, y):

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are the same just choose one
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self, is_automated):

        i = 0  # actual graph increment check
        e = 0  # check edges for loop
        minimal_cost = 0
        # Sort graph in descending order
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create initial sets [0   1   2   3] with no connections and root as itself with rank 0
        for node in range(self.V):
            parent.append(node)  # ex. [0,1,2,3] for Graph(4) constructor
            rank.append(0)  # ex. [0,0,0,0]

        # Main condition for mst
        while e < self.V - 1:

            u, v, w = self.graph[i]  # Pick the smallest edge
            self.result.append([u, v, w])
            for line_color_callback in self.line_color_observers:
                if is_automated:
                    time.sleep(0.6)
                else:
                    input("Press...")
                line_color_callback(self.get_last_result(), colors.BLUE)
            i = i + 1  # increment helper for next
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:  # do smth only if not cycle
                e = e + 1  # increment added edge for loop condition
                minimal_cost += w
                for line_color_callback in self.line_color_observers:
                    if is_automated:
                        time.sleep(0.6)
                    else:
                        input("Press...")
                    line_color_callback(self.get_last_result(), colors.GREEN)

                self.union(parent, rank, x, y)

            else:
                for line_color_callback in self.line_color_observers:
                    if is_automated:
                        time.sleep(0.6)
                    else:
                        input("Press...")
                    line_color_callback(self.get_last_result(), colors.RED)
                    if is_automated:
                        time.sleep(0.4)
                    else:
                        input("Press...")
                    line_color_callback(self.get_last_result(), colors.BG_COLOR)

        # callback for the game about finish algorithm
        for finish_callback in self.finish_observers:
            finish_callback(minimal_cost)
