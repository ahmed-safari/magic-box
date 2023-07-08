from hyper_heuritics import HyperHeuristic
import csv
import json
import itertools


RUNS = 21

# Load the config file
with open("config.json", "r") as f:
    config = json.load(f)

# Define the parameter ranges
param_ranges = {
    "acceptance_method": ["accept_improving", "accept_annealing"],
    "selection_method": [
        "efficacy_roulette",
        "random",
        "reinforcement",
        "random_reinforcement",
    ],
    "n": [3],
}

# Get all combinations of parameter values
param_combinations = list(itertools.product(*param_ranges.values()))

# Create a CSV file to store the results
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Define the header row
    header = ["num_runs"] + list(param_ranges.keys()) + ["best_cost", "found_at"]

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

    writer.writerow(header)

    # For each combination of parameters...
    for params in param_combinations:
        # Create a new config dictionary for this combination
        new_config = dict(zip(param_ranges.keys(), params))

        # Update the main config with the new parameters
        config.update(new_config)

        # Initialize the lists to store the results for the runs
        best_costs = []
        found_at_list = []
        solutions = []

        # Initialize operator stats
        op_stats = {
            op.__class__.__name__: {
                "score": [],
                "selected": [],
                "accepted": [],
                "rejected": [],
            }
            for op in hyper_heuristic.llh_list
        }

        # Run the solver times
        for i in range(RUNS):
            # Create a new HyperHeuristic instance with the new config
            hyper_heuristic = HyperHeuristic(**config)
            # Solve the problem
            hyper_heuristic.solve()

            # Append the results to the respective lists
            best_costs.append(hyper_heuristic.best_cost)
            found_at_list.append(hyper_heuristic.found_at)
            # If the best cost is zero, append the solution
            if hyper_heuristic.best_cost == 0:
                solutions.append(hyper_heuristic.solution)

            # Collect operator stats
            for op in hyper_heuristic.llh_list:
                op_name = op.__class__.__name__
                op_stats[op_name]["score"].append(op.score)
                op_stats[op_name]["selected"].append(op.selected_count)
                op_stats[op_name]["accepted"].append(op.accepted_count)
                op_stats[op_name]["rejected"].append(
                    op.selected_count - op.accepted_count
                )

        # Prepare the row to write
        print(found_at_list)
        row = (
            [RUNS] + list(params) + [sum(best_costs) / RUNS, sum(found_at_list) / RUNS]
        )
        # Add operator stats
        for op in hyper_heuristic.llh_list:
            op_name = op.__class__.__name__
            row += [
                sum(op_stats[op_name][stat]) / RUNS
                for stat in ["score", "selected", "accepted", "rejected"]
            ]

        # Write a new row with the average results for this parameter combination
        writer.writerow(row)
