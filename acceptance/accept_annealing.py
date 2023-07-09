from .base_acceptance import BaseAcceptance
import random
import numpy as np


class AcceptAnnealing(BaseAcceptance):
    def accept(self, new_cost, old_cost, current_iteration):
        if new_cost < old_cost:  # If the new solution is better than the old one
            return True  # Accept the new solution

        acceptance_probability = np.exp(((old_cost - new_cost) / current_iteration))
        if random.random() < acceptance_probability:
            return True

        return False
