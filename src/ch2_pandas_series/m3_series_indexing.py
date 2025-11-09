"""Python Pandas Series Indexing"""

import common_utils as util
import pandas as pd

# ##############################################################################
# Pandas Series Indexing
# ##############################################################################
# 1. Series can be indexed using labels or integer positions
# 2. Label-based indexing uses the index labels to access data
# 3. Position-based indexing uses integer positions to access data
# 4. Series support slicing, boolean indexing, and fancy indexing
# ##############################################################################

student_series = pd.Series(["Alice", "Bob", "Charlie", "David", "Eva"], name="Students")

util.print_delimiter()
print(f"{util.cy_colored('STUDENTS SERIES')}:")
print(student_series)
print(f"{util.ye_colored('Index')}: {student_series.index}")

util.print_delimiter()
print(util.gr_colored("ACCESSING STUDENTS:"))
print(f"First Student               : {student_series[0]}")
print(f"Last Student                : {student_series[4]}")
print(f"Students 1 to 3             : {student_series[1:4].values}")

util.print_delimiter()
student_ids = ["SID101", "SID102", "SID103", "SID104", "SID105"]
student_series.index = student_ids  # Assigning custom index (roll numbers)
print(f"{util.cy_colored('STUDENTS SERIES WITH ROLL NUMBERS AS INDEX')}:")
print(student_series)
print(f"{util.ye_colored('Index')}: {student_series.index}")

util.print_delimiter()
print(util.gr_colored("ACCESSING STUDENTS USING ROLL NUMBERS:"))
print(f"First Student               : {student_series.loc['SID101']}")
print(f"Last Student                : {student_series.loc['SID105']}")
print(f"Students SID102 to SID104   : {student_series.loc['SID102':'SID104'].values}")

util.print_delimiter()
