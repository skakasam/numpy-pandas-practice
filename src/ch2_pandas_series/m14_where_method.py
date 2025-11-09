"""Where Method in Pandas Series"""

import common_const as const
import common_utils as utils
import numpy as np
import pandas as pd

# Create a Numpy array for student scores
np_scores = np.array(
    [score for score in const.STUDENT_SCORES if score is not None], dtype="float64"
)
print(f"{utils.ye_colored('STUDENT SCORES NUMPY ARRAY:')}")
print(np_scores)

# Create a Pandas Series for student scores
pd_scores = pd.Series(
    data=const.STUDENT_SCORES,
    index=const.STUDENT_NAMES,
    name="Student Scores",
    dtype="float64",
).dropna()

print(f"\n{utils.ye_colored('STUDENT SCORES PANDAS SERIES:')}")
print(pd_scores)

# Use the where method to filter scores >= 90
# Using Numpy
np_filtered_scores = np.where(np_scores >= 90, np_scores, np.nan)
print(f"\n{utils.ye_colored('FILTERED STUDENT SCORES USING NUMPY WHERE (scores >= 90):')}")
print(np_filtered_scores)
# Using Pandas
pd_filtered_scores = pd_scores.where(pd_scores >= 90)
print(f"\n{utils.ye_colored('FILTERED STUDENT SCORES USING PANDAS WHERE (scores >= 90):')}")
print(pd_filtered_scores)

# Use where method to assign student grades
# Using Numpy
np_grades = np.where(
    np_scores >= 90,
    "A",
    np.where(
        np_scores >= 80,
        "B",
        np.where(
            np_scores >= 70,
            "C",
            np.where(
                np_scores < 70,
                "D",
                "X",
            ),
        ),
    ),
)
print(f"\n{utils.ye_colored('STUDENT GRADES USING NUMPY WHERE:')}")
print(np_grades)
# Using Pandas - Does not support nested conditions directly
pd_grades = pd_scores.where(pd_scores >= 0, "X")
print(f"\n{utils.ye_colored('STUDENT GRADES USING PANDAS WHERE:')}")
print(pd_grades)
