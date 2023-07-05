from utils import *
from acceptance import *
from .base_solver import BaseSolver


class ReinforcementSolver(BaseSolver):
    def solve(self):
        # list of operators
        llh = self.llh_list

        # Create the list with scores of operators initalized to 0

        operators_scores= [0 for _ in range(len(llh))]

    
        # split of iterations
    
        test_operators = int(self.max_iterations * 0.2) # 20%
        rest_iterations = self.max_iterations - test_operators

        # first score the operators
        for i in range(test_operators):

            operator = llh[i % len(llh)]

            # Apply the operator
            operator.apply(self.solution)


            # Calculate the new cost
            cost = calculate_objective(self.solution)
            # Check if the new solution is better than the current best one (and update it if so)      


            if cost == 0:
                operators_scores[i]+=1

            else:
                operators_scores[i]-=1


        # second choose the operator with maximum score
        
        for j in range(rest_iterations):

            max_score = operators_scores.index(max(operators_scores))
            max_op = llh[max_score]
             
            max_op(self.solution) # Call the function with the solution argument
            
            # calc the score
            new_cost = calculate_objective(self.solution)    
            self.check_best(new_cost, self.solution, j)

            # Check if the new solution is accepted
            if self.acceptance.accept(new_cost=new_cost, old_cost=self.cost):
                self.cost = new_cost  # Update the current cost

            # Otherwise, revert the operator
            else:
                operator.revert(self.solution)



