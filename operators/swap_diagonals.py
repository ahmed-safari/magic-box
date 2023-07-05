from .base_operator import BaseOperator

class SwapDiagonals(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)

    def apply(self, box):
        # Get the size of the box
        n = len(box)
        for i in range(n):
            box[i][i], box[i][n-i-1] = box[i][n-i-1], box[i][i]

        # Note: we do not need to return the box, because we are modifying the box in-place

    def revert(self, box):
        n = len(box)
        # Swap back the columns
        for i in range(len(box)):
            box[i][i], box[i][n-i-1] = box[i][n-i-1], box[i][i]

        # Note: we do not need to return the box, because we are modifying the box in-place
