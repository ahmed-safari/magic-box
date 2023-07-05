from .base_operator import BaseOperator
import random

class ReverseColumn(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)
        self.index = 0

    def reverse_column(self, box):
        n = len(box)
        start = 0
        end = n - 1

        # Till start < end, swap the elements in the specified column
        while start < end:
            # Swap the elements
            temp = box[start][self.index]
            box[start][self.index] = box[end][self.index]
            box[end][self.index] = temp

            # Increment start and decrement end for next pair of swapping
            start += 1
            end -= 1

    def apply(self, box):
        n = len(box)
        self.index = random.randint(0, n - 1)
        self.reverse_column(box)

        # Note: we do not need to return the box because we are modifying it in-place

    def revert(self, box):
        self.reverse_column(box)

        # Note: we do not need to return the box because we are modifying it in-place
