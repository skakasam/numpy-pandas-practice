"""Python Array Vectorization and Broadcasting"""

import numpy as np


def print_delimiter():
    print("\n====================================================================\n")


################################################################################
# Vectorization:
# This is the process of pushing array operations into optmized C code,
# which is easier and more efficient than writing for loops
#
# Broadcating:
# This lets us perform vectorized operations with arrays of different
# sizes, where NumPy will expand the smaller array to 'fit' the larger
# one. As long as there is one matching dimension, NumPy will figure
# out a way to operate on them.
################################################################################

# Scores of 3 students (rows) per 5 subject (columns)
scores = np.array(
    [
        [87, 69, 91, 72, 68],
        [91, 85, 67, 99, 75],
        [93, 73, 82, 65, 83],
    ]
)
print(f"scores.size                        : {scores.size}")
print(f"scores.shape                       : {scores.shape}")

print_delimiter()
print(f"scores                             : \n{scores}")

# Add 1 to all scores. Numpy broadcasts 1 to 3x5 matrix of 1's
# and performs the matrix addition, which is optimized and much
# faster than looping.
print_delimiter()
print(f"scores + 1                         : \n{scores + 1}")

# Add 5 to scores of subjects 1, 3, and 5, i.e., [5, 0, 5, 0, 5]
# In this case NumPy broadcasts the [5, 0, 5, 0, 5] row for all
# rows to generate the 3x5 matrix and performs the matrix addition
print_delimiter()
print(f"scores + np.array([5, 0, 5, 0, 5]) : \n{scores + np.array([5, 0, 5, 0, 5])}")

# Add 5 to Student 1's scores, 0 to other Student scores. In this
# case NumPy broadcats the [[5], [0], [0]] column for all columns
# to generate the 3x5 matrix and performs the matrix addition
print_delimiter()
print(f"scores + np.array([[5], [0], [0]]) : \n{scores + np.array([[5], [0], [0]])}")

# If the 2nd argument is neither of shape (1,) scalar, (3,) row,
# nor (3,1) col, then Numpy rejects the action with a value error
# "operands could not be broadcast together with shapes (3,5) (2,)"
print_delimiter()
print(f"scores + np.array([2, 3])          : \n{scores + np.array([2, 3])}")
