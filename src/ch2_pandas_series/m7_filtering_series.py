"""Python Pandas Series Filtering"""

import numpy as np
import pandas as pd
import common_utils as utils

rng = np.random.default_rng(1987)

oil_prices = pd.Series(
    data=rng.uniform(110, 140, size=31).round(2),
    index=pd.date_range(start="2025-01-01", periods=31, freq="D"),
    name="Oil Prices",
)

print(utils.ye_colored("Oil Prices for Jan'2025:"))
print(oil_prices)

print(utils.ye_colored("Oil Prices >= 130.00 using Python Operators:"))
print(oil_prices.loc[oil_prices >= 130.00])

print(utils.ye_colored("Oil Prices >= 130.00 using Pandas Method:"))
print(oil_prices.loc[oil_prices.ge(130.00)])

print(utils.ye_colored("Oil Prices >= 130.00 in the last 10 days using Python Operators:"))
mask = (oil_prices >= 130.00) & (oil_prices.index >= "2025-01-22")
print(oil_prices[mask])

print(utils.ye_colored("Oil Prices >= 130.00 **NOT** in the last 10 days using Pandas Method:"))
print(
    oil_prices[
        oil_prices.ge(130.00)
        & ~(oil_prices.index.isin(pd.date_range(start="2025-01-22", periods=10, freq="D")))
    ]
)

print(utils.ye_colored("Oil Prices on 14th and 28th Jan:"))
print(
    oil_prices[
        oil_prices.index.isin(
            [
                pd.to_datetime("2025-01-14", format="%Y-%m-%d"),
                pd.to_datetime("2025-01-21"),
            ]
        )
    ]
)
