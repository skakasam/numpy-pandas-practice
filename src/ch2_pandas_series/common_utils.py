"""CH2 Package Common Utilities"""

from termcolor import colored


def print_delimiter():
    print("\n" + "=-" * 40 + "\n")


def rd_colored(text):
    return colored(text, "red")


def gr_colored(text):
    return colored(text, "green")


def bu_colored(text):
    return colored(text, "blue")


def cy_colored(text):
    return colored(text, "cyan")


def mg_colored(text):
    return colored(text, "magenta")


def ye_colored(text):
    return colored(text, "yellow")
