from operators import LLH_CLASSES
from solvers import RandomSelectionSolver
from utils import create_initial, calculate_objective


# Set parameters
N = 4
MAX_ITERATIONS = 1000


# Create a box
box = create_initial(N)

# Create the list of operators
operators = LLH_CLASSES


# Create a solver
solver = RandomSelectionSolver(box, operators, MAX_ITERATIONS)

# Solve the box
solver.solve()

# Print the solution
print("Best Solution:", solver.best_solution)
print("Best Cost:", solver.best_cost)
print("Found at iteration:", solver.found_at)

print("Final accepted cost:", solver.cost)
print("Final accepted solution:", solver.solution)
