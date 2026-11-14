"""Prim's minimum spanning tree algorithm."""

def prims(graph):
    vertices = list(graph.keys())
    visited = {vertices[0]}
    edges = []
    total_cost = 0

    while len(visited) < len(vertices):
        best_edge = None
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and (best_edge is None or weight < best_edge[2]):
                    best_edge = (u, v, weight)

        if best_edge is None:
            raise ValueError("Graph is disconnected")

        u, v, weight = best_edge
        edges.append((u, v, weight))
        visited.add(v)
        total_cost += weight

    return edges, total_cost


def main():
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 5)],
        'C': [('A', 3), ('B', 1), ('D', 4), ('E', 6)],
        'D': [('B', 5), ('C', 4), ('E', 2)],
        'E': [('C', 6), ('D', 2)],
    }
    mst, cost = prims(graph)
    print("Minimum spanning tree edges:", mst)
    print("Total cost:", cost)


if __name__ == "__main__":
    main()
