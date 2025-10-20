"""Numpy Array Operations"""

import numpy as np


def print_separator():
    print("=-" * 40)


product_types = np.array(
    [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Smartwatch",
    ]
)
product_names = np.array(
    [
        ["MacBook Pro", "Dell XPS 13", "HP Spectre x360"],
        ["iPhone 13", "Samsung Galaxy S21", "Google Pixel 6"],
        ["iPad Pro", "Samsung Galaxy Tab S7", "Amazon Fire HD 10"],
        ["Apple Watch Series 7", "Samsung Galaxy Watch 4", "Fitbit Versa 3"],
    ]
)
product_prices = np.array(
    [
        [2399, 1499, 1299],
        [999, 799, 599],
        [1099, 649, 149],
        [399, 249, 229],
    ]
)

# Apply 5% discount on all products
discounted_prices = product_prices * 0.95
print(f"Original Prices:\n{product_prices}")
print(f"Discounted Prices (5% off):\n{discounted_prices}")

print_separator()

# Calculate total inventory value per product type
total_inventory_value = product_prices.sum(axis=1)
for p_type, total_value in zip(product_types, total_inventory_value):
    print(f"Total inventory value for {p_type}: ${total_value}")
