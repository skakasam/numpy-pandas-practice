"""Melting DataFrames with Pandas"""

import pandas as pd
from commons import blue_colored, green_colored, red_colored

# Create a sample DataFrame
people = pd.DataFrame(
    {
        "NAME": ["Alice", "Bob", "Charlie"],
        "AGE": [25, 30, 35],
        "HOBBIES": [["Reading", "Cycling"], ["Cycling", "Swimming"], ["Photography", "Reading"]],
    }
)

# Display the original DataFrame
print(red_colored("\nOriginal People DataFrame:"))
print(people)

# Melt the DataFrame to unpivot/normalize the HOBBIES column
melted_people = (
    people.explode("HOBBIES").reset_index(drop=True).rename(columns={"HOBBIES": "HOBBY"})
)
print(blue_colored("\nMelted People DataFrame:"))
print(melted_people)

# Create another sample DataFrame
country_revenues = pd.DataFrame(
    {
        "COUNTRY": ["USA", "Canada", "Germany"],
        "Q1_REVENUE": [15000, 12000, 13000],
        "Q2_REVENUE": [16000, 11000, 14000],
        "Q3_REVENUE": [17000, 11500, 13500],
        "Q4_REVENUE": [18000, 12500, 14500],
    }
)

# Display the original DataFrame
print(red_colored("\nOriginal Country Revenues DataFrame:"))
print(country_revenues)

# Melt the DataFrame to unpivot/normalize the quarterly revenue columns
melted_revenues = country_revenues.melt()
print(blue_colored("\nMelted Country Revenues DataFrame:"))
print(melted_revenues)

melted_revenues_with_idvars = country_revenues.melt(
    id_vars=["COUNTRY"], var_name="QUARTER", value_name="REVENUE"
).transform(lambda x: x.assign(QUARTER=x["QUARTER"].str.replace("_REVENUE", "")))
print(green_colored("\nMelted Country Revenues DataFrame with id_vars:"))
print(melted_revenues_with_idvars)
