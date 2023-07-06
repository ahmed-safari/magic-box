from operators import LLH_CLASSES
from solvers import (
    RandomSelectionSolver,
    EfficacyRouletteSolver,
    ReinforcementSolver,
    RandomReinforcementSolver,
)
from utils import create_initial, calculate_objective


# Set parameters
N = 4
MAX_ITERATIONS = 100


# Create a box
box = create_initial(N)

# Create the list of operators
operators = LLH_CLASSES


# Create a solver
solver = RandomReinforcementSolver(
    box,
    operators,
    MAX_ITERATIONS,
    acceptance_criterion="accept_improving",
    training_percentage=0.2,
    random_selection_percentage=0.5,
)

# Solve the box
solver.solve()

# Print the solution
print("Best Solution:", solver.best_solution)
print("Best Cost:", solver.best_cost)
print("Found at iteration:", solver.found_at)

print("Final accepted cost:", solver.cost)
print("Final accepted solution:", solver.solution)

# Print scores of the operators
print("Scores:")
for operator in solver.llh_list:
    print(f"{operator.__class__.__name__}: {operator.score}")
