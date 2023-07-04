from utils import *


class RandomSelectionSolver:
    def __init__(self, solution, llh_list, max_iterations):
        self.llh_list = llh_list
        self.max_iterations = max_iterations
        self.solution = solution
        self.cost = calculate_objective(self.solution)
        self.found_at = 0

    def solve(self):
        # Iterate until the maximum number of iterations is reached
        for i in range(self.max_iterations):
            if self.cost == 0:
                # print("Solution found!")
                break

            # Choose a random operator
            operator = random.choice(self.llh_list)

            # Apply the operator
            operator.apply(self.solution)

            # Calculate the new cost
            new_cost = calculate_objective(self.solution)

            # TODO: Implement acceptance criterion method
            # If the new cost is better than the current cost, update the current cost and the best solution
            if new_cost < self.cost:
                self.cost = new_cost
                self.found_at = i
            # Otherwise, revert the operator
            else:
                operator.revert(self.solution)
        return self.solution
