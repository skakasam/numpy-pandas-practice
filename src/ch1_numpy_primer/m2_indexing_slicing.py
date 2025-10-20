"""Numpy Array Indexing and Slicing"""

import numpy as np


def print_separator():
    print("=-" * 40)


# Numpy 1D Array - Daily avg temperatures for a week
WEEKLY_AVG_TEMPS = np.array([22.1, 21.9, 23.0, 24.5, 25.2, 26.1, 27.3])
print(f"Average Temperature on SUN: {WEEKLY_AVG_TEMPS[0]}°C")
print(f"Average Temperature on SAT: {WEEKLY_AVG_TEMPS[-1]}°C")

WEEKDAY_AVG_TEMPS = WEEKLY_AVG_TEMPS[1:6]
print(f"{type(WEEKDAY_AVG_TEMPS) = }")
print(f"Average Temperatures from MON to FRI: {WEEKDAY_AVG_TEMPS}°C")
print(f"Average Temperature on Alternate Days (MON, WED, FRI): {WEEKLY_AVG_TEMPS[1:6:2]}°C")

print_separator()

# Numpy 2D Array - Daily avg temperatures per week for a month
MONTHLY_AVG_TEMPS = np.array(
    [
        [22.1, 21.9, 23.0, 24.5, 25.2, 26.1, 27.3],
        [22.3, 22.0, 23.5, 24.7, 25.5, 26.3, 27.8],
        [22.5, 22.2, 23.8, 25.0, 25.8, 26.5, 28.0],
        [22.7, 22.4, 24.0, 25.3, 26.0, 26.8, 28.3],
        [22.9, 22.6, 24.3, 25.5, 26.3, 27.0, 28.5],
    ]
)
print(f"Average Temperature on Week 1, SUN: {MONTHLY_AVG_TEMPS[0, 0]}°C")
print(f"Average Temperature on Week 5, SAT: {MONTHLY_AVG_TEMPS[-1, -1]}°C")

MONTHLY_AVG_TEMPS_ON_WEEKENDS = MONTHLY_AVG_TEMPS[:, [0, -1]]
print(
    f"""Average Temperatures on Weekends for the Month:
{MONTHLY_AVG_TEMPS_ON_WEEKENDS}°C"""
)
MONTHLY_AVG_TEMPS_ON_WEEKDAYS_OF_2ND_4TH_WEEKS = MONTHLY_AVG_TEMPS[1::2, 1:6]
print(
    f"""Average Temperatures on Weekdays of 2nd & 4th Weeks:
{MONTHLY_AVG_TEMPS_ON_WEEKDAYS_OF_2ND_4TH_WEEKS}°C"""
)
