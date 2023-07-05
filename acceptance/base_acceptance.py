class BaseAcceptance:
    def __init__(self):
        self.stuck_count = 0

    def accept(self, new_cost, old_cost):
        raise NotImplementedError()
