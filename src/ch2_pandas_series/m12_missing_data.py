"""Handling Missing Data in Python Pandas Series"""

import pandas as pd
import common_utils as utils
import common_const as const


# NumPy NaN coerces integers to floats - Note the scores are now floats
# If you want to keep integers with missing values, use pandas nullable
# integer dtype 'Int16' or 'Int32'
scores = pd.Series(
    data=const.STUDENT_SCORES,
    index=const.STUDENT_NAMES,
    name="Student Scores",
    dtype="Int16",  # Using nullable integer dtype
)

print(f"{utils.ye_colored('STUDENT SCORES SERIES WITH MISSING VALUES:')}")
print(scores)

# Detecting Missing Data using isna() and isnull(). Both methods return a
# boolean Series indicating the presence of missing values (NaN).
print(f"\n{utils.ye_colored('IS NA?:')}")
print(scores.isna())

print(f"\n{utils.ye_colored('IS NULL?:')}")
print(scores.isnull())


# Handling Missing Data using fillna() and dropna(). Fillna() replaces
# missing values with a specified value, while dropna() removes any
# entries with missing values from the Series.
print(f"\n{utils.ye_colored('FILL NA WITH -1:')}")
filled_scores = scores.fillna(-1)
print(filled_scores)

print(f"\n{utils.ye_colored('DROP NA VALUES:')}")
dropped_scores = scores.dropna()
print(dropped_scores)
