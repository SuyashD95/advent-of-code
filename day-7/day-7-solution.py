"""
Advent of Code 2022
-------------------
Day 7: No Space Left On Device (Pending)

Part 1 (Pending):
    Question: What is the sum of the total sizes of those directories?
    Answer:
"""
import typing

from dataclasses import dataclass
from enum import Enum, auto

# Initialization
# --------------
fs_root: FSElement | None
cwd: FSElement | None


# Filesystem
# ----------
class FSType(Enum):
    """Type of node in filesystem."""

    DIRECTORY = auto()
    FILE = auto()


@dataclass
class FSElement:
    """A representation of a file/directory in the filesystem."""

    fs_type: FSType
    children: list[FSElement]
    size: int
    name: str
    parent: FSElement | None


# Parser
# ------
class InputParser:

    def __init__(self, termstream: typing.TextIO) -> InputParser
        """Initializes an object.
        
        Parameters
        ----------
        termstream: A file containing a set of commands and their outputs
        as present in a virtual terminal application.
        """
        self.termstream = termstream

    def parse_command(self, command: str) -> list[str]:
        """Parse the given command in the file to perform some action in
        the virtual filesystem and move the file pointer to the next
        statement to be executed.

        Parameters
        ----------
        command: A string representing a command of the virtual OS.
        """
        pass
            

# Part 1 Solution
# ---------------
def sum_of_directories_under_100k(puzzle_input_filename: str) -> int:
    """Returns the total size of all directories whose size is less than or
    equal to 100K present in the filesystem represented by the provided puzzle
    input file.

    Parameters
    ----------
    puzzle_input_filename: Name of text file containing input dataset.

    Returns
    -------
    The total size of all directories whose size is utmost 100K.
    """
    with open(puzzle_input_filename) as puzzle_file:
        while terminal_output := puzzle_file.readline()[:-1]:
            print(terminal_output)

    return 0


if __name__ == "__main__":
    puzzle_input_filename = "day-7-input.txt"
    print(
        "Day 7 Answers:\n"
        f"  Part 1: {sum_of_directories_under_100k(puzzle_input_filename)}"
    )
