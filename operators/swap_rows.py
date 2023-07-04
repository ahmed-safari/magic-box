from .base_operator import BaseOperator
import random


class SwapElements(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)
        self.row1 = 0
        self.row2 = 0

    def apply(self, box):
        # Get the size of the box
        n = len(box)

        # Select two random rows in the box
        self.row1, self.row2 = random.randrange(n), random.randrange(n)

        # Swap the rows
        box[self.row1], box[self.row2] = box[self.row2], box[self.row1]

        # Note: we do not need to return the box, because we are modifying the box in-place

    def revert(self, box):
        # Swap back the rows
        box[self.row1], box[self.row2] = box[self.row2], box[self.row1]

        # Note: we do not need to return the box, because we are modifying the box in-place
