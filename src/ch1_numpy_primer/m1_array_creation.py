"""Introduction to Numpy Arrays"""

import numpy as np


def print_separator():
    print("=-" * 40)


################################################################################
# Notes:
################################################################################
# 1. NumPy arrays require all elements to be of the same data type
# 2. NumPy arrays are more memory efficient and faster for numerical
#    computations compared to Python lists
# 3. NumPy arrays support vectorized operations, allowing for
#    element-wise operations without explicit loops
# 4. NumPy provides a wide range of functions for array manipulation,
#    mathematical operations, and statistical analysis
# 5. NumPy arrays can be multi-dimensional, making them suitable for
#    representing matrices and higher-dimensional data structures
# 6. NumPy integrates well with other scientific computing libraries
#    in Python, such as SciPy, Pandas, and Matplotlib
# 7. NumPy is widely used in data science, machine learning, and
#    scientific computing due to its efficiency and ease of use
################################################################################

# NumPy 1D Array - Daily avg temperatures for a week
# Can use this for simple lists/arrays of data
WKL_TEMPS_NP_1D_ARRAY = np.array(
    [22.1, 21.9, 23.0, 24.5, 25.2, 26.1, 27.3],
)
print(f"{WKL_TEMPS_NP_1D_ARRAY = }")
print(f"{type(WKL_TEMPS_NP_1D_ARRAY) = }")
print(f"Dimensions: {WKL_TEMPS_NP_1D_ARRAY.ndim}")
print(f"Shape: {WKL_TEMPS_NP_1D_ARRAY.shape}")
print(f"Size: {WKL_TEMPS_NP_1D_ARRAY.size}")
print(f"Data type: {WKL_TEMPS_NP_1D_ARRAY.dtype}")

print_separator()

# NumPy 2D Array - Daily avg temperatures per week for a month
# Can use this to represent tabular data/files
MTH_TEMPS_NP_2D_ARRAY = np.array(
    [
        [22.1, 21.9, 23.0, 24.5, 25.2, 26.1, 27.3],
        [22.3, 22.0, 23.5, 24.7, 25.5, 26.3, 27.8],
        [22.5, 22.2, 23.8, 25.0, 25.8, 26.5, 28.0],
        [22.7, 22.4, 24.0, 25.3, 26.0, 26.8, 28.3],
        [22.9, 22.6, 24.3, 25.5, 26.3, 27.0, 28.5],
    ]
)
print(f"{MTH_TEMPS_NP_2D_ARRAY = }")
print(f"{type(MTH_TEMPS_NP_2D_ARRAY) = }")
print(f"Dimensions: {MTH_TEMPS_NP_2D_ARRAY.ndim}")
print(f"Shape: {MTH_TEMPS_NP_2D_ARRAY.shape}")
print(f"Size: {MTH_TEMPS_NP_2D_ARRAY.size}")
print(f"Data type: {MTH_TEMPS_NP_2D_ARRAY.dtype}")

print_separator()

# NumPy 3D Array - Weekly avg temperatures per month per quarter
# Can use this to represent file generations
QTR_TEMPS_NP_3D_ARRAY = np.array(
    [
        [
            [22.1, 21.9, 23.0, 24.5, 25.2],
            [22.3, 22.0, 23.5, 24.7, 25.5],
            [22.5, 22.2, 23.8, 25.0, 25.8],
        ],
        [
            [23.1, 22.9, 24.0, 25.5, 26.2],
            [23.3, 23.0, 24.5, 25.7, 26.5],
            [23.5, 23.2, 24.8, 26.0, 26.8],
        ],
        [
            [24.1, 23.9, 25.0, 26.5, 27.2],
            [24.3, 24.0, 25.5, 26.7, 27.5],
            [24.5, 24.2, 25.8, 27.0, 27.8],
        ],
        [
            [24.7, 24.4, 26.0, 27.3, 28.0],
            [24.9, 24.6, 26.3, 27.5, 28.3],
            [25.1, 24.8, 26.5, 27.8, 28.5],
        ],
    ]
)
print(f"{QTR_TEMPS_NP_3D_ARRAY = }")
print(f"{type(QTR_TEMPS_NP_3D_ARRAY) = }")
print(f"Dimensions: {QTR_TEMPS_NP_3D_ARRAY.ndim}")
print(f"Shape: {QTR_TEMPS_NP_3D_ARRAY.shape}")
print(f"Size: {QTR_TEMPS_NP_3D_ARRAY.size}")
print(f"Data type: {QTR_TEMPS_NP_3D_ARRAY.dtype}")

print_separator()

# Other ways to create NumPy arrays
print(f"{np.zeros((3, 4)) = }")  # 3x4 array of zeros
print(f"{np.ones((2, 5), dtype=int) = }")  # 2x5 array of ones
print(f"{np.full((3, 3), 7) = }")  # 3x3 array filled with 7s
print(f"{np.eye(4, dtype=int) = }")  # 4x4 identity matrix
print(f"{np.arange(0, 11, 2) = }")  # Array of even numbers from 0 to 10
print(f"{np.arange(0, 11, 2).reshape(3, 2) = }")  # 3x2 array of even numbers from 0 to 10
print(f"{np.arange(0, 11, 2).reshape(3, 2).T = }")  # Transpose of the 3x2 array
print(f"{np.linspace(0, 1, 5) = }")  # 5 values evenly spaced between 0 and 1
print(
    f"{np.linspace(start=10, stop=100, num=10, dtype=int).reshape(5,2) = }"
)  # 10 values evenly spaced between 10 and 100, reshaped to 5x2
print(
    f"{np.arange(start=10, stop=101, step=10).reshape(5,2) = }"
)  # 10 to 100 step 10, reshaped to 5x2
print(
    f"{(np.arange(start=1, stop=11) * 10).reshape(5,2) = }"
)  # 10 to 100 step 10, reshaped to 5x2


# Random array generation (for simulations, testing, etc.)
rng = np.random.default_rng(seed=42)  # Random number generator with a seed for reproducibility
print(f"{rng.random(10) = }")  # 1D array of 10 random floats in [0.0, 1.0)
print(f"{rng.integers(0, 100, size=(3, 4)) = }")  # 3x4 array of random integers in [0, 100)
print(
    f"{rng.normal(loc=0.0, scale=1.0, size=(2, 3)) = }"
)  # 2x3 array of random floats from a normal distribution
print(f"{rng.normal(50, 5, 10) = }")  # 1D array of 10 random floats from N(50, 5^2)
print(
    f"{rng.choice(['red', 'blue', 'green'], size=5) = }"
)  # 1D array of 5 random choices from the list
