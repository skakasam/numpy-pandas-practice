"""Named Aggregations on Pandas DataFrames using groupby and agg Methods."""

import numpy as np
import pandas as pd
from commons import STUDENT_NAMES, blue_colored, red_colored

# Create a sample DataFrame
rng = np.random.default_rng(2020)

section_options = ["S1", "S2"]
term_options = ["Freshman", "Sophomore", "Junior", "Senior"]
students = pd.DataFrame(
    data={
        "NAME": STUDENT_NAMES,
        "TERM": pd.Categorical(
            np.random.choice(term_options, size=len(STUDENT_NAMES)),
            categories=term_options,
            ordered=True,
        ),
        "SECTION": pd.Categorical(
            np.random.choice(section_options, size=len(STUDENT_NAMES)),
            categories=section_options,
            ordered=True,
        ),
        "SCORE": rng.integers(
            low=35,
            high=100,
            size=len(STUDENT_NAMES),
            dtype=np.int8,
        ),
    }
)

# Display the original DataFrame
print(red_colored("\nStudents DataFrame:"))
print(students)

# Average Student Scores per Term & Section
avg_student_scores = (
    students.groupby(["TERM", "SECTION"], observed=True)
    .agg(
        CNT_STUDENT=("NAME", "count"),
        AVG_SCORE=("SCORE", "mean"),
    )
    .round(2)
)
print(blue_colored("\nStudent Counts and Average Student Scores per Term & Section:"))
print(avg_student_scores)
