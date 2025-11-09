"""Working With MultiIndex DataFrames in Pandas"""

import pandas as pd
from commons import (
    cyan_colored,
    green_colored,
    magenta_colored,
    red_colored,
    yellow_colored,
)

# Create a sample MultiIndex DataFrame
arryas = [
    ["Honda", "Honda", "Honda", "Honda", "Toyota", "Toyota", "Toyota", "Toyota"],
    ["Civic", "Civic", "CRV", "CRV", "Corolla", "Corolla", "RAV4", "RAV4"],
    ["LX", "EX", "LX", "EX", "LE", "XLE", "LE", "XLE"],
]
multi_index = pd.MultiIndex.from_arrays(arryas, names=("Make", "Model", "Trim"))
data = {
    "Price": [20000, 22000, 35000, 43000, 21000, 23000, 38000, 45000],
    "Mileage": [30, 28, 25, 22, 32, 30, 27, 24],
    "DriveTrain": ["FWD", "FWD", "AWD", "AWD", "FWD", "FWD", "AWD", "AWD"],
}
car_dealer = pd.DataFrame(data, index=multi_index)

# Sort the MultiIndex DataFrame for better organization and to avoid
# `indexing past lexsort depth may impact performance` warning
car_dealer.sort_index(inplace=True)

# The MultiIndex DataFrames are generally created through aggregation operations
# such as groupby, pivot_table, etc. Here, we create one manually for demonstration
print(red_colored("\nMultiIndex DataFrame:"))
print(car_dealer)

# Print the indices
print(yellow_colored("\nIndices:"))
print(car_dealer.index)

# Print the index levels
# print(blue_colored("\nIndex Levels:"))
# print(car_dealer.index.levels)

# Accessing outer level (Make) using .loc indexer
print(green_colored("\nAccessing data for Honda:"))
print(car_dealer.loc["Honda"])

# Accessing middle level (Model) using .loc indexer
print(cyan_colored("\nAccessing data for Honda CRV:"))
print(car_dealer.loc[("Honda", "CRV")])

# Accessing inner level (Trim) using .loc indexer
print(magenta_colored("\nAccessing data for Honda CRV EX:"))
print(car_dealer.loc[("Honda", "CRV", "EX"), :])
