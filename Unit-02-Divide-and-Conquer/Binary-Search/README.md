# Binary Search: Divide and Conquer

**Status:** Implementation pending.

## Problem
Find a target value in a sorted sequence and return its index, or report that
it is absent. State how duplicate values are handled.

## Algorithm and Complexity
Repeatedly halve the remaining search interval. Expected time is `O(log n)`;
iterative auxiliary space is `O(1)`, while recursive space is `O(log n)`.

## Validation and Results
Test empty and singleton inputs, boundary targets, duplicates, and missing
targets. Add pseudocode, sample input/output, implementation command, and
measured results when the experiment is implemented.