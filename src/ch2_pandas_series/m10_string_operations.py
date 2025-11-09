"""String Operations on Python Pandas Series"""

import pandas as pd
import common_utils as utils
import common_const as const

students_series = pd.Series(
    data=const.STUDENT_NAMES,
    index=const.STUDENT_IDS,
    name="Student Names",
)

# Convert all names to uppercase
print(f"{utils.ye_colored('STUDENT NAMES IN UPPERCASE:')}")
print(students_series.str.upper())

# Get the length of each name
print(f"\n{utils.ye_colored('LENGTH OF EACH STUDENT NAME:')}")
print(students_series.str.len())

# Check if names contain the substring 'an'
print(f"\n{utils.ye_colored('DOES THE NAME CONTAIN "an"?')}")
print(students_series.str.contains("an", case=False))

# Get the first names (assuming names are in "First Last" format)
print(f"{utils.ye_colored('FIRST NAMES OF STUDENTS:')}")
print(students_series.str.split().str[0])

# Split names into first and last names, and add column names
print(f"\n{utils.ye_colored('SPLIT NAMES INTO FIRST AND LAST NAMES:')}")
students_df = students_series.str.split(expand=True)
students_df.columns = ["f_name", "l_name"]
print(students_df)
print(f"{type(students_df)=}")

# Get initials of each student
print(f"\n{utils.ye_colored('INITIALS OF EACH STUDENT:')}")
print(students_series.str.split().str[0].str[0] + students_series.str.split().str[1].str[0])

student_ages = pd.Series(["Alice-20", "Bob-22", "Charlie-19", "Diana-21"], name="Student Ages")
# Split names and ages into separate columns
print(f"\n{utils.ye_colored('SPLIT NAMES AND AGES:')}")
ages_df = student_ages.str.split("-", expand=True)
print(ages_df)
print(f"{type(ages_df)=}")
print(f"{type(ages_df[1])=}")
print(f"{type(ages_df[1][0])=}")

# Convert ages to integers
ages_df[1] = ages_df[1].astype(int)
print(f"\n{utils.ye_colored('AGES AS INTEGERS:')}")
print(ages_df)
print(f"{type(ages_df[1])=}")
print(f"{type(ages_df[1][0])=}")
