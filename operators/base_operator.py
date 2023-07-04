class BaseOperator:
    def __init__(self):
        self.score = 0

    def apply(self, box):
        raise NotImplementedError()

    def update_score(self, change):
        self.score += change

    def revert(self, box):
        raise NotImplementedError()
