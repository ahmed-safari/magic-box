from .base_acceptance import BaseAcceptance


class AcceptImproving(BaseAcceptance):
    def accept(self, new_cost, old_cost, current_iteration):
        if new_cost <= old_cost:  # If the new solution is better than the old one
            return True  # Accept the new solution
        else:  # If the new solution is worse than the old one
            self.stuck_count += 1  # Increment the stuck counter
            if self.escape_local_optima(new_cost, old_cost):
                return True  # Accept the new solution
            return False  # Reject the new solution
