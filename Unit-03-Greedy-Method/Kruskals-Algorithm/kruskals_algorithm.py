class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskals_algorithm(edges, vertices):
    edges = sorted(edges, key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


def main():
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4),
        (1, 2, 5),
    ]
    mst, cost = kruskals_algorithm(edges, vertices)
    print(f"Minimum spanning tree edges: {mst}")
    print(f"Total cost: {cost}")


if __name__ == "__main__":
    main()
