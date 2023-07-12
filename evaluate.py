from hyper_heuritics import HyperHeuristic
import csv
import json
import itertools
from datetime import datetime

RUNS = 31

# Load the config file
with open("config.json", "r") as f:
    config = json.load(f)

# Define the parameter ranges
param_ranges = {
    "acceptance_method": ["accept_any", "accept_improving", "accept_annealing", "accept_with_probability", "accept_with_tolerance"],
    "selection_method": [
        "efficacy_roulette",
        "random",
        "reinforcement",
        "random_reinforcement",
    ],
    "n": [8],
}

# Get all combinations of parameter values
param_combinations = list(itertools.product(*param_ranges.values()))

# Define the header row
header = ["run_number"] + list(param_ranges.keys()) + ["best_cost", "found_at"]

hyper_heuristic = HyperHeuristic.setup("config.json")
# Add headers for operator stats
for op in hyper_heuristic.llh_list:
    op_name = op.__class__.__name__
    header += [
        f"{op_name}_score",
        f"{op_name}_selected",
        f"{op_name}_accepted",
        f"{op_name}_rejected",
    ]

# Create a timestamped filename
filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_results.csv"

# Create a CSV file to store the results
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    # For each combination of parameters...
    for params in param_combinations:
        # Create a new config dictionary for this combination
        new_config = dict(zip(param_ranges.keys(), params))

        # Update the main config with the new parameters
        config.update(new_config)

        # Run the solver
        for i in range(RUNS):
            # Create a new HyperHeuristic instance with the new config
            hyper_heuristic = HyperHeuristic(**config)
            # Solve the problem
            hyper_heuristic.solve()

            # Initialize operator stats
            op_stats = {
                op.__class__.__name__: {
                    "score": op.score,
                    "selected": op.selected_count,
                    "accepted": op.accepted_count,
                    "rejected": op.selected_count - op.accepted_count,
                }
                for op in hyper_heuristic.llh_list
            }

            # Prepare the row to write
            row = (
                [i + 1]
                + list(params)
                + [hyper_heuristic.best_cost, hyper_heuristic.found_at]
            )

            # Add operator stats
            for op in hyper_heuristic.llh_list:
                op_name = op.__class__.__name__
                row += [
                    op_stats[op_name][stat]
                    for stat in ["score", "selected", "accepted", "rejected"]
                ]

            # Write a new row for each run
            writer.writerow(row)
