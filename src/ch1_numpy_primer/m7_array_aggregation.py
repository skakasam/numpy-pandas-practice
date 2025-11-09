"""NumPy Array Aggregation"""

from numpy.random import default_rng


def print_separator():
    print("=-" * 40)


rng = default_rng(12345)
scores = rng.integers(60, 100, size=(3, 5))  # 3 Students x 5 Subjects Array

# Scores Array
print(f"Scores array             : \n{scores}")
print(f"Scores shape             : {scores.shape}")
print(f"Scores ndim              : {scores.ndim}")
print(f"Scores size              : {scores.size}")
print(f"Scores dtype             : {scores.dtype}")

print_separator()

# Aggregation functions: sum, mean, std, var, min, max
print(f"Mean score of the class  : {scores.mean().round(2)}")
print(f"Min score per subject    : {scores.min(axis=0).round(2)}")  # Axis 0 = Rows
print(f"Max score per student    : {scores.max(axis=1).round(2)}")  # Axis 1 = Cols

print_separator()

# Other aggregation functions: argmin, argmax, cumsum, cumprod
print(f"Index of max score       : {scores.argmax()}")
print(f"Index of min score       : {scores.argmin()}")
