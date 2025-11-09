"""Dropping Rows/Columns in a DataFrame using pandas"""

import pandas as pd
from commons import (
    blue_colored,
    red_colored,
)

products_csv_path = r"D:\Python\numpy-pandas-practice\data\input\products.csv"
products_df = pd.read_csv(products_csv_path, index_col="Index").head(10)

print(red_colored("Products DataFrame Information:"))
print(products_df.info(show_counts=True))

# ##############################################################################
# Dropping Rows and Columns from a DataFrame
# ##############################################################################
# 1. Dropping Rows
#    dropped_rows_df = products_df.drop([0, 1])
#    dropped_rows_df = products_df.drop(index=[0, 1], axis=0)
# 2. Dropping Columns
#    dropped_columns_df = products_df.drop(columns=["Name", "Price"])
#    dropped_columns_df = products_df.drop(["Name", "Price"], axis=1)
# 3. Dropping In-Place
#    products_df.drop([0, 1], inplace=True)
# 4. Dropping with Labels vs. Positions
#    Labels: Use the actual index/column names
#    Positions: Use iloc to get positions and drop accordingly
# ##############################################################################
sample_products_df = products_df.drop(
    columns=[
        "Description",
        "Brand",
        "EAN",
        "Color",
        "Size",
        "Availability",
        "Internal ID",
    ],
    axis=1,
)
sample_products_df.drop(labels=[6, 7, 8, 9, 10], axis=0, inplace=True)

print(blue_colored("\nAfter dropping rows and columns:"))
print(sample_products_df)
