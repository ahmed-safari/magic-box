from utils import *
from acceptance import *
from .base_solver import BaseSolver


class RandomReinforcementSolver(BaseSolver):
    def __init__(
        self,
        solution,
        llh_list,
        max_iterations,
        acceptance_criterion="accept_any",
        training_percentage=0.1,
        random_selection_percentage=0.1,
    ):
        super().__init__(solution, llh_list, max_iterations, acceptance_criterion)
        self.training_percentage = training_percentage
        self.random_selection_percentage = random_selection_percentage

    def solve(self):
        # Create the list with scores of operators initalized to 0

        # operators_scores = [0 for _ in range(len(self.llh))]
        operators_scores = [0] * len(self.llh_list)

        for i in range(self.max_iterations):
            if self.cost == 0:
                return self.solution  # return the solution if found

            # if we are in the first x% of the iterations, select an operator in a round robin fashion
            if i < self.max_iterations * self.training_percentage:
                # print("Training phase")
                operator_index = i % len(operators_scores)
                operator = self.llh_list[operator_index]
                # print(operator.__class__.__name__)

            # Else, select the LLH with the highest score
            else:
                # print("Selection phase")
                # generate number between where the training phase ends and and number of iterations
                random_number = random.randint(
                    self.max_iterations * self.training_percentage,
                    self.max_iterations,
                )
                # print(random_number)
                # if the random number is less than the random selection percentage, select a random operator
                if (
                    random_number
                    < self.max_iterations * self.random_selection_percentage
                ):
                    # print("Random selection")
                    operator_index = random.randint(0, len(operators_scores) - 1)
                    operator = self.llh_list[operator_index]
                else:
                    # print("Highest score selection")
                    operator_index = operators_scores.index(max(operators_scores))
                    operator = self.llh_list[operator_index]
                # print(operator.__class__.__name__)

            # Apply the operator
            operator.apply(self.solution)

            # Calculate the new cost
            new_cost = calculate_objective(self.solution)

            # Check if the new solution is better than the current best one (and update it if so)
            self.check_best(new_cost, self.solution, i)

            if self.acceptance.accept(new_cost=new_cost, old_cost=self.cost):
                self.cost = new_cost
                operators_scores[
                    operator_index
                ] += 1  # incrementing the score of the operator
                operator.update_score(1)  # incrementing the score of the operator
            else:
                operator.revert(self.solution)
                operators_scores[operator_index] -= 1
                operator.update_score(-1)  # decrementing the score of the operator

        return self.solution
