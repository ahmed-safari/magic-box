from .base_acceptance import BaseAcceptance


class AcceptWithTolerance(BaseAcceptance):
    def __init__(
        self,
        tolerance=0.1,
        max_stuck_count=10,
        stuck_tolerance=0.1,
        stuck_tolerance_increment=0,
    ):
        super().__init__(
            max_stuck_count=max_stuck_count,
            stuck_tolerance=stuck_tolerance,
            stuck_tolerance_increment=stuck_tolerance_increment,
        )  # call the parent constructor (to initialize self.stuck_count)
        self.tolerance = tolerance  # How much worse we allow the new solution to be

    def accept(self, new_cost, old_cost, current_iteration):
        # Escape local optima/minima (if we are stuck for too long, accept if within tolerance)
        if self.escape_local_optima(new_cost, old_cost):
            return True  # Accept the new solution

        if new_cost <= old_cost * (
            1 + self.tolerance
        ):  # If the new solution is better than the old one (or within the tolerance)
            return True  # Accept the new solution
        else:
            self.stuck_count += 1  # Increment the stuck counter
            return False  # Reject the new solution
