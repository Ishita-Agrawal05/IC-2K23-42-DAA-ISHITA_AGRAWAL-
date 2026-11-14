def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


def main():
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2],
    }
    print(dfs(graph, 0))


if __name__ == "__main__":
    main()
