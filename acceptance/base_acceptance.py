"""
Base class for acceptance criteria.
"""


class BaseAcceptance:
    def __init__(self, max_stuck_count=10):
        self.stuck_count = 0  # How many iterations we are stuck
        self.max_stuck_count = (
            max_stuck_count  # How many iterations we allow ourselves to be stuck
        )

    def accept(self, new_cost, old_cost):
        raise NotImplementedError()
