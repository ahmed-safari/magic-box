"""
Base class for acceptance criteria.
"""


class BaseAcceptance:
    def __init__(
        self,
        max_stuck_count=10,
        stuck_tolerance=0.3,
    ):
        self.stuck_count = 0  # How many iterations we are stuck
        self.max_stuck_count = (
            max_stuck_count  # How many iterations we allow ourselves to be stuck
        )
        self.stuck_tolerance = stuck_tolerance  # How much tolerance we allow

    def accept(self, new_cost, old_cost):
        raise NotImplementedError()

    def escape_local_optima(self, new_cost, old_cost):
        #    Check if stuck for too long and accept if within tolerance

        if self.stuck_count >= self.max_stuck_count:
            # print("Stuck for too long")
            # print("New cost: ", new_cost)
            # print("Old cost: ", old_cost)
            # print("Stuck count: ", self.stuck_count)
            if new_cost <= old_cost * 1 + self.stuck_tolerance:
                # print("Escaped local optima")
                self.stuck_count = 0
                return True
            # else:
            # print("Did not escape local optima")
        return False
