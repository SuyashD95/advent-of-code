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
    of the trees in a given regions and its associated metadata.
    """
    trees: list[list[int]]
    height: int = 0
    width: int = 0

    @property
    def no_of_trees_on_map_edges(self) -> int:
        """Returns no. of trees that are present on the edges of the map."""
        if self.height == 0:
            return 0
        elif self.height == 1:
            return self.width
        elif self.width == 1:
            return self.height
        else:
            return (self.height * 2) + (self.width - 2) * 2)

    def is_tree_located_on_the_edge(self, tree_position: tuple[int, int]) -> bool:
        """Returns `True` if the tree is located on the edge of the map;
        otherwise, it returns `False`.

        Parameters
        ----------
        tree_position: A tuple containing X & Y location of a tree (0-based index).

        Returns
        -------
        A boolean indicating whether a tree is located on the edge or not.
        """
        return (
            (tree_position[0] == 0) or (tree_position[0] == self.width - 1)
            or (tree_position[1] == 0) or (tree_position[1] == self.height - 1)
        )

    def is_tree_visible_from_northern_direction(self, tree_position: tuple[int, int]) -> bool:
        """Returns `True` if the tree located in the interior is visible from the
        northern edge of the map; otherwise, it returns `False`.

        Parameters
        ----------
        tree_position: A tuple containing X & Y location of a tree (0-based index).

        Returns
        -------
        A boolean indicating whether a tree is visible from the northern edge or not.

        Raises
        ------
        ValueError: A position of a given tree is located on the edge of the map.
        """
        if self.is_tree_located_on_edge(tree_position):
            raise ValueError("The given tree is located on the edge of the map.")

        target_tree_height = self.trees[tree_position[1]][tree_position[0]]
        for y_position in range(0, tree_position[1]):
            current_tree_height = self.trees[y_position][tree_position[0]]
            if current_tree_height >= target_tree_height:
                return True
        return False

    def is_tree_visible_from_eastern_direction(self, tree_position: tuple[int, int]) -> bool:
        """Returns `True` if the tree located in the interior is visible from the
        eastern edge of the map; otherwise, it returns `False`.

        Parameters
        ----------
        tree_position: A tuple containing X & Y location of a tree (0-based index).

        Returns
        -------
        A boolean indicating whether a tree is visible from the eastern edge or not.

        Raises
        ------
        ValueError: A position of a given tree is located on the edge of the map.
        """
        pass

    def is_tree_visible_from_southern_direction(self, tree_position: tuple[int, int]) -> bool:
        """Returns `True` if the tree located in the interior is visible from the
        southern edge of the map; otherwise, it returns `False`.

        Parameters
        ----------
        tree_position: A tuple containing X & Y location of a tree (0-based index).

        Returns
        -------
        A boolean indicating whether a tree is visible from the southern edge or not.

        Raises
        ------
        ValueError: A position of a given tree is located on the edge of the map.
        """
        pass

    def is_tree_visible_from_western_direction(self, tree_position: tuple[int, int]) -> bool:
        """Returns `True` if the tree located in the interior is visible from the
        western edge of the map; otherwise, it returns `False`.

        Parameters
        ----------
        tree_position: A tuple containing X & Y location of a tree (0-based index).

        Returns
        -------
        A boolean indicating whether a tree is visible from the western edge or not.

        Raises
        ------
        ValueError: A position of a given tree is located on the edge of the map.
        """
        pass


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


if __name__ == "__main__":
    puzzle_input_filename = "day-8-input.txt"
    print(
        "Day 8 Answers:\n"
        f"  Part 1: {find_visible_trees_count(puzzle_input_filename)}"
    )
