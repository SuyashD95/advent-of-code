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
from collections import deque
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

    def __str__(self) -> str:
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
        LS_DIR_IDENTIFIER = "dir"

        if (not self.workdir) or (self.workdir.is_explored):
            return None

        while True:
            current_position_in_file = self.file_handler.tell()
            next_line = self.file_handler.readline()[:-1]
            if next_line:
                if next_line[0] == COMMAND_IDENTIFIER:
                    self.file_handler.seek(current_position_in_file)
                    break
                type_or_filesize, name = next_line.split()
                if type_or_filesize == LS_DIR_IDENTIFIER:
                    new_directory = FSElement(name=name, parent=self.workdir)
                    self.workdir.children.append(new_directory)
                else:
                    new_file = FSElement(
                        name=name,
                        parent=self.workdir,
                        fs_type=FSType.FILE,
                        size=int(type_or_filesize),
                        is_explored=True
                    )
                    self.workdir.children.append(new_file)
            else:
                break
        self.workdir.is_explored = True


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


def calculate_directory_sizes(vfs_tree: FSElement) -> None:
    """This helper function traverses the given virtual fileystem
    tree and calculate the total size of every directory node.
    The total size of a directory node is equivalent to the sum
    of all files and directories contained inside it.

    Parameters
    ----------
    vfs_tree: A tree data structure that represents the virtual
    filesystem where each node is an abstraction of a file/folder.
    """
    traversal_queue = deque([vfs_tree])
    node_expansion_queue = deque([False])

    while front_traversal_node := traversal_queue[0] if traversal_queue else None:
        if front_traversal_node.fs_type == FSType.DIRECTORY:
            if not node_expansion_queue[0]:
                node_expansion_queue[0] = True
                traversal_queue.extendleft(front_traversal_node.children)
                node_expansion_queue.extendleft([False]*len(front_traversal_node.children))
            else:
                front_traversal_node.size = sum(map(lambda child: child.size, front_traversal_node.children))
                traversal_queue.popleft()
                node_expansion_queue.popleft()
        else:
            front_traversal_node.parent.size += front_traversal_node.size
            traversal_queue.popleft()
            node_expansion_queue.popleft()


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
    MAX_DIR_SIZE = 100_000
    file_parser = InputParser(puzzle_input_filename)
    fs_tree = file_parser.parse()
    calculate_directory_sizes(fs_tree)

    total_size_of_dirs_under_100k = 0
    traversal_queue = deque([fs_tree])
    while front_traversal_node := traversal_queue.popleft() if traversal_queue else None:
        if front_traversal_node.fs_type == FSType.DIRECTORY:
            traversal_queue.extend(front_traversal_node.children)
            if front_traversal_node.size <= MAX_DIR_SIZE:
                total_size_of_dirs_under_100k += front_traversal_node.size

    return total_size_of_dirs_under_100k


if __name__ == "__main__":
    puzzle_input_filename = "day-7-input.txt"
    print(
        "Day 7 Answers:\n"
        f"  Part 1: {sum_of_directories_under_100k(puzzle_input_filename)}"
    )
