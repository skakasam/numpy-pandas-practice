"""Numpy Array Sorting"""

import numpy as np

# Strudent (Rows) Scores per Subject (Columns)
# 3 Students x 5 Subjects
scores = np.array(
    [
        [87, 69, 91, 72, 68],
        [91, 85, 67, 99, 75],
        [93, 73, 82, 65, 83],
    ]
)


# Non-Inplace Sorting, returns a new np array
print(f"Scores before               : \n{scores}")
print(f"Scores sorted by rows       : \n{np.sort(scores)}")  # Sorted by rows by default, axes = 1
print(f"Scores sorted by cols       : \n{np.sort(scores, axis=0)}")
print(f"Scores after                : \n{scores}")

# Inplace Sorting, returns the existing array after sorting
scores.sort()
print(f"Scores after inplace sort   : \n{scores}")
