from .base_operator import BaseOperator


class SwapLargest(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def apply(self, box):
        # Find the indices of the two largest elements in the 2D box
        n = len(box)
        largest_val1 = largest_val2 = float("-inf")
        for i in range(n):
            for j in range(n):
                if box[i][j] > largest_val1:
                    largest_val2 = largest_val1
                    self.x2, self.y2 = self.x1, self.y1
                    largest_val1 = box[i][j]
                    self.x1, self.y1 = i, j
                elif box[i][j] > largest_val2:
                    largest_val2 = box[i][j]
                    self.x2, self.y2 = i, j

        # Swap the two largest elements
        box[self.x1][self.y1], box[self.x2][self.y2] = (
            box[self.x2][self.y2],
            box[self.x1][self.y1],
        )

    def revert(self, box):
        # Swap back the elements with the same indexes
        box[self.x1][self.y1], box[self.x2][self.y2] = (
            box[self.x2][self.y2],
            box[self.x1][self.y1],
        )
