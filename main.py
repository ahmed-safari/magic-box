from operators import SwapElements
from solvers import RandomSelectionSolver
from utils import create_initial, calculate_objective


# Set parameters
N = 4
MAX_ITERATIONS = 1000


# Create a box
box = create_initial(N)

# Create the list of operators
operators = [SwapElements()]


# Create a solver
solver = RandomSelectionSolver(box, operators, MAX_ITERATIONS)

# Solve the box
# solver.solve()

# Test operators
print("Initial:", box)
operators[0].apply(box)
print("After apply:", box)
operators[0].revert(box)
print("After revert:", box)
