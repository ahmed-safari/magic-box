from .base_selection import BaseSelection
import random


class RandomSelection(BaseSelection):
    def select_operator(self, new_cost, old_cost, did_accept):
        return random.choice(self.llh_list)
