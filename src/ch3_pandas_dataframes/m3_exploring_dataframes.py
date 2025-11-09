"""Exploring DataFrames in Pandas"""

import pandas as pd
from commons import yellow_colored

customers_csv_path = r"D:\Python\numpy-pandas-practice\data\input\customers.csv"
customers_df = pd.read_csv(customers_csv_path, index_col="Index")

# Display the first few rows of the DataFrame
print(yellow_colored("First 5 rows of the DataFrame:"))
print(customers_df.head())

# Display the last few rows of the DataFrame
print(yellow_colored("\nLast 5 rows of the DataFrame:"))
print(customers_df.tail())

# Display a random sample of rows from the DataFrame
print(yellow_colored("\nRandom sample of 5 rows from the DataFrame:"))
print(customers_df.sample(5))

# Display the shape of the DataFrame
print(yellow_colored("\nShape of the DataFrame:"))
print(customers_df.shape)

# Display the index of the DataFrame
print(yellow_colored("\nIndex of the DataFrame:"))
print(customers_df.index)

# Display the column names of the DataFrame
print(yellow_colored("\nColumn names of the DataFrame:"))
print(customers_df.columns)

# Display the data types of each column
print(yellow_colored("\nData types of each column:"))
print(customers_df.dtypes)

# Display summary statistics of the DataFrame
print(yellow_colored("\nSummary statistics of the DataFrame:"))
print(customers_df.describe(include="all"))

# Display information about the DataFrame
print(yellow_colored("\nInformation about the DataFrame:"))
print(customers_df.info(show_counts=True))

# Display the number of non-null entries in each column
print(yellow_colored("\nNumber of non-null entries in each column:"))
print(customers_df.count())

# Display the number of null values in each column
print(yellow_colored("\nNumber of null values in each column:"))
print(customers_df.isnull().sum())

# Display the number of unique values in each column
print(yellow_colored("\nNumber of unique values in each column:"))
print(customers_df.nunique())
