"""Aggregating DataFrames in Pandas."""

import numpy as np
import pandas as pd
from commons import (
    STUDENT_NAMES,
    blue_colored,
    green_colored,
    red_colored,
    yellow_colored,
)

# Create a sample DataFrame
rng = np.random.default_rng(2020)

section_options = ["S1", "S2"]
term_options = ["Freshman", "Sophomore", "Junior", "Senior"]
club_options = ["Drama", "Science", "Math", "Art", "Sports"]
students = pd.DataFrame(
    data={
        "STUDENT": STUDENT_NAMES,
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
        "CLUBS": [
            rng.choice(club_options, size=rng.integers(1, 3), replace=False).tolist()
            for _ in range(len(STUDENT_NAMES))
        ],
    }
)

# Display the original DataFrame
print(red_colored("\nStudents DataFrame:"))
print(students)

print(blue_colored("\nDataframe Information:"))
print(students.info())

# Group by TERM and calculate mean SCORE
mean_scores_by_term = students.groupby("TERM", observed=True)[["SCORE"]].mean().round(2)
print(green_colored("\nMean Scores by Term:"))
print(mean_scores_by_term)

# Group by TERM and SECTION, then calculate mean SCORE
# Setting observed=True to consider only the observed categories in the groupby
#   This avoids including combinations of TERM and SECTION that do not exist in the data
#   (e.g., if no students are in "Freshman" and "S2", that group won't appear)
# Not setting as_index=False generates a MultiIndex DataFrame with TERM and SECTION as indices
#   This is often useful for further analysis or plotting. Individual columns can be accessed
#   using .loc method. ex: mean_scores_by_term_section.loc[("Freshman", "S1")]
#   If as_index=True, TERM and SECTION would be regular columns.
mean_scores_by_term_section = (
    students.groupby(["TERM", "SECTION"], observed=True)[["SCORE"]].mean().round(2)
)
print(yellow_colored("\nMean Scores by Term and Section:"))
print(mean_scores_by_term_section)
