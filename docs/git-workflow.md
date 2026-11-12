# Git Workflow

## Repository Setup

Create one GitHub repository for the course using the name
`RollNo-DAA-Your_Name`, then connect this local repository to it. Do not create
separate repositories for individual units.

## Day-to-Day Work

1. Pull the latest `main` before starting a lab.
2. Work in the relevant unit and experiment folder.
3. Run the program and its correctness checks; inspect generated CSV and plots.
4. Review `git status` and `git diff` before staging.
5. Commit focused changes with a message describing the experiment or fix.
6. Push the branch and open a pull request if the repository uses review.

Example commands:

```bash
git pull --ff-only
git switch -c unit-2-merge-sort
git status
git diff
git add Unit-02-Divide-and-Conquer/Merge-Sort
git commit -m "Add divide-and-conquer merge sort experiment"
git push -u origin unit-2-merge-sort
```

Do not commit virtual environments, bytecode caches, editor state, or unrelated
generated files. Keep experiment results and graphs when they are requested
deliverables, and regenerate them when their source measurements change.