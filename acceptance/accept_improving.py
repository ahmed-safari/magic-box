from .base_acceptance import BaseAcceptance


class AcceptImproving(BaseAcceptance):
    def __init__(self):
        super().__init__()  # call the parent constructor (to initialize self.stuck_count)

    def accept(self, new_cost, old_cost):
        if self.stuck_count >= self.max_stuck_count:
            self.stuck_count = 0
            return True
        if new_cost < old_cost:
            return True
        else:
            self.stuck_count += 1
            return False
