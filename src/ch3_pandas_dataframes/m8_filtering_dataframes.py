"""Filtering DataFrames in Pandas"""

import numpy as np
import pandas as pd
from commons import (
    STUDENT_NAMES,
    STUDENT_SCORES,
    blue_colored,
    cyan_colored,
    green_colored,
    red_colored,
    yellow_colored,
)

# Create a sample DataFrame
term_options = ["Freshman", "Sophomore", "Junior", "Senior"]
terms = np.random.choice(term_options, size=32)
scores = pd.DataFrame(
    data={
        "STUDENT": STUDENT_NAMES,
        "SCORE": STUDENT_SCORES,
        "TERM": terms,
    }
).dropna(subset=["SCORE"])

print(red_colored("Scores DataFrame:"))
print(scores)

# ##############################################################################
# Filtering DataFrames
# ##############################################################################
# 1. Using boolean indexing
#    Example:
#    To filter students with scores greater than 80
#      high_scorers = scores[scores["SCORE"] > 80]
#    To filter based on multiple conditions use & (and), | (or) operators
#      senior_high_scorers = scores[(scores["TERM"] == "Senior") & (scores["SCORE"] > 80)]
# 2. Using loc[] and iloc[] methods - Preferred Method
#    Keywords:
#      & (and),
#      | (or),
#      ~ (not),
#      ==, !=, >, <, >=, <=
#    Methods:
#      isin() - to filter based on a list of values
#      between() - to filter based on a range of values
#    Example:
#    To filter rows by label using loc
#      high_scorers_loc = scores.loc[scores["SCORE"] > 80]
#    To filter rows by position using iloc
#      first_five_rows = scores.iloc[0:5]
#    To filter based on multiple conditions with loc
#      senior_high_scorers_loc = scores.loc[(scores["TERM"] == "Senior") & (scores["SCORE"] > 80)]
#    To filter specific columns with loc
#      senior_high_scorers_columns = scores.loc[
#        (scores["TERM"] == "Senior") & (scores["SCORE"] > 80),
#        ["STUDENT", "SCORE"]
#      ]
# 3. Using query() method to use SQL-like syntax
#   Keywords:
#     and,
#     or,
#     not,
#     in, between
#     ==, !=, >, <, >=, <=,
#   Example:
#   To filter students with scores greater than 80
#     high_scorers_query = scores.query("SCORE > 80")
#   To filter based on multiple conditions
#     senior_high_scorers_query = scores.query("TERM == 'Senior' and SCORE > 80")
#   To filter specific columns
#     high_scorers_query = scores.query("SCORE > 80")[["STUDENT", "SCORE"]]
#   To handling special column names with spaces use backticks
#     special_column_filter = scores.query("`Special Column` > 50")
#   To reference variables use @
#     threshold = 80
#     variable_filter = scores.query("SCORE > @threshold")
# ##############################################################################

senior_high_scorers = scores.loc[
    (scores["TERM"] == "Senior") & (scores["SCORE"] > 80),
    ["STUDENT", "SCORE"],
]
print(blue_colored("\nSenior Students with Scores Greater than 80:"))
print(senior_high_scorers)

junior_low_scorers = scores.query("TERM == 'Junior' and SCORE < 80")[["STUDENT", "SCORE"]]
print(green_colored("\nJunior Students with Scores Less than 80:"))
print(junior_low_scorers)

min_score = 65
max_score = 85
print(yellow_colored("\nJunior/Senior Students with scores Between 65 and 85 using query method:"))
print(scores.query("TERM in ['Junior', 'Senior'] and SCORE > @min_score and SCORE < @max_score"))
print(cyan_colored("\nJunior/Senior Students with scores Between 65 and 85 using loc method:"))
print(
    scores.loc[
        (
            ~scores["TERM"].isin(["Freshman", "Sophomore"])
            & scores["SCORE"].between(min_score, max_score)
        )
    ]
)
