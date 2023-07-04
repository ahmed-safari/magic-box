from operators import SwapElements, SwapRows, SwapColumns
from solvers import RandomSelectionSolver
from utils import create_initial, calculate_objective


# Set parameters
N = 4
MAX_ITERATIONS = 1000


# Create a box
box = create_initial(N)

# Create the list of operators
operators = [SwapElements(), SwapRows(), SwapColumns()]


# Create a solver
solver = RandomSelectionSolver(box, operators, MAX_ITERATIONS)

# Solve the box
solver.solve()

# Print the solution
print("Solution:", solver.solution)
print("Cost:", solver.cost)
print("Found at iteration:", solver.found_at)
