from .base_operator import BaseOperator
import random


class SwapColumns(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)
        self.col1 = 0
        self.col2 = 0

    def apply(self, box):
        # Generate two random columns in the box
        self.col1, self.col2 = random.randrange(len(box)), random.randrange(len(box))

        # Swap the columns
        for i in range(len(box)):
            box[i][self.col1], box[i][self.col2] = box[i][self.col2], box[i][self.col1]

        # Note: we do not need to return the box, because we are modifying the box in-place

    def revert(self, box):
        # Swap back the columns
        for i in range(len(box)):
            box[i][self.col1], box[i][self.col2] = box[i][self.col2], box[i][self.col1]

        # Note: we do not need to return the box, because we are modifying the box in-place
