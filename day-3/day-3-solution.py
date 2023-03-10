"""
Advent of Code 2022
-------------------
Day 3: Rucksack Reorganization (Finished)

Part 1 (Completed):
    Question: Find the item type that appears in both compartments of each
    rucksack. What is the sum of priorities of those item types?
    Answer: 8053

Part 2 (Completed):
    Question: Find the item type that corresponds to the badges of each
    three-Elf group. What is the sum of the priorities of those item types?
    Answer: 2425
-------------------

Author: Suyash Dayal
Orginally Completed On: 21st January 2023
"""
from typing import cast
from functools import reduce
from string import ascii_letters

ITEM_PRIORITY_MAP = {
    letter: index + 1
    for index, letter in enumerate(ascii_letters)
}


# -------------------------- PART 1 SOLUTION -----------------------------
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
            left_compartment_itemset = set(rucksack_items[:compartment_size])
            right_compartment_itemset = set(rucksack_items[compartment_size:])
            common_item = (
                left_compartment_itemset & right_compartment_itemset
            ).pop()
            total_priority += ITEM_PRIORITY_MAP[common_item]
    return total_priority
# ------------------------------------------------------------------------


# -------------------------- PART 2 SOLUTION -----------------------------
def elfgroup_badges_total_priority(puzzle_input_filename: str) -> int:
    """Returns the sum of the priorities of badge items that have been found
    in the rucksacks of each member of a three-elf group.

    Parameters
    ----------
    puzzle_input_filename: Name of the text file containing puzzle dataset.
    """
    total_badge_priority = 0
    ELF_GROUP_SIZE = 3

    with open(puzzle_input_filename) as puzzle_file:
        elf_group_rucksacks: list[str] = []

        while rucksack_items := puzzle_file.readline()[:-1]:
            elf_group_rucksacks.append(rucksack_items)
            if not len(elf_group_rucksacks) == ELF_GROUP_SIZE:
                continue

            group_badge = cast(str, reduce(
                lambda elf_bag_1, elf_bag_2: elf_bag_1 & elf_bag_2,
                map(
                    lambda rucksack: set(rucksack),
                    elf_group_rucksacks
                )
            ).pop())

            total_badge_priority += ITEM_PRIORITY_MAP[group_badge]
            elf_group_rucksacks.clear()
    return total_badge_priority
# ------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input_filename = "day-3-input.txt"
    print(
        "Day 3 Answers:\n"
        f"  Part 1: {common_items_total_priority(puzzle_input_filename)}\n"
        f"  Part 2: {elfgroup_badges_total_priority(puzzle_input_filename)}"
    )
