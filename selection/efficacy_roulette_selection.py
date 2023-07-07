from .base_selection import BaseSelection
from utils import calculate_objective
import random


class EfficacyRouletteSelection(BaseSelection):
    def __init__(self, llh_list, max_iterations):
        super().__init__(llh_list, max_iterations)
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

    def select_operator(self, new_cost, old_cost, did_accept, current_iteration):
        #  Select a random LLH from the list of LLHs with a probability proportional to its score
        self.operator = self.roulette_wheel_select()

        return self.operator

    def update_operator_score(self, new_cost, old_cost, did_accept):
        self.llh_scores[self.llh_list.index(self.operator)] += old_cost - new_cost
        self.operator.update_score(old_cost - new_cost)
