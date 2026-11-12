# Traveling Salesperson Problem: Dynamic Programming

**Status:** Implementation pending.

## Problem and Algorithm
Find a minimum-cost tour visiting each city once and returning to the start.
Document the state representation and whether the graph must be complete.

## Complexity
The Held-Karp subset dynamic program takes `O(n^2 2^n)` time and `O(n 2^n)`
space.

## Validation and Results
Test one or two cities, symmetric and asymmetric costs, and known small tours.
Compare with exhaustive search for small instances and report memory growth.