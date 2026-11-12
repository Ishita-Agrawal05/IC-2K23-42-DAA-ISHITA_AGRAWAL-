# Traveling Salesperson Problem: Branch and Bound

**Status:** Implementation pending.

## Problem and Algorithm
Find a minimum-cost tour visiting each city once and returning to the start.
Describe the tour expansion order, lower bound, and pruning rule.

## Complexity
Worst-case time is factorial, `O(n!)`; actual work depends on bound quality
and input. Record the memory required by the active search frontier.

## Validation and Results
Compare tour cost with Unit 4 dynamic programming and exhaustive search on
small graphs. Record runtime, explored nodes, memory, and solution quality as
the number of cities grows.