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
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto

# Initialization
# --------------
COMMAND_IDENTIFIER = "$"
ROOT_DIR_PATH = "/"
GOTO_PARENT_DIR = ".."

# Filesystem
# ----------
class FSType(Enum):
    """Type of node in filesystem."""

    DIRECTORY = auto()
    FILE = auto()


@dataclass
class FSElement:
    """A representation of a file/directory in the filesystem."""

    children: list[FSElement] = field(default_factory=lambda: [])
    fs_type: FSType = FSType.DIRECTORY
    size: int = 0
    name: str = ""
    parent: FSElement | None = None
    is_explored: bool = False

    def __str__(self):
        """A string representation for the instance."""
        if self.fs_type == FSType.FILE:
            return f"File: {self.name} ({self.size})"
        else:
            no_of_files = no_of_folders = 0
            for child in self.children:
                if child.fs_type == FSType.FILE:
                    no_of_files += 1
                else:
                    no_of_folders += 1
            return f"Directory: {self.name} [{no_of_folders} folder(s), {no_of_files} file(s)]"


# Command Executioners
# --------------------
class CmdExec(ABC):
    """This abstract bas  class defines the structure of all classes that
    will be responsible for the execution of a particular command.
    """

    def __init__(self, workdir: FSElement | None) -> None:
        self.workdir = workdir

    @abstractmethod
    def execute(self) -> typing.Any:
        pass


class CdExec(CmdExec):
    """This class handles the execution of the Change Directory ('cd') command."""

    def __init__(self, current_dir: FSElement | None, root_dir: FSElement | None, pathname: str) -> None:
        """Initializes an object.

        Parameters
        ----------
        current_dir: An object representing current working directory.
        root_dir: An object representing the root directory.
        pathname: The string representing the target location.
        """
        super().__init__(current_dir)
        self.root_dir = root_dir
        self.pathname = pathname

    def execute(self) -> FSElement | None:
        """This method make changes to the tree structure for the virtual filesystem
        based on the information provided with the 'cd' command.
        """
        if self.pathname == ROOT_DIR_PATH:
            if not self.root_dir:
                self.root_dir = FSElement(name=ROOT_DIR_PATH)
            return self.root_dir
        elif self.pathname == GOTO_PARENT_DIR:
            if self.workdir and self.workdir.parent:
                return self.workdir.parent
        else:
            if self.workdir:
                for child in self.workdir.children:
                    if child.fs_type == FSType.DIRECTORY and child.name == self.pathname:
                        return child
            return self.workdir


class LsExec(CmdExec):
    """This class handles the execution of List ('ls') command."""

    def __init__(self, current_dir: FSElement | None, file_handler: typing.TextIO) -> None:
        """Initializes an object.

        Parameters
        ----------
        current_dir: An oject representing current working directory.
        file_handler: File pointer processing a terminal output file.
        """
        super().__init__(current_dir)
        self.file_handler = file_handler

    def execute(self) -> None:
        """This method make changes to the tree structure for the virtual
        filesystem based on the information provided with the 'ls' command.
        """
        while True:
            current_position_in_file = self.file_handler.tell()
            next_line = self.file_handler.readline()[:-1]
            if next_line:
                if next_line[0] == COMMAND_IDENTIFIER:
                    self.file_handler.seek(current_position_in_file)
                    break
                continue
            break


# Parser
# ------
class InputParser:
    """This class is used for parsing the stream of text from a given file."""

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
            lsRunner = LsExec(self.cwd, file_handler)
            lsRunner.execute()
        elif command == "cd":
            cdRunner = CdExec(self.cwd, self.fs_root, cmd_terms[1])
            new_workdir = cdRunner.execute()
            self.fs_root = self.fs_root or new_workdir
            self.cwd = new_workdir


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
