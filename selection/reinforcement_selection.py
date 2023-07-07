from utils import *
from acceptance import *
from .base_selection import BaseSelection


class ReinforcementSelection(BaseSelection):
    def __init__(self, llh_list, max_iterations, training_percentage=0.1):
        super().__init__(llh_list, max_iterations)
        self.training_percentage = training_percentage
        self.llh_scores = [0.0] * len(self.llh_list)  # List of scores for each LLH

    def select_operator(self, new_cost, old_cost, did_accept, current_iteration):
        # If we are in the training phase, select an operator in a round robin fashion
        if current_iteration < self.max_iterations * self.training_percentage:
            operator_index = current_iteration % len(self.llh_scores)
        # Else, select the LLH with the highest score
        else:
            operator_index = self.llh_scores.index(max(self.llh_scores))

        self.operator = self.llh_list[operator_index]

        # Update the score of the operator
        if did_accept:
            self.llh_scores[operator_index] += 1
            self.operator.update_score(1)
        else:
            self.llh_scores[operator_index] -= 1
            self.operator.update_score(-1)

        return self.operator

    def update_operator_score(self, new_cost, old_cost, did_accept):
        if did_accept:
            self.llh_scores[self.llh_list.index(self.operator)] += 1
            self.operator.update_score(1)
        else:
            self.llh_scores[self.llh_list.index(self.operator)] -= 1
            self.operator.update_score(-1)
