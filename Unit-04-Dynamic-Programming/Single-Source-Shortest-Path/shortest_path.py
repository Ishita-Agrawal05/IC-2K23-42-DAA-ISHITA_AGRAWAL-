import heapq


def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue

        for v, w in graph[u]:
            new_dist = current_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


def main():
    graph = [
        [(1, 2), (2, 4)],
        [(2, 1), (3, 7)],
        [(3, 2), (4, 5)],
        [(4, 1)],
        [],
    ]
    print(dijkstra(graph, 0))


if __name__ == "__main__":
    main()
