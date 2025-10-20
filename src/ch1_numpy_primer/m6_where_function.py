"""NumPy Where Function"""

import numpy as np


def print_separator():
    print("=-" * 40)


subjects = np.array(["Math", "English", "Biology", "History", "Art", "PE", "Music", "Economics"])
scores = np.array([85, 65, 78, 92, 88, 76, 95, 69])
is_gte_80, is_bw_70_and_80, is_lt_70 = scores >= 80, (scores >= 70) & (scores < 80), scores < 70
grades = np.where(is_gte_80, "A", np.where(is_bw_70_and_80, "B", "C"))

print(f"Subjects           : {subjects}")
print(f"Scores             : {scores}")
print(f"Grades             : {grades}")
