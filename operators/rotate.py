from .base_operator import BaseOperator
import random

#Rotations
class Rotate270(BaseOperator):
    def _init_(self):
        super()._init_()  # Call the constructor of the parent class (to initialize self.score)

    def apply(self, box):
        n = len(box)
        
        for i in range(n):
            for j in range(i, n):
                box[i][j], box[j][i] = box[j][i], box[i][j]

        for i in range(n):
            for j in range(n // 2):
                box[j][i], box[n - 1 - j][i] = box[n - 1 - j][i], box[j][i]

        
        
    def revert(self, box):
        n = len(box)

        for i in range(n):
            for j in range(i, n):
                box[i][j], box[j][i] = box[j][i], box[i][j]
        for i in range(n):
            box[i].reverse()