"""
Advent of Code 2024
-------------------
Day 3: Mull It Over (Finished)

Part 1 (Finished)
    Question: What do you get if you add up all of the results of the multiplications?
    Answer: 167650499

Part 2 (Finished):
    Question: What do you get if you add up all of the results of just the enabled multiplications?
    Answer: 95846796
-------------------

Author: Suyash Dayal
Originally Completed On: 16th January 2025
"""
import re
from typing import Generator


def yield_all_multiplication_operations(input_string: str) -> Generator[tuple[int, int]]:
    """A generator function that yields a tuple containing 2 integers denoting
    numbers provided to a discovered multiplication operation.
    """
    matches = re.findall(pattern=r"mul\((\d{1,3}),(\d{1,3})\)", string=input_string)
    for operands in matches:
        yield int(operands[0]), int(operands[1])


def remove_all_disabled_multiplications(
        input_string: str,
        current_machine_state: bool = True
    ) -> tuple[str, bool]:
    """Returns a tuple where the first element is a string containing a sequence of
    multiplication operations, filtering out all disabled operations based on the
    presence of `do()` & `don't()` conditional statements in the given input string
    and the second element contains a boolean indicating whether the multiplication
    statements will be considered or ignored.
    """
    matches = re.findall(pattern=r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", string=input_string)
    valid_multiplications = []
    for operation in matches:
        if operation == "do()":
            current_machine_state = True
        elif operation == "don't()":
            current_machine_state = False
        elif current_machine_state:
            valid_multiplications.append(operation)
    return "".join(valid_multiplications), current_machine_state


def add_all_valid_products(puzzle_filename: str) -> int:
    """Fetches info about all valid multiplication operations, and returns the
    sum of their products.

    Parameters
    ----------
    puzzle_filename: Name of puzzle input file.

    Returns
    -------
    Sum of all the products calculated from their mulitplication operations.
    """
    total = 0
    with open(puzzle_filename, encoding="utf-8") as puzzle_file:
        while input_line := puzzle_file.readline()[:-1]:
            for x, y in yield_all_multiplication_operations(input_line):
                total += x * y
    return total


def add_all_enabled_products(puzzle_filename: str) -> int:
    """Fetches info about all valid multiplication operations, and returns the
    sum of their products.

    Parameters
    ----------
    puzzle_filename: Name of puzzle input file.

    Returns
    -------
    Sum of all the products calculated from their mulitplication operations.
    """
    total = 0
    current_machine_state = True
    with open(puzzle_filename, encoding="utf-8") as puzzle_file:
        while input_line := puzzle_file.readline()[:-1]:
            valid_multiplication_sequence, current_machine_state = remove_all_disabled_multiplications(input_line, current_machine_state)
            for x, y in yield_all_multiplication_operations(valid_multiplication_sequence):
                total += x * y
    return total


if __name__ == "__main__":
    PUZZLE_INPUT_FILENAME = "day-3-input.txt"
    print(
        "Day 3 Answers:\n"
        f"  Part 1: {add_all_valid_products(PUZZLE_INPUT_FILENAME)}\n"
        f"  Part 2: {add_all_enabled_products(PUZZLE_INPUT_FILENAME)}"
    )
