"""Identifying Missing Data in Pandas DataFrames"""

import pandas as pd
from commons import (
    STUDENT_NAMES,
    STUDENT_SCORES,
    blue_colored,
    cyan_colored,
    green_colored,
    red_colored,
    yellow_colored,
)

# Create a sample DataFrame with missing values
scores = pd.DataFrame(
    data={
        "STUDENT": STUDENT_NAMES + [None],
        "SCORE": STUDENT_SCORES + [85.0],
    },
)
print(red_colored("\nScores DataFrame with Missing Values:"))
print(scores)

# ##############################################################################
# Identify missing values in the DataFrame
# ##############################################################################
# 1. Using isnull() and notnull() methods
# 2. Using isna() and notna() methods (not shown here, similar to isnull/notnull)
# ##############################################################################

# Using isnull() to create a boolean DataFrame
missing_values = scores.isnull()
print(blue_colored("\nMissing Values (isnull):"))
print(missing_values)

# Using notnull() to create a boolean DataFrame
not_missing_values = scores.notnull()
print(green_colored("\nNot Missing Values (notnull):"))
print(not_missing_values)

# Summarize missing values per column
missing_summary = scores.isnull().sum()
print(yellow_colored("\nSummary of Missing Values per Column:"))
print(missing_summary)

# ##############################################################################
# Drop or Fill missing values in the DataFrame
# ##############################################################################
# 1. Using dropna() method
#    This method removes any rows with missing values.
#    dropped_scores = scores.dropna()
#    To drop rows with missing values in a specific column use subset parameter
#    dropped_scores = scores.dropna(subset=["SCORE"])
# 2. Using fillna() method
#    This method fills missing values with a specified value.
#    filled_scores = scores.fillna(value={"SCORE": 0})
# ##############################################################################
cleansed_scores = scores.dropna(subset=["STUDENT"]).fillna(value={"SCORE": -1})
print(cyan_colored("\nCleansed Scores DataFrame (Missing Names dropped & Scores Filled with -1):"))
print(cleansed_scores)
