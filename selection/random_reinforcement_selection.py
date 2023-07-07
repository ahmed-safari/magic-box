import random
from .base_selection import BaseSelection


class RandomReinforcementSelection(BaseSelection):
    def __init__(
        self,
        llh_list,
        max_iterations,
        training_percentage=0.1,
        random_selection_percentage=0.1,
    ):
        super().__init__(llh_list, max_iterations)
        self.training_percentage = training_percentage
        self.random_selection_percentage = random_selection_percentage
        self.llh_scores = [0.0] * len(self.llh_list)  # List of scores for each LLH

    def select_operator(self, new_cost, old_cost, did_accept, current_iteration):
        # If we are in the training phase, select an operator in a round robin fashion
        if current_iteration < self.max_iterations * self.training_percentage:
            operator_index = current_iteration % len(self.llh_scores)

        else:  # Else, select the LLH with the highest score
            # generate number between where the training phase ends and and number of iterations
            random_number = random.randint(
                self.max_iterations * self.training_percentage,
                self.max_iterations,
            )
            # print(random_number)
            # if the random number is less than the random selection percentage, select a random operator
            if random_number < self.max_iterations * self.random_selection_percentage:
                # print("Random selection")
                operator_index = random.randint(0, len(self.llh_scores) - 1)

            else:
                # print("Highest score selection")
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
