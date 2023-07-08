from .base_acceptance import BaseAcceptance


class AcceptAny(BaseAcceptance):
    def accept(self, new_cost, old_cost, current_iteration):
        return True  # Always accept the new solution
