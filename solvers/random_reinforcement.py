from utils import *
from acceptance import *
from .base_solver import BaseSolver

class RandomReinforcementSolver(BaseSolver):
    def solve(self):

         # list of operators
        llh = self.llh_list

        # Create the list with scores of operators initalized to 0
        operators_scores= [0 for _ in range(len(llh))]

        """
            splitting the total iterations 
            20 % for scoring and ranking the operators
            80% for actually applying the best operators   
            Score is tracked in both cases 
        """
         
        test_operators = int(self.max_iterations * 0.2) # 20%
        rest_iterations = self.max_iterations - test_operators

        # first score the operators
        for i in range(test_operators):

            operator = llh[i % len(llh)]    # wrapping to restart the list each time

            # Apply the operator
            operator.apply(self.solution)


            # Calculate the new cost
            cost = calculate_objective(self.solution)
            # Check if the new solution is better than the current best one (and update it if so)      

            # incrementing or decrementing score at the index of the operator
            if cost == 0:
                operators_scores[i]+=1

            else:
                operators_scores[i]-=1
                
            
        """
            Now we have two cases again
            Reinforcement Selection which will be applied 90% of the time (90 iterations out of every 100)
            Random Selection which will be applied for the rest of the 10%
        """
        
        counter_RL = 0      # this for the random
        counter_Random = 0
        
        for j in range(rest_iterations):
            
            if counter_RL == 90:

                operator = random.choice(self.llh_list)

                counter_Random +=1
                
                if counter_Random == 10:
                    counter_RL = 0
                    counter_Random = 0
                
            else:
            
                # retrieving the operators with highest score
                max_score = operators_scores.index(max(operators_scores))
                operator = llh[max_score]
                
                counter_RL +=1

            operator.apply(self.solution)

             # calc the score
            new_cost = calculate_objective(self.solution)    
            self.check_best(new_cost, self.solution, j)

            # Check if the new solution is accepted
            if self.acceptance.accept(new_cost=new_cost, old_cost=self.cost):
                self.cost = new_cost  # Update the current cost

            # Otherwise, revert the operator
            else:
                operator.revert(self.solution)

        return self.solution