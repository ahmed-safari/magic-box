from .base_operator import BaseOperator
import random
class SwapElements(BaseOperator):
    def __init__(self):
        super(  ).__init__() # Call the constructor of the parent class (to initialize self.score)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0 
        self.y2 = 0 

    def apply(self, box):
        # Get the size of the box
        n = len(box)
        # Generate two random positions in the box
        self.x1 = random.randint(0,n - 1)
        self.y1 = random.randint(0,n - 1)
        self.x2 = random.randint(0,n - 1)
        self.y2 = random.randint(0,n - 1)

        # Swap the elements
        box[self.x1][self.y1], box[self.x2][self.y2] = box[self.x2][self.y2], box[self.x1][self.y1]
        # Note: we do not need to return the box, because we are modifying the box in-place


    def revert(self, box):
        # Swap back the elements with the same indexes (we did not generate new indexes, so we can just swap back)
        box[self.x1][self.y1], box[self.x2][self.y2] = box[self.x2][self.y2], box[self.x1][self.y1] 
        # Note: we do not need to return the box, because we are modifying the box in-place
        
