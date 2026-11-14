def prims_algorithm(graph):
    n = len(graph)
    visited = [False] * n
    key = [float('inf')] * n
    parent = [-1] * n
    key[0] = 0

    for _ in range(n):
        min_key = float('inf')
        u = -1
        for v in range(n):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    total_cost = sum(key)
    return parent, total_cost


def main():
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    parent, cost = prims_algorithm(graph)
    print(f"Parent array: {parent}")
    print(f"Minimum spanning tree cost: {cost}")


if __name__ == "__main__":
    main()
