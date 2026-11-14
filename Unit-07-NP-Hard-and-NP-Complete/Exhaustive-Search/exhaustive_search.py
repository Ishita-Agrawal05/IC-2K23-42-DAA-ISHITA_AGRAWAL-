from itertools import permutations


def tsp_exhaustive(graph):
    n = len(graph)
    best_cost = float('inf')
    best_path = None

    for perm in permutations(range(1, n)):
        cost = graph[0][perm[0]]
        for i in range(len(perm) - 1):
            cost += graph[perm[i]][perm[i + 1]]
        cost += graph[perm[-1]][0]
        if cost < best_cost:
            best_cost = cost
            best_path = (0,) + perm + (0,)

    return best_cost, best_path


def main():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    cost, path = tsp_exhaustive(graph)
    print(f"Best cost: {cost}")
    print(f"Best path: {path}")


if __name__ == "__main__":
    main()
