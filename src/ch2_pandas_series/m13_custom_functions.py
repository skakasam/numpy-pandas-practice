"""Applying Custom Functions to Pandas Series"""

import pandas as pd
import common_utils as utils
import common_const as const

# Create a Pandas Series for grocery item prices
item_prices = pd.Series(
    data=const.ITEM_PRICES,
    index=const.GROCERY_ITEMS,
    name="Grocery Item Prices",
    dtype="float64",
)

print(f"{utils.ye_colored('GROCERY ITEM PRICES SERIES:')}")
print(item_prices)

# ##############################################################################
# Apply Method with Custom Functions
# ##############################################################################
# The apply() method allows you to apply custom functions to each element
# in a Pandas Series. This is useful for performing complex transformations.
# However, this function will not be vectorized and may not be as efficient
# as using built-in (vectorized) Pandas functions.
# ##############################################################################


# Define a custom function to apply a discount
def apply_discount(price, discount_rate=0.0):
    """Apply a discount to the given price."""
    return price * (1 - discount_rate)


# Apply a 10% discount to all item prices
discounted_prices = item_prices.apply(apply_discount, discount_rate=0.10)

print(f"\n{utils.ye_colored('DISCOUNTED GROCERY ITEM PRICES (10% OFF):')}")
print(discounted_prices)
