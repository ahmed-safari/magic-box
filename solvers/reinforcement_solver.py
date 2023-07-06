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
            score_index = i % len(operators_scores)


            # Apply the operator
            operator.apply(self.solution)


            # Calculate the new cost
            cost = calculate_objective(self.solution)
            # Check if the new solution is better than the current best one (and update it if so)      

            if cost == 0:
                return self.solution # not sure if we should consider returning in the tracking phase
            
            if cost <10: # baseline cost as cost = 0 means found the solution

                operators_scores[score_index]+=1

            else:
                operators_scores[score_index]-=1


        # second choose the operator with maximum score
        
        for j in range(rest_iterations):

            max_score_index = operators_scores.index(max(operators_scores))
            max_op = llh[max_score_index]
             
            max_op.apply(self.solution) # Call the function with the solution argument
            
            # calc the score
            new_cost = calculate_objective(self.solution) 

            if new_cost == 0:
                return self.solution
            
            elif new_cost < 10:
                operators_scores[max_score_index]+=1
            else:
                operators_scores[max_score_index]-=1


            self.check_best(new_cost, self.solution, j)

            # Check if the new solution is accepted
            if self.acceptance.accept(new_cost=new_cost, old_cost=self.cost):
                self.cost = new_cost  # Update the current cost

            # Otherwise, revert the operator
            else:
                operator.revert(self.solution)

        return self.solution



