import math


def tsp_branch_and_bound(graph):
    n = len(graph)
    best_cost = math.inf
    best_path = None
    visited = [False] * n
    path = [0]
    visited[0] = True
    lower_bound = [0] * n

    def bound(current_cost, current_node):
        min_outgoing = min(graph[current_node])
        return current_cost + min_outgoing

    def dfs(current_cost, current_node):
        nonlocal best_cost, best_path

        if len(path) == n:
            total_cost = current_cost + graph[current_node][0]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [0]
            return

        for nxt in range(n):
            if not visited[nxt] and graph[current_node][nxt] != math.inf:
                if current_cost + graph[current_node][nxt] < best_cost:
                    visited[nxt] = True
                    path.append(nxt)
                    dfs(current_cost + graph[current_node][nxt], nxt)
                    path.pop()
                    visited[nxt] = False

    dfs(0, 0)
    return best_cost, best_path


def main():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    cost, path = tsp_branch_and_bound(graph)
    print(f"Best cost: {cost}")
    print(f"Best path: {path}")


if __name__ == "__main__":
    main()
