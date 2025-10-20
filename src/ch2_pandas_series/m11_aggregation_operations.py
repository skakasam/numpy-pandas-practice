"""Aggregation Operations on Python Pandas Series"""

import pandas as pd
import common_utils as utils
import common_const as const

scores = pd.Series(
    data=const.STUDENT_SCORES,
    index=const.STUDENT_NAMES,
    name="Student Scores",
)

print(f"{utils.ye_colored('STUDENT SCORES SERIES:')}")
print(scores)

# ##############################################################################
# Numerical Aggregation Operations
# ##############################################################################
# Method                 Description
# count()                Returns the number of non-null elements
# sum()                  Returns the sum of all elements
# mean()                 Returns the mean (average) of the elements
# median()               Returns the median (middle value) of the elements
# std()                  Returns the standard deviation of the elements
# min()                  Returns the minimum value among the elements
# max()                  Returns the maximum value among the elements
# ##############################################################################

print(f"\n{utils.ye_colored('NUMERICAL AGGREGATION OPERATIONS:')}")
print(f"Count               : {scores.count()}")
print(f"Sum                 : {scores.sum()}")
print(f"Min                 : {scores.min()}")
print(f"Max                 : {scores.max()}")
print(f"Mean                : {round(scores.mean(), 2)}")
print(f"Median              : {round(scores.median(), 2)}")
print(f"Variance            : {scores.var()}")
print(f"Standard Deviation  : {round(scores.std(), 2)}")

# ##############################################################################
# Categorical Aggregation Operations
# ##############################################################################
# Method                 Description
# unique()               Returns an array of unique elements
# nunique()              Returns the number of unique elements
# value_counts()        Returns a Series containing counts of unique elements
# ##############################################################################

print(f"\n{utils.ye_colored('CATEGORICAL AGGREGATION OPERATIONS:')}")
print(f"Unique Values       : {scores.unique()}")
print(f"Number of Unique    : {scores.nunique()}")
print(f"Value Counts        : {scores.value_counts()}")
