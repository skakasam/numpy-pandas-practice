"""Python Pandas Series Sorting"""

import numpy as np
import pandas as pd
import common_utils as utils

rng = np.random.default_rng(seed=2020)

rnd_temps = rng.uniform(
    low=18.0,
    high=24.0,
    size=7,
).round(2)

date_index = [
    pd.to_datetime("2025-10-17"),
    pd.to_datetime("2025-10-14"),
    pd.to_datetime("2025-10-18"),
    pd.to_datetime("2025-10-13"),
    pd.to_datetime("2025-10-16"),
    pd.to_datetime("2025-10-12"),
    pd.to_datetime("2025-10-15"),
]

wk_temps = pd.Series(
    data=rnd_temps,
    index=date_index,
    name="Temperatures",
)

print(f"{utils.ye_colored("Weekly Temperatures b/w 12th and 18th January, 2025:")}")
print(wk_temps)

# Sorting Series by Values (in asc order by default, use ascending=False for descending order)
wk_temps_sorted_by_val = wk_temps.sort_values(ascending=False)
print(f"{utils.ye_colored("Weekly Temperatures sorted by value:")}")
print(wk_temps_sorted_by_val)

# Sorting Series by Index
wk_temps_sorted_by_idx = wk_temps.sort_index()
print(f"{utils.ye_colored("Weekly Temperatures sorted by index:")}")
print(wk_temps_sorted_by_idx)

# Do inplace sorting using inplace=True to affect the original series
wk_temps.sort_index(ascending=True, inplace=True)
print(f"{utils.ye_colored("Weekly Temperatures after inplace sorting:")}")
print(wk_temps)

# Get first 3 lowest temperatures startiung with most recent first
print(f"{utils.ye_colored("Three lowest temperatures with most recent first:")}")
print(wk_temps.sort_values().iloc[:3:].sort_index(ascending=False))

# Get rows with temperatures <= 22.00 celsius within the provided dates
dates = [pd.to_datetime("2025-10-14"), pd.to_datetime("2025-10-15")]
print(f"{utils.ye_colored("Temperatures <= 22.00 celsius within the provided dates:")}")
print(wk_temps.loc[wk_temps.le(22.00) & wk_temps.index.isin(dates)])
