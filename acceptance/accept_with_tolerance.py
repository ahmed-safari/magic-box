from .base_acceptance import BaseAcceptance


class AcceptWithTolerance(BaseAcceptance):
    def __init__(self, tolerance=0.1, max_stuck_count=10):
        super().__init__(
            max_stuck_count=max_stuck_count
        )  # call the parent constructor (to initialize self.stuck_count)
        self.tolerance = tolerance  # How much worse we allow the new solution to be

    def accept(self, new_cost, old_cost):
        # Escape local optima/minima
        if self.stuck_count >= self.max_stuck_count:  # If we are stuck for too long
            self.stuck_count = 0  # Reset the stuck counter
            return True  # Accept the new solution

        if new_cost <= old_cost * (
            1 + self.tolerance
        ):  # If the new solution is better than the old one (or within the tolerance)
            return True  # Accept the new solution
        else:
            self.stuck_count += 1  # Increment the stuck counter
            return False  # Reject the new solution
