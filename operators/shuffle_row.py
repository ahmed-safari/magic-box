import random
from .base_operator import BaseOperator


class ShuffleRow(BaseOperator):
    def __init__(self):
        super().__init__()
        self.row_index = None
        self.row_original_state = None

    def apply(self, box):
        self.row_index = random.randrange(len(box))  # select a random row
        self.row_original_state = list(
            box[self.row_index]
        )  # create a copy of the original row
        box = random.shuffle(box[self.row_index])  # shuffle the row in-place
        return box

    def revert(self, box):
        if self.row_index is not None and self.row_original_state is not None:
            box[self.row_index] = self.row_original_state  # restore the original row
        return box
