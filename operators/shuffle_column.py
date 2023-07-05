import random
from typing import List
from .base_operator import BaseOperator


class ShuffleColumn(BaseOperator):
    def __init__(self):
        super().__init__()
        self.col_idx = None
        self.original_order = None

    def apply(self, box):
        # Choose a random column index
        self.col_idx = random.randint(0, len(box) - 1)

        # Save the original order of the elements in the chosen column
        self.original_order = [row[self.col_idx] for row in box]

        # Create a shuffled version of the column
        shuffled_column = self.original_order[:]
        random.shuffle(shuffled_column)

        # Replace the chosen column with the shuffled version
        for i, row in enumerate(box):
            row[self.col_idx] = shuffled_column[i]

    def revert(self, box: List[List[int]]):
        # Replace the shuffled column with the original column
        for i, row in enumerate(box):
            row[self.col_idx] = self.original_order[i]
