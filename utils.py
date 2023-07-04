import random 


def create_initial(n):
    nums = list(range(1, n*n + 1)) # Create a list of numbers from 1 to n^2
    random.shuffle(nums) # Shuffle the list

    box = []  # Initialize the 2D list
    for i in range(n): # For each row
        row = []  # Initialize an empty row
        for _ in range(n):
            row.append(nums.pop())  # Append the last number to the row, and remove it from the list
        box.append(row)  # Append the row to the box
        
    return box

def calculate_objective(box):

    # n is the length of the box (number of rows, or number of columns, as it's a square matrix).
    n = len(box)

    # The target_sum for each row, column, or diagonal in a magic square of order n 
    # is calculated as n*(n*n + 1) // 2.
    target_sum = n*(n*n + 1) // 2

    # Initialize lists of size n with all values as 0. These will hold the sum of elements in each row and column.
    row_sums = [0]*n
    col_sums = [0]*n

    # Initialize the sums of the two diagonals as 0.
    diag1_sum = diag2_sum = 0

    # This loop iterates over each row (and column, as it's a square matrix) of the box.
    for i in range(n):

        # This inner loop calculates the sum of elements in each row, each column and both diagonals.
        for j in range(n):
            # Add the j-th element of the i-th row to the sum of the i-th row.
            row_sums[i] += box[i][j]

            # Add the i-th element of the j-th column to the sum of the j-th column.
            col_sums[j] += box[i][j]
            
            # If we are on the main diagonal (where the row index equals the column index), 
            # add the current element to the main diagonal sum.
            if i == j:
                diag1_sum += box[i][j]

            # If we are on the second diagonal (where the row index and column index sum to n-1), 
            # add the current element to the second diagonal sum.
            if i == n - j - 1:
                diag2_sum += box[i][j]

    # Calculate the total difference between the target sum and the sum of each row.
    total = sum(abs(target_sum - row_sum) for row_sum in row_sums)

    # Add the difference between the target sum and the sum of each column to the total.
    total += sum(abs(target_sum - col_sum) for col_sum in col_sums)

    # Add the difference between the target sum and the sum of the main diagonal to the total.
    total += abs(target_sum - diag1_sum)

    # Add the difference between the target sum and the sum of the second diagonal to the total.
    total += abs(target_sum - diag2_sum)

    # Return the total difference. This total represents how far off the box is from being a magic square.
    return total
