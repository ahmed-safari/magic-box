from operators import LLH_CLASSES
from utils import create_initial


# Create a box
box = create_initial(3)

# Operators
operators = LLH_CLASSES


# Test the operators

for operator in operators:
    print(
        "Operator:", operator.__class__.__name__
    )  # Print the name of the class of the operator
    print("Initial:", box)  # Print the initial box
    operator.apply(box)  # Apply the operator
    print("After apply:", box)  # Print the box after applying the operator
    operator.revert(box)  # Revert the operator
    print("After revert:", box)  # Print the box after reverting the operator
    print()  # Print an empty line
