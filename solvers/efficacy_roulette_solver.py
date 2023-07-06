from .base_solver import BaseSolver
from utils import calculate_objective
import random


class EfficacyRouletteSolver(BaseSolver):
    def __init__(
        self,
        solution,
        llh_list,
        max_iterations,
        acceptance_criterion="accept_any",
    ):
        super().__init__(solution, llh_list, max_iterations, acceptance_criterion)
        self.llh_scores = [0.0] * len(self.llh_list)  # List of scores for each LLH

    # This function is used to select a random LLH from the list of LLHs with a probability proportional to its score
    def roulette_wheel_select(self):
        normalized_scores = [
            max(0, score) for score in self.llh_scores
        ]  # Remove negative scores
        total_score = sum(normalized_scores)  # Calculate the total score

        if total_score == 0:  # If all scores are 0, return a random LLH
            return random.choice(self.llh_list)

        pick = random.uniform(
            0, total_score
        )  # Pick a random number between 0 and the total score
        current = 0  # Current score

        # Iterate over the LLHs and return the first one whose score is greater than the random number
        for llh, score in zip(self.llh_list, normalized_scores):
            current += score  # Add the current score
            if current > pick:  # If the current score is greater than the random number
                return llh  # Return the current LLH

    def solve(self):
        for i in range(
            self.max_iterations
        ):  # Iterate until the maximum number of iterations is reached
            if self.cost == 0:  # If the cost is 0, the solution is optimal
                break  # Stop iterating

            operator = self.roulette_wheel_select()  # Select a random LLH

            # Apply the operator
            operator.apply(self.solution)

            # Calculate the new cost
            new_cost = calculate_objective(self.solution)

            # Check if the new solution is better than the current best one (and update it if so)
            self.check_best(new_cost, self.solution, i)

            # Update the score of the LLH
            self.llh_scores[self.llh_list.index(operator)] += self.cost - new_cost
            operator.update_score(self.cost - new_cost)

            # Check if the new solution is accepted
            if self.acceptance.accept(new_cost, self.cost):
                self.cost = new_cost  # Update the current cost
            else:
                operator.revert(self.solution)  # Otherwise, revert the operator

        return self.best_solution
