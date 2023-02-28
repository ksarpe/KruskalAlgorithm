# TODO add incrementation of vertices along with visual aspects
# TODO add edges along with visual aspects [harder]
import time


class Graph:

    def __init__(self):
        self.V = 0  # No. of vertices (initially 0)
        self.graph = []
        self.result = []
        self.observers = []

    def add_observer(self, callback):
        self.observers.append(callback)

    def clear(self):
        self.graph = []
        self.result = []
        self.V = 0

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

    def kruskal_mst(self):

        i = 0  # actual graph increment check
        e = 0  # check edges for loop

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
            i = i + 1  # increment helper for next
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:  # do smth only if not cycle
                e = e + 1  # increment added edge for loop condition
                self.result.append([u, v, w])
                for color_change_callback in self.observers:
                    color_change_callback(self.get_last_result())
                    time.sleep(1)

                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in self.result:
            minimum_cost += weight
            print(f"{u} -- {v} == {weight}")
        print("Total minimum cost:", minimum_cost)
