# Maximum and Minimum: Divide and Conquer

**Status:** Implementation pending.

## Problem
Find both the minimum and maximum values in a non-empty sequence.

## Algorithm and Complexity
Split the sequence, solve each half, and combine the two pairs of extrema.
The divide-and-conquer method takes `O(n)` time and `O(log n)` recursion space
for balanced splits.

## Validation and Results
Test one element, repeated values, negative values, and mixed input. Add
pseudocode, sample input/output, comparison counts, and measured results when
implemented.