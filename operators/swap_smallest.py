from .base_operator import BaseOperator


class SwapSmallest(BaseOperator):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (to initialize self.score)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def apply(self, box):
        # Get the size of the box
        n = len(box)
        smallest1, smallest2 = 1, 2  # The smallest and second largest numbers

        # Find the locations of the two smallest numbers
        for i in range(n):
            for j in range(n):
                if box[i][j] == smallest1:
                    self.x1, self.y1 = i, j
                elif box[i][j] == smallest2:
                    self.x2, self.y2 = i, j

        # Swap the two smallest numbers
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
