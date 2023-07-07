from hyper_heuritics import HyperHeuristic

MAX_ITERATIONS = 20

# Create a solver
solver = HyperHeuristic(
    max_iterations=MAX_ITERATIONS,
    n=4,
    acceptance_method="accept_improving",
    selection_method="random_reinforcement_selection",
    random_reinforcement_selection_percentage=0.5,
)

# Solve the box
solver.solve()

# Print the solution
# print("Best Solution:", solver.best_solution)
print("Best Cost:", solver.best_cost)
print("Found at iteration:", solver.found_at)

# print("Final accepted cost:", solver.cost)
print("Final accepted solution:", solver.solution)

#  self.selected_count = 0
# self.accepted_count = 0
# Print scores of the operators
print("Operators Stats:")
selections_total = 0
for operator in solver.llh_list:
    print(
        f"{operator.__class__.__name__}: Selected: {operator.selected_count}, Accepted: {operator.accepted_count}, Score: {operator.score}"
    )
    selections_total += operator.selected_count

print("Total selections:", selections_total)
