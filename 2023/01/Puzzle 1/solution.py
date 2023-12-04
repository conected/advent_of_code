"""
Advent of Code 2023 - Day 1 - Puzzle 1

Code reads a set of inpur strings from file input, one per line.

Each string contains letters and numbers. The puzzle solution is found by concatenating the first and last number of each string into a
new number and summing those up to a single number.

From the puzzle text:

    On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""


def _get_numbers_from_string(input):
    """Returns an array of all numbers read from a string in order of appearance.

    :param input: The input string.
    :return: Array of integers corresponding to the order of appearance in the input.
    """


def _first_number_in_string(input):
    """Finds the first number character in a string read from left to right and returns it.

    :param input: The input string
    :return: The first character"""
    pass


def _last_number_in_string(input):
    """Finds the last number character in a string read from left to right and returns it.

    :param input: The input string
    :return: The first character"""
    pass


def get_puzzle_number_from_string(input):
    """Extracts an integer from a string that is represented by the first and last number from a given string.

    :param input: The input string.
    :return: The integer defined by the input string.
    """
    if type(input) is not str:
        raise Exception("Input is not a string")

    
    
input = open('input', 'r')

sum = 0
for line in input.readlines():
    sum += get_puzzle_number_from_string(line)

print(f"I counted a sum of {sum}")
