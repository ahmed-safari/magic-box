import random
from .base_acceptance import BaseAcceptance


class AcceptWithProbability(BaseAcceptance):
    def __init__(
        self, max_stuck_count=10, stuck_tolerance=0.1, acceptance_probability=0.5
    ):
        super().__init__(
            max_stuck_count=max_stuck_count, stuck_tolerance=stuck_tolerance
        )
        self.acceptance_probability = acceptance_probability

    def accept(self, new_cost, old_cost):
        if random.random() < self.acceptance_probability:
            return True
        else:
            return False
