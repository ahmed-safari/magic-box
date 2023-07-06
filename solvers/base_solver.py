from acceptance import *
from utils import *
import copy

"""
Base class for solvers.
"""


class BaseSolver:
    # Dictionary of available acceptance criteria
    ACCEPTANCE_CLASSES = {
        "accept_any": AcceptAny(),
        "accept_improving": AcceptImproving(),
        "accept_with_tolerance": AcceptWithTolerance(tolerance=0.2),
        "accept_with_probability": AcceptWithProbability(acceptance_probability=0.05),
    }

    def __init__(
        self, solution, llh_list, max_iterations, acceptance_criterion="accept_any"
    ):
        self.llh_list = llh_list  # List of local search operators
        self.max_iterations = max_iterations  # Maximum number of iterations
        self.solution = solution  # Current solution
        self.best_solution = solution  # Best solution found so far
        self.cost = calculate_objective(self.solution)  # Current cost
        self.best_cost = self.cost  # Best cost found so far
        self.found_at = 0  # Iteration at which the best solution was found

        if (
            acceptance_criterion not in self.ACCEPTANCE_CLASSES
        ):  # If the acceptance criterion is not available
            # Raise an error
            raise ValueError(
                f"Unknown acceptance criterion '{acceptance_criterion}'. Available options: {list(self.ACCEPTANCE_CLASSES.keys())}"
            )
        else:  # If the acceptance criterion is available
            self.acceptance = self.ACCEPTANCE_CLASSES[
                acceptance_criterion
            ]  # Set the acceptance criterion

    def solve(self):
        raise NotImplementedError()

    # Check if the new solution is better than the current best one (and update it if so)
    def check_best(self, new_cost, new_solution, found_at):
        if (
            new_cost < self.best_cost
        ):  # If the new solution is better than the current best one
            self.best_cost = new_cost  # Update the best cost
            self.best_solution = copy.deepcopy(
                new_solution
            )  # Update the best solution by making a copy of the new solution
            self.found_at = (
                found_at  # Update the iteration at which the best solution was found
            )
