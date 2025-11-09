"""Identifying Duplicates in Pandas DataFrames"""

import pandas as pd
from commons import (
    EVENT_DATES,
    ORDER_EVENTS,
    ORDER_IDS,
    blue_colored,
    green_colored,
    red_colored,
    yellow_colored,
)

notifications = pd.DataFrame(
    {"Order": ORDER_IDS, "Event": ORDER_EVENTS, "UpdtDt": pd.to_datetime(EVENT_DATES)}
)

print(red_colored("Notifications DataFrame:"))
print(notifications)
print(blue_colored("\nNotifications DataFrame Information:"))
print(notifications.info(show_counts=True))
print(green_colored("\nNotifications DataFrame Shape:"))
print(notifications.shape)
print(yellow_colored("\nNotifications DataFrame Unique Counts:"))
print(notifications.nunique())

# ##############################################################################
# Identifying Duplicated Rows in a DataFrame
# ##############################################################################
# 1. Using duplicated() Method. Specify subset=columns to check for duplicates
#    in specific columns. By default, it marks all duplicates as True except for
#    the first occurrence.
#      To mark all duplicates as True, use keep=False.
#      To mark the last occurrence as False, use keep='last'.
#      To reset the index after filtering, use reset_index(drop=True).
#    duplicated_rows = notifications.duplicated(subset=["Order", "Event"], keep='first')
# 2. Using drop_duplicates() Method. This method removes duplicate rows from the
#    DataFrame.
#    deduplicated_df = notifications.drop_duplicates(subset=["Order", "Event"], keep='first')
# ##############################################################################

latest_notifications = notifications.drop_duplicates(subset=["Order"], keep="last")
latest_notifications.reset_index(drop=True, inplace=True)

print(green_colored("\nLatest notifications by Order after dropping old rows:"))
print(latest_notifications)
