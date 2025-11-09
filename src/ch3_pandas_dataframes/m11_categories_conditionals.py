"""Pandas Categoricals vs. Numpy Conditionals"""

import numpy as np
import pandas as pd
from commons import (
    STUDENT_NAMES,
    blue_colored,
    green_colored,
    red_colored,
)

# Create a sample DataFrame
FRESHMAN, SOPHOMORE, JUNIOR, SENIOR = "Freshman", "Sophomore", "Junior", "Senior"
term_options = [FRESHMAN, SOPHOMORE, JUNIOR, SENIOR]
scores = pd.DataFrame(
    data={
        "STUDENT": STUDENT_NAMES,
        "TERM": pd.Categorical(
            np.random.choice(term_options, size=len(STUDENT_NAMES)),
            categories=term_options,
            ordered=True,
        ),
        "SCORE": np.random.default_rng(1987).integers(35, 100, size=len(STUDENT_NAMES)),
    }
)

# Display the original DataFrame
print(red_colored("\nOriginal DataFrame:"))
print(scores)

# Add categorical column based on score ranges using Pandas pd.cut()
scores["GRADE"] = pd.cut(
    scores["SCORE"],
    bins=[0, 35, 50, 70, 85, 100],
    labels=["F", "D", "C", "B", "A"],
)

# Add conditional column based on score ranges using NumPy np.select()
gpa = [0.0, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]
conditions = [
    (scores["SCORE"] < 65),
    (scores["SCORE"] >= 65) & (scores["SCORE"] <= 66),
    (scores["SCORE"] >= 67) & (scores["SCORE"] <= 69),
    (scores["SCORE"] >= 70) & (scores["SCORE"] <= 72),
    (scores["SCORE"] >= 73) & (scores["SCORE"] <= 76),
    (scores["SCORE"] >= 77) & (scores["SCORE"] <= 79),
    (scores["SCORE"] >= 80) & (scores["SCORE"] <= 82),
    (scores["SCORE"] >= 83) & (scores["SCORE"] <= 86),
    (scores["SCORE"] >= 87) & (scores["SCORE"] <= 89),
    (scores["SCORE"] >= 90) & (scores["SCORE"] <= 93),
    (scores["SCORE"] >= 94),
]
scores["GPA"] = np.select(conditions, gpa, default=0.0)

# Add conditional column based on score ranges using NumPy np.where()
scores["GPA_ALT"] = np.where(
    scores["SCORE"] >= 94,
    4.0,
    np.where(
        scores["SCORE"] >= 90,
        3.7,
        np.where(
            scores["SCORE"] >= 87,
            3.3,
            np.where(
                scores["SCORE"] >= 83,
                3.0,
                np.where(
                    scores["SCORE"] >= 80,
                    2.7,
                    np.where(
                        scores["SCORE"] >= 77,
                        2.3,
                        np.where(
                            scores["SCORE"] >= 73,
                            2.0,
                            np.where(
                                scores["SCORE"] >= 70,
                                1.7,
                                np.where(
                                    scores["SCORE"] >= 67,
                                    1.3,
                                    np.where(
                                        scores["SCORE"] >= 65,
                                        1.0,
                                        0.0,
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)

# Add a new column using pandas map() method
# By passing a dictionary of mappings
scores["YEAR"] = scores["TERM"].map(
    {
        "Freshman": 1,
        "Sophomore": 2,
        "Junior": 3,
        "Senior": 4,
    }
)
# By passing a lambda function
scores["YEAR_ALT"] = scores["TERM"].map(
    lambda x: 1 if x == "Freshman" else 2 if x == "Sophomore" else 3 if x == "Junior" else 4
)

# Add new columns using assign() method
scores = scores.assign(
    PASS_FAIL=lambda df: np.where(df["SCORE"] >= 50, "Pass", "Fail"),
    HONOR_ROLL=lambda df: df["GPA"] >= 3.5,
)

print(blue_colored("\nDataFrame after adding new columns:"))
print(scores)

print(green_colored("\nDataFrame Info:"))
print(scores.info())
