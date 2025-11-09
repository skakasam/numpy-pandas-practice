"""Time Series in Pandas"""

import datetime

import numpy as np
import pandas as pd
from commons import (
    blue_colored,
    cyan_colored,
    green_colored,
    magenta_colored,
    red_colored,
    yellow_colored,
)

# ##############################################################################
# Python datetime Type
# ##############################################################################

py_dttm = datetime.datetime.now()
print(red_colored("Python datetime: "), py_dttm)

# ##############################################################################
# Numpy datetime64 type lets us work with datetimes in Pandas DataFrames
# ##############################################################################

np_dttm = np.datetime64("2024-06-01 12:30:45")
print(blue_colored("\nNumpy datetime64: "), np_dttm)


# ##############################################################################
# Using Datetime in Pandas DataFrames
# ##############################################################################
orders = pd.DataFrame(
    {
        "ORDER_ID": [1, 2, 3],
        "ORDER_DTTM": ["2024-06-01 10:00:00", "2024-06-02 11:30:00", "2024-06-03 14:45:00"],
        "DELIVERY_DTTM": ["2024-06-05 16:00:00", "2024-06-06 18:30:00", "N/A"],
    }
)

print(green_colored("\nOrders DataFrame and the corresponding dtypes:"))
print(orders)
print(orders.dtypes)

# Convert ORDER_DTTM to datetime64[ns] dtype
orders["ORDER_DTTM"] = orders["ORDER_DTTM"].astype("datetime64[ns]")

# Convert DELIVERY_DTTM to datetime64[ns] dtype
# The astype method will raise an error due to the "N/A" value
# orders["DELIVERY_DTTM"] = orders["DELIVERY_DTTM"].astype("datetime64[ns]")
# Instead, we use pd.to_datetime which can handle errors.
# Datetime Formats
# %Y - 4-digit year
# %m - 2-digit month
# %d - 2-digit day
# %T - time (equivalent to %H:%M:%S)
# %H - 2-digit hour (24-hour clock)
# %M - 2-digit minute
# %S - 2-digit second
# %f - microsecond
# %p - AM/PM
orders["DELIVERY_DTTM"] = pd.to_datetime(
    orders["DELIVERY_DTTM"],
    errors="coerce",
    format="%Y-%m-%d %H:%M:%S",
)

print(magenta_colored("\nOrders DataFrame after converting to datetime dtypes:"))
print(orders)
print(orders.dtypes)

# ##############################################################################
# Parsing Datetimes during DataFrame Creation
# ##############################################################################
grocery_inventory = pd.DataFrame(
    data={
        "ITEM": ["Milk", "Eggs", "Bread"],
        "PKG_DT": ["2024-06-01", "2024-06-02", "2024-06-03"],
        "EXP_DT": ["2024-06-05", "2024-06-06", "2024-06-07"],
    }
)
grocery_inventory["PKG_DT"] = pd.to_datetime(grocery_inventory["PKG_DT"], format="%Y-%m-%d")
grocery_inventory["EXP_DT"] = pd.to_datetime(grocery_inventory["EXP_DT"], format="%Y-%m-%d")

print(cyan_colored("\nGrocery Inventory DataFrame with parsed datetime columns:"))
print(grocery_inventory)
print(grocery_inventory.dtypes)

# ##############################################################################
# Extracting Date and Time Components using dt accessor
# ##############################################################################
print(yellow_colored("\nDate component from ORDER_DTTM   :\n"), orders["ORDER_DTTM"].dt.date)
print(yellow_colored("\nHour component from ORDER_DTTM   :\n"), orders["ORDER_DTTM"].dt.hour)

# ##############################################################################
# Time Delta Operations
# ##############################################################################
# 1. "D" -> days
# 2. "W" -> week
# 3. "H" -> hours
# 4. "T" -> minutes
# 5. "S" -> seconds
# ##############################################################################
orders["SHIPPING_DURATION"] = (orders["DELIVERY_DTTM"] - orders["ORDER_DTTM"]).dt.days
print(green_colored("\nOrders DataFrame with SHIPPING_DURATION column (days):"))
print(orders)

orders["CUSTOMER_SURVEY_DTTM"] = orders["DELIVERY_DTTM"] + pd.to_timedelta(2, unit="D")
print(magenta_colored("\nOrders DataFrame with CUSTOMER_SURVEY_DTTM column:"))
print(orders)

# ##############################################################################
# Using Time Series as Index
# ##############################################################################
gold_prices = pd.read_csv(
    r"D:\Python\numpy-pandas-practice\data\input\gold.csv",
    parse_dates=["MARKET_DATE"],
    index_col="MARKET_DATE",
)

print(cyan_colored("\nGold Prices DataFrame with Date as Index:"))
print(gold_prices.head())
print(gold_prices.index)
print(gold_prices.dtypes)

print(yellow_colored("\nGold Prices for 2004:"))
print(gold_prices.loc["2004"])

print(yellow_colored("\nGold Prices for January 2004:"))
print(gold_prices.loc["2004-01"])

print(yellow_colored("\nGold Prices between 2004-01-01 and 2004-01-07:"))
print(gold_prices.loc["2004-01-01":"2004-01-07"])

# ##############################################################################
# Handling Missing Dates in Time Series
# ##############################################################################
# Available methods:
# 1. asfreq() - change frequency of time series
# 2. resample() - resample time series data
# 3. fillna() - fill missing values
# 4. interpolate() - interpolate missing values
# 5. ffill() / bfill() - forward fill / backward fill
# ##############################################################################
print(blue_colored("\nGold Prices with missing dates filled (forward fill):"))
print("BEFORE:")
print(gold_prices.head())
print("AFTER:")
print(gold_prices.head().asfreq("D", method="ffill"))
