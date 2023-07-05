class BaseAcceptance:
    def __init__(self, max_stuck_count=10):
        self.stuck_count = 0
        self.max_stuck_count = max_stuck_count

    def accept(self, new_cost, old_cost):
        raise NotImplementedError()
