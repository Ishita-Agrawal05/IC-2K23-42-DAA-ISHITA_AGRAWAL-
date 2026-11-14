def multistage_graph(graph):
    n = len(graph)
    dist = [float('inf')] * n
    dist[n - 1] = 0

    for i in range(n - 2, -1, -1):
        best = float('inf')
        for j in range(i + 1, n):
            if graph[i][j] != float('inf'):
                best = min(best, graph[i][j] + dist[j])
        dist[i] = best

    return dist[0]


def main():
    graph = [
        [float('inf'), 1, 2, 5, float('inf'), float('inf')],
        [float('inf'), float('inf'), 0, 3, 4, float('inf')],
        [float('inf'), float('inf'), float('inf'), 1, 2, float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), 2, 3],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0],
    ]
    print(f"Minimum cost: {multistage_graph(graph)}")


if __name__ == "__main__":
    main()
