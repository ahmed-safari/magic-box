from .base_acceptance import BaseAcceptance
import random
import math


class AcceptAnnealing(BaseAcceptance):
    def accept(self, new_cost, old_cost, current_iteration):
        acceptance_probability = math.exp(
            ((old_cost - new_cost) / current_iteration) * -1
        )
        if random.random() < acceptance_probability:
            return True
        return False
