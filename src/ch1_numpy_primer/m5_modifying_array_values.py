"""Modifying Array Values"""

import numpy as np


def print_separator():
    print("=-" * 40)


subjects = np.array(["English", "History", "Music", "Math", "Social", "Biology", "Science", "Art"])
scores = np.array([85, 65, 78, 92, 88, 76, 95, 89])
grades = np.array([""] * len(scores), dtype="<U1")  # Create an empty array for grades

print(f"Subjects           : {subjects}")

print_separator()
print(f"Original scores    : {scores}")
scores[-1] = 68  # Modify the last score
print(f"Modified scores    : {scores}")

print_separator()
is_grade_a = scores >= 80
grades[is_grade_a] = "A"
is_grade_b = (scores >= 70) & (scores < 80)
grades[is_grade_b] = "B"
is_grade_c = scores < 70
grades[is_grade_c] = "C"
print(f"Grades             : {grades}")


print_separator()
condition = (scores >= 70) & (scores < 80)
print(f"scores b/w 70 & 80 : {scores[condition]}")  # ~ NOT, | OR, & AND
