"""Python Dataframe Introduction using Pandas."""

import pandas as pd
from commons import blue_colored, red_colored

# ##############################################################################
# Pandas DataFrames
# ##############################################################################
# DataFrames are 2-dimensional labeled data structures with columns of potentially
# different types. They are similar to SQL tables or Excel spreadsheets.
# 1. Each column of data in a DataFrame is a Pandas Series that shares the same
#    row index. The column headers work as a column index that contains the Series
#    names.
# 2. DataFrames can be created from various data sources, including CSV files,
#    Excel files, SQL databases, and dictionaries.
# 3. They provide powerful data manipulation capabilities, such as filtering,
#    grouping, merging, and reshaping data.
# 4. DataFrames support a wide range of operations, including arithmetic operations,
#    statistical functions, and data aggregation.
# 5. They are widely used in data analysis, data cleaning, and machine learning
#    tasks.
# ##############################################################################

# Creating a DataFrame from a dictionary
inventory_df = pd.DataFrame(
    {
        "Product": ["Laptop", "Smartphone", "Tablet", "Monitor", "Smartwatch"],
        "Price": [999.99, 499.99, 299.99, 199.99, 149.99],
        "Stock": [50, 200, 150, 75, 120],
        "CheckedOn": pd.to_datetime(
            ["2025-10-23", "2025-10-25", "2025-10-22", "2025-10-25", "2025-10-21"]
        ),
    }
)
print(f"{red_colored('\nProduct Inventory DataFrame:')}")
print(inventory_df)

# ##############################################################################
# Pandas Dataframe Properties
# ##############################################################################
# 1. shape: Returns a tuple representing the dimensionality of the DataFrame
#    (number of rows, number of columns).
# 2. columns: Returns the column labels of the DataFrame.
# 3. index: Returns the row labels of the DataFrame.
# 4. dtypes: Returns the data types of each column in the DataFrame.
# 5. axes: Returns a tuple representing the axes of the DataFrame
#    (row axis, column axis).
# ##############################################################################
formatted_inventory_df_dtypes = [
    str(inventory_df.dtypes.index[idx]) + " -> " + str(inventory_df.dtypes.iloc[idx])
    for idx in range(inventory_df.shape[1])
]
print(f"{blue_colored('\nProduct Inventory DataFrame Properties:')}")
print(f"Shape         : {inventory_df.shape}")
print(f"Index         : {inventory_df.index}")
print(f"Columns       : {inventory_df.columns}")
print(f"Dtypes        : {formatted_inventory_df_dtypes}")
print(f"Rows (Axis 0) : {inventory_df.axes[0]}")
print(f"Cols (Axis 1) : {inventory_df.axes[1]}")
