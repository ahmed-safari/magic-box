from .base_operator import BaseOperator
import random

class ReverseRow(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)
        self.index = 0


    def apply(self, box):   # randomly selects a row based on index and reverses it
        n = len(box)
        self.index = random.randint(0,n - 1)
        box[self.index] = box[self.index][::-1]
   

        # Note: we do not need to return the box, because we are modifying the box in-place

    def revert(self, box):
        box[self.index] = box[self.index][::-1]

        # Note: we do not need to return the box, because we are modifying the box in-place
