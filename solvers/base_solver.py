from acceptance import *
from utils import *
import copy


class BaseSolver:
    ACCEPTANCE_CLASSES = {
        "accept_any": AcceptAny(),
        "accept_improving": AcceptImproving(),
    }

    def __init__(
        self, solution, llh_list, max_iterations, acceptance_criterion="accept_any"
    ):
        self.llh_list = llh_list
        self.max_iterations = max_iterations
        self.solution = solution
        self.best_solution = solution
        self.cost = calculate_objective(self.solution)
        self.best_cost = self.cost
        self.found_at = 0

        if acceptance_criterion not in self.ACCEPTANCE_CLASSES:
            raise ValueError(
                f"Unknown acceptance criterion '{acceptance_criterion}'. Available options: {list(self.ACCEPTANCE_CLASSES.keys())}"
            )
        else:
            self.acceptance = self.ACCEPTANCE_CLASSES[acceptance_criterion]

        self.acceptance = self.ACCEPTANCE_CLASSES[acceptance_criterion]

    def solve(self):
        raise NotImplementedError()

    def check_best(self, new_cost, new_solution, found_at):
        if new_cost < self.best_cost:
            self.best_cost = new_cost
            self.best_solution = copy.deepcopy(new_solution)
            self.found_at = found_at
