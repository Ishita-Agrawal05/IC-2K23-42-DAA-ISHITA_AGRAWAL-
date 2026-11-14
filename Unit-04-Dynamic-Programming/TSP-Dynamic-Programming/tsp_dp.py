"""Traveling Salesman Problem using dynamic programming."""


def tsp_dp(graph):
    n = len(graph)
    if n <= 1:
        return 0

    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        if not (mask & 1):
            continue
        for current in range(n):
            if not (mask & (1 << current)):
                continue
            for nxt in range(1, n):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                dp[new_mask][nxt] = min(
                    dp[new_mask][nxt],
                    dp[mask][current] + graph[current][nxt],
                )

    final_mask = (1 << n) - 1
    best_cost = float('inf')
    for city in range(1, n):
        best_cost = min(best_cost, dp[final_mask][city] + graph[city][0])

    return best_cost


def main():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    print(f"Minimum tour cost: {tsp_dp(graph)}")


if __name__ == "__main__":
    main()
