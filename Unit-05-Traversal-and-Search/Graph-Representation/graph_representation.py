class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.display()


if __name__ == "__main__":
    main()
