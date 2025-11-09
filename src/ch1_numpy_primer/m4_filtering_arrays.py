"""Filtering NumPy Arrays"""

import numpy as np


def print_separator():
    print("=-" * 40)


subjects = np.array(["Math", "English", "Biology", "History", "Art", "PE", "Music", "Economics"])
scores = np.array([85, 65, 78, 92, 88, 76, 95, 69])
a_grade = scores >= 80
b_grade = (scores >= 70) & (scores < 80)
c_grade = scores < 70

print(f"scores             : {scores}")
print(f"subjects           : {subjects}")

print_separator()
print(f"boolean a_grade    : {a_grade}")
print(f"scores >= 80       : {scores[a_grade]}")
print(f"subjects           : {subjects[a_grade]}")

print_separator()
print(f"boolean b_grade    : {b_grade}")
print(f"scores >= 70 & < 80: {scores[b_grade]}")
print(f"subjects           : {subjects[b_grade]}")

print_separator()
print(f"boolean c_grade    : {c_grade}")
print(f"scores < 70        : {scores[c_grade]}")
print(f"subjects           : {subjects[c_grade]}")

grades = np.where(
    scores >= 80,
    "A",
    np.where(
        (scores >= 70) & (scores < 80),
        "B",
        "C",
    ),
)
print_separator()
print(f"scores             : {scores}")
print(f"grades             : {grades}")
