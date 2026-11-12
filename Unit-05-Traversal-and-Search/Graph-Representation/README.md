# Graph Representation

**Status:** Implementation pending.

## Problem and Algorithm
Represent the same graph as an adjacency matrix and adjacency list. Document
whether graphs are directed and weighted and how duplicate edges are handled.

## Complexity
An adjacency matrix uses `O(V^2)` space and offers `O(1)` edge lookup. An
adjacency list uses `O(V + E)` space; neighbor iteration is proportional to
the vertex degree.

## Validation and Results
Test isolated vertices, self-loops if allowed, and directed/undirected edges.
Compare edge sets after converting between representations.