# import copy
# import matplotlib.pyplot as plt
# from operators import LLH_CLASSES
# from solvers import (
#     RandomSelectionSolver,
#     EfficacyRouletteSolver,
#     ReinforcementSolver,
#     RandomReinforcementSolver,
# )
# from utils import create_initial
# import numpy as np

# # Set parameters
# N = 4
# MAX_ITERATIONS = 10000
# ACCEPTANCE_CRITERIA = [
#     "accept_improving",
#     "accept_any",
#     "accept_with_tolerance",
#     "accept_with_probability",
# ]
# SOLVER_CLASSES = [
#     RandomSelectionSolver,
#     EfficacyRouletteSolver,
#     ReinforcementSolver,
#     # RandomReinforcementSolver,
# ]
# RUNS = 31

# # Create a box
# box = create_initial(N)

# # Create the list of operators
# operators = LLH_CLASSES

# # Test all solver/criterion combinations
# costs = {
#     solver.__name__ + " (" + criterion + ")": []
#     for solver in SOLVER_CLASSES
#     for criterion in ACCEPTANCE_CRITERIA
# }
# iterations = {
#     solver.__name__ + " (" + criterion + ")": []
#     for solver in SOLVER_CLASSES
#     for criterion in ACCEPTANCE_CRITERIA
# }

# for Solver in SOLVER_CLASSES:
#     for criterion in ACCEPTANCE_CRITERIA:
#         for _ in range(RUNS):
#             # box = create_initial(N)
#             box_copy = copy.deepcopy(box)

#             # Create a solver
#             solver = Solver(
#                 box_copy, operators, MAX_ITERATIONS, acceptance_criterion=criterion
#             )

#             # Solve the box
#             solver.solve()

#             # Store the result
#             costs[Solver.__name__ + " (" + criterion + ")"].append(solver.best_cost)
#             iterations[Solver.__name__ + " (" + criterion + ")"].append(solver.found_at)

# # Sort the results by median best cost, ascending
# sorted_keys = sorted(costs.keys(), key=lambda x: np.median(costs[x]))

# # Plot the results
# plt.figure(figsize=(10, 5))

# # Box plot of best costs
# plt.subplot(121)
# plt.boxplot([costs[key] for key in sorted_keys], vert=False, patch_artist=True)
# plt.yticks(np.arange(1, len(sorted_keys) + 1), sorted_keys)
# plt.xlabel("Best Cost")
# plt.title("Best Cost Box Plots")

# # Box plot of iterations at which the best solution was found
# plt.subplot(122)
# plt.boxplot([iterations[key] for key in sorted_keys], vert=False, patch_artist=True)
# plt.yticks(np.arange(1, len(sorted_keys) + 1), sorted_keys)
# plt.xlabel("Found_at Iteration")
# plt.title("Iteration Box Plots")

# plt.tight_layout()
# plt.show()
