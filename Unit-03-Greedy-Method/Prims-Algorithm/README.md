# Prim's Minimum Spanning Tree

**Status:** Implementation pending.

## Problem and Algorithm
Find a minimum spanning tree of a connected, undirected, weighted graph.
Grow one tree by repeatedly adding its lightest outgoing edge.

## Complexity
Document the graph representation and priority-queue choice. An adjacency
matrix implementation is `O(V^2)`; a binary heap with adjacency lists is
`O((V + E) log V)`.

## Validation and Results
Test a single vertex, equal edge weights, disconnected graphs, and known small
MSTs. Compare total weight with Kruskal's result on the same graphs.