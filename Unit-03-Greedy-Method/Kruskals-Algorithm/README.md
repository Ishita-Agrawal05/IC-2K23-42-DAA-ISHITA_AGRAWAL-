# Kruskal's Minimum Spanning Tree

**Status:** Implementation pending.

## Problem and Algorithm
Find a minimum spanning tree of a connected, undirected, weighted graph. Sort
edges by weight and add an edge only when it joins two components.

## Complexity
Sorting edges takes `O(E log E)`; disjoint-set operations are nearly constant a mortized time, giving overall `O(E log E)` time.

## Validation and Results
Test equal weights, cycles, disconnected inputs, and known small MSTs. Compare
total weight with Prim's result on the same graphs and record graph sizes and
timings when implemented.
