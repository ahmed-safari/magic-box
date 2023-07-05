from .base_acceptance import BaseAcceptance


class AcceptImproving(BaseAcceptance):
    def __init__(self):
        super().__init__()  # call the parent constructor (to initialize self.stuck_count)

    def accept(self, new_cost, old_cost):
        # Escape local optima/minima
        if self.stuck_count >= self.max_stuck_count:  # If we are stuck for too long
            self.stuck_count = 0  # Reset the stuck counter
            return True  # Accept the new solution

        if new_cost < old_cost:  # If the new solution is better than the old one
            return True  # Accept the new solution
        else:  # If the new solution is worse than the old one
            self.stuck_count += 1  # Increment the stuck counter
            return False  # Reject the new solution
