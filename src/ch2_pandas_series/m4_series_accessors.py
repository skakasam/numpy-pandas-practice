"""Accessing Pandas Series Elements"""

import pandas as pd
import common_utils as util

student_series = pd.Series(
    ["Alice", "Bob", "Charlie", "David", "Eva"],
    index=[101, 102, 103, 104, 105],
    name="Students",
)

util.print_delimiter()
print(f"{util.cy_colored('STUDENTS SERIES')}:")
print(student_series)
print(f"{util.ye_colored('Index')}: {student_series.index}")

# ##############################################################################
# Pandas series accessor using iloc method - Integer location based indexing
# ##############################################################################
# Syntax: series.iloc[<integer position>]
#         where <integer position> is one of the following:
#         - Single integer position (e.g., 0, 1, 2)
#         - Slice of integer positions (e.g., 0:3, 2:5)
#         - List of integer positions (e.g., [0, 2, 4])
# Note that iloc is strictly integer position based indexing
# ##############################################################################

util.print_delimiter()
print(util.gr_colored("ACCESSING STUDENTS USING ILOC:"))
print(f"First Student               : {student_series.iloc[0]}")
print(f"Last Student                : {student_series.iloc[-1]}")
print(f"Students 2 to 4             : {student_series.iloc[1:4].values}")
print(f"Students 1, 3, and 5        : {student_series.iloc[[0, 2, 4]].values}")  # type: ignore

# ##############################################################################
# Pandas series accessor using loc method - Custom label based indexing
# ##############################################################################
# Syntax: series.loc[<label>]
#         where <label> is one of the following:
#         - Single label (e.g., 101, 102, 103)
#         - Slice of labels (e.g., 101:104, 102:105)
#         - List of labels (e.g., [101, 103, 105])
# Note that loc is strictly label based indexing
# ##############################################################################

util.print_delimiter()
print(util.bu_colored("ACCESSING STUDENTS USING LOC:"))
print(f"First Student               : {student_series.loc[101]}")
print(f"Last Student                : {student_series.loc[105]}")
print(f"Students 102 to 104         : {student_series.loc[102:104].values}")
print(f"Students 101, 103, and 105  : {student_series.loc[[101, 103, 105]].values}")

util.print_delimiter()
