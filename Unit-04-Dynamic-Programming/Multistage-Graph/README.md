# Multistage Graph

**Status:** Implementation pending.

## Problem and Algorithm
Find a minimum-cost path from a source stage to a destination stage in a
directed multistage graph. State edge direction and unreachable-node handling.

## Complexity
Backward dynamic programming processes each vertex and edge once, for
`O(V + E)` time and `O(V)` auxiliary storage, excluding the graph.

## Validation and Results
Test a single path, competing paths, unreachable vertices, and negative edge
weights when the graph remains acyclic. Compare with a reference shortest-path
calculation.