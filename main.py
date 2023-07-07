from hyper_heuritics import HyperHeuristic


# # Create a solver
# hyper_heuristic = HyperHeuristic(
#     max_iterations=10000,
#     n=4,
#     acceptance_method="accept_improving",
#     selection_method="random_reinforcement",
#     random_reinforcement_selection_percentage=0.5,
# )

hyper_heuristic = HyperHeuristic.setup("config.json")

# Solve the box
hyper_heuristic.solve()

# Print the solution
# print("Best Solution:", solver.best_solution)
print("Best Cost:", hyper_heuristic.best_cost)
print("Found at iteration:", hyper_heuristic.found_at)

# print("Final accepted cost:", solver.cost)
print("Final accepted solution:", hyper_heuristic.solution)

#  self.selected_count = 0
# self.accepted_count = 0
# Print scores of the operators
print("Operators Stats:")
selections_total = 0
for operator in hyper_heuristic.llh_list:
    print(
        f"{operator.__class__.__name__}: Selected: {operator.selected_count}, Accepted: {operator.accepted_count}, Score: {operator.score}"
    )
    selections_total += operator.selected_count

print("Total selections:", selections_total)
