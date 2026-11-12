# Breadth-First Search

**Status:** Implementation pending.

## Problem and Algorithm
Traverse a graph from a start vertex in increasing distance layers using a
queue. Specify behavior for disconnected vertices.

## Complexity
With adjacency lists, time is `O(V + E)` and auxiliary space is `O(V)`.

## Validation and Results
Test an isolated start, cycles, disconnected components, and a graph with
multiple shortest paths. Verify visit order and distances on small graphs.