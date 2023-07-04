class RandomSelectionSolver:

    def __init__(self, solution, llh_list, max_iterations):
        self.llh_list = llh_list
        self.max_iterations = max_iterations
        self.solution = solution
        self.best_solution = solution

    def solve(self):
        print("solve")



