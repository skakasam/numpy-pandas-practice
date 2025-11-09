"""Creating DataFrames from CSV and Excel files using Pandas."""

import pandas as pd
from commons import cyan_colored, yellow_colored

# ##############################################################################
# Creating DataFrames from CSV File
# ##############################################################################
customers_csv_path = r"D:\Python\numpy-pandas-practice\data\input\customers.csv"
customers_df = pd.read_csv(customers_csv_path)

print(f"{yellow_colored('\nCustomers DataFrame Information:')}")

print(f"{cyan_colored('Shape:')}")
print(f"    {customers_df.shape}")

print(f"{cyan_colored('Columns:')}")
for col in customers_df.columns.tolist():
    print(f"    {col}")

print(f"{cyan_colored('DataTypes:')}")
for col, dtype in customers_df.dtypes.to_dict().items():
    print(f"    {col:20s} {dtype}")

print(f"{cyan_colored('First 2 Rows:')}")
for index, row in customers_df.head(n=2).iterrows():
    for col in customers_df.columns:
        print(f"    {col:20s} {row[col]}")
    print()
