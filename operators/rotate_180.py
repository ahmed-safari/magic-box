from .base_operator import BaseOperator
import random


class Rotate180(BaseOperator):
    def _init_(self):
        super()._init_()  # Call the constructor of the parent class (to initialize self.score)
      
    def apply(self, box):
        n = len(box)
        
        for i in range(n // 2):
            for j in range(n):
                box[i][j], box[n - i - 1][n - j - 1] = box[n - i - 1][n - j - 1], box[i][j]

            # Handle the case when the boxrix has odd dimensions
            
        if n % 2 == 1:
            for j in range(n // 2):
                box[n // 2][j], box[n // 2][n - j - 1] = box[n // 2][n - j - 1], box[n // 2][j]


    def revert(self, box):
        n = len(box)
        for i in range(n//2):
            for j in range(n):
                box[i][j], box[n-1-i][n-1-j] = box[n-1-i][n-1-j], box[i][j]

        if n % 2 == 1:
            for j in range(n // 2):
                box[n // 2][j], box[n // 2][n - j - 1] = box[n // 2][n - j - 1], box[n // 2][j]