# Unit 7: NP-Hard, NP-Complete, and Advanced Optimization

This unit explores optimization problems that are computationally difficult to solve exactly in polynomial time. The focus is on understanding how branch-and-bound strategies improve search efficiency over naive exhaustive enumeration.

## Experiments

- [Exhaustive Search](Exhaustive-Search/)
  - Solve the Traveling Salesman Problem by enumerating all possible tours.
  - Use this as a baseline for measuring combinatorial explosion.

- [0/1 Knapsack with Branch and Bound](0-1-Knapsack-Branch-and-Bound/)
  - Apply branch-and-bound to maximize profit under weight constraints.
  - Compare with the dynamic-programming solution from Unit 4.

- [TSP with Branch and Bound](TSP-Branch-and-Bound/)
  - Use a bounded search tree to find the minimum-cost tour.
  - Compare with the dynamic-programming TSP solution from Unit 4.

## Objectives

- Understand the idea of NP-hard and NP-complete optimization problems.
- Demonstrate how exhaustive search grows exponentially with problem size.
- Analyze the improvement provided by branch-and-bound pruning.
- Compare exact optimization methods with dynamic-programming approaches where applicable.

## Evaluation Criteria

For each experiment, record:

- execution time
- number of explored nodes / states
- memory usage
- quality of the final solution
- scalability as input size increases

## Comparison with Unit 4

Where relevant, compare branch-and-bound methods with the dynamic-programming solutions implemented in Unit 4:

- 0/1 knapsack: DP vs branch-and-bound
- TSP: DP vs branch-and-bound

This helps demonstrate the trade-off between exact optimization and search-space pruning.

## Reference

- [Experiment guidelines](../docs/experiment-guidelines.md)
- [Main project README](../README.md)