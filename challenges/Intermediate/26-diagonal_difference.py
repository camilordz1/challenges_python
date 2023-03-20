# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9 

# The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. 
# Their absolute difference is |15-17|=2.

def diagonalDifference(arr):
    right = sum(rightDiagonal(arr))
    left = sum(leftDiagonal(arr))
    return abs(right-left)

def rightDiagonal(arr):
    return [row[pos] for pos,row in enumerate(arr)]

def leftDiagonal(arr):
    inv = [arr[row] for row in range(len(arr)-1,-1,-1)]
    return rightDiagonal(inv)


matrix = [[1, 2, 3],
          [5, 6, 7],
          [9, 1, 1]]

print(rightDiagonal(matrix))
print(leftDiagonal(matrix))
print(diagonalDifference(matrix))