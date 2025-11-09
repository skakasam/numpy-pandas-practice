"""Column Modification in Pandas DataFrame"""

import numpy as np
import pandas as pd
from commons import (
    STUDENT_NAMES,
    blue_colored,
    cyan_colored,
    green_colored,
    magenta_colored,
    red_colored,
    yellow_colored,
)

# Create a sample DataFrame
FRESHMAN, SOPHOMORE, JUNIOR, SENIOR = "Freshman", "Sophomore", "Junior", "Senior"
term_options = [FRESHMAN, SOPHOMORE, JUNIOR, SENIOR]
scores = pd.DataFrame(
    data={
        "student": STUDENT_NAMES,
        "term": pd.Categorical(
            np.random.choice(term_options, size=len(STUDENT_NAMES)),
            categories=term_options,
            ordered=True,
        ),
        "score": np.random.default_rng(1987).integers(35, 100, size=len(STUDENT_NAMES)),
    }
)

# Display the original DataFrame
print(red_colored("\nOriginal DataFrame:"))
print(scores)

# Rename columns using rename() method
scores.rename(columns={"term": "year"}, inplace=True)
print(blue_colored("\nDataFrame after renaming columns:"))
print(scores)

# Rename columns by assigning to columns attribute
scores.columns = [col.upper() for col in scores.columns]
print(blue_colored("\nDataFrame after upcasing column names:"))
print(scores)

# Add a new column based on existing columns
# Boolean column
scores["PASSED"] = scores["SCORE"] >= 50
# Categorical column based on score ranges
scores["GRADE"] = pd.cut(
    scores["SCORE"],
    bins=[0, 35, 50, 70, 85, 100],
    labels=["F", "D", "C", "B", "A"],
)
print(yellow_colored("\nDataFrame after adding GRADE and PASSED column:"))
print(scores)

# Drop a column
scores.drop(columns=["PASSED"], inplace=True)
print(cyan_colored("\nDataFrame after dropping PASSED column:"))
print(scores)

# Reindex columns to a specific order
new_order = ["STUDENT", "YEAR", "SCORE", "GRADE"]
scores = scores.reindex(columns=new_order)
print(green_colored("\nDataFrame after reindexing columns:"))
print(scores)

# Display final DataFrame information
print(magenta_colored("\nFinal DataFrame Information:"))
scores.info()
