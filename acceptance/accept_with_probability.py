import random
from .base_acceptance import BaseAcceptance


class AcceptWithProbability(BaseAcceptance):
    def __init__(self, acceptance_probability=0.5):
        super().__init__()
        self.acceptance_probability = acceptance_probability

    def accept(self, new_cost, old_cost):
        if random.random() < self.acceptance_probability:
            return True
        else:
            return False
