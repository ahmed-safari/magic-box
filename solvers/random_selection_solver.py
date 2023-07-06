from utils import *
from acceptance import *
from .base_solver import BaseSolver


class RandomSelectionSolver(BaseSolver):
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
            # Check if the new solution is better than the current best one (and update it if so)
            self.check_best(new_cost, self.solution, i)

            # Check if the new solution is accepted
            if self.acceptance.accept(new_cost=new_cost, old_cost=self.cost):
                self.cost = new_cost  # Update the current cost

            # Otherwise, revert the operator
            else:
                operator.revert(self.solution)

        return self.best_solution
