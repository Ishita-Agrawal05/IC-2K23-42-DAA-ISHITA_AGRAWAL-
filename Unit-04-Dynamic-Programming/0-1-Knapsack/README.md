# 0/1 Knapsack: Dynamic Programming

**Status:** Implementation pending.

## Problem and Algorithm
Choose each item at most once to maximize value without exceeding capacity.
Document the recurrence and whether the table uses one or two dimensions.

## Complexity
The standard table takes `O(nW)` time and `O(nW)` space, or `O(W)` space with
a correctly ordered one-dimensional update. `W` is capacity, so this is
pseudo-polynomial in the numeric input.

## Validation and Results
Test zero capacity, zero-weight assumptions, no items, and cases where an
item cannot fit. Compare small cases with exhaustive search.