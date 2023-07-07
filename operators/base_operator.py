class BaseOperator:
    def __init__(self):
        self.score = 0
        self.selected_count = 0
        self.accepted_count = 0

    def apply(self, box):
        raise NotImplementedError()

    def update_selected(self):
        self.selected_count += 1

    def update_accepted(self):
        self.accepted_count += 1

    def update_score(self, change):
        self.score += change

    def revert(self, box):
        raise NotImplementedError()
