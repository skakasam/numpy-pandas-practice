"""Pivot Tables in Pandas"""

import pandas as pd
from commons import blue_colored, green_colored, red_colored

# Create a sample DataFrame
students = pd.read_csv(r"D:\Python\numpy-pandas-practice\data\input\students.csv")

# Display the original DataFrame
print(red_colored("\nStudents DataFrame:"))
print(students)

# Single aggration in a pivot table
# Create a pivot table to analyze average scores by YEAR and CLASS
pivot_table_avg_score = pd.pivot_table(
    data=students,
    values="SCORE",
    index="YEAR",
    columns="CLASS",
    aggfunc="mean",
    fill_value=0,
    observed=True,
).round(2)
print(blue_colored("\nPivot Table - Average Scores by YEAR and CLASS:"))
print(pivot_table_avg_score)

# Multiple aggrations in a pivot table
pivot_table_multiple_agg = pd.pivot_table(
    data=students,
    index=("YEAR", "CLASS"),
    # columns=["AVG_SCORE", "CLUB_ENROLLMENTS", "TOTAL_STUDENTS"],
    aggfunc=({"SCORE": "mean", "CLUB": "count", "NAME": "count"}),
    fill_value=0,
    observed=True,
).round(2)
print(green_colored("\nPivot Table - Mean SCORES and CLUB enrollments by YEAR and CLASS:"))
print(pivot_table_multiple_agg)
