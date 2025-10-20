"""Arithmetic Operations on Python Pandas Series"""

import numpy as np
import pandas as pd
import common_utils as utils
import common_const as const


# ##############################################################################
# Arithmetic Operations on Pandas Series
# ##############################################################################
# Operation                   Python Operator     Pandas Method
# Addition                    +                   .add()
# Subtraction                 -                   .sub(), .subtract()
# Multiplication              *                   .mul(), .multiply()
# Division                    /                   .div(), .divide(), .truediv()
# Floor Division              //                  .floordiv()
# Modulus                     %                   .mod(), .remainder()
# Exponentiation              **                  .pow()
# ##############################################################################

grocery_prices = pd.Series(
    data=const.ITEM_PRICES,
    index=const.GROCERY_ITEMS,
    name="Grocery Prices",
).head(5)

# grocery_prices.loc["Banana"] = np.nan Introduce a missing value for demonstration

print(f"{utils.ye_colored('GROCERY PRICES:')}")
print(grocery_prices)

# Adding a constant value to each element in the Series
print(f"\n{utils.ye_colored('ADDING 0.05 TO EACH PRICE:')}")
print(grocery_prices + 0.05)
# print(grocery_prices.add(0.05, fill_value=0)) Using fill_value to handle NaN

# Subtracting a constant value from each element in the Series
print(f"\n{utils.ye_colored('SUBTRACTING 0.10 FROM EACH PRICE:')}")
print(grocery_prices - 0.10)

# Conveting prices from int to string and concatenating a suffix
print(f"\n{utils.ye_colored('CONVERTING PRICES TO STRINGS WITH SUFFIX:')}")
print("$" + grocery_prices.astype(str) + " USD")

# Multiplying each element in the Series by a constant factor
print(f"\n{utils.ye_colored('MULTIPLYING EACH PRICE BY 0.9 (10% DISCOUNT):')}")
print(round(grocery_prices * 0.9, 2))

# Dividing each element in the Series by a constant value
print(f"\n{utils.ye_colored('DIVIDING EACH PRICE BY 2:')}")
print(grocery_prices / 2)

# Exponentiating each element in the Series
print(f"\n{utils.ye_colored('SQUARING EACH PRICE:')}")
print(grocery_prices**2)

# Modulus operation on each element in the Series
print(f"\n{utils.ye_colored('MODULUS 1 ON EACH PRICE:')}")
print(grocery_prices % 1)
