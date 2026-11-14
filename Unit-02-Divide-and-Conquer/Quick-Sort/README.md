# Quick Sort

**Status:** Implementation pending in this unit. A quick-sort implementation
and performance results already exist in [Unit 1 Sorting](../../Unit-01-Introduction-to-Algorithms/Sorting/README.md).

## Algorithm and Complexity
Partition around a pivot and recursively sort the partitions. Expected time is
`O(n log n)`, worst-case time is `O(n^2)`, and average recursion space is
`O(log n)` (worst case `O(n)`).

## Validation and Results
Test duplicates, sorted and reverse-sorted inputs, and pivot-sensitive cases.
Verify output and record timings for increasing `n`; document pivot policy and
the observed recursion behavior.