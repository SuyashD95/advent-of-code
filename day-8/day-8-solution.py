"""
Advent of Code 2022
-------------------
Day 8: Treetop Tree House (Pending)

Part 1 (Pending):
    Question: How many trees are visible from outside the grid?
    Answer:
-------------------

Author: Suyash Dayal
"""
from dataclasses import dataclass


@dataclass
class TreeMap:
    """This dataclass stores information about the different heights
    of the trees in a given regiona and its associated metadata.
    """
    trees: list[list[int]]
    height: int = 0
    width: int = 0


# Part 1 Solution
# ---------------
def find_visible_trees_count(puzzle_input_filename: str) -> int:
    """Returns the no. of trees that are visible from outside the grid.

    Parameters
    ----------
    puzzle_input_filename: Name of text file containing input dataset.

    Returns
    -------
    Number of trees visible from outside the grid.
    """
    tree_map_matrix = []
    with open(puzzle_input_filename) as puzzle_file:
        while output_line := puzzle_file.readline()[:-1]:
            tree_row = [int(digit) for digit in output_line]
            tree_map_matrix.append(tree_row)
    tree_map = TreeMap(
        trees=tree_map_matrix,
        height=len(tree_map_matrix),
        width=len(tree_map_matrix[0]) if len(tree_map_matrix) else 0 
    )
    print(tree_map)



if __name__ == "__main__":
    puzzle_input_filename = "day-8-input.txt"
    print(
        "Day 8 Answers:\n"
        f"  Part 1: {find_visible_trees_count(puzzle_input_filename)}"
    )
