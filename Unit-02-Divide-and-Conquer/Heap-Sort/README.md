# Heap Sort

**Status:** Implementation pending in this unit. A heap-sort implementation
is included in the [Unit 1 Sorting comparison](../../Unit-01-Introduction-to-Algorithms/Sorting/README.md).

## Algorithm and Complexity
Build a max heap, repeatedly move its root to the sorted suffix, and restore
the heap. Time is `O(n log n)` in best, average, and worst cases; in-place
auxiliary space is `O(1)` for an iterative implementation.

## Validation and Results
Test empty, singleton, duplicate, and already ordered inputs. Verify sorted
output and record timings for increasing input sizes when this unit's version
is added.