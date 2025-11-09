"""Transforming DataFrames using pandas."""

import numpy as np
import pandas as pd
from commons import STUDENT_NAMES, blue_colored, green_colored, red_colored

# Create a sample DataFrame
rng = np.random.default_rng(2020)

class_options = ["C1", "C2"]
year_options = ["Freshman", "Sophomore", "Junior", "Senior"]
club_options = ["", "Art", "Drama", "Math", "Science", "Sports"]
students = pd.DataFrame(
    data={
        "NAME": STUDENT_NAMES,
        "YEAR": pd.Categorical(
            np.random.choice(year_options, size=len(STUDENT_NAMES)),
            categories=year_options,
            ordered=True,
        ),
        "CLASS": pd.Categorical(
            np.random.choice(class_options, size=len(STUDENT_NAMES)),
            categories=class_options,
            ordered=True,
        ),
        "SCORE": rng.integers(
            low=50,
            high=100,
            size=len(STUDENT_NAMES),
            dtype=np.int8,
        ),
        "CLUB": pd.Categorical(
            np.random.choice(club_options, size=len(STUDENT_NAMES)),
            categories=club_options,
            ordered=True,
        ),
    }
)

# Display the original DataFrame
print(red_colored("\nStudents DataFrame:"))
print(students)

# The transform method allows you to execute a function for each value of the
# DataFrame and return a DataFrame with the same shape as the original one.


# Transform the CLUB colum to CLUB_CREDITS based on the following rules:
# - If the student is not in any club, CLUB_CREDITS = 0
# - If the student is in Art or Drama club, CLUB_CREDITS = 10
# - If the student is in Math or Science club, CLUB_CREDITS = 15
# - If the student is in Sports club, CLUB_CREDITS = 20
# Use the transform method to achieve this.
def club_credits(club):
    if club == "":
        return 0
    elif club in ["Art", "Drama"]:
        return 10
    elif club in ["Math", "Science"]:
        return 15
    elif club == "Sports":
        return 20


students["CLUB_CREDITS"] = students["CLUB"].transform(club_credits)
print(blue_colored("\nStudents DataFrame with CLUB_CREDITS:"))
print(students)


# Assign a new column GRADE based on the SCORE and CLUB_CREDITS:
# - If SCORE + CLUB_CREDITS >= 100, GRADE = 'A+'
# - If SCORE + CLUB_CREDITS >= 90, GRADE = 'A'
# - If SCORE + CLUB_CREDITS >= 80, GRADE = 'B'
# - If SCORE + CLUB_CREDITS >= 65, GRADE = 'C'
# - If SCORE + CLUB_CREDITS >= 50, GRADE = 'D'
# - Otherwise, GRADE = 'D'
students["GRADE"] = pd.cut(
    students["SCORE"] + students["CLUB_CREDITS"],
    bins=[0, 50, 65, 80, 90, 100, 120],
    labels=["F", "D", "C", "B", "A", "A+"],
)

print(green_colored("\nStudents DataFrame with GRADE:"))
print(students)
