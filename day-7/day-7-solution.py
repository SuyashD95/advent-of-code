"""
Advent of Code 2022
-------------------
Day 7: No Space Left On Device (Pending)

Part 1 (Pending):
    Question: What is the sum of the total sizes of those directories?
    Answer:
"""
from __future__ import annotations
import typing

from dataclasses import dataclass
from enum import Enum, auto

# Initialization
# --------------
COMMAND_IDENTIFIER = "$"
ROOT_DIR_PATH = "/"

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


# Command Executioners
# --------------------
class CmdExec(typing.Protocol):
    """This Protocol class defines the structure of all classes that
    will be responsible for the execution of a particular command.
    """

    def execute(self) -> None:
	...


# Parser
# ------
class InputParser:

    def __init__(self, termstream: typing.TextIO) -> InputParser:
        """Initializes an object.
        
        Parameters
        ----------
        termstream: A file containing a set of commands and their outputs
        as present in a virtual terminal application.
        """
        self.termstream = termstream
        self.fs_root: FSElement | None = None
        self.cwd: FSElement | None = None

    def parse(self) -> FSElement | None:
        """This function is used for parsing the given stream and
        constructing the virtual filesystem on which further operations
        can be performed.

        Returns
        -------
        The root element of the FSTree, representing the '/' directory
        of the filesystem.
        """
        with open(puzzle_input_filename) as puzzle_file:
            while terminal_output := puzzle_file.readline()[:-1]:
                output_terms = terminal_output.split()
                if output_terms[0] == COMMAND_IDENTIFIER:
                    self.parse_command(output_terms[1:], puzzle_file)
        print("Reached the end of file.")
        return self.fs_root

    def parse_command(self, cmd_terms: list[str], file_handler: typing.TextIO) -> None:
        """Parse the given command in the file to perform some action in
        the virtual filesystem and move the file pointer to the next
        statement to be executed.

        Parameters
        ----------
        cmd_terms: A list of strings representing the terms of a command on
        the virtual OS.
        file_handler: Pointer operating on the given file.
        """
        command = cmd_terms[0]
        if command == "ls":
            while True:
                current_position_in_file = file_handler.tell()
                next_line = file_handler.readline()[:-1]
                if next_line:
                    if next_line[0] == COMMAND_IDENTIFIER:
                        file_handler.seek(current_position_in_file)
                        break
                    else:
                        print(f"ls command output: {next_line}")
                else:
                    break
        elif command == "cd":
            print(f"Change path to: {cmd_terms[1]}")


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
    file_parser = InputParser(puzzle_input_filename)
    fs_tree = file_parser.parse()
    return 0


if __name__ == "__main__":
    puzzle_input_filename = "day-7-input.txt"
    print(
        "Day 7 Answers:\n"
        f"  Part 1: {sum_of_directories_under_100k(puzzle_input_filename)}"
    )
