# N-Queens

**Status:** Implementation pending.

## Problem and Algorithm
Place `N` queens on an `N x N` board so no two share a row, column, or
diagonal. Include the 4-Queens and 8-Queens cases and support general `N`.

## Complexity
The search is exponential in `N`; a straightforward row-by-row solver has at
most `O(N!)` candidate placements with `O(N)` auxiliary state, excluding
solutions stored in memory.

## Validation and Results
Verify every returned board's constraints and count solutions for known small
values. Record explored states and runtime as `N` grows.