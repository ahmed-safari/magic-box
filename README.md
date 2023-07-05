# Magic Square Solver 🧩

## Overview 📚

The Magic Square Solver is a python-based project 🐍 designed to solve the challenging problem of constructing a magic square. A magic square is an `n x n` matrix, filled with distinct positive integers in the range `1,2,...,n²`, such that each of the `n` rows, `n` columns, and the two diagonals sum to the same total.

This project utilizes a variety of heuristic strategies 🔀 to solve the magic square problem. These strategies include:

1. Random Selection 🎲
   ... More soon

## Structure 🏗️

The codebase is divided into several modules, each responsible for a particular part of the solution:

- `operators/`: This directory contains low-level heuristics, with each heuristic represented by its own class.
- `solvers/`: This directory contains different solver classes, each implementing a specific high-level heuristic strategy.
- `acceptannce/`: This directory contains different acceptance criteria, each represented by its own class.
- `utils.py`: This file contains helper functions used throughout the project.
- `playground.py`: This file is used for testing and playing around.
- `main.py`: This file is the main entry point where everything will be combined.

## Usage 💻

First, import the necessary modules:

```python
from operators import SwapElements, SwapRows, SwapColumns
from solvers import RandomSelectionSolver
from utils import create_initial, calculate_objective
```

Create a list of low-level heuristics:

```python
LLH_LIST = [SwapElements(), SwapRows(), SwapColumns(), ...]
```

Create an instance of a solver, and use it to solve the problem:

```python
solver = RandomSelectionSolver(LLH_LIST, create_initial, calculate_objective)
box, cost, found_at = solver.solve()
```

The `solve` method returns the best box found, but you can access its cost (how far it is from being a perfect magic square), and the iteration at which it was found, by using the attributes of the solver class (cost and found_at).
