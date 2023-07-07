from acceptance import *
from operators import LLH_CLASSES
from selection import *
from utils import *
import json


class HyperHeuristic:
    def __init__(
        self,
        acceptance_method="accept_any",
        selection_method="random_selection",
        max_iterations=1000,
        n=3,
        max_stuck_count=10,
        acceptance_tolerance=0.2,
        acceptance_probability=0.5,
        reinforcment_training_percentage=0.1,
        random_reinforcement_selection_percentage=0.1,
    ):
        self.llh_list = LLH_CLASSES
        self.max_iterations = max_iterations
        self.n = n
        self.max_stuck_count = max_stuck_count
        self.best_cost = None
        self.found_at = None
        self.solution = None
        self.acceptance_classes = {
            "accept_any": AcceptAny(),
            "accept_improving": AcceptImproving(),
            "accept_with_tolerance": AcceptWithTolerance(
                tolerance=acceptance_tolerance,
                max_stuck_count=max_stuck_count,
            ),
            "accept_with_probability": AcceptWithProbability(
                acceptance_probability=acceptance_probability
            ),
        }

        self.selection_classes = {
            "random_selection": RandomSelection(
                llh_list=self.llh_list,
                max_iterations=self.max_iterations,
            ),
            "efficacy_roulette_selection": EfficacyRouletteSelection(
                llh_list=self.llh_list,
                max_iterations=self.max_iterations,
            ),
            "reinforcment_selection": ReinforcementSelection(
                llh_list=self.llh_list,
                max_iterations=self.max_iterations,
                training_percentage=reinforcment_training_percentage,
            ),
            "random_reinforcement_selection": RandomReinforcementSelection(
                llh_list=self.llh_list,
                max_iterations=self.max_iterations,
                training_percentage=reinforcment_training_percentage,
                random_selection_percentage=random_reinforcement_selection_percentage,
            ),
        }
        # TODO: Add checks
        if (
            acceptance_method not in self.acceptance_classes
        ):  # If the acceptance criterion is not available
            # Raise an error
            raise ValueError(
                f"Unknown acceptance criterion '{acceptance_method}'. Available options: {list(self.acceptance_classes.keys())}"
            )
        else:  # If the acceptance criterion is available
            self.acceptance_method = self.acceptance_classes[acceptance_method]

        if (
            selection_method not in self.selection_classes
        ):  # If the selection method is not available
            # Raise an error
            raise ValueError(
                f"Unknown selection method '{selection_method}'. Available options: {list(self.selection_classes.keys())}"
            )
        else:  # If the selection method is available
            self.selection_method = self.selection_classes[selection_method]

    @classmethod
    def setup(self, filename="config.json"):
        # Read the configuration file

        with open(filename, "r") as f:
            params = json.load(f)
        # print(params)
        # Create the HyperHeuristic instance using the parameters from the configuration file
        return self(**params)

    def solve(self):
        print(
            f"Running hyper-heuristic with {self.max_iterations} iterations, to solve {self.n}x{self.n} box with {self.max_stuck_count} max stuck count. \nAcceptance criterion: {self.acceptance_method.__class__.__name__}, Selection method: {self.selection_method.__class__.__name__}"
        )

        solution = create_initial(self.n)
        new_cost = old_cost = self.best_cost = calculate_objective(solution)
        did_accept = True

        for i in range(0, self.max_iterations):
            if old_cost == 0:
                break

            operator = self.selection_method.select_operator(
                new_cost,
                old_cost,
                did_accept,
                current_iteration=i,
            )

            operator.apply(solution)

            new_cost = calculate_objective(solution)
            self.check_best(new_cost, i + 1)

            did_accept = self.acceptance_method.accept(new_cost, old_cost)
            self.selection_method.update_operator_stats(did_accept)
            self.selection_method.update_operator_score(new_cost, old_cost, did_accept)

            if did_accept:
                old_cost = new_cost
            else:
                operator.revert(solution)

        self.solution = solution
        return solution

    # Check if the new solution is better than the current best one (and update it if so)
    def check_best(self, new_cost, found_at):
        if (
            new_cost < self.best_cost
        ):  # If the new solution is better than the current best one
            self.best_cost = new_cost  # Update the best cost
            # self.best_solution = copy.deepcopy(
            #     new_solution
            # )  # Update the best solution by making a copy of the new solution
            self.found_at = (
                found_at  # Update the iteration at which the best solution was found
            )
