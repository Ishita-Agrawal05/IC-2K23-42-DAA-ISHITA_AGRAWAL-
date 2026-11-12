# Algorithm Design & Analysis Laboratory

Repository for the DAA laboratory experiments, organized by course unit. The
repository name should follow `RollNo-DAA-Your_Name` when creating or renaming
the GitHub repository. The current Git remote is preserved as-is.

## Units

| Unit | Topic | Experiments |
| --- | --- | --- |
| [Unit 1](Unit-01-Introduction-to-Algorithms/) | Introduction to Algorithms and Performance Analysis | [Searching](Unit-01-Introduction-to-Algorithms/Searching/), [Sorting](Unit-01-Introduction-to-Algorithms/Sorting/), [Complexity Analysis](Unit-01-Introduction-to-Algorithms/Complexity-Analysis/), [Performance Measurement](Unit-01-Introduction-to-Algorithms/Performance-Measurement/) |
| [Unit 2](Unit-02-Divide-and-Conquer/) | Divide and Conquer | [Binary Search](Unit-02-Divide-and-Conquer/Binary-Search/), [Max-Min](Unit-02-Divide-and-Conquer/Max-Min/), [Merge Sort](Unit-02-Divide-and-Conquer/Merge-Sort/), [Quick Sort](Unit-02-Divide-and-Conquer/Quick-Sort/), [Heap Sort](Unit-02-Divide-and-Conquer/Heap-Sort/), [Strassen Matrix Multiplication](Unit-02-Divide-and-Conquer/Strassen-Matrix-Multiplication/) |
| [Unit 3](Unit-03-Greedy-Method/) | Greedy Method | [Fractional Knapsack](Unit-03-Greedy-Method/Fractional-Knapsack/), [Job Sequencing](Unit-03-Greedy-Method/Job-Sequencing/), [Prim's Algorithm](Unit-03-Greedy-Method/Prims-Algorithm/), [Kruskal's Algorithm](Unit-03-Greedy-Method/Kruskals-Algorithm/) |
| [Unit 4](Unit-04-Dynamic-Programming/) | Dynamic Programming | [Recursive Fibonacci](Unit-04-Dynamic-Programming/Recursive-Fibonacci/), [Memoized Fibonacci](Unit-04-Dynamic-Programming/Memoized-Fibonacci/), [0/1 Knapsack](Unit-04-Dynamic-Programming/0-1-Knapsack/), [Multistage Graph](Unit-04-Dynamic-Programming/Multistage-Graph/), [Floyd-Warshall](Unit-04-Dynamic-Programming/Floyd-Warshall/), [Single-Source Shortest Path](Unit-04-Dynamic-Programming/Single-Source-Shortest-Path/), [TSP](Unit-04-Dynamic-Programming/TSP-Dynamic-Programming/) |
| [Unit 5](Unit-05-Traversal-and-Search/) | Traversal and Search | [Binary Tree Traversals](Unit-05-Traversal-and-Search/Binary-Tree-Traversals/), [Graph Representation](Unit-05-Traversal-and-Search/Graph-Representation/), [BFS](Unit-05-Traversal-and-Search/BFS/), [DFS](Unit-05-Traversal-and-Search/DFS/) |
| [Unit 6](Unit-06-Backtracking/) | Backtracking | [General Backtracking](Unit-06-Backtracking/General-Backtracking/), [N-Queens](Unit-06-Backtracking/N-Queens/), [Sum of Subsets](Unit-06-Backtracking/Sum-of-Subsets/) |
| [Unit 7](Unit-07-NP-Hard-and-NP-Complete/) | NP-Hard, NP-Complete, and Advanced Optimization | [Exhaustive Search](Unit-07-NP-Hard-and-NP-Complete/Exhaustive-Search/), [0/1 Knapsack with Branch and Bound](Unit-07-NP-Hard-and-NP-Complete/0-1-Knapsack-Branch-and-Bound/), [TSP with Branch and Bound](Unit-07-NP-Hard-and-NP-Complete/TSP-Branch-and-Bound/) |

Unit 1 contains the existing implementations and experimental artifacts. The
other experiment directories currently contain documentation scaffolds; add
the implementation and measured results as each lab is completed.

## Documentation and Practices

- [Experiment documentation checklist](docs/experiment-guidelines.md)
- [Git workflow](docs/git-workflow.md)
- Each experiment folder has its own `README.md` documenting the work and its
	implementation status.
- Keep implementations focused, readable, validated with representative edge
	cases, and accompanied by complexity analysis.
- Performance experiments should use reproducible inputs, verify correctness,
	record measurements in CSV, and generate labeled plots. Compare algorithms
	on the same inputs where the comparison is meaningful.

## Running Existing Unit 1 Programs

Run a script from its experiment directory. For example:

```bash
cd Unit-01-Introduction-to-Algorithms/Sorting
python sorting_performance_comparison.py
```

The searching and sorting folders also contain notebooks, result CSV files,
and generated performance graphs. See their READMEs for details and commands.