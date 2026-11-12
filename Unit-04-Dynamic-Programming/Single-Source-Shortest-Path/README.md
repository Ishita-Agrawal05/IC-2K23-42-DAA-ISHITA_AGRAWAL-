# Single-Source Shortest Path

**Status:** Implementation pending.

## Problem and Algorithm
Compute shortest paths from one source. Specify the selected algorithm and
the graph constraints, especially whether negative edge weights are allowed.

## Complexity
State complexity for the chosen algorithm and representation. For example,
Dijkstra with a binary heap and adjacency lists is `O((V + E) log V)` and does
not support negative edge weights; Bellman-Ford is `O(VE)`.

## Validation and Results
Test unreachable vertices, multiple routes, and weights at the supported
boundary. Compare results with a reference and document the algorithm choice.