from operators import (
    SwapElements,
    SwapRows,
    SwapColumns,
    Transpose,
    ShuffleRow,
    ShuffleColumn,
    SwapDiagonals,
    SwapOddEven,
    ReverseRow,
    ReverseColumn
)
from utils import create_initial


# Create a box
box = create_initial(3)

# Operators
operators = [
    SwapElements(),
    SwapRows(),
    SwapColumns(),
    Transpose(),
    ShuffleRow(),
    ShuffleColumn(),
    SwapDiagonals(), 
    SwapOddEven(),
    ReverseRow(),
    ReverseColumn()
]


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
