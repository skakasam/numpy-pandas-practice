"""Numpy Array Functions"""

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

print(f"Median Score                  : {np.median(scores).round(2)}")
print(f"Mean Score                    : {np.mean(scores).round(2)}")
print(f"Min Score                     : {np.min(scores)}")
print(f"Min Score per row (Subject)   : {np.min(scores, axis=0)}")
print(f"Max Score                     : {np.max(scores)}")
print(f"Max Score per col (Student)   : {np.max(scores, axis=1)}")
print(f"Unique Scores                 : {np.unique(scores)}")

print("\n====================================================================\n")

print(f"75th Percentile Score         : {np.percentile(scores, 75)}")
print(f"Scores                        : \n{scores}")
print(f"Scores>=75th Percentile       : \n{scores >= np.percentile(scores, 75)}")
