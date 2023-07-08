import json
import itertools
import numpy as np
from hyper_heuritics import HyperHeuristic

parameters = {
    "acceptance_method": ["accept_improving"],
    "n": [5],
    "max_iterations": [10000],
    "selection_method": [
        "efficacy_roulette",
        "reinforcement",
        "random",
        "random_reinforcement",
    ],
    "max_stuck_count": range(10, 101, 10),
    "stuck_tolerance": [0.2, 0.3, 0.4, 0.5],
    "stuck_tolerance_increment": [0, 0.1, 0.2, 0.01, 0.02],
}

# Generate all combinations of parameters
parameter_combinations = list(itertools.product(*parameters.values()))

best_cost_avg = float("inf")
best_cost_std = float("inf")
best_parameters = None


runs_per_set = 21

# Test each combination of parameters
for combination in parameter_combinations:
    params = dict(zip(parameters.keys(), combination))
    print(f"Testing parameters: {params}")

    # Create the HyperHeuristic with the current parameters and run multiple times
    costs = []
    for _ in range(runs_per_set):
        hh = HyperHeuristic(**params)
        solution = hh.solve()
        cost = hh.best_cost
        costs.append(cost)

    # Calculate average and standard deviation of cost
    cost_avg = np.mean(costs)
    cost_std = np.std(costs)

    print(f"Average cost: {cost_avg}, Standard deviation: {cost_std}")

    # If this average cost is the best so far, save the parameters and the standard deviation
    if cost_avg < best_cost_avg:
        best_cost_avg = cost_avg
        best_cost_std = cost_std
        best_parameters = params

print(f"Best average cost: {best_cost_avg}, Standard deviation: {best_cost_std}")
print(f"Best parameters: {best_parameters}")

# Save the best parameters to a file
with open("best_parameters.json", "w") as f:
    json.dump(best_parameters, f)
