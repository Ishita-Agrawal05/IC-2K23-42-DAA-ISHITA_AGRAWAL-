# Experiment Guidelines

Every program folder should contain its own `README.md` and implementation.
Use the following sections in the README and adapt them to the experiment:

1. **Problem statement**: Define the inputs, outputs, assumptions, and goal.
2. **Algorithm and approach**: Explain the method; include pseudocode and a
   flowchart when useful.
3. **Complexity analysis**: State best, average, and worst-case time and
   auxiliary-space complexity, with assumptions.
4. **Sample input and output**: Include a small, reproducible example.
5. **Correctness checks**: Describe edge cases and how results are validated.
6. **Experimental results**: Include input sizes, environment, measured data,
   and plots when analysis is required.
7. **Learning outcomes**: Summarize the algorithmic concepts demonstrated.

## Programming Practices

- Use descriptive names, small functions, docstrings, and consistent formatting.
- Validate inputs and handle empty, singleton, boundary, and invalid cases.
- Separate algorithm logic from input/output and performance measurement.
- Keep generated measurements reproducible where possible; record the random
  seed, repetitions, input distributions, and relevant environment details.
- Verify outputs against a simple trusted result or invariant before reporting
  timing. Exclude input generation and correctness checks from timed sections
  unless the experiment explicitly measures them.
- Store machine-readable measurements as CSV with a header and clear units.
- Label axes, units, algorithms, and input cases in every performance graph.
- Compare algorithms using the same datasets and explain sources of timing
  variation. Avoid conclusions based on a single measurement.

## Performance-Analysis Checklist

- Generate representative input for several increasing values of `n`.
- Include best-, average-, and worst-case patterns when applicable.
- Check the result for correctness on every input.
- Repeat timings and report an aggregate such as the mean or median.
- Save raw measurements and plot `n` against execution time.
- For algorithm comparisons, reuse each generated input across the algorithms.
- Discuss measured trends alongside theoretical time and space complexity.

The experiment README is the source of truth for dependencies and commands.
Keep shared diagrams and course-level supporting material in `docs/`.