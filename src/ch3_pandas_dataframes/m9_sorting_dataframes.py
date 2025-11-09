"""Sorting DataFrames in Pandas"""

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
scores = (
    pd.DataFrame(
        data={
            "TERM": np.random.choice(term_options, size=len(STUDENT_NAMES)),
            "STUDENT": STUDENT_NAMES,
            "SCORE": np.random.default_rng(1987).integers(35, 100, size=len(STUDENT_NAMES)),
        }
    )
    .dropna(subset=["SCORE"])
    .sort_values(by="SCORE")
)

# Display the original DataFrame
print(red_colored("\nOriginal DataFrame:"))
print(scores)

print(red_colored("\nDataFrame Information:"))
scores.info()

# ##############################################################################
# Sorting DataFrames in Pandas
# ##############################################################################
# 1. Sort by Index
#      - Use axis parameter to specify sorting by index (0 for rows, 1 for columns)
#      - Sorting by column index is less common
# 2. Sort by Value
#      - Use the by parameter to specify the column to sort by
#      - ascending parameter to specify sort order (default is True)
# 3. Sort by Multiple Columns
#      - Use a list of column names to sort by multiple columns
#      - ascending can also be a list to specify order for each column
# 4. Sort with Custom Order
#      - Use pd.Categorical to define a custom order for sorting
# 5. Sort with Custom Order and Multiple Columns
# ##############################################################################

# 1. Sort by Index
print(blue_colored("\n1. Sort by Index:"))
print(scores.sort_index())

# 2. Sort by Value
print(green_colored("\n2. Sort by Value (TERM):"))
print(scores.sort_values(by="TERM"))

# 3. Sort by Multiple Columns
print(yellow_colored("\n3. Sort by Multiple Columns (TERM, SCORE):"))
print(scores.sort_values(by=["TERM", "SCORE"], ascending=[True, False]))

# 4. Sort with Custom Order
print(cyan_colored("\n4. Sort with Custom Order (TERM):"))
term_order = [FRESHMAN, SOPHOMORE, JUNIOR, SENIOR]
scores["TERM"] = pd.Categorical(scores["TERM"], categories=term_order, ordered=True)
print(scores.sort_values(by="TERM"))

# 5. Sort with Custom Order and Multiple Columns
print(magenta_colored("\n5. Sort with Custom Order and Multiple Columns (TERM, SCORE):"))
print(scores.sort_values(by=["TERM", "SCORE"], ascending=[True, False]))
