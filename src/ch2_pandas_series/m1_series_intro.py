"""Pandas Series Introduction"""

import numpy as np
import pandas as pd

# ##############################################################################
# Pandas Series
# ##############################################################################
# 1. Series are Pandas data stuctures built on top of NumPy arrays
# 2. They also contain an index and an optional name, in addition to
#    the array of data
# 3. They can be created from other data types, but are usually imported
#    from external sources
# 4. Two or more Series grouped together form a Pandas DataFrame
# ##############################################################################


def print_delimiter():
    print("\n" + "=-" * 40 + "\n")


# NumPy/Pandas Version
print_delimiter()
print("NUMPY/PANDAS VERSION:")
print(f"NumPy              : {np.__version__}")
print(f"Pandas             : {pd.__version__}")


# Create a Series from a list
temperature_list = [22.1, 21.9, 23.0, 24.1, 25.0, 26.5, 27.3]
temperature_series = pd.Series(temperature_list, name="Temperature")

print_delimiter()
print("TEMPLERATURE SERIES:")
print(f"Series             :\n{temperature_series}")

print_delimiter()
print("TEMPLERATURE SERIES ATTRIBUTES:")
print(f"Type               : {type(temperature_series)}")
print(f"Name               : {temperature_series.name}")
print(f"Data Type          : {temperature_series.dtype}")
print(f"Dimensions         : {temperature_series.ndim}")
print(f"Size               : {temperature_series.size}")
print(f"Index              : {temperature_series.index}")
print(f"Values             : {temperature_series.values}")
print(f"Values Type        : {type(temperature_series.values)}")

print_delimiter()
