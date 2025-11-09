"""Pandas Series Assignment - Accessing Series Data"""

import common_utils as util
import numpy as np
import pandas as pd

rng = np.random.default_rng(1987)

oil_prices = pd.Series(
    data=rng.uniform(110, 140, size=31).round(2),
    index=pd.date_range(start="2023-01-01", periods=31, freq="D"),
    name="Oil Prices",
)

print(util.ye_colored("Original Oil Prices Series:"))
print(oil_prices)

print(util.ye_colored("Mean Oil Price of First 10 Days:"))
print(round(oil_prices[:10].mean(), 2))

print(util.ye_colored("Mean Oil Price of Last 10 Days:"))
print(round(oil_prices[-10:].mean(), 2))

oil_prices_first_week = oil_prices.loc["2023-01-01":"2023-01-07"].reset_index(drop=True)
print(util.ye_colored("Oil Prices for the First Week (Reset Index):"))
print(oil_prices_first_week)
