# Fractional Knapsack

**Status:** Implementation pending.

## Problem and Algorithm
Given item values and weights plus a capacity, maximize value when fractions
of items are allowed. Greedily take items in descending value-to-weight ratio.

## Complexity
Sorting dominates at `O(n log n)` time; auxiliary space depends on whether
items are copied for sorting.

## Validation and Results
Test zero capacity, an item heavier than capacity, exact fits, and tied ratios.
Compare small cases with an independent reference and record sample input,
output, and results when implemented.