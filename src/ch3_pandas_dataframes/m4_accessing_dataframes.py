"""Accessing Pandas DataFrames"""

import pandas as pd
from commons import (
    blue_colored,
    cyan_colored,
    green_colored,
    magenta_colored,
    red_colored,
    yellow_colored,
)

products_csv_path = r"D:\Python\numpy-pandas-practice\data\input\products.csv"
products_df = pd.read_csv(products_csv_path, index_col="Index").head(10)

print(red_colored("Products DataFrame Information:"))
print(products_df.info(show_counts=True))

# ##############################################################################
# Access a DataFrame Column
# ##############################################################################
# 1. Using Bracket Notation - Preferred method!
#    column_series = products_df["Name"]
# 2. Using Dot Notation - Note that this method only works if the
#    column name is a valid Python identifier.
#    column_series = products_df.Name
# ##############################################################################
print(blue_colored("\nAccessing Name column from Products DataFrame using bracket notation:"))
print(products_df["Name"])  # Pandas Series
# print(products_df["Internal ID"]) Works!

print(green_colored("\nAccessing Name column from Products DataFrame using dot notation:"))
print(products_df.Name)
# print(products_df.Internal ID) Doesn't Work!

# ##############################################################################
# Access Multiple DataFrame Columns
# ##############################################################################
print(yellow_colored("\nAccessing Name and Price columns from Products DataFrame:"))
print(products_df[["Name", "Price"]])  # Pandas DataFrame

# ##############################################################################
# Accessing Data with ILOC and LOC
# ##############################################################################
print(cyan_colored("\nAccessing first 3 rows and first 2 columns using ILOC:"))
print(products_df.iloc[0:3, 0:2])  # Frist 3 rows and first 2 columns

print(magenta_colored("\nAccessing rows with Index 2 to 4 and columns Name and Price using LOC:"))
print(products_df.loc[2:4, ["Name", "Price"]])  # Get Specific axes with [a, b] and Slice with a:b
