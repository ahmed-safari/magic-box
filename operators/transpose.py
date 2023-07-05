from .base_operator import BaseOperator


class Transpose(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)


    def apply(self, box):
        # Switch all the rows and columns of the box
        n = len(box)    # same number of rows and columns
        for i in range(n):
            for j in range(i + 1, n):
                box[i][j], box[j][i] = box[j][i], box[i][j]
   

        # Note: we do not need to return the box, because we are modifying the box in-place

    def revert(self, box):
        n = len(box)
        # Swap back the rows and columns of the box
        for i in range(n):
            for j in range(i + 1, n):
                box[i][j], box[j][i] = box[j][i], box[i][j]

        # Note: we do not need to return the box, because we are modifying the box in-place
