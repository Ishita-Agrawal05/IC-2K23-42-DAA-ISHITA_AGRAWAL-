# N-Queens

**Status:** Implemented.

## Problem and Algorithm
Place `N` queens on an `N x N` board so no two share a row, column, or
diagonal. Include the 4-Queens and 8-Queens cases and support general `N`.

### Example board for 4-Queens

```text
Q . . .
. . Q .
. . . .
. Q . .
```

This is one valid arrangement for the 4-Queens problem. The `Q` positions are in different rows, columns, and diagonals.

### Diagram of a 4x4 board

```text
  c1 c2 c3 c4
r1  Q  .  .  .
r2  .  .  Q  .
r3  .  .  .  .
r4  .  Q  .  .
```

The backtracking algorithm places one queen in each row and checks safety before moving to the next row.

## Complexity
The search is exponential in `N`; a straightforward row-by-row solver has at
most `O(N!)` candidate placements with `O(N)` auxiliary state, excluding
solutions stored in memory.

## Validation and Results
Verify every returned board's constraints and count solutions for known small
values. Record explored states and runtime as `N` grows.