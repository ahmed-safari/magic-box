from acceptance import *
from utils import *
import copy

"""
Base class for solvers.
"""


class BaseSelection:
    def __init__(self, llh_list, max_iterations):
        self.llh_list = llh_list
        self.max_iterations = max_iterations
        self.operator = None

    def update_operator_stats(self, did_accept):
        if self.operator:
            self.operator.update_selected()  # Increment the applied count
            if did_accept:
                self.operator.update_accepted()  # Increment the accepted count

    def select_operator(self, new_cost, old_cost, did_accept):
        raise NotImplementedError()
