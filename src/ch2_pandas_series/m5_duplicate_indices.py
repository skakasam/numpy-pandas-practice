"""Pandas Series with Duplicate Indices"""

import pandas as pd
import common_utils as util

student_series = pd.Series(
    ["Alice", "Bob", "Charlie", "David", "Eva"],
    index=[101, 102, 101, 104, 105],
    name="Students",
)

util.print_delimiter()
print(f"{util.cy_colored('STUDENTS SERIES')}:")
print(student_series)
print(f"{util.ye_colored('Index')}: {student_series.index}")

util.print_delimiter()
print(util.bu_colored("ACCESSING STUDENTS USING DUPLICATE INDICES:"))
print(f"Students with ID 101      : {student_series[101].values}")  # type: ignore
print(f"1st Student with ID 101   : {student_series[101].iloc[0]}")  # type: ignore
print(f"2nd Student with ID 101   : {student_series[101].iloc[1]}")  # type: ignore

util.print_delimiter()
student_series.reset_index(drop=True, inplace=True)
print(f"{util.cy_colored('STUDENTS SERIES AFTER RESETTING INDEX')}:")
print(student_series)
print(f"{util.ye_colored('Index')}: {student_series.index}")

util.print_delimiter()
