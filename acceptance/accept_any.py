from .base_acceptance import BaseAcceptance


class AcceptAny(BaseAcceptance):
    def __init__(self):
        super().__init__()  # call the parent constructor (to initialize self.stuck_count)

    def accept(self, new_cost, old_cost):
        return True  # Always accept the new solution
