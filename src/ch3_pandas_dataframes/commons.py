"""Color Utilities"""

from termcolor import colored


# ##############################################################################
# Common Utilities
# ##############################################################################
def red_colored(text: object) -> str:
    return colored(text, "red")


def green_colored(text: object) -> str:
    return colored(text, "green")


def blue_colored(text: object) -> str:
    return colored(text, "blue")


def cyan_colored(text: object) -> str:
    return colored(text, "cyan")


def magenta_colored(text: object) -> str:
    return colored(text, "magenta")


def yellow_colored(text: object) -> str:
    return colored(text, "yellow")


def print_delimiter() -> None:
    print("\n" + "=*~-" * 20 + "\n")


# ##############################################################################
# Common Constants
# ##############################################################################
GROCERY_ITEMS = [
    "Gala Apple",
    "Honeycrisp Apple",
    "Banana",
    "Navel Orange",
    "Lemon",
    "Lime",
    "Red Seedless Grapes",
    "Strawberries",
    "Blueberries",
    "Raspberries",
    "Mango",
    "Pineapple",
    "Hass Avocado",
    "Bartlett Pear",
    "Kiwi",
    "Cranberries",
    "Cantaloupe",
    "Pomegranate",
    "Grapefruit",
    "Bag Clementine",
    "Bag Limes",
    "Coconut",
    "Persimmon",
    "Blackberries",
    "Fig",
    "Broccoli",
    "Carrots",
    "Russet Potatoes",
    "Sweet Potato",
    "Fresh Bag Spinach",
    "Kale",
    "Head Romaine Lettuce",
    "Iceberg Lettuce",
    "Regular Cucumber",
    "Zucchini",
    "Red Bell Pepper",
    "Green Bell Pepper",
    "Yellow Onion",
    "Red Onion",
    "Garlic",
    "Green Beans",
    "White Mushroom",
    "Grape Tomato",
    "Celery",
    "Green Cabbage",
    "Cauliflower",
    "Asparagus",
    "Artichoke",
    "Butternut Squash",
    "Eggplant",
]

ITEM_PRICES = [
    1.69,
    3.49,
    0.64,
    1.49,
    1.55,
    1.99,
    2.79,
    3.99,
    8.77,
    11.97,
    1.64,
    1.26,
    4.42,
    1.75,
    3.69,
    3.99,
    0.99,
    4.43,
    1.49,
    2.33,
    3.49,
    1.93,
    4.29,
    13.31,
    8.78,
    1.99,
    1.29,
    0.79,
    1.19,
    12.77,
    4.98,
    1.66,
    1.53,
    1.11,
    1.69,
    2.99,
    1.99,
    0.75,
    0.99,
    4.60,
    2.49,
    5.98,
    6.06,
    1.33,
    0.79,
    1.56,
    4.99,
    3.99,
    0.99,
    1.89,
]

STUDENT_IDS = range(1, 33)  # Student IDs from 1 to 32

STUDENT_SCORES = [
    85,
    92,
    78,
    90,
    88,
    76,
    95,
    89,
    None,
    84,
    91,
    87,
    93,
    None,
    80,
    82,
    94,
    77,
    81,
    None,
    86,
    79,
    83,
    92,
    None,
    88,
    76,
    95,
    89,
    84,
    91,
    87,
]

STUDENT_NAMES = [
    "Alice Johnson",
    "Bob Smith",
    "Charlie Brown",
    "David Wilson",
    "Eva Green",
    "Frank Wright",
    "Grace Lee",
    "Hannah Scott",
    "Ian Thomas",
    "Ivy Martinez",
    "Jack White",
    "Kathy Black",
    "Leo King",
    "Mona Hall",
    "Mark Young",
    "Nina Adams",
    "Oscar Baker",
    "Paul Clark",
    "Quinn Lewis",
    "Quincy Walker",
    "Rachel Young",
    "Steve Allen",
    "Tina King",
    "Uma Harris",
    "Ursula Nelson",
    "Victor Turner",
    "Wendy Carter",
    "Xander Mitchell",
    "Yara Perez",
    "Zoe Roberts",
    "Aaron Campbell",
    "Bella Evans",
]

ORDER_IDS = [
    101,
    102,
    103,
    101,
    101,
    102,
    101,
]

ORDER_EVENTS = [
    "Ordered",
    "Shipped",
    "Ordered",
    "Processing",
    "Shipped",
    "Transit",
    "Delivered",
]

EVENT_DATES = [
    "2024-01-01",
    "2024-01-02",
    "2024-01-03",
    "2024-01-04",
    "2024-01-05",
    "2024-01-06",
    "2024-01-07",
]
