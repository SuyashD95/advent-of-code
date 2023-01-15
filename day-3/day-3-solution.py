"""
Advent of Code 2022
-------------------
Day 3: Rucksack Reorganization

Part 1 (Pending):
    Question: Find the item type that appears in both compartments of each
    rucksack. What is the sum of priorities of those item types?
    Answer:
"""
from string import ascii_letters

ITEM_PRIORITY_MAP = {
    letter: index + 1
    for index, letter in enumerate(ascii_letters)
}


def common_items_total_priority(puzzle_input_filename: str) -> int:
    """Returns the sum of the priorities of items that have been found to
    be placed on both the compartments (having the same size) of a rucksack.

    Parameters
    ----------
    puzzle_input_filename: Name of the text file containing puzzle dataset.
    """
    total_priority = 0
    with open(puzzle_input_filename) as puzzle_file:
        while rucksack_items := puzzle_file.readline()[:-1]:
            compartment_size = len(rucksack_items) // 2
            left_compartment = rucksack_items[:compartment_size]
            right_compartment = rucksack_items[compartment_size:]
            for position in range(compartment_size):
                if left_compartment[position] == right_compartment[position]:
                    total_priority += ITEM_PRIORITY_MAP[left_compartment[position]]
                    break
    return total_priority


if __name__ == "__main__":
    puzzle_input_filename = "day-3-input.txt"
    print("Day 3 Answers:")
    print(f"\tPart 1: {common_items_total_priority(puzzle_input_filename)}")
